from flask import *
import pyrebase
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
app = Flask(__name__)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Appoinments").sheet1  # Open the spreadhseet

def add_row(arr):
    data = sheet.get_all_records()
    today = datetime.today()
    for _, bno in enumerate(data):
        d = datetime.strptime(bno["d"], '%Y-%m-%d')
        if d < today:
            sheet.delete_row(_ + 2)
    data = sheet.get_all_records()
    n = len(data) + 2
    for i, k in enumerate(arr):
        sheet.update_cell(n, i+2, k)

config = {
   "apiKey": ",
   "authDomain":,
   "projectId": "",
   "databaseURL": "\",
   "storageBucket": "\",
   "messagingSenderId": "\",
   "appId": "",
   "measurementId": "\"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

app.secret_key = "hello"

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/book')
def book():
   return render_template('book.html')

@app.route('/services')
def services():
   return render_template('services.html')

@app.route('/otp', methods =['POST', 'GET'])
def otp():
   if request.method == 'POST':
      name= request.form["name"]
      number= request.form["number"]
      treatment= request.form["treatment"]
      datee= request.form["datee"]
      time= request.form["time"]
      data = [datee, name, number, treatment, time]
      add_row(data)
   return render_template('otp.html', name=name)

if __name__ == '__main__':
   app.run(debug = True)