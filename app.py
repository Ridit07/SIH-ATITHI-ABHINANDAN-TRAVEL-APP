try:
    model = pickle.load(open('decision_tree_model (1).pkl', 'rb'))
except FileNotFoundError:
    st.error("Model file not found.")
    st.stop()
except Exception as e:
    st.error("Error loading the model: {}".format(e))
    st.stop()


import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('decision_tree_model (1).pkl', 'rb'))

st.title('Which Destination Will They Choose')

Traveller_Profile_Type = st.slider("Traveller Profile Type", 0, 3)
Choice_Preference = st.slider("Choice/Preference", 0, 3)
Mode_of_Travel = st.slider("Mode of Travel", 0, 3)
Budget = st.slider("Budget", 10000, 1000000)


def predict():
    try:
        float_features = [float(Traveller_Profile_Type), float(Choice_Preference), float(Mode_of_Travel), float(Budget)]
        final_features = [np.array(float_features)]
        prediction = model.predict(final_features)
        label = prediction[0]

        if int(label) == 1:
            st.success('Hurray!! The customer will make a purchase :thumbsup:')
        else:
            st.success('Ohh, the customer won\'t make a purchase :thumbsdown:')
    except Exception as e:
        st.error("Error during prediction: {}".format(e))


if st.button('Predict'):
    predict()

