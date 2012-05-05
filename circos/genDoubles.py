#! /usr/bin/env python
# -*- coding: utf8 -*-
import sys, os, re

csvfile = open('normalisedListCodes.csv', 'r')
matched = {}
double = {}

for line in csvfile:
  circo = line.split(";")
  if matched.has_key(circo[0]):
    double[circo[0]] = 1
  else :
    matched[circo[0]] = 1

for code_insee in sorted(double):
  print(code_insee)