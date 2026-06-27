import re

with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
in_table = False

for line in lines:
    # Check if line is a blockquoted table line
    if re.match(r'^>\s*\|.*\|', line):
        # Remove the blockquote prefix for the table
        new_lines.append(re.sub(r'^>\s*', '', line))
    else:
        new_lines.append(line)

with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Removed blockquotes from all tables to ensure native rendering.")
