import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="caesar cipher tool",
    page_icon="🔐",
    layout="centered"
)
def encrypt(text, shift):
    result=""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result+= chr((ord(char)- ord('a')+shift) %26 +ord('a'))

        else:
            result+=char
    return result


def decrypt(text, shift):
    result=""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result+= chr((ord(char)- ord('a')-shift) %26 +ord('a'))

        else:
            result+=char
    return result

if "history" not in st.session_state:
    st.session_state.history=[]

st.title("🔐Caesar cipher encryption & decryption tool")
st.markdown("Encrupt or decrupt the message using the Caesar cipher tool")
text= st.text_area("Enter text...",placeholder="Type your message here...")
shift= st.slider("Enter number of shifts", min_value= 0,max_value=25, value=3)

operation = st.radio("Choose option",["Encrypt","Decrypt"],horizontal=True)

if st.button("🚀 Run Cipher", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text...")
    else :
        if operation=="Encrypt":
            result= encrypt(text,shift)
        else:
            result= decrypt(text,shift)
        st.success("Operation Completed!")

        st.subheader("Result")
        st.code(result)


        st.session_state.history.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operation": operation,
            "shift": shift,
            "input": text,
            "output": result
        })

        st.text_area(
            "Copy Result",
            value=result,
            height=100
        )

        st.download_button(
            label="📥 Download Result",
            data=result,
            file_name="caesar_cipher_result.txt",
            mime="text/plain"
        )

st.divider()
st.subheader("📜 History")
if st.session_state.history:
    for i, item in enumerate(reversed(st.session_state.history), start=1):
        with st.expander(
            f"{i}. {item['operation']} | Shift={item['shift']} | {item['time']}"
        ):
            st.write("**Input:**")
            st.code(item["input"])
            st.write("**Output:**")
            st.code(item["output"])
    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.rerun()
else:
    st.info("No history available.")

st.divider()
st.caption("Built with Python and Streamlit")


