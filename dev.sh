#!/bin/bash

VENV_DIR="./venv"
REQUIREMENTS="./requirements.txt"

init_env() {
  if [ ! -d "$VENV_DIR" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv $VENV_DIR
  fi

  source $VENV_DIR/bin/activate

  if [ -f "$REQUIREMENTS" ]; then
    echo "Instalando dependencias desde requirements.txt..."
    pip install -r $REQUIREMENTS
  fi

  echo "Instalando uvicorn..."
  pip install uvicorn

  echo "Iniciando la aplicación con uvicorn..."
  uvicorn app.main:app --reload
}

stop_uvicorn() {
  echo "Para detener uvicorn, presiona Ctrl+C o detén el proceso manualmente."
}

clear_env() {
  if [ -d "$VENV_DIR" ]; then
    echo "Eliminando entorno virtual..."
    rm -rf $VENV_DIR
    echo "Entorno virtual eliminado."
  else
    echo "No se encontró el entorno virtual."
  fi
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
  *)
    echo "Uso: ./dev.sh {init|stop|clear}"
    exit 1
    ;;
esac
