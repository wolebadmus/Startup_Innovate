from flask import Flask, render_template, request, redirect, url_for, flash
#import sheets  # Import the sheets module
from sheets import append_row
import os

application = Flask(__name__)
application.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_key_for_development')  # Use a default key for development

@application.route('/')
def index():
    return render_template('index.html')


@application.route('/terms_and_conditions.html')
def terms_and_conditions():
    return render_template('terms_and_condition.html')

@application.route('/submit', methods=['POST'])
def submit():
    full_name = request.form['fullName']
    email = request.form['email']
    idea_title = request.form['ideaTitle']
    industry = request.form['industry']
    description = request.form['description']
    impact = request.form['impact']
    usp = request.form['usp']
    
 #    Prepare data to append
    data = [full_name, email, idea_title, industry, description, impact, usp]
    
 #    Append data to Google Sheets
    try:
        append_row(data)
 #        flash('Your idea has been submitted successfully!')
    except Exception as e:
 #        flash(f'There was an error submitting your idea: {e}')
        return redirect(url_for('index', error=True))
    
    return redirect(url_for('index', success=True))


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
