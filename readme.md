**1. String**
   1.1 Common String Methods in Python:
    - upper(): Converts all characters in a string to uppercase.
    - lower(): Converts all characters in a string to lowercase.
    - find(substring): Returns the lowest index in the string where the substring is found.
    - strip(): Removes any leading and trailing characters (space is the default).
    - replace(old, new): Replaces occurrences of a substring within the string.
    - split(delimiter): Splits the string at the specified delimiter and returns a list of substrings.
    - join(iterable): Concatenates elements of an iterable with a specified separator.
    - startswith(prefix): Checks if the string starts with the specified prefix.
    - endswith(suffix): Checks if the string ends with the specified suffix.

**2. List Item** 
    2.1 Syntax of list comprehension
        ```python
        [expression for item in iterable if condition]
        ```
    expression: The transformation or value to be included in the new list.
    item: The current element taken from the iterable.
    iterable: A sequence or collection (e.g., list, tuple, set).
    if condition (optional): A filtering condition that decides whether the current item should be included.
    This syntax allows us to combine iteration, modification, and conditional filtering all in one line.

    2.2 List Methods
        append()	Adds an element at the end of the list
        clear()	Removes all the elements from the list
        copy()	Returns a copy of the list 
        count()	Returns the number of elements with the specified value
        extend()	Add the elements of a list (or any iterable), to the end of the current list
        index()	Returns the index of the first element with the specified value
        insert(index, "new_item")	Adds an element at the specified position
        pop()	Removes the element at the specified position
        remove("item_value")	Removes the item with the specified value
        reverse()	Reverses the order of the list
        sort()	Sorts the list
