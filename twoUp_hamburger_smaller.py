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
pdfWriteFile = splitExt[0] + '_2upSmall' + splitExt[1]

infile = PdfFileReader(open(pdfFile,'rb'))
(w,h) = infile.getPage(0).mediaBox.upperRight
twoUp = PdfFileWriter()

# add existing pages to new PDF Writer (No Scaling)
for i in range(infile.getNumPages()):
    p = infile.getPage(i)
    twoUp.addPage(p)

# this is the new PDF Writer that will have correct page ordering
twoOrder = PdfFileWriter()

for i in (range(int(twoUp.getNumPages()/4))):
    # create a blank page with twice width for 2UP
    twoOrder.addBlankPage(w,h*2)
    # then reorder the pages
    topPage = twoUp.getPage((i*4))
    bottomPage = twoUp.getPage((i*4)+2)
    backTopPage = twoUp.getPage((i*4)+1)
    backBottomPage = twoUp.getPage((i*4)+3)

    currentPage = twoOrder.getPage(i*2)
    currentPage.mergePage(topPage)
    currentPage.mergeTranslatedPage(bottomPage,0,h)

    twoOrder.addBlankPage(w,h*2)
    currentPage = twoOrder.getPage((i*2)+1)
    currentPage.mergePage(backTopPage)
    currentPage.mergeTranslatedPage(backBottomPage,0,h)
    
with open(pdfWriteFile,'wb') as f:
    twoOrder.write(f)
