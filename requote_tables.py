import re

with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith("|"):
        new_lines.append("> " + line)
    else:
        new_lines.append(line)

with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Reverted unquoting of tables.")
