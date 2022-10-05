#  returns the first item and adds the last inputted item behind
def queue(arr,item):
  arr.append(item)
  stepped_out = arr.pop(0)
  return stepped_out



arr = []

print("press 'x' to exit\n")
while True:
  item = input("Add to list: ")
  if item == 'x':
    break
    
  elif item == "":
    continue
  else:
      arr.append(item)
      print(arr)

#display the earliest item
print(queue(arr, item))

# display the current list item
arr.pop()
print(arr)