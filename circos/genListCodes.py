#! /usr/bin/env python
# -*- coding: utf8 -*-
import sys, os, re

csvfile = open('circos-data-gouv.csv', 'r')

for line in csvfile:
  line = line.strip()
  info = line.split(";")
  print (info[1].rjust(2, '0')+info[5].rjust(3, '0')+';'+info[1].rjust(3, '0')+'-'+info[8].rjust(2, '0'))

# code_dept_canton;code_dept;nom_dept;code_canton;nom_canton;code_commune;nom_commune;circo_1986;num_circo

