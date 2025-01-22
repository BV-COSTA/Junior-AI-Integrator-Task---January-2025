import tkinter as tk
from tkinter import messagebox, ttk
from threading import Thread
from speech_to_text import transcribe_speech
from llm_feedback import get_ielts_feedback
from generate_pdf import generate_pdf

root = tk.Tk()
root.title("IELTS Practice Tool")
root.geometry("600x500")
root.config(bg="#2c3e50")  # Dark background color

is_recording = False

def start_practice():
    instructions_label.config(text="Practice Mode: Speak to get instant feedback.")
    start_recording()

def start_test_part(part):
    if part == 1:
        instructions_label.config(text="Part 1: Introduction. Please introduce yourself.")
        messagebox.showinfo("Part 1", "Please introduce yourself.")
    elif part == 2:
        instructions_label.config(text="Part 2: Long Turn. Talk about the cue card.")
        messagebox.showinfo("Part 2", "Talk about the cue card.")
    elif part == 3:
        instructions_label.config(text="Part 3: Two-Way Discussion. Let's discuss your views.")
        messagebox.showinfo("Part 3", "Let's discuss your views.")
    start_recording()

def start_recording():
    global is_recording
    if not is_recording:
        is_recording = True
        status_label.config(text="Recording in progress...", fg="orange")
        threading = Thread(target=process_speech)
        threading.start()

def process_speech():
    transcription = transcribe_speech()
    if transcription:
        feedback = get_ielts_feedback(transcription)
        generate_pdf(transcription, feedback)
        messagebox.showinfo("Feedback", f"Instant feedback:\n{feedback}\nPDF generated.")
    else:
        messagebox.showerror("Error", "No speech detected. Please try again.")
    global is_recording
    is_recording = False
    status_label.config(text="Ready to start.", fg="green")

def toggle_mode(mode):
    if mode == "Practice":
        instructions_label.config(text="Practice Mode: Speak to get instant feedback.")
        start_practice()
    elif mode == "Test":
        current_part = 1
        start_test_part(current_part)

frame = ttk.Frame(root, padding="20")
frame.pack(pady=30)

practice_button = ttk.Button(frame, text="Start Practice Mode", command=lambda: toggle_mode("Practice"), width=20, style="Accent.TButton")
practice_button.grid(row=0, column=0, padx=20, pady=10)

test_button = ttk.Button(frame, text="Start Test Mode", command=lambda: toggle_mode("Test"), width=20, style="Accent.TButton")
test_button.grid(row=0, column=1, padx=20, pady=10)

instructions_label = tk.Label(root, text="Choose a mode to begin practicing or testing your IELTS speaking skills.",
                              wraplength=500, font=("Arial", 12), bg="#2c3e50", fg="black")  # Text color changed to black
instructions_label.pack(pady=20)

status_label = tk.Label(root, text="Ready to start.", font=("Arial", 12), bg="#2c3e50", fg="green")
status_label.pack(pady=10)

style = ttk.Style()
style.configure("Accent.TButton", font=("Arial", 12), foreground="white", background="#0078d4")
style.map("Accent.TButton", background=[("active", "#005a9e")])

root.mainloop()