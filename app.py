# import streamlit as st
# import pickle
# import helper


# model = pickle.load(open('./Notebook/model.pkl', 'rb'))


# st.header('Duplicate Question Pairs')

# q1 = st.text_input('Enter question 1')
# q2 = st.text_input('Enter question 2')

# if st.button('Validate'):
#     query = helper.query_point_creator(q1,q2)
#     result = model.predict(query)[0]

#     if result:
#         st.header('Duplicate')
#     else:
#         st.header('Not Duplicate')





import streamlit as st
import pickle
import helper

# Load model
model = pickle.load(open('./Notebook/model.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Duplicate Question Detector", page_icon="🔍", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            background: -webkit-linear-gradient(#00c6ff, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtext {
            text-align: center;
            color: #aaa;
            margin-bottom: 30px;
        }
        .card {
            background-color: #161b22;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
        }
        .result-duplicate {
            background-color: #1f6f4a;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 22px;
            color: white;
        }
        .result-not {
            background-color: #8b1e1e;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 22px;
            color: white;
        }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            color: white;
            font-size: 18px;
            font-weight: bold;
            height: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🔍 Duplicate Question Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Check if two questions mean the same thing</div>', unsafe_allow_html=True)

# Card layout
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    q1 = st.text_area("📝 Enter Question 1", placeholder="Type first question here...")
    q2 = st.text_area("📝 Enter Question 2", placeholder="Type second question here...")

    if st.button("🚀 Check Similarity"):
        if q1.strip() == "" or q2.strip() == "":
            st.warning("⚠️ Please enter both questions")
        else:
            query = helper.query_point_creator(q1, q2)
            result = model.predict(query)[0]

            st.markdown("<br>", unsafe_allow_html=True)

            if result:
                st.markdown('<div class="result-duplicate">✅ Duplicate Questions</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="result-not">❌ Not Duplicate</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="text-align:center; margin-top:30px; color:gray;">
        Built with ❤️ using Streamlit
    </div>
""", unsafe_allow_html=True)
