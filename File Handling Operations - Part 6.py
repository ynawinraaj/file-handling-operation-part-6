
# chek if file exists
import os
print("checing if the file exists or not")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file does not exists")
    
# create new file
my_file=open("my_file.txt","w")
my_file.write("the sweetes snaks is kolukatai")
my_file.close()
# delete the file named codingal
os.remove('Codingal.txt')
os.rmdir('Folder')