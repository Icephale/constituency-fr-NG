#!/usr/bin/python
#-*- coding: utf-8 -*-

import csv
import os
import argparse

DEP_CODES = {'ZD': '974',
            'ZC': '973',
            'ZB': '972',
            'ZA': '971',
            
}

def cpad(s, n, c=' '):
    l = (n - len(s))/2
    r = n - l
    return '{1}{0}{2}'.format(s, c*l, c*r)

def lpad(s, n, c=' '):
    return '{1}{0}'.format(s, c*(n-len(s)))

def rpad(s, n, c=' '):
    return '{0}{1}'.format(s, c*(n-len(s)))

def commune_encode(dep, com):
    if DEP_CODES.has_key(dep):
        return '{0}{1}'.format(DEP_CODES[dep][:2], lpad(com, 3, c='0'))
    else:
        return '{0}{1}'.format(lpad(dep, 2, c='0'), lpad(com, 3, c='0'))

def constituency_encode(dep, const):
    if DEP_CODES.has_key(dep):
        return '{0}-{1}'.format(DEP_CODES[dep], lpad(const, 3, c='0'))
    else:
        return '{0}-{1}'.format(lpad(dep, 3, c='0'), lpad(const, 3, c='0'))

def filter_uncertain(l):
    # {code_insee: [circos]}
    d = {}
    for i in l:
        d[i[0]] = d.get(i[0], []) + [i[1]]
    l = [(i, d[i][0]) for i in d if len(d[i]) == 1]
    l.sort()
    return l

def parse_csv(f):
    basename = os.path.basename(f).split('.')[0]
    with open(f, 'rb') as f:
        communes = [i for i in csv.reader(f, delimiter='\t', quotechar='"')]
    communes = filter_uncertain([(commune_encode(c[1], c[5]), constituency_encode(c[1], c[8])) for c in communes[1:]])
    with open(basename + '_processed.csv', 'wb') as f:
        for commune in communes:
            f.write('{0}\t{1}\n'.format(commune[0], commune[1]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='traitement de la liste de correspondance commune-circonscription électorale')
    parser.add_argument('csv', help='fichier csv à traiter')
    args = parser.parse_args()
    filename = os.path.abspath(args.csv)
    print filename
    parse_csv(filename)
