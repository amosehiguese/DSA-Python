number = int(input("Enter a number: "))

a = 0
b = 1

for _ in range(number):
  a , b = b, a+b
  print(a)
