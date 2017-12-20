#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Wertolf"
__pkuid__  = "1700017811"
__email__  = "1700017811@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lines2 = ''
    for i in lines:
        if i not in ',.':
            lines2 = lines2 + i
    t = lines2.split()
    dic = {}
    for i in t:
        c = 0
        for j in t:
            if i == j:
                c += 1
            dic[i] = c
    keys = dic.keys()
    t2 = sorted(dic.values(),reverse=True)
    t_wanted = t2[:topn]
    t3 = []
    for i in t_wanted:
        if i not in t3:
            t3.append(i)
    c = 0
    for i in range(len(t3)):
        v = t3[i]
        for j in keys:
            if dic.get(j) == v:
                if c < topn:
                    print(j,v,sep='           ')
                c += 1
    pass


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
