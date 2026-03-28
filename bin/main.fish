#!/usr/bin/env fish

# Get the directory where the script is located
set SCRIPT_DIR (status dirname)

# Resolve to absolute path
set PROJECT_DIR (realpath "$SCRIPT_DIR/..")

# Get the current working directory
set CURRENT_DIR (pwd)

# Check if current directory is within the project path
if not string match -q "$PROJECT_DIR*" "$CURRENT_DIR"
    echo "Error: Must be run from within the project directory."
    echo "Current: "$CURRENT_DIR
    echo "Project: "$PROJECT_DIR
    exit 1
end

# Check for venv (common names)
if test -d "$PROJECT_DIR/.venv"
    set VENV_PATH "$PROJECT_DIR/.venv"
else if test -d "$PROJECT_DIR/venv"
    set VENV_PATH "$PROJECT_DIR/venv"
else
    echo "Error: No virtual environment found (.venv or venv)"
    exit 1
end

# Run main.py using the venv's python interpreter
"$VENV_PATH/bin/python" -m src.main $argv
