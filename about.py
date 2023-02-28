import streamlit as st

def app():
    st.title("Glass Classification Problem")
    st.subheader('This is a Glass Identification Data Set from UCI. It contains 10 attributes including id. The response is glass type(discrete 7 values).')
    st.subheader('Attributes:')
    st.text('''Id number: 1 to 214 (removed from CSV file)
RI: refractive index
Na: Sodium (unit measurement: weight percent in corresponding oxide, as are attributes 4-10)
Mg: Magnesium
Al: Aluminum
Si: Silicon
K: Potassium
Ca: Calcium
Ba: Barium
Fe: Iron
Type of glass: (class attribute)
-- 1 buildingwindowsfloatprocessed -- 2 buildingwindowsnonfloatprocessed -- 3 vehiclewindowsfloatprocessed
-- 4 vehiclewindowsnonfloatprocessed (none in this database)
-- 5 containers
-- 6 tableware
-- 7 headlamps''')

    st.subheader("Reference: https://archive.ics.uci.edu/ml/datasets/Glass+Identification")