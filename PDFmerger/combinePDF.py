import PyPDF2
import os

#go to the directory where the pdfs are stored
os.chdir('c://users//kosta//desktop')

#open the pdfs you want to merge
pdf1File = open('1.pdf','rb')
pdf2File = open('2.pdf','rb')

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

#new PDF 
writer = PyPDF2.PdfFileWriter()

#loop to copy every single page of each pdf
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)
    
for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)
    
    
#paste the pages to the new pdf named combinedPDF.pdf   
outputFile = open('combinedpdf.pdf','wb')
writer.write(outputFile)

#close open files
outputFile.close()
pdf1File.close()
pdf2File.close()
