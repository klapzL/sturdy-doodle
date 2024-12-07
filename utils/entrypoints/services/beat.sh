#!/bin/sh

set -eo pipefail

celery -A config beat
