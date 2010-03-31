#!/bin/env python
"""pdfMerger doc

pdfmerger.py docOutput docInput1 docInput2 ... docInputN
"""

import sys
import getopt

from pyPdf import PdfFileWriter, PdfFileReader

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    if len(args) < 2:
        print __doc__
        sys.exit(0)
    # process arguments
    outfileName = args[0]
    output = PdfFileWriter()
    for arg in args[1:]:
        input = PdfFileReader(file(arg, "rb"))
        for i in range(input.getNumPages()):
            output.addPage(input.getPage(i))
    outputStream = file(outfileName, "wb")
    output.write(outputStream)
    outputStream.close()


if __name__ == "__main__":
    main()
