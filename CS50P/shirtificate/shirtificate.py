from fpdf import FPDF
def main():
    shirt()


def shirt():
    pdf = FPDF(format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=50)
    pdf.text(40, 40, "CS50 Shirtificate")
    pdf.image("shirtificate.png", x =10 , y=60 , w=190, h=200)
    pdf.set_font("helvetica", style="B", size=25)
    pdf.set_text_color(255,255,255)
    pdf.text(60, 130, f"{input('Name: ')} took CS50")
    pdf.page_mode = "FULL_SCREEN"
    pdf.output("shirtificate.pdf")

main()
