#import libraries
import deployment.eda as eda
import deployment.prediction as prediction
import streamlit as st

#navigation
navigation = st.sidebar.selectbox('Choose Page: ', ('Predictor', 'EDA'))

#pilih page
if navigation == 'Predictor':
    prediction.run()
else:
    eda.run()