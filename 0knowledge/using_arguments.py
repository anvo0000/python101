#  args = arguments
def add(*args):
    print(args)
    print("number of args", len(args))
    print(args[0])
    result = sum([i for i in args])
    print(result)
# add(2,3,4,1)

# kwargs/kw = keyword arguments
def calculator(n, **kwargs):
    # print(kwargs) # {'add': 3, 'multiply': 5}
    # print(type(kwargs)) # <class 'dict'>
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculator(2, add=3, multiply=5)
