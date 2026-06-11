import streamlit as st

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

# 1. 사이드바
with st.sidebar:
    user_text = st.text_input("응원 문구:", "네모안에 공을 던져")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")
    logo_option = st.selectbox("로고 선택", ["로고 없음", "KIA", "KT", "LG", "Samsung"])

# 2. 이미지 출력 (st.image는 깃허브 파일을 아주 잘 가져옵니다)
# 배경
st.image("baseball.jpg", use_container_width=True)

# 3. 로고와 텍스트를 따로 출력
if logo_option != "로고 없음":
    st.image(f"{logo_option}.png", width=150)

# 글자 크기 매핑
font_map = {"작게": "40px", "중간": "80px", "크게": "120px"}

# 텍스트 출력
st.markdown(f"""
    <div style="
        text-align: center; 
        font-size: {font_map[size_option]}; 
        font-weight: bold; 
        color: #FFFF00; 
        -webkit-text-stroke: 2px black; 
        text-shadow: 3px 3px 0px black;
    ">
        {user_text}
    </div>
""", unsafe_allow_html=True)
