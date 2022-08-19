#write operation
file_ob=open("f1.txt","w")
print("file created")
file_ob.write("my first file created by me...........")
file_ob.close()
file_ob=open("f1.mp4","w")
print("mp4 file created")
file_ob=open("tanuja.docx","w")
print("docx file created")
#append operation
file_ob=open("f1.txt","a")
print("file append")
file_ob.write("my first\n append \n operation")
file_ob.close()
#Read operation
file_ob=open("f1.txt","r")
print("read operation")
txt=file_ob.read()
print(txt)
file_ob.close()
print("end of the file")
#reading n bytes
file_ob=open("f1.txt","r")
print("reading n number of bytes")
txt=file_ob.readline()
txt=file_ob.readlines()
print(txt)
file_ob.close()
file_ob=open("f1.txt","a")
print("file append")
file_ob.write("my first\n append \n operation")
file_ob.writelines()



