import argparse
from PyPDF2 import PdfFileWriter, PdfFileReader

parser = argparse.ArgumentParser()
parser.add_argument("-input", help="Pdf file to be encoded", type=str)
parser.add_argument("-output", help="Name of the encoded pdf file", type=str)
parser.add_argument("-password", help="Password to set", type=str)
args = parser.parse_args()

pdfwriter = PdfFileWriter()
pdf = PdfFileReader(args.input)
for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))
pdfwriter.encrypt(args.password)
with open(args.output, 'wb') as f:
    pdfwriter.write(f)
    f.close()
