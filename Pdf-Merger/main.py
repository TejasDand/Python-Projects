import PyPDF2

pdf_files = ["dummy.pdf", "sample.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdf_files:
    
    with open(filename, 'rb') as pdf_File:
        pdf_reader = PyPDF2.PdfReader(pdf_File)
        merger.append(pdf_reader)

merger.write('merged.pdf')