# merge two pdf files
from PyPDF2 import PdfFileReader, PdfFileMerger
file1 = PdfFileReader("testfile1.pdf")  
file2 = PdfFileReader("testfile2.pdf")
output = PdfFileMerger()
output.append(file1)
output.append(file2)


with open("mergedfile.pdf", "wb") as output_stream:
    output.write(output_stream)