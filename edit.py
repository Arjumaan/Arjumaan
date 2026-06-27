import re

with open('README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_section = False
for line in lines:
    if line.startswith('## '):
        in_section = True
        
    if in_section:
        if line.strip() == '---':
            in_section = False
            new_lines.append(line)
        else:
            if line == '\n':
                new_lines.append('> \n')
            else:
                new_lines.append('> ' + line)
    else:
        new_lines.append(line)

text = ''.join(new_lines)

def replace_table(match):
    s = match.group(0)
    if 'border=' in s:
        s = re.sub(r'border="[^"]*"', 'border="3"', s)
    else:
        s = s.replace('<table', '<table border="3"')
    return s

text = re.sub(r'<table\b[^>]*>', replace_table, text)

with open('README_test.md', 'w', encoding='utf-8') as f:
    f.write(text)
print('Done!')
