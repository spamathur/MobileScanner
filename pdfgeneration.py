from reportlab.lib.pagesizes import letter # Generating PDF
from reportlab.pdfgen import canvas # Generating PDF
from io import BytesIO # Transferring image data

def create_pdf(name, image_data):
    c = canvas.Canvas(name, pagesize=letter)
    width, height = letter

    # Add title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, height - 100, "Here is your scanned pdf!")

    # Add the scanned image
    image = BytesIO(image_data)
    c.drawImage(image, 100, height - 300, width=200, height=100) 

    # Save the PDF file
    c.save()