import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_page_number_pdf(num_pages, output):
    c = canvas.Canvas(output, pagesize=letter)
    width, height = letter
    
    for i in range(num_pages):
        c.drawString(width - 100, 10, f"Page {i + 1}")
        c.showPage()
    
    c.save()

def merge_pdfs(pdf_list, output):
    pdf_writer = PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PdfReader(pdf)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output, 'wb') as out:
        pdf_writer.write(out)

def main():
    input_dir = '.'  # Répertoire courant
    output_pdf = 'book_of_abstracts.pdf'
    page_number_pdf = 'page_numbers.pdf'

    # Récupérer tous les fichiers PDF dans le répertoire
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
    pdf_files.sort()

    # Fusionner les fichiers PDF
    merge_pdfs(pdf_files, output_pdf)

    # Créer un PDF de numéros de page
    pdf_reader = PdfReader(output_pdf)
    num_pages = len(pdf_reader.pages)
    create_page_number_pdf(num_pages, page_number_pdf)

    # Fusionner le PDF original avec le PDF des numéros de page
    final_output = 'final_book_of_abstracts.pdf'
    final_writer = PdfWriter()

    for i in range(num_pages):
        final_writer.add_page(pdf_reader.pages[i])
        # Ajouter la page de numéro de page
        page_num_reader = PdfReader(page_number_pdf)
        final_writer.add_page(page_num_reader.pages[i])

    with open(final_output, 'wb') as out:
        final_writer.write(out)

    print(f'Le book of abstracts avec pagination a été créé : {final_output}')

if __name__ == '__main__':
    main()
