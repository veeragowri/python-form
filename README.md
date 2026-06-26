# Simple Flask Form Project

This small Flask app provides a form with the following fields:

- Name
- Email ID (mandatory)
- Phone Number (mandatory)

Validation
- Email: basic regex validation
- Phone: digits with optional leading +, 10-15 digits

On successful submission the data is appended to `data/submissions.csv` and the user is shown a confirmation page.

Quick start

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

Notes
- This is intentionally minimal and suitable for local testing. For production, configure a proper secret key, use HTTPS, and secure storage.
 - To run and make the site reachable on your local network, use the helper script:

```bash
./run.sh
```
Then open http://<your-machine-ip>:5000 from other devices on the same network.
