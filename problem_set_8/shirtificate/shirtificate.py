from fpdf import FPDF


# Gather name from user
name = input('Name: ')

# Instantiation of inherited class
pdf = FPDF(orientation="P", unit="mm", format="A4")
# Disable auto page break to allow image overflow
pdf.set_auto_page_break(False)

pdf.add_page()
# Insert image
pdf.image("shirtificate.png", x=1, y=40)
# Set font to helvetica and size 32
pdf.set_font('helvetica', "B", 32)
# Add title
pdf.cell(w=0, h=12, text="CS50 Shirtificate", border=0, align="C")
# Set font to size 24
pdf.set_font('helvetica', "B", 24)
# Set text color to white
pdf.set_text_color(255, 255, 255)
# Add user name
pdf.cell(w=-185, h=185, text=f"{name} took CS50", border=0, align="C")
# Save pdf
pdf.output("shirtificate.pdf")
