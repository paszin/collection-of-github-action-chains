#!/bin/bash

score=$(tail pylint.txt -n 2 | sed 's/[^0-9]*//1' | bc -l)

echo "Score: $score"

if (( $(echo "$score > 0.77" |bc -l) ));
then
    echo "ok"
    exit 0
else
    echo "not ok"
    exit 1
fi
