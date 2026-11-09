
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enquiry', methods=['GET', 'POST'])
def enquiry():
    submitted = False

    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        message = request.form.get('message')

        if name and phone and message:
            submitted = True

    return render_template('enquiry.html', submitted=submitted)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
