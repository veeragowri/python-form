from flask import Flask, render_template, request, redirect, url_for
import re, csv, os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'change-me-local-dev'

EMAIL_RE = re.compile(r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$', re.I)
PHONE_RE = re.compile(r'^\+?\d{10,15}$')

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, 'data')
CSV_FILE = os.path.join(DATA_DIR, 'submissions.csv')
os.makedirs(DATA_DIR, exist_ok=True)
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp','name','email','phone'])

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = (request.form.get('name') or '').strip()
        email = (request.form.get('email') or '').strip()
        phone = (request.form.get('phone') or '').strip()
        errors = {}
        if not email or not EMAIL_RE.match(email):
            errors['email'] = 'Please enter a valid email address.'
        if not phone or not PHONE_RE.match(phone):
            errors['phone'] = 'Please enter a valid phone number (10-15 digits, optional leading +).'
        if errors:
            return render_template('form.html', errors=errors, name=name, email=email, phone=phone)
        # save
        with open(CSV_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.utcnow().isoformat(), name, email, phone])
        return redirect(url_for('thanks'))
    return render_template('form.html', errors={}, name='', email='', phone='')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    import os
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', '5000'))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() in ('1', 'true', 'yes')
    app.run(debug=debug, host=host, port=port)
