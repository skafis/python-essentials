#oppening and reading and searching a file

import re
fh = open("README.md")
for line in fh:
    if re.search(r"a",line):
        print (line.rstrip())
fh.close
