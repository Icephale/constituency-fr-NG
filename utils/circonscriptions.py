#!/usr/bin/python
#-*- coding: utf-8 -*-

import argparse
import re
import os
import shapefile

def points(s):
    s = s.split('z M')
    s = [re.sub(r'[a-zA-Z]', r'', i) for i in s]
    s = [re.sub(r' +', r' ', i) for i in s]
    s = [i.strip() for i in s]
    for i in range(len(s)):
        s[i] = s[i].split(' ')
        s[i] = [(1000*float(j.split(',')[0])+700000,
            -1000*float(j.split(',')[1])+6600000) for j in s[i]]
    return s

def n(s):
    return re.sub(r'\n', r'', s)


def id(s):
    pass

def parse_csv(s):
    s = s.split('\n')
    s = [i.split(';') for i in s]
    s = [(n(i[1]), points(i[0])) for i in s]
    return s


# pypi.python.org/pypi/pyshp
def populate(data, dest):
    dest = os.path.abspath(dest)
    w=shapefile.Writer(shapefile.POLYGON)
    # création des champs contenant les informations supplémentaires
    w.field('ID', 'C', '50')
    #w.field('DESCR', 'C', '50')
    for poly in data:
        # pour chaque (multi)polygone, enregistrement de la géométrie puis des attributs
        w.poly(parts=poly[1])
        w.record(poly[0])
    # sauvegarde une fois fini
    w.save(dest)


def main():

    parser = argparse.ArgumentParser(description='Convert circonscriptions from csv to shapefile', epilog='This script uses pyshp to create shapefile: pypi.python.org/pypi/pyshp')
    parser.add_argument('csv', help='file to be converted')
    parser.add_argument('shp', help='shapefile to create')
    args = parser.parse_args()
    filename = os.path.abspath(args.csv)

    with open(filename, 'r') as f:
        data = f.read()

    circos = parse_csv(data)
    populate(circos, args.shp)

if __name__ == "__main__":
    main()
