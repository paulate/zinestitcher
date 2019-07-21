from PyPDF2 import PdfFileWriter, PdfFileReader
import PyPDF2
import os, sys

# You can run:
# python twoUp_sizeFix_hamburger.py 'filename.pdf'
if len(sys.argv) > 1:
    pdfFile = sys.argv[1]
else:
    pdfFile = 'johnCage.pdf'
splitExt = os.path.splitext(pdfFile)
pdfWriteFile = splitExt[0] + '_2upLetter' + splitExt[1]

infile = PdfFileReader(open(pdfFile,'rb'))
(w,h) = infile.getPage(0).mediaBox.upperRight
twoUp = PdfFileWriter()

# add existing pages to new PDF Writer (No Scaling)
for i in range(infile.getNumPages()):
    p = infile.getPage(i)
    twoUp.addPage(p)

# add blank pages to get correct twoUp / twoFold layout (# pages must be divisible by 4)
while twoUp.getNumPages() % 4:
    twoUp.addBlankPage()

# this is the new PDF Writer that will have correct page ordering
twoOrder = PdfFileWriter()

for i in (range(int(twoUp.getNumPages()/2))):
    # create a blank page with twice width for 2UP
    twoOrder.addBlankPage(w*2,h)
    # then reorder the pages
    if i % 2:
            leftPage = twoUp.getPage(i)
            rightPage = twoUp.getPage(twoUp.getNumPages()-i-1)
    else:
            leftPage = twoUp.getPage(twoUp.getNumPages()-i-1)
            rightPage = twoUp.getPage(i)
    currentPage = twoOrder.getPage(i)
    currentPage.mergePage(leftPage)
    currentPage.mergeTranslatedPage(rightPage,w,0)

with open(pdfWriteFile,'wb') as f:
    twoOrder.write(f)
