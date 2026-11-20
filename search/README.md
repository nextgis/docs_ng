# Локальный поиск Typesense

Команды выполняются из корня `docs_ng`

Скопируйте локальные настройки:

```bash
cp .env.example .env
```

Запуск Typesense:

```bash
docker compose --env-file .env -f search/compose.yaml up -d --build
curl --fail http://127.0.0.1:8108/health
```

Создайте конфигурацию с отдельным поисковым ключом:

```bash
python scripts/typesense_search.py configure --language en --output build/typesense/search-config.json
```

Запустите сборку документации:

```bash
npm run build:assets
pybabel compile --directory=source/locale --domain=messages
pybabel compile --directory=source/locale --domain=sphinx
sphinx-autobuild source build
```

After a successful build or after editing the aliases, update the index in another terminal:

```bash
python scripts/typesense_search.py local build --language en
```

Edit aliases in `search/aliases.txt`. Put one group on each line and separate its
variants with `|`.

```text
NGW | NextGIS Web
basemap | base map
```
