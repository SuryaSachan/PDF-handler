import PyPDF2 as p
import os
import stdiomask

output=p.PdfFileWriter()
input_stream=p.PdfFileReader(open("file path","rb"))

for i in range(0,input_stream.getNumPages()):
    output.addPage(input_stream.getPage(i))

#password=input("password:")
password= stdiomask.getpass()
output.encrypt(password, use_128bit=True)

filename=input("Save as(ex-filename.pdf) :")
with open(filename, "wb") as output_stream:
    output.write(output_stream)