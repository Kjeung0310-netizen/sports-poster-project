import streamlit as st

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

with st.sidebar:
    user_text = st.text_input("응원 문구:", "네모안에 공을 던져")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")
    logo_option = st.selectbox("로고 선택", ["로고 없음", "KIA", "KT", "LG", "Samsung"])

# 글자 크기 매핑
font_map = {"작게": "40px", "중간": "80px", "크게": "120px"}

# 로고 HTML 생성
logo_html = ""
if logo_option != "로고 없음":
    logo_html = f'<img src="https://raw.githubusercontent.com/Kjeung0310-netizen/poster-project/main/{logo_option}.png" style="width: 120px; position: absolute; top: 10px; left: 10px;">'

# 핵심: 사진, 로고, 글자를 하나의 박스(relative)에 넣어서 절대 안 밀리게 함!
st.markdown(f"""
    <div style="position: relative; width: 100%;">
        <img src="https://raw.githubusercontent.com/Kjeung0310-netizen/poster-project/main/baseball.jpg" style="width: 100%; border-radius: 10px;">
        {logo_html}
        <div style="
            position: absolute; 
            top: 50%; 
            left: 50%; 
            transform: translate(-50%, -50%);
            width: 100%;
            text-align: center; 
            font-size: {font_map[size_option]}; 
            font-weight: bold; 
            color: #FFFF00; 
            -webkit-text-stroke: 2px black; 
            text-shadow: 4px 4px 0px black;
        ">
            {user_text}
        </div>
    </div>
""", unsafe_allow_html=True)
