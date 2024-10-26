from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():

    pdf = FPDF(orientation='P', unit='mm', format='A4')

    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=17, txt='Variable', border=0, ln=1, align='L')
    pdf.line(10, 23, 200, 23)

pdf.output("output.pdf")



