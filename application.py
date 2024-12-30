from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
import locale

locale.setlocale(locale.LC_ALL, 'en-IN.UTF-8')

car = pd.read_csv('Cleaned_data.csv')
model = pickle.load(open('LinearRegressor.pkl', 'rb'))

companies = sorted(car['company'].unique())
car_name = sorted(car['name'].unique())
years = sorted(car['year'].unique(), reverse=True)
fuel_type = sorted(car['fuel_type'].unique())

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html' , companies=companies, car_name=car_name, years=years, fuel_type=fuel_type)
 
@app.route("/predict", methods=['POST'])
def predict():
    company = request.form.get("company")
    carname = request.form.get("car_name")
    year = request.form.get("year")
    fueltype = request.form.get("fuel_type")
    kms = request.form.get("kms")

    print(carname, company, year, kms, fueltype)
    prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([carname,company,year,kms,fueltype]).reshape(1, 5)))
    prediction = locale.format_string("%.2f",prediction[0], grouping=True)
    
    return render_template('index.html' , companies=companies, car_name=car_name, years=years, fuel_type=fuel_type, prediction=prediction)

@app.route("/get_car_names", methods=['GET'])
def get_car_names():
    company = request.args.get('company')
    if not company:
        return {"car_names": []}

    # Filter car names based on the company
    filtered_car_names = [name for name in car_name if name.lower().startswith(company.lower())]
    return {"car_names": filtered_car_names}


if __name__ == "__main__":
    app.run(debug=True)