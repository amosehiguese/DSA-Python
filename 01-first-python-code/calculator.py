num_one = int(input("Number one: "))
num_two = int(input("Number two: "))
operator = input("operator (+,-,*,/): ")


if operator == "+":
  result = num_one + num_two
elif operator == "-":
  result = num_one - num_two
elif operator == "*":
  result = num_one * num_two
elif operator == "/" and num_two != 0:
  result = num_one/num_two
  
print(result)