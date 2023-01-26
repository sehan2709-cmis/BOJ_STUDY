input = int(input(""))

for i in range(0, input):
  for j in range(0, input):
    if(input - i - 1 > j):
      print(" ", end ="")
    else:
      print("*", end ="")
  print("")
