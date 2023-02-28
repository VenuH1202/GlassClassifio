import streamlit as st
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
import pandas as pd
import numpy as np

def app():
    st.title("Can you correctly identify glass type?")
    st.text('''-- 1 buildingwindowsfloatprocessed -- 2 buildingwindowsnonfloatprocessed -- 3 vehiclewindowsfloatprocessed
-- 4 vehiclewindowsnonfloatprocessed (none in this database)
-- 5 containers
-- 6 tableware
-- 7 headlamps''')
    RI = st.number_input('Enter the value of refractive index:')
    Na = st.number_input('Enter the value of Sodium present in the sample:')
    Mg = st.number_input('Enter the value of Magnesium present in the sample:')
    Al = st.number_input('Enter the value of Aluminium present in the sample:')
    Si = st.number_input('Enter the value of Silicon present in the sample:')
    K = st.number_input('Enter the value of Potassium present in the sample:')
    Ca = st.number_input('Enter the value of Calcium present in the sample:')
    Ba = st.number_input('Enter the value of Barium present in the sample:')
    Fe = st.number_input('Enter the value of Iron present in the sample:')

    df = pd.read_csv("glass.csv")
    X = df.drop('Type', axis=1)
    y = df['Type']

    scaler = RobustScaler()
    X = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    vector = np.array([RI,Na,Mg,Al,Si,K,Ca,Ba,Fe])
    vector = vector.reshape(1,-1)
    if vector.all():
        output = dt.predict(vector)
        st.subheader("Based on the given inputs, The glass type must be:")
        st.subheader(output)
    else:
        st.title("Please Wait!!")



