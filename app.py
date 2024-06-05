from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)

# Ensure the 'submissions' folder exists
if not os.path.exists('submissions'):
    os.makedirs('submissions')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'Full Name': request.form['fullName'],
        'University and Department': request.form['university'],
        'Email Address': request.form['email'],
        'Phone Number': request.form['phone'],
        'Idea Title': request.form['ideaTitle'],
        'Industry': request.form['industry'],
        'Short Description': request.form['description'],
        'Potential Impact': request.form['impact'],
        'Unique Selling Point': request.form['usp']
    }

    df = pd.DataFrame([data])
    file_path = os.path.join('submissions', 'submissions.xlsx')

    if os.path.exists(file_path):
        existing_df = pd.read_excel(file_path)
        df = pd.concat([existing_df, df], ignore_index=True)

    df.to_excel(file_path, index=False)

    return 'Success', 200

if __name__ == '__main__':
    app.run(debug=True)
