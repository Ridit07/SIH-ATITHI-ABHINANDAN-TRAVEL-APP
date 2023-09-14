import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('project.pkl', 'rb'))

st.title('Will the person make a purchase or not')

PageValues = st.slider("PageValues",0.00,200.76)
ExitRates = st.slider("ExitRates",0.000,0.200,step=0.001,format="%.3f")
ProductRelated_Duration = st.slider("ProductRelated_Duration",0.00,15000.00)
ProductRelated = st.slider("ProductRelated",0,200)


def predict():
    float_features = [float(x) for x in [PageValues, ExitRates, ProductRelated_Duration, ProductRelated]]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    label = prediction[0]
    
    print(type(label))
    print(label)


    if(int(label)==1):
        st.success('Hureyyyy!! The costomer will make a purchase '  + ' :thumbsup:')
    else:
        st.success('Ohhh The costomer wont make a purchase '  + ' :thumbsup:')

trigger = st.button('Predict', on_click=predict)

