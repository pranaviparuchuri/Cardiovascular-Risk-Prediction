import pandas as pd
import pickle
import streamlit as st
from sklearn.linear_model import LogisticRegression


loaded_model = pickle.load(open('C:/Users/paruc/Data Science/Projects/heart_model.sav','rb'))

def main():
    html_temp = """
    <div style = "background-color : Light;padding : 7px">
    <h2 style ='color:red; text-align : right'> Heart Disease Prediction Using Machine Learning</h2>
    </div>
    """
    
    #model = LogisticRegression()
   
  #  loaded_model = joblib.load('Heart_Disease_Prediction.pkl')
    
   # model.load_model('Heart_Disease_Prediction.pkl')
    
    st.markdown(html_temp, unsafe_allow_html = True)
    st.write('')
    st.write('')
    
    st.markdown("#### Let's predict whether patient have heart disease or not")
    
    p1 = st.number_input('Enter age',20,100)
    p2 = st.number_input('gender',0,3)
    
    p3 = st.number_input('Enter chest pain type',0,5)
    p4 = st.number_input('Enter resting blood pressure',100,300)
    p5 = st.number_input('Enter serum cholestoral',100,400)
    p6 = st.number_input('Enter fasting blood sugar',0,5)
    p7 = st.number_input('Enter resting electrocardiographic results',0,5)
    p8 = st.number_input('Enter maximum heart rate achieved',100,400)
    p9 = st.number_input('Enter exercise induced angina',0,3)
    p10 = st.number_input('Enter oldpeak',0,5)
    p11 = st.number_input('Enter slope of the peak exercise ST segment',0,5)
    p12 = st.number_input('Enter number of major vessels',0,5)
    p13 = st.number_input('Enter thal',0,4)
    
    
    data_new = pd.DataFrame({
    'age' : p1,
    'sex' : p2,
    'cp' : p3,
    'trestbps' : p4,
    'chol' : p5,
    'fbs' : p6,
    'restecg' : p7,
    'thalach' : p8,
    'exang' : p9,
    'oldpeak' : p10,
    'slope' : p11,
    'ca' : p12,
    'thal' : p13
}, index = [0])
    pred = loaded_model.predict(data_new)
    
    if st.button('Predict') == 0:
        st.success(' Patient does not have heart disease because model prediction is {:}'.format(pred[0]))
    else:
        st.success(' Patient have heart disease because model prediction is {:}'.format(pred[0]))
           
        
if __name__ == '__main__':
    main()