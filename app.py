from flask import Flask, request, redirect, render_template
import sqlite3
import string
import random
import os

app = Flask(__name__)

# Initialize DB
def init_db():
    if not os.path.exists("database.db"):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, long_url TEXT, short_code TEXT UNIQUE)')
        conn.commit()
        conn.close()

init_db()

# Generate unique short code
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    if request.method == 'POST':
        long_url = request.form['long_url']
        code = generate_code()
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO urls (long_url, short_code) VALUES (?, ?)', (long_url, code))
        conn.commit()
        conn.close()
        short_url = request.host_url + code
    return render_template('index.html', short_url=short_url)

@app.route('/<code>')
def redirect_to_long_url(code):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT long_url FROM urls WHERE short_code = ?', (code,))
    result = c.fetchone()
    conn.close()
    if result:
        return redirect(result[0])
    return "URL not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
