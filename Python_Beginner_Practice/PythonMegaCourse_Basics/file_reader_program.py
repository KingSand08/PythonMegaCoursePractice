myfile = open("files/fruits.txt")
textFileContent = myfile.read()
print(textFileContent)
myfile.close()

# same as this, with will close file after ending this
with open("files/fruits.txt") as myfile:
    textFileContent = myfile.read()
    print(textFileContent)
