number_one = int(input("Enter a number : "))
number_two = int(input("Enter another number: "))


for num in range(number_one,number_two+1):
  original = num
  sum = 0
  while original > 0:
    rem = original % 10
    sum  = sum + (rem ** 3)
    original = original // 10

  if num == sum:
    print(sum)
