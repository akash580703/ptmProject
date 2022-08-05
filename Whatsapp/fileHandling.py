from PyPDF2 import PdfReader



def pdfPage(path):
    pdf = PdfReader(path)
    pages = len(pdf.pages)
    return pages


def Price(price,page):
    return price*page

    
