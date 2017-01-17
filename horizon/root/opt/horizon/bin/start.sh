#!/usr/bin/env bash

# Generate configs

echo "Migrating database..."
python /opt/horizon/bin/rethinkdb-migration.py
echo "Finish migrate database"

bash /usr/app/.hz/config.toml.sh
bash /usr/app/.hz/schema.toml.sh
bash /usr/app/.hz/secrets.toml.sh

su -s /bin/bash horizon -c "hz serve /usr/app"
