import streamlit as st

st.set_page_config(
    page_title="AI-Powered Customer Support Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI-Powered Customer Support Chatbot")
st.write("Welcome! Ask me anything about orders, refunds, delivery, payments, or customer support.")

if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

customer_queries = {
    "hello": "Hello! Welcome to our AI Customer Support. How may I assist you today?",
    "hi": "Hello! Welcome to our AI Customer Support. How may I assist you today?",
    "good morning": "Good morning! Hope you have a wonderful day. How can I help you?",
    "good afternoon": "Good afternoon! How may I assist you today?",
    "good evening": "Good evening! How can I assist you today?",
    "refund": "Refund requests are processed within 5–7 business days after approval.",
    "cancel order": "Your order can be cancelled before it has been shipped.",
    "delivery": "Orders are usually delivered within 3–5 business days.",
    "payment": "We accept UPI, Credit Cards, Debit Cards, Net Banking, and Cash on Delivery.",
    "order status": "Please provide your Order ID to check the status of your order.",
    "contact": "You can contact our support team at support@example.com.",
    "who are you": "I am an AI-powered Customer Support Chatbot designed to assist customers with common queries.",
    "okay": "Great! I'm glad I could help. Is there anything else I can assist you with?",
    "thanks": "You're welcome! Happy to assist you.",
    "bye": "Thank you for using our AI Customer Support Chatbot. Have a wonderful day!",
    "working hours": "Our customer support is available from 9:00 AM to 6:00 PM, Monday to Saturday.",
    "shipping charges": "Free shipping is available on orders above ₹499.",
    "track order": "Please enter your Order ID to track your shipment.",
    "location": "We currently provide services across India."
}

if "messages" not in st.session_state:
    st.session_state.messages = []
  
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user = st.chat_input("Type your message here...")

if user:

    st.session_state.messages.append(
        {"role": "user", "content": user}
    )

    with st.chat_message("user"):
        st.write(user)

    text = user.lower()

    response = """❌ Sorry! I couldn't understand your question.

You can ask me about:
• Orders
• Refunds
• Delivery
• Payments
• Order Tracking
• Shipping Charges
• Working Hours
• Contact Support
"""

    if "hello" in text or "hi" in text:
        response = customer_queries["hello"]

    elif "good morning" in text:
        response = customer_queries["good morning"]

    elif "good afternoon" in text:
        response = customer_queries["good afternoon"]

    elif "good evening" in text:
        response = customer_queries["good evening"]

    elif "refund" in text:
        response = customer_queries["refund"]

    elif "cancel" in text:
        response = customer_queries["cancel order"]

    elif "delivery" in text:
        response = customer_queries["delivery"]

    elif "payment" in text:
        response = customer_queries["payment"]

    elif "order status" in text or ("order" in text and "status" in text):
        response = customer_queries["order status"]

    elif "track" in text:
        response = customer_queries["track order"]

    elif "shipping" in text:
        response = customer_queries["shipping charges"]

    elif "working hours" in text or "timing" in text or "open" in text:
        response = customer_queries["working hours"]

    elif "contact" in text:
        response = customer_queries["contact"]

    elif "location" in text or "where" in text:
        response = customer_queries["location"]

    elif "who are you" in text:
        response = customer_queries["who are you"]

    elif "okay" in text or "ok" in text:
        response = customer_queries["okay"]

    elif "thanks" in text or "thank you" in text:
        response = customer_queries["thanks"]

    elif "bye" in text:
        response = customer_queries["bye"]

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)
