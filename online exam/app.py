from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Madrid'],
        'answer': 'Paris'
    },
    {
        'question': 'Which programming language is this exam built with?',
        'options': ['Java', 'C++', 'Python', 'JavaScript'],
        'answer': 'Python'
    },
    
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exam', methods=['GET', 'POST'])
def exam():
    if request.method == 'POST':
        answers = request.form.to_dict()
        score = 0
        for i, question in enumerate(questions):
            if answers.get(f'question_{i}') == question['answer']:
                score += 1
        return render_template('result.html', score=score, total=len(questions))

    return render_template('exam.html', questions=questions)

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
