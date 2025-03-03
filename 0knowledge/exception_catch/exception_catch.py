# try:
#     # Sth that might cause an exception
# except:
#     # Do this if there WAS AN EXCEPTION
# else:
#     # Do this if there were NO EXCEPTION
# finally:
#     # Do this no matter what happends.

# FileNotFound
try:
    file = open("a_file.txt")
    a_dict = {"key": "value1"}
    print(a_dict["not_existence_key"])
except FileNotFoundError as file_error:
    file = open("a_file.txt", "w")
    file.write(f"Something")
    print(f'This exception is catching file = open("a_file.txt"), {file_error}')
except KeyError as key_error:
    print(f'This except is catching the line of code: print(a_dict["not_existence_key"]), {key_error}')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed®")
    # raise TypeError("My error")





