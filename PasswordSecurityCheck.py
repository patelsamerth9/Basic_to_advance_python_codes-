import streamlit as st
import re
st.set_page_config(page_title="SecureCheck", page_icon="🔐")
st.title("🔐 SecureCheck: Password Auditor")
st.write("Check your password strength locally. **Your data never leaves your computer.**")
password = st.text_input("Enter your password to audit:", type="password")
if password:
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Increase length to 8+ characters.")
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("❌ Use both Uppercase and Lowercase letters.")
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("❌ Add a special character (e.g., @, #, $).")
    if score == 4:
        st.success("### Grade: A+ (Very Strong)")
        st.balloons()
    elif score == 3:
        st.warning("### Grade: B (Good)")
    elif score == 2:
        st.info("### Grade: C (Fair)")
    else:
        st.error("### Grade: F (Weak)")
    if feedback:
        with st.expander("How to improve your password:"):
            for line in feedback:
                st.write(line)
else:
    st.info("Start typing a password to see the audit.")
st.divider()
st.caption("Built with Python & Streamlit • Secure & Local")