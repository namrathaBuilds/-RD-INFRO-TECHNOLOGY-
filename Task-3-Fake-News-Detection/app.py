import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

st.set_page_config(page_title="AI Fake News Detector", page_icon="📰")

st.title("📰 AI-Based Fake News Detection")
st.write("Enter a news article below to check whether it is likely Real or Fake.")

news = st.text_area("News Article")

if st.button("Check News"):

    if news.strip() == "":
        st.warning("Please enter some news text.")
    else:
        vector = vectorizer.transform([news])
        prediction = model.predict(vector)

        if prediction[0] == 1:
            st.success("✅ Real News")
        else:
            st.error("❌ Fake News")
