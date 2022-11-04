import qrcode
from fpdf import FPDF
from pathlib import Path

url = "https://www.corner.ch/en/cgt-letter-tracking/{round}/{code}"
pdf_folder = "output/pdf"
img_folder = "output/img"
Path(pdf_folder).mkdir(parents=True, exist_ok=True)
Path(img_folder).mkdir(parents=True, exist_ok=True)

for r in ["a", "b", "c", "d", "e", "f", "g", "h"]:

    for c in range(9):

        # filenames
        pdf_filename = pdf_folder + "/" + r + str(c) + ".pdf"
        img_filename = img_folder + "/" + r + str(c) + ".png"
        
        # image
        link = url.format(code = c, round = r)
        img = qrcode.make(link)
        img.save(img_filename)
        
        # pdf 
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 24)
    
        pdf.cell(200, 10, txt = "TEST INTERNO", ln = 1, align = 'C')

        pdf.set_font("Arial", size = 10)
        pdf.cell(200, 15, txt = "Questo esperimento permette di capire quanto tempo impiega una lettera interna a giungere destinazione.", ln = 1, align = 'C')
        
        pdf.set_font("Arial", size = 12)
        pdf.cell(200, 10, txt = "Prendi il tuo Smartphone, inquadra il QR-Code e accedi al link.", ln = 1, align = 'C')

        pdf.image(img_filename, x=43, y=50)
        # separator
        pdf.cell(200, 140, txt = " ", ln = 1, align = 'C')

        pdf.set_font("Arial", size = 10)
        pdf.cell(200, 5, txt = "Se non riesci ad usare la fotocamera del tuo Smartphone, puoi accedere con un browser al seguente link:", ln = 1, align = 'C')
        pdf.cell(200, 5, txt = link, ln = 1, align = 'C')

        pdf.set_font("Arial", size = 12)
        pdf.cell(200, 10, txt = " ", ln = 1, align = 'C')
        pdf.cell(200, 5, txt = "Facendo questo, i nostri sistemi si accorgeranno che questo documento è giunto a destinazione", ln = 1, align = 'C')
        pdf.cell(200, 5, txt = " e ne calcoleranno il tempo in maniera automatica.", ln = 1, align = 'C')

        pdf.set_font("Arial", size = 12)
        pdf.cell(200, 10, txt = " ", ln = 1, align = 'C')
        pdf.cell(200, 5, txt = "Grazie per la collaborazione!", ln = 1, align = 'C')
        pdf.cell(200, 5, txt = "Matteo e Lorenzo", ln = 1, align = 'C')
        
        pdf.output(pdf_filename)