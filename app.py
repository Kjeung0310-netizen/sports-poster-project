import streamlit as st

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

# 1. 사이드바
with st.sidebar:
    user_text = st.text_input("응원 문구 입력:", "네모안에 공을 던져")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")
    logo_option = st.selectbox("로고 선택", ["로고 없음", "KIA", "KT", "LG", "Samsung"])

# 2. 포스터 영역 (컨테이너 사용)
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

# 배경 이미지
st.image("baseball.jpg", use_container_width=True)

# 로고 출력 (공식 명령어 사용)
if logo_option != "로고 없음":
    st.image(f"{logo_option}.png", width=150)

# 텍스트 출력
font_map = {"작게": "50px", "중간": "90px", "크게": "130px"}
st.markdown(f"""
    <div style="
        margin-top: -300px;
        text-align: center; 
        font-size: {font_map[size_option]}; 
        font-weight: bold; 
        color: #FFFF00; 
        -webkit-text-stroke: 3px black; 
        text-shadow: 4px 4px 0px black;
    ">
        {user_text}
    </div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
