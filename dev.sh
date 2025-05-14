#!/bin/bash

VENV_DIR="./venv"
REQUIREMENTS="./requirements.txt"

init_env() {
  if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
  fi

  source $VENV_DIR/bin/activate

  if [ -f "$REQUIREMENTS" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r $REQUIREMENTS
  fi

  echo "Installing Uvicorn..."
  pip install uvicorn

  echo "Starting the application with Uvicorn..."
  uvicorn app.main:app --reload
}

stop_uvicorn() {
  echo "To stop Uvicorn, press Ctrl+C or stop the process manually."
}

clear_env() {
  if [ -d "$VENV_DIR" ]; then
    echo "Removing virtual environment..."
    rm -rf $VENV_DIR
    echo "Virtual environment removed."
  else
    echo "Virtual environment not found."
  fi
}

run_app() {
  source $VENV_DIR/bin/activate
  echo "Starting the application with Uvicorn..."
  uvicorn app.main:app --reload
}

run_tests() {
  if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Run './dev.sh init' first."
    exit 1
  fi

  source $VENV_DIR/bin/activate
  echo "Running tests with pytest..."
  PYTHONPATH=. pytest -p no:warnings
}

case "$1" in
  init)
    init_env
    ;;
  stop)
    stop_uvicorn
    ;;
  clear)
    clear_env
    ;;
  run)
    run_app
    ;;
  test)
    run_tests
    ;;
  *)
    echo "Usage: ./dev.sh {init|stop|clear|run|test}"
    exit 1
    ;;
esac
