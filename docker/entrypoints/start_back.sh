#!/bin/bash

run_alembic() {
  local command="$1"
  alembic --config src/alembic.ini $command
}

run_alembic check || run_alembic revision --autogenerate

if ! run_alembic "upgrade head"; then
  echo "Failed to apply migrations"
  exit 1
else
  echo "Migrations were applied"
fi

uvicorn src.main:app --reload --host 0.0.0.0 --port 8000