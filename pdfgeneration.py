from reportlab.lib.pagesizes import letter # Generating PDF
from reportlab.pdfgen import canvas # Generating PDF

def create_pdf(name, image):
    c = canvas.Canvas(name, pagesize=letter)
    width, height = letter

    # Add title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, height - 100, "Hello, PDF World!")

    # Add some text
    c.setFont("Helvetica", 12)
    text = "This is a simple PDF file created using the reportlab library in Python."
    c.drawString(100, height - 150, text)

    # Save the PDF file
    c.save()