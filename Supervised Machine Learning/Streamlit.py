import streamlit as st
import pickle as pkl

pickle_in = open('regressor.pickle', 'rb')
model = pkl.load(pickle_in)

pickle_in.close()
st.title('SCORE PREDICTION APP')
st.header('ADD HOURS OF STUDY BELOW')

hours = st.number_input("ENTER HOURS")

st.success("PREDICTED SCORE OF THE STUDENT: {}".format(model.predict([[hours]])))
	