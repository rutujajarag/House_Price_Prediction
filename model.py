#1 Import Necessaries Libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

#2 Create Datast
df=pd.read_csv('house_price_data.csv')

#3 Extract X and y
X=df[['size_sqft','no_of_bedrooms','no_of_bathrooms','age_of_house_years','distance_to_city_centre_miles']]
y=df['price_lakhs']

#4 Create Linear Model
model=LinearRegression()

#5 Train the Model
model.fit(X,y)

#6 Make Prediction
model.predict([[600,1,1,20,15,]])

#7 Save Model in pickle file
with open('model.pkl','wb') as f:
    pickle.dump(model,f)