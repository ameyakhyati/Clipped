from flask import Flask, render_template, request
from summarizer import summarize_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    if request.method == 'POST':
        text = request.form['text']
        if text:
            summary = summarize_text(text, max_length=150, min_length=40, num_lines=3)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)