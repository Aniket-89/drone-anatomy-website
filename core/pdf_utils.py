from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import os


def generate_pdf(name, email, message):
    try:
        # Create a temporary file
        temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
        pdf_path = temp_pdf.name

        # Generate the PDF
        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter
        margin = 72  # 1 inch margin

        c.drawString(margin, height - margin, f"Name: {name}")
        c.drawString(margin, height - margin - 20, f"Email: {email}")
        c.drawString(margin, height - margin - 40, "Message:")

        text_object = c.beginText(margin, height - margin - 60)
        text_object.setFont("Helvetica", 12)
        text_object.setTextOrigin(margin, height - margin - 60)
        for line in message.split('\n'):
            text_object.textLine(line)
        c.drawText(text_object)
        c.showPage()
        c.save()

        return pdf_path

    except Exception as e:
        print(f"Error generating PDF: {e}")
        raise
