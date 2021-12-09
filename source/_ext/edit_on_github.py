"""
Sphinx extension to add ReadTheDocs-style "Edit on GitHub" links to the
sidebar.

Loosely based on https://github.com/astropy/astropy/pull/347

Modified by Dmitry Baryshnikov <dmitry.baryshnikov@nextgis.com> for NextGIS documentation
"""

import os
import warnings

__licence__ = 'BSD (3 clause)'

def get_github_url(app, repo, view, branch, path):
    return 'https://github.com/{user}/{repo}/{view}/{branch}/{path}'.format(
        user=app.config.edit_on_github_user,
        repo=repo,
        view=view,
        branch=branch,
        path=path)

def splitpath(path, maxdepth=20):
     ( head, tail ) = os.path.split(path)
     return splitpath(head, maxdepth - 1) + [ tail ] \
         if maxdepth and head and head != path \
         else [ head or tail ]

def html_page_context(app, pagename, templatename, context, doctree):
    if templatename != 'page.html':
        return

    if not app.config.edit_on_github_user:
        warnings.warn("edit_on_github_user not specified")
        return

    if not doctree:
        warnings.warn("doctree is not init")
        return

    path = os.path.relpath(doctree.get('source'), app.builder.srcdir)
    #modify path to support submodules
    dirs = splitpath(path)
    #if path start with docs_* split docs_* to repo and other part to path
    if dirs[0].startswith('docs_ngweb_dev'):
        repo = 'nextgisweb'
        path = os.path.join(*dirs[1:])
        branch = 'master'
    elif dirs[0].startswith('docs_ngweb_3D'):
        repo = 'docs_ng'
        path = os.path.join('source', path)
        branch = app.config.edit_on_github_branch
    elif dirs[0].startswith('qms_srv_dev'):
        repo = 'quickmapservices_server'
        path = os.path.join(*dirs[1:])
        branch = 'master'
    elif dirs[0].startswith('docs_formbuilder_dev'):
        repo = 'formbuilder'
        path = os.path.join(*dirs[1:])
        branch = 'master'
    elif dirs[0].startswith('docs_ogportal') or dirs[0].startswith('docs_howto') or dirs[0].startswith('docs_ngbio') or dirs[0].startswith('docs_forestinspector') or dirs[0].startswith('docs_ngcourses'):
        repo = dirs[0]
        path = os.path.join(*dirs[1:])
        branch = 'master'
    elif dirs[0].startswith('docs_ngcom') or dirs[0].startswith('docs_ngweb') or dirs[0].startswith('docs_ngqgis') or dirs[0].startswith('docs_ngmobile') or dirs[0].startswith('docs_ngmanager') or dirs[0].startswith('docs_formbuilder') or dirs[0].startswith('docs_simplecollector') or dirs[0].startswith('docs_collector') or dirs[0].startswith('docs_toolbox') or dirs[0].startswith('docs_data') or dirs[0].startswith('docs_ngid'):
        repo = dirs[0]
        path = os.path.join(*dirs[1:])
        branch = app.config.edit_on_github_branch
    else:
        repo = 'docs_ng'
        path = os.path.join('source', path)
        branch = app.config.edit_on_github_branch

    show_url = get_github_url(app, repo, 'blob', branch, path)
    edit_url = get_github_url(app, repo, 'edit', branch, path)

    context['show_on_github_url'] = show_url
    context['edit_on_github_url'] = edit_url

def setup(app):
    app.add_config_value('edit_on_github_user', '', True)
    app.add_config_value('edit_on_github_branch', 'master', True)
    app.connect('html-page-context', html_page_context)
