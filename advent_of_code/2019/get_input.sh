#!/bin/bash

if [ "$1" == "" ]
then
    echo "usage: $0 <day_number>";
    exit 1;
fi

source ./.env;

mkdir -p day$1;

curl -o day$1/input -H "cookie: session=$SESSION_COOKIE" "https://adventofcode.com/2019/day/$1/input";

touch day$1/script.py;
touch day$1/script2.py;