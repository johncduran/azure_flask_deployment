from flask import Flask, render_template
import pandas as pd
import random
from faker import Faker

fake = Faker()

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/random')
def randomnumber():
    number_var = random.randint(1,10000)
    fake_address = fake.address()
    return render_template('random.html', single_number = number_var, single_address = fake_address)

@app.route('/data')
def datapage():
    csv = pd.read_csv('https://raw.githubusercontent.com/johncduran/azure_flask_deployment/main/data_files_used/adult-depression-lghc-indicator-24.csv')
    return render_template('data.html', first_csv = csv)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )