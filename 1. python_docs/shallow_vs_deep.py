import copy as cp
# shallow and deep copy concepts are applied when there is nested objects

### shallow copy (if nested object is immutable)
# obj = [1, 2, 3]
# s_copied_obj = cp.copy(obj)
# s_copied_obj[0] = 100
# print(obj)

# print(id(obj))
# print(id(s_copied_obj))

# print(id(obj[0]))
# print(id(s_copied_obj[0]))

### shallow copy (if nested object is mutable)
# obj = [[1, 2, 3], [4, 5, 6]]
# s_copied_obj = cp.copy(obj)

# print(id(obj))
# print(id(s_copied_obj))

# print(id(obj[0]))
# print(id(s_copied_obj[0]))

# s_copied_obj[1].append(100)
# print(obj)

### deep copy (if nested object is mutable)
# obj = [[1, 2, 3], [4, 5, 6]]
# d_copied_obj = cp.deepcopy(obj)

# print(id(d_copied_obj))
# print(id(obj))

# print(id(obj[0]))
# print(id(d_copied_obj[0]))

# d_copied_obj[1].append(100)
# print(obj)
# print(d_copied_obj)