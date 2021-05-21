#!/bin/zsh

source ./.env;

for i in {1..25}
do
    result=$(curl -s -H "cookie: session=$SESSION_COOKIE" "https://adventofcode.com/2020/day/$i");
    count=$(echo $result | grep "Your puzzle answer was" -c);
    not_available=$(echo $result | grep "Please don't repeatedly request this endpoint before it unlocks! The calendar countdown is synchronized with the server time; the link will be enabled on the calendar the instant this puzzle becomes available." -c);
    if [[ $not_available == 1 ]]
    then
        echo "Day $i: Not available yet";
    elif [[ $count == 1 ]]
    then
        echo "Day $i: [x] [ ]";
    elif [[ $count == 2 ]]
    then
        echo "Day $i: [x] [x]";
    else
        echo "Day $i: [ ] [ ]";
    fi
done