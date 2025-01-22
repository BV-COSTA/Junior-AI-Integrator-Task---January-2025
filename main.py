# main.py

from speech_to_text import transcribe_speech
from llm_feedback import get_ielts_feedback
from generate_pdf import generate_pdf

def main():
    print("Starting the program...")

    # Step 1: Transcribe speech
    print("Transcribing speech...")
    transcription = transcribe_speech()
    if not transcription:
        print("No transcription received. Please check your microphone or speak louder.")
        return
    print(f"Transcription: {transcription}")

    # Step 2: Generate feedback
    print("Generating feedback...")
    feedback = get_ielts_feedback(transcription)  # Updated function call
    if not feedback:
        print("Feedback generation failed. Check your LLM API or input data.")
        return
    print(f"Feedback: {feedback}")

    # Step 3: Generate PDF report
    print("Generating PDF report...")
    try:
        generate_pdf(transcription, feedback)
        print("PDF generated successfully! Check your output directory.")
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return


if __name__ == "__main__":
    main()