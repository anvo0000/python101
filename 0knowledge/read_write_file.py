# # Method 1
# file = open("myfile.txt")
# content = file.read()
# print(content)
# file.close()


#Method 2- Best practice for dev
with open("myfile.txt") as file:
    content2 = file.read()
    print(content2[:])


# # Write text to the file [Overwrite]
# # mode = [r:read, w:write, a:append]
# with open("myfile.txt", mode="w") as file:
#     file.write("Editable lines")

# #Append text
# with open("myfile.txt", mode="a") as file:
#     file.write("\nMy Name is Anvo0000")
