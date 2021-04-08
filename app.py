import streamlit as st
import pickle

pickle_in=open('spPickle1.pkl','rb')
spPickle1=pickle.load(pickle_in)

pickle_in=open('spPickle2.pkl','rb')
spPickle2=pickle.load(pickle_in)


@st.cache()

def prediction1(gen,age,marr,res,glucose,tension,hdisease,bmi):

    if  gen=="Male":
        gen=1
    else:
        gen=0

    if marr=="Yes":
        marr=1
    else:
        marr=0
    
    if res=="Urban":
        res=1
    else:
        res=0

    if tension=="Yes":
        tension=1
    else:
        tension=0

    if hdisease=="Yes":
        hdisease=1
    else:
        hdisease=0

    pred=spPickle1.predict([[gen,age,tension,hdisease,marr,res,glucose,bmi]])

    return pred


def prediction2(gen,age,marr,res,glucose,tension,hdisease,bmi):

    if  gen=="Male":
        gen=1
    else:
        gen=0

    if marr=="Yes":
        marr=1
    else:
        marr=0
    
    if res=="Urban":
        res=1
    else:
        res=0

    if tension=="Yes":
        tension=1
    else:
        tension=0

    if hdisease=="Yes":
        hdisease=1
    else:
        hdisease=0

    pred=spPickle2.predict([[gen,age,tension,hdisease,marr,res,glucose,bmi]])

    return pred

def main():

    header=st.beta_container()
    features=st.beta_container()
    result=st.beta_container()


    with header:
        st.title("Stroke Prediction WebApp")
        st.text("Enter the data asked below and know wheather you are at a risk of having a stroke or not!")

    with features:
        st.header("Enter the data of the features listed below.")

        gen=st.selectbox('Gender:', options=['Male','Female'])
        age=st.slider("Age:", 0, 120)
        marr=st.selectbox("Ever married:", options=['Yes','No'])
        res=st.selectbox("Residence Type:", options=["Urban", "Rural"])
        glucose=st.number_input("Enter your Glucose Level (Lastest):")
        tension=st.selectbox("Hypertension:", options=['Yes','No'])
        hdisease=st.selectbox("Heart Disease:", options=['Yes','No'])
        bmi=st.number_input("Enter your BMI (in kilogram per metre square):")
        st.info("BMI=Weight(kg)/(Height*Height (m))")


    with result: 
        st.text("")
        st.text("")

        if st.button("Predict for Stroke"):
            r=prediction2(gen,age,marr,res,glucose,tension,hdisease,bmi)
            if r==0:
                st.success('You are safe') 
            else:
                st.error('You are at risk')           

if __name__=='__main__': 
    main()


