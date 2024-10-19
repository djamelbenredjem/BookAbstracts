#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:22:54 2024

@author: djamelbenredjem
"""

import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pdf_list, output):
    pdf_writer = PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PdfReader(pdf)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output, 'wb') as out:
        pdf_writer.write(out)

def main():
    # Répertoire courant
    input_dir = '.'  # Répertoire courant
    output_pdf = 'book_of_abstracts.pdf'

    # Récupérer tous les fichiers PDF dans le répertoire
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]

    # Trier les fichiers PDF par nom si nécessaire
    pdf_files.sort()

    # Fusionner les fichiers PDF
    merge_pdfs(pdf_files, output_pdf)

    print(f'Le book of abstracts a été créé : {output_pdf}')

if __name__ == '__main__':
    main()
