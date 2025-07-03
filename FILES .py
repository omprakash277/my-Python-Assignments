#Q.1 Write a program to read text file
#answr

f = open("om story.txt","r")
content = f.read()
print(content)

#Q.2 Write a program to write text to .txt file using  InputStream
#answr
# Open the file in write mode
with open("om story.txt", "w") as file:
    # Read input from user (simulating InputStream)
    text = input("Enter text to write to file: ")
    # Write the input text to the file
    file.write(text + "\n ")


#Q.3  Write a program to read a file stream
#answr
with open('om2.txt', 'r') as file:
    content = file.read()
    print(content)


#Q.4 Write a program to read a file stream supports random access
#answr
with open('om story.txt', 'r') as f:
    f.seek(1)
    print(f.read(6))
    print(f.tell())
    f.seek(1, 2)
    print(f.read(10))

#Q.5 Write a program to read a file a just to a particular index using seek()
#answr
with open('om2.txt', 'r') as file:
    file.seek(1)
    content = file.read()
    print(content)
