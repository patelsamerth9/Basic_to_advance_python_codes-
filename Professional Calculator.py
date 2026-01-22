import streamlit as st
import math

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Advanced Calculator",
    page_icon="🧮",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.calc-card {
    background: #0f172a;
    padding: 25px;
    border-radius: 20px;
    width: 360px;
    margin: auto;
    box-shadow: 0 20px 40px rgba(0,0,0,0.5);
}
.display {
    background: #020617;
    color: #22c55e;
    font-size: 34px;
    padding: 18px;
    text-align: right;
    border-radius: 12px;
    margin-bottom: 15px;
    font-family: monospace;
}
button[kind="primary"] {
    background-color: #2563eb;
}
.stButton>button {
    width: 100%;
    height: 55px;
    font-size: 18px;
    border-radius: 12px;
}
.history {
    color: #94a3b8;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- State ----------------
if "expr" not in st.session_state:
    st.session_state.expr = ""

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- Functions ----------------
SAFE_DICT = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log10,
    "pi": math.pi,
    "e": math.e
}

def press(val):
    st.session_state.expr += str(val)

def clear():
    st.session_state.expr = ""

def calculate():
    try:
        result = eval(st.session_state.expr, {"__builtins__": None}, SAFE_DICT)
        st.session_state.history.insert(0, f"{st.session_state.expr} = {result}")
        st.session_state.expr = str(result)
    except:
        st.session_state.expr = "Error"

# ---------------- UI ----------------
st.markdown('<div class="calc-card">', unsafe_allow_html=True)

st.markdown(
    f'<div class="display">{st.session_state.expr or "0"}</div>',
    unsafe_allow_html=True
)

mode = st.toggle("Scientific Mode")

# -------- Buttons --------
if not mode:
    buttons = [
        ["7","8","9","/"],
        ["4","5","6","*"],
        ["1","2","3","-"],
        ["0",".","=","+"]
    ]
else:
    buttons = [
        ["sin(","cos(","tan(","sqrt("],
        ["log(","pi","e","/"],
        ["7","8","9","*"],
        ["4","5","6","-"],
        ["1","2","3","+"],
        ["0",".","=","C"]
    ]

for row in buttons:
    cols = st.columns(4)
    for i, b in enumerate(row):
        with cols[i]:
            if b == "=":
                st.button(b, on_click=calculate, type="primary")
            elif b == "C":
                st.button(b, on_click=clear)
            else:
                st.button(b, on_click=lambda x=b: press(x))

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- History ----------------
if st.session_state.history:
    st.markdown("### 🧾 History")
    for h in st.session_state.history[:5]:
        st.markdown(f"<div class='history'>{h}</div>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center;color:gray;'>Advanced Calculator • Streamlit</p>",
    unsafe_allow_html=True
)