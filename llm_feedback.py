import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def get_ielts_feedback(transcription):
    prompt = f"""
    Act as an IELTS examiner. Assess the following speech transcription:
    "{transcription}"

    Provide a detailed evaluation based on:
    1. Fluency & Coherence
    2. Lexical Resource
    3. Grammatical Range & Accuracy
    4. Pronunciation

    Conclude with suggestions for improvement.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=500
    )
    feedback = response['choices'][0]['message']['content']
    return feedback
def calculate_scores(transcription):
    # Dummy scoring logic (0-9 scale)
    fluency = len(transcription.split()) / 10
    grammar = 7.5  # Example score
    vocabulary = 8  # Example score
    pronunciation = 6.5  # Example score

    return {
        "Fluency": round(fluency, 1),
        "Grammar": grammar,
        "Vocabulary": vocabulary,
        "Pronunciation": pronunciation,
    }