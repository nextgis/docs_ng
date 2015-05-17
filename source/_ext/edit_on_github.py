"""
Sphinx extension to add ReadTheDocs-style "Edit on GitHub" links to the
sidebar.

Loosely based on https://github.com/astropy/astropy/pull/347
"""

import os
import warnings


__licence__ = 'BSD (3 clause)'


def get_github_url(app, repo, view, path):
    return 'https://github.com/{user}/{repo}/{view}/{branch}/source/{path}'.format(
        user=app.config.edit_on_github_user,
        repo=repo,
        view=view,
        branch=app.config.edit_on_github_branch,
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

    path = os.path.relpath(doctree.get('source'), app.builder.srcdir)
    #modify path to support submodules
    dirs = splitpath(path)
    #if path start with docs_* split docs_* to repo and other part to path
    if dirs[0].startswith('docs_'):
        repo = dirs[0]  
        path = os.path.join(*dirs[2:])
    else:
        repo = 'docs_ng'
    
    #else repo = 'docs_ng'
    show_url = get_github_url(app, repo, 'blob', path)
    edit_url = get_github_url(app, repo, 'edit', path)

    context['show_on_github_url'] = show_url
    context['edit_on_github_url'] = edit_url


def setup(app):
    app.add_config_value('edit_on_github_user', '', True)
    app.add_config_value('edit_on_github_branch', 'master', True)
    app.connect('html-page-context', html_page_context)
