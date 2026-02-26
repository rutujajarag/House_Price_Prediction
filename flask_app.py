import pickle
from flask import Flask, render_template,request

app = Flask(__name__)
with open('model.pkl','rb') as f:
    model = pickle.load(f)
@app.route('/price',methods=[ 'GET','POST'])
def priceView():
    if request.method == 'GET':
        return render_template('price.html')
    elif request.method =='POST':
        size_sqft = int(request.form['sq'])
        no_bedrooms =int(request.form['bed'])
        no_bathrooms = int(request.form['br'])
        age_house = int(request.form['age'])
        distance_city= int(request.form['dtc'])
        y_pred = model.predict([[size_sqft, no_bedrooms, no_bathrooms,age_house,distance_city]])
        y_pred = round(y_pred[0],2)

        return render_template('prediction.html',ans=y_pred)

app.run(debug=True)