#!/usr/bin/env bash
set -e

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Resolve to absolute path
PROJECT_DIR="$(realpath "$SCRIPT_DIR/..")"

# Get the current working directory
CURRENT_DIR="$(pwd)"

# Check if current directory is within the project path
if [[ "$CURRENT_DIR" != "$PROJECT_DIR"* ]]; then
    echo "Error: Must be run from within the project directory."
    echo "Current: $CURRENT_DIR"
    echo "Project: $PROJECT_DIR"
    exit 1
fi

# Check for venv (common names)
if [[ -d "$PROJECT_DIR/.venv" ]]; then
    VENV_PATH="$PROJECT_DIR/.venv"
elif [[ -d "$PROJECT_DIR/venv" ]]; then
    VENV_PATH="$PROJECT_DIR/venv"
else
    echo "Error: No virtual environment found (.venv or venv)"
    exit 1
fi

# Prepend src to PYTHONPATH
export PYTHONPATH="$PROJECT_DIR/src${PYTHONPATH:+:$PYTHONPATH}"

# Run pytest
"$VENV_PATH/bin/python" -m pytest "$PROJECT_DIR/tests" "$@"
