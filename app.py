import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('decision_tree_model.pkl', 'rb'))

st.title('which distination will he choose')

Traveller_Profile_Type = st.slider("Traveller Profile Type",0,3)
Choice_Preference = st.slider("Choice/Preference",0,3)
Mode_of_Travel = st.slider("Mode of Travel",0,3)
Budget = st.slider("Budget",10000,1000000)



def predict():
    float_features = [float(x) for x in [Traveller_Profile_Type, Choice_Preference, Mode_of_Travel, Budget]]
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
