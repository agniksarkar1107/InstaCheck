import streamlit as st
import joblib
import pandas as pd
import tensorflow
import keras
st.write("#  CheckInsta ")
col1, col2, col3 = st.columns(3)

#profile pic	
# nums/length username	
# fullname words	nums/length fullname	name==username	description length	external URL	private	#posts	#followers	#follows




profile_pic = col1.selectbox("Is profile picture present?",["Yes","No"])

nums_length_username = col2.number_input("Ratio of numbers to length of username")

fullname_words= col2.number_input("Number of full names in username")

nums_length_fullname = col2.number_input("Ratio of number of numerical characters in full name to its length")

name_username = col3.selectbox("Are username and full name literally the same?",["Yes","No"])

description_length = col2.number_input("Bio length in characters")

external_URL = col3.selectbox("Is any external URL present?",["Yes","No"])

private = col1.selectbox("Is the account private?",["Yes","No"])

posts = col3.number_input("Number of posts")

followers = col1.number_input("Number of followers")

follows = col1.number_input("Number of following")

df_pred = pd.DataFrame([[profile_pic,nums_length_username,fullname_words,nums_length_fullname
                         ,name_username,description_length,external_URL,private,posts,followers,follows]],

columns= ['profile pic','nums/length username','fullname words','nums/length fullname','name==username','description length'
          ,'external URL'
          ,'private','#posts','#followers','#follows'])


df_pred['profile pic'] = df_pred['profile pic'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['name==username'] = df_pred['name==username'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['external URL'] = df_pred['external URL'].apply(lambda x: 1 if x == 'Yes' else 0)

df_pred['private'] = df_pred['private'].apply(lambda x: 1 if x == 'Yes' else 0)


model1 =keras.models.load_model("model.keras")
prediction = model1.predict(df_pred)


if st.button('Check',key="1"):

    if(prediction[0]==0):
        st.write('<p class="big-font">The provided Instagram Account is GENUINE.</p>',unsafe_allow_html=True)

    else:
        st.write('<p class="big-font">The provided Instagram Account is FAKE.</p>',unsafe_allow_html=True)







