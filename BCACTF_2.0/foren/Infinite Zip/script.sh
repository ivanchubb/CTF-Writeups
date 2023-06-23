#!/bin/bash
unzip flag.zip
for i in {999..0}
do
 unzip $i.zip
done
