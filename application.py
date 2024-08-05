from flask import Flask, render_template, request, redirect, url_for, flash
#import sheets  # Import the sheets module
from sheets import append_row
import os
import requests

application = Flask(__name__)
application.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_key_for_development')  # Use a default key for development

BASE_PATH = application.root_path

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
        url = "https://script.google.com/macros/s/AKfycbwY5lLQ5CmivUW7-n7SRuCZDvKH4IJWVhop9i1bP03tnrTshWR0PkXYEBUzCQnSfKiBYw/exec"
       
        payload = {
            "fullName": data[0],
            "email": data[1],
            "ideaTitle": data[2],
            "industry": data[3],
            "description": data[4],
            "impact": data[5],
            "usp": data[6]       
        }

        response = requests.post(url, data=payload)
   

        
 #       append_row(data, BASE_PATH)
 #        flash('Your idea has been submitted successfully!')
        return redirect(url_for('success'))
    except Exception as e:
        print(f"ERROR {e}")
        return redirect(url_for('index', error=True))
    
    return redirect(url_for('index', success=True))


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=9000)
