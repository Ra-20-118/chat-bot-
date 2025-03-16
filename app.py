import streamlit as st
import requests

# ن FastAPI (استبدلي your-server-ip بعنوان IP الحقيقي)
FASTAPI_URL = "http://20.115.92.35:8000"

st.title("Chatbot Messages Viewer")

# FastAPI
def get_messages():
    response = requests.get(f"{FASTAPI_URL}/messages/")
    if response.status_code == 200:
        return response.json()
    else:
        return []

messages = get_messages()

# عرض البيانات في جدول
if messages:
    st.write("### المحادثات المخزنة:")
    for msg in messages:
        st.write(f"**👤 المستخدم:** {msg['user_input']}")
        st.write(f"**🤖 الرد:** {msg['bot_response']}")
        st.write("---")
else:
    st.write("لا توجد محادثات بعد.")

# 
st.write 
user_input = st.text_input("رسالة المستخدم")
bot_response = st.text_input("رد البوت")

if st.button("إرسال"):
    if user_input and bot_response:
        response = requests.post(f"{FASTAPI_URL}/messages/", json={
            "user_input": user_input,
            "bot_response": bot_response
        })
        if response.status_code == 200:
            st.success("تمت إضافة الرسالة بنجاح!")
        else:
            st.error("حدث خطأ أثناء الإرسال.")