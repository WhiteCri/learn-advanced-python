'''단어가 나타는 위치를 가리키는 인덱스를 만든다'''

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location) # this can make dict not to explore keys again and again
