from transformers import pipeline

nlp = pipeline("text2text-generation", model="facebook/bart-large")

def get_ai_suggestions(error_message):
    response = nlp(error_message, max_length=50)
    return response[0]['generated_text']