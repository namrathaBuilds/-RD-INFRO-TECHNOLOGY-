import streamlit as st
import pickle

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="AI-Powered Fake News Detection",
    page_icon="📰",
    layout="centered"
)

# ---------------- Load Model ----------------
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# ---------------- Title ----------------
st.title("📰 AI-Powered Fake News Detection System")

st.markdown("""
Detect whether a news article is **Real** or **Fake** using Machine Learning.

💡 **Tip:** For better accuracy, paste a complete news paragraph instead of just one sentence.
""")

# ---------------- Session State ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- Input ----------------
news = st.text_area(
    "Paste News Article",
    height=220,
    placeholder="Paste the complete news article here..."
)

col1, col2 = st.columns(2)

# ---------------- Prediction ----------------
with col1:

    if st.button("🔍 Check News"):

        if news.strip() == "":
            st.warning("⚠ Please enter a news article.")

        else:

            vector = vectorizer.transform([news])

            prediction = model.predict(vector)[0]

            probability = model.predict_proba(vector)

            confidence = max(probability[0]) * 100

            if prediction == 1:

                result = "✅ REAL NEWS"

                st.success(result)

            else:

                result = "❌ FAKE NEWS"

                st.error(result)

            st.info(f"Confidence : {confidence:.2f}%")

            st.session_state.history.append(
                {
                    "News": news[:80] + "...",
                    "Prediction": result,
                    "Confidence": f"{confidence:.2f}%"
                }
            )

# ---------------- Clear Button ----------------
with col2:

    if st.button("🗑 Clear History"):
        st.session_state.history = []
        st.rerun()

# ---------------- Prediction History ----------------
if len(st.session_state.history) > 0:

    st.subheader("📜 Prediction History")

    st.table(st.session_state.history)

# ---------------- Information ----------------
with st.expander("ℹ About this Project"):

    st.write("""
This project uses:

- Logistic Regression
- TF-IDF Vectorization
- Natural Language Processing (NLP)

The model was trained using the Fake & Real News Dataset to classify news articles.
""")

# ---------------- Footer ----------------
st.markdown("---")

st.caption("Developed as part of AI & Machine Learning Internship")
