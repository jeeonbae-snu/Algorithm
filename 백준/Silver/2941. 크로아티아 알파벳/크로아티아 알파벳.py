import re
t = input()
pattern = r'dz=|c=|c-|d-|lj|nj|s=|z=|.'
units = re.findall(pattern, t)
print(len(units))