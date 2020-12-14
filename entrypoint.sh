#!/usr/bin/env sh

firstarg=$1
shift;

cd ./ping_pong/src


case $firstarg in

  "service_a")
    uvicorn service_a:app --port $PORT --host 0.0.0.0 --log-config=../../$LOG_CONFIG "$@"
    ;;

  "service_b")
    uvicorn service_b:app --port $PORT --host 0.0.0.0 --log-config=../../$LOG_CONFIG "$@"
    ;;

  "tests")
    echo "run tests"
    python -m unittest discover -s ../tests "$@"
    ;;

  "format")
    echo "run format"
    black ../ "$@"
    ;;

  "static_check")
    echo "run static check of code"
    echo "run black"
    black --check .
    echo "run mypy"
    mypy $(pwd)
    ;;

  *)
    echo -n "unknown option"
    ;;
esac