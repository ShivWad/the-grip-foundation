import streamlit as st
import pickle as pkl
import matplotlib.pyplot as plt

pickle_in = open('DecisionTreeClassifier.pickle', 'rb')
model = pkl.load(pickle_in)
pickle_in.close()



st.header('DECISION TREE GRAPH')

st.image('DecisionTreeGraph.png',width = 1200)

SL = st.number_input('Enter Sepal Length')
SW = st.number_input('Enter Sepal Width')
PL = st.number_input('Enter Petal Length')
PW = st.number_input('Enter Petal Width')

input = [SL,SW,PL,PW]

if st.button('Predict Class'):
	st.success('PREDICTED CLASS: {}'.format(model.predict([input])[0]))





