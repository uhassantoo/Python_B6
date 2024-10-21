import os
# What are the 4 file handling functions?
#  The four primary functions used for file handling in Python are: 


#  open()  : Opens a file and returns a file object. 
#  read()  : Reads data from a file. 
#  write()  : Writes data to a file. 
#  close()  : Closes the file, releasing its resources. 

def createfile(filename):
    with open(filename , 'w') as f:
        print('File ' +filename+ 'Created')
        
def readfile(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        print(contents)

def append_file(filename , text):
    with open(filename, 'a') as f:
        f.write(text)
        print('text Append to file ' +filename +'Successfully')

#rename the file
def rename_file(filename,new_file):
    os.rename(filename , new_file)
    print('File : '+filename+ 'renamed to '+new_file+ 'Changed File name')

# delete the file
        

filename = 'example.txt'
new_file = 'new_example.txt'

createfile(filename)
readfile(filename)
append_file(filename, 'This is a new line use the file append . \n')
readfile(filename)
rename_file(filename, new_file)
readfile(new_file)