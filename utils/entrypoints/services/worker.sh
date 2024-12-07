#!/bin/sh

set -euo pipefail

LOGLEVEL="INFO"

if [ "$DEBUG" = "True" ] || [ "$DEBUG" = "true" ]; then
    LOGLEVEL="DEBUG"
fi

celery -A config worker \
    --concurrency=10 \
    --autoscale=10,3 \
    --prefetch-multiplier=2 \
    --max-tasks-per-child=1000 \
    --max-memory-per-child=300MB \
    --loglevel=$LOGLEVEL
