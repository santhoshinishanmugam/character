import re
st = input()
if re.match(r'[a-z]', st, re.I):
            print("Alphabet")
else:
            print("No")
