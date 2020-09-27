endStr = "end"
str = ""

for line in iter(input, endStr):
    if line != endStr:
        str += line
    else:
        str += "\n"

print(str)
