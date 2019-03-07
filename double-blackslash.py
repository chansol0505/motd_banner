import sys

filename = sys.argv[1]
output_sh = filename.rsplit('.', 1)[0]+'.sh'
print(output_sh)

with open(filename) as f:
    content = f.read()
with open(output_sh, 'w') as f:
    f.write("#!/bin/sh\n")
    f.write('printf "')
    for i, c in enumerate(content):
        if c == '\\':
            if content[i+1] != '\\':
                f.write(c)
            else:
                f.write('\\\\\\\\')
        elif c == '\n':
            f.write('\\n"')
            f.write(c)
            f.write('printf "')
        else:
            f.write(c)
    f.write('"')