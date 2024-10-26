from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    # Set up the header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=17, txt=row['Topic'], border=0, ln=1, align='L')
    pdf.line(10, 23, 200, 23)

    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=9)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], border=0, ln=1, align='R')

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=9)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], border=0, ln=1, align='R')

pdf.output("output.pdf")
