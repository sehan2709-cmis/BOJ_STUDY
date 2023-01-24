txt = input("").upper()

alph = list(set(txt));
count = []

for i in alph:
  count.append(txt.count(i))

if count.count(max(count)) >= 2:
  print("?")
else:
  print(alph[count.index(max(count))])