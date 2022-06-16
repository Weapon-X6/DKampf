import re

pattern = re.compile(r"[+-]?\d+[\.\d]*\s[CF]{1}")
text = "scale: +23 C, 0 C, -20.0 C, -2.2 C, -5.65 C, 0.0001 C, AND +73.4 F, 32 F, -4.0 F,  9/5 and add 32 to the result"

print(re.findall(pattern, text))

# Remove year from movie info
pattern = re.compile(r',')  # (r',\s\d+,\s')
split_result = re.split(pattern, "The Godfather, 1972, Francis Ford Coppola")
print(split_result)
print(' '.join(split_result[0:3:2]))  # split_result
