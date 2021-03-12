import sys
import re

WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[1], encoding='utf-8')as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            #보기 좋은 코드는 아니지만, 설명하기 위해 이렇ㄷ게 구현했다.
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

for word in sorted(index, key=str.upper):
    print(word, index[word])