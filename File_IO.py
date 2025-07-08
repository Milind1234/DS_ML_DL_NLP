# # Open a file for reading
# file = open('demo.txt', 'r')

# # Read the first line of the file
# line = file.readline()

# # Loop through the rest of the file and print each line
# while line:
#     print(line)
#     line = file.readline()

# # Close the file when you're done
# file.close()

# program to read data
# f= open("demo.txt", "r")
# data=f.read()
# print(data)
# f.close()

# program to read letters in data
# f= open("demo.txt", "r")
# data=f.read(5)
# print(data)
# f.close()

# program to read line in data
# f=open("demo.txt","r")
# line1 = f.readline()
# line2 = f.readline()
# print(line1)
# print(line2)
# f.close()

# f = open("demo.txt","w")
# data = f.write("Hi this is milind! You are watching the venom's gameplay at the very best moment of you life")
# f.close()

# f = open("demo.txt","a")
# f.write("You are watching the work of art. You are at the best")0
# f.close()

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
#     print(f)

# WAF to replace words in txt file
# def replace_words(): 
#     with open("practice.txt","r") as f:
#         data = f.read()
#     new_data=data.replace("Java", "Python")
#     print(new_data)
#     with open("practice.txt","w") as f:
#         f.write(new_data)
# replace_words()

# WAF to search word exits in file or not
# def check_word():
#     word = "learning" 
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if (data.find(word) != -1):
#             print("Found")
#         else:
#             print("not found")
# check_word()

# WAF to find in which line of file  does the word "learning" occurs first.
# def find_line():
#     word = "xlearning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no += 1

#     return -1
# print(find_line())

# Waf from a file containing numbers seperated by cooma, print the count of even numbers
# with open("demo.txt", "r") as f:
#     data = f.read()
#     count = 0
#     num = ""
#     for char in data:
#         if char == ",":
#             if num:  # Ensure num is not empty
#                 if int(num) % 2 == 0:
#                     count += 1
#                 num = ""
#         else:
#             num += char
#     # Check last number if no trailing comma
#     if num:
#         if int(num) % 2 == 0:
#             count += 1
# print("Count of even numbers:", count)

# Another method using split
# with open("demo.txt","r") as f:
#     data = f.read()

#     count = 0
#     nums = data.split(",")
#     for val in nums:
#         if (int(val)%2 == 0):
#             count +=1
# print("No of even no's in the file are:",count)