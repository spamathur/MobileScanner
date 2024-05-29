from reportlab.lib.pagesizes import letter # Generating PDF
from reportlab.pdfgen import canvas # Generating PDF
from io import BytesIO # Transferring image data
from PIL import Image # Helps remove some errors encountered

def create_pdf(name, image_data):
    c = canvas.Canvas(name, pagesize=letter)
    width, height = letter

    # Add title
    c.setFont("Helvetica-Bold", 15)
    c.drawString(100, height - 100, "Here is your scanned pdf!")

    # Add the scanned image
    image = BytesIO(image_data)
    image = Image.open(image)
    
    # Save image to a temporary file
    temp_image_path = "/tmp/temp_image.jpg"
    image.save(temp_image_path)
    
    c.drawImage(temp_image_path, 100, height - 775, width=250, height=650) 

    # Save the PDF file
    c.save()