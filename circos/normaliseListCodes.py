#! /usr/bin/env python
# -*- coding: utf8 -*-
import re

def str_replace(to_replace, text):
  pattern = "|".join(map(re.escape, to_replace.keys()))
  return re.sub(pattern, lambda m: to_replace[m.group()], text)

crap = {'0ZA' : '971', '0ZB' : '972', '0ZC' : '973', '0ZD' : '974', 'ZA' : '97', 'ZB' : '97', 'ZC' : '97', 'ZD' : '97', '2A' : '20', '2B' : '20',}

csvfile = open('listCodes.csv', 'r')
listcodes = csvfile.read().strip()
csvfile.close()

listcodes = str_replace(crap, listcodes).split("\n")

reg_ssdiv = re.compile("([0-9]{5})(SN|AR|SR)[0-9]{2}") #79123SN01 75056AR20...
uniqs = {}

for codes in listcodes:
  if re.match(reg_ssdiv, codes) is not None:
    matched = re.match(reg_ssdiv, codes)
    codes = re.sub(reg_ssdiv, matched.group(1), codes)
  uniqs[codes] = 1

for uniq in sorted(uniqs):
  print(uniq)
