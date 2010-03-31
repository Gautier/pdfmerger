#!/bin/env python
"""pdfMerger doc

pdfmerger.py docOutput docInput1 docInput2 ... docInputN
"""

import sys
import getopt

from pyPdf import PdfFileWriter, PdfFileReader

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr", ["help", "rotate"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    docs = args
    rotate = 0
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
        if o in ("-r", "--rotate"):
            rotate = int(args[0])
            docs = args[1:]
    if len(args) < 2:
        print __doc__
        sys.exit(0)
    # process arguments
    outfileName = docs[0]
    output = PdfFileWriter()
    for arg in docs[1:]:
        input = PdfFileReader(file(arg, "rb"))
        for i in range(input.getNumPages()):
            page = input.getPage(i)
            if rotate != 0:
                page = page.rotateClockwise(rotate)
            output.addPage(page)
    outputStream = file(outfileName, "wb")
    output.write(outputStream)
    outputStream.close()


if __name__ == "__main__":
    main()
