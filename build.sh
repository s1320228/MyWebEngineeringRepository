#!/usr/bin/env bash

set -o errexit

uv sync --locked
uv run python manage.py collectstatic --noinput
uv run python manage.py migrate