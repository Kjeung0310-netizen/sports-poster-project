import streamlit as st

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

# 1. 왼쪽 설정창
with st.sidebar:
    # 엔터키를 치면 바로 반영되도록 text_input 사용
    user_text = st.text_input("응원 문구 입력:", "최원준 안타쳐줘!")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")
    logo_option = st.selectbox("로고 선택", ["로고 없음", "KIA", "KT", "LG", "Samsung"])

# 2. 메인 화면
col1, col2 = st.columns([1, 3])

with col2:
    # 배경 이미지 출력
    st.image("baseball.jpg", use_container_width=True)
    
    # 폰트 사이즈 설정
    font_map = {"작게": "50px", "중간": "90px", "크게": "130px"}
    
    # 흰색 글씨 + 빨간색 테두리 스타일
    st.markdown(f"""
        <div style="
            text-align: center; 
            margin-top: -300px;
            font-size: {font_map[size_option]}; 
            font-weight: bold; 
            color: white; 
            -webkit-text-stroke: 4px red; 
            text-shadow: 4px 4px 0px red;
        ">
            {user_text}
        </div>
    """, unsafe_allow_html=True)

st.info("입력창에 문구를 쓰고 엔터를 치면 바로 반영됩니다!")
