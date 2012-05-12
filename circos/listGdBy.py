#! /usr/bin/env python
# -*- coding: utf8 -*-
import sys, os, re

fulllist = 'listAllByCirco.csv'

csvfile = open(fulllist, 'r')
doublesfile = open('doubles.txt', 'r')
doubles = doublesfile.readlines()

for line in csvfile:
  line = line.strip()
  nop = 1
  for double in doubles:
    if re.search(double.strip(), line) is not None:
      nop = 0
  if nop:
    if len(sys.argv) > 1:
      print(line)
    else:
      circos = line.split(';')
      circo = circos[1].split(',')
      for town in circo:
        print(town+';"'+circos[0]+'";"good"')