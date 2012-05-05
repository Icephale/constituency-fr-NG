#! /usr/bin/env python
# -*- coding: utf8 -*-

csvfile = open('normalisedListCodes.csv', 'r')
matched = {}

for line in csvfile:
  circo = line.strip()
  circo = circo.split(";")
  try:
    matched[circo[1]] = matched[circo[1]]+','+circo[0]
  except KeyError:
    matched[circo[1]] = circo[0]

for key in sorted(matched):
  print (key+';'+matched[key])