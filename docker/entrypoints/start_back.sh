#!/bin/bash

run_alembic() {
  local command="$1"
  alembic --config src/alembic/alembic.ini $command
}

run_alembic "check" || run_alembic "revision --autogenerate"

run_alembic "upgrade head"

uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
