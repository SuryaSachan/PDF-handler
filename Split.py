from PyPDF2 import PdfFileWriter, PdfFileReader
file = PdfFileReader("testfile2.pdf")
output=PdfFileWriter()
print("extract from page no. a to b")
a=int(input("a :"))
b=int(input("b :"))
for i in range(a-1,b):
    output.addPage(file.getPage(i)) 
with open("split.pdf", "wb") as output_stream:
    output.write(output_stream)