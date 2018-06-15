import re

print("YES" if re.compile(".*(0{7,}|1{7,}).*").match(input()) else "NO")
