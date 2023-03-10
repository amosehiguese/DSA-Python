def sum(arr, y):
 if y <= 0:
  return 0
 else:
  return sum(arr, y-1) + arr[y-1]

print(sum([1], 0))
print(sum([1,2,3,4,5,6], 3))
print(sum([11,22,33], 2))
