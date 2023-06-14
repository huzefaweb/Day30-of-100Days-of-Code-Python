# file not found error
# with open("a_text.txt") as file:
#     file.read()

# key error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non__existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Exceptions:
# try: trying to run something that might cause an exception, sometimes the code might run but sometimes not
# except: do this is there is exception(something goes wrong)
# else: do this if there was no exception
# finally: do this no matter what happens

# file not found
# first try block would try to run the code if don't work then the except block
# try:
#     file = open("a_text.txt")
# except:
#     file = open("a_text.txt", "w")
#     file.write("something")

# if we want to catch a specific error(exception) then do this
# try:
#     file = open("a_text.txt")
#     dicti = {"key": "value"}
#     print(dicti["sdf"])
# except FileNotFoundError:
#     file = open("a_text.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:  # this code block would only run if the try block would have no exception
#     content = file.read()
#     print(content)
# finally:  # this code would execute no matter what happens
#     file.close()
#     print("file was closed")
# raise ValueError("This value should not be like this")  # this would raise an error by yourself
