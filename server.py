from flask import Flask, render_template, request, redirect, Response
import csv
import datetime

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open("/home/stefanshipinkoski/portfolio_website/database.csv", 'a', newline='') as csv_file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message, timestamp])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong, please try again'


@app.route('/robots.txt')
def noindex():
    r = Response(response="User-Agent: *\nDisallow: \n", status=200, mimetype="text/plain")
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r