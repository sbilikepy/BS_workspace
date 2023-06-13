# set_item
# get_item
# d = {"a": 3,
#      "b": 5}
# print(d["a"])
# print(d.__getitem__("a"))
# 1 hash("a") const time O(1)
# 2 somehash1028938913091 % 8 (capacity) = index O(1)
# 3 get_element_by_index in list O(1)
# 3 const steps
# __getitem__ 3*O(1) = const O(1)
# d.__setitem__("a", 10)
# 1 hash("a") const time O(1)
# 2 somehash1028938913091 % 8 (capacity) = index O(1)
# 3 set_element_by_index in list O(1)
# 3 const steps
# __setitem__ 3*O(1) = const O(1)
# print(d.__getitem__("a"))
# print(d)
# print(hash(-1))
# print(hash(3493789020213))
print(146%8)
print(tuple([1]+[2]))