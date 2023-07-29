class BinarySearch():
    def search_iterative(self, list_items, item):
        low = 0
        high = len(list_items) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = list_items[mid]

            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None

if __name__ == "__main__":
  list_items = [1,2,3,4,5,6,7]
  sorted_list_items = sorted(list_items)

  bs = BinarySearch()
  print(bs.search_iterative(sorted_list_items, 2))
