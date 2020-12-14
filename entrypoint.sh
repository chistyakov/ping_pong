#!/usr/bin/env sh

firstarg=$1
shift;

cd ./ping_pong/src


case $firstarg in

  "service_a")
    python -m service_a "$@"
    ;;

  "service_b")
    python -m service_b "$@"
    ;;

  "tests")
    echo "run tests"
    python -m unittest discover -s ../tests "$@"
    ;;

  "format")
    echo "run format"
    black . "$@"
    ;;

  "static_check")
    echo "run static check of code"
    echo "run black"
    black --check .
    echo "run mypy"
    mypy .
    ;;

  *)
    echo -n "unknown option"
    ;;
esac