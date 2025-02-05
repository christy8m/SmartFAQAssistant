import streamlit as st
import openai
openai.api_key =  st.secrets["mykey"]

# Define answer
Answer = [
product_benefits = ["Convenience", "Reduced food waste", "Personalized cooking assistance", "Energy efficiency", "Longer food freshness"]




# Streamlit UI
st.title("Smart FAQ Assistant")

product_name = st.text_input("Please enter your question:", value="Type your question here")


if st.button("Generate Answer"):
    caption, image_description = generate_copy(answer)
    st.subheader("Answer:")
  
