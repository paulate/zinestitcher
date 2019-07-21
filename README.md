# zinestitcher
 takes a pdf and outputs a version for printing double-sided to fold it into a book.

## usage
In terminal, type `python twoUp_hamburger.py '[filename.pdf]'` to output a .pdf file in the same directory as the filename.pdf.
The output pdf can be printed on a duplex printer (settings: letter paper, scale to fit page, short-edge binding) and then folded in half to create a half-page-size booklet.

Run `python twoUp_hamburger_smaller.py '[stitched_file.pdf]'` using the output file of the above terminal command to get a .pdf file that
creates quarter-page-size booklets from letter paper. (settings: letter paper, scale to fit page, long-edge binding) The output pages must be
chopped in half and then folded together to create a quarter-page booklet.

## dependencies
* PyPDF2

## known wrongs
* twoUp_hamburger_smaller.py doesn't order the pages for easy assembly - you need to collate afterwards.
* the python filenames and output names are kind of confusing
