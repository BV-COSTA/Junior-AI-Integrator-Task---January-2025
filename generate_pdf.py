from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(transcription, feedback):
    """Generates a PDF report with transcription and feedback."""
    # Define PDF file path
    file_path = "IELTS_Feedback_Report.pdf"

    # Create PDF
    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Add content to PDF
    c.drawString(100, 750, "IELTS Speaking Test Feedback Report")
    c.drawString(100, 730, f"Transcription: {transcription}")
    c.drawString(100, 710, f"Feedback: {feedback}")

    # Save the PDF
    c.save()

    print(f"PDF generated and saved as {file_path}")