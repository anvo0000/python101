"""Slicing can be used with both LIST and TUPLE
return list or tuple depends on the source
"""
# piano_keys = ["a", "b", "c", "d", "e", "f", "g"] # list
piano_keys = ("a", "b", "c", "d", "e", "f", "g") # tuple

slicing = piano_keys[2:5]
print(slicing) # ['c', 'd', 'e'], ('c', 'd', 'e')

slicing = piano_keys[2:-1]
print(slicing) # ['c', 'd', 'e', 'f']


slicing = piano_keys[2:5:2]
print(slicing) # ['c', 'e']

slicing = piano_keys[::2]
print(slicing) # ['a', 'c', 'e', 'g']

slicing = piano_keys[::-1]
print(slicing) # ['g', 'f', 'e', 'd', 'c', 'b', 'a'] # revert the list