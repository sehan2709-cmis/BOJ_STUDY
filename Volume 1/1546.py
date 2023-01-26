classes = int(input(""))
grades = list(map(int, input("").split()))
maxgrade = max(grades)
average = 0

for i in grades:
  average += (i/maxgrade*100)

print(average/classes)
