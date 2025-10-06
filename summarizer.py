from transformers import pipeline
import re

# Initialize summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_length=80, min_length=10, num_lines=3):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=True)
    summary_text = summary[0]['summary_text']  # Extract only the text
    
    # Optional: Clean up extra spaces and ensure readable formatting
    summary_text = re.sub(r'\s+', ' ', summary_text).strip()
    
    # Optional: Split into limited number of lines (if needed)
    sentences = re.split(r'(?<=[.!?]) +', summary_text)
    summary_text = ' '.join(sentences[:num_lines])
    
    return summary_text
