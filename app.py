import streamlit as st

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

# 1. 왼쪽 설정창
with st.sidebar:
    user_text = st.text_input("응원 문구 입력:", "제발 네모안에 공을 던져")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")
    logo_option = st.selectbox("로고 선택", ["로고 없음", "KIA", "KT", "LG", "Samsung"])

# 2. 메인 화면
col1, col2 = st.columns([1, 3])

with col2:
    # 로고를 사진 위에 띄우는 스타일
    logo_html = ""
    if logo_option != "로고 없음":
        logo_html = f'<img src="https://raw.githubusercontent.com/Kjeung0310-netizen/poster-project/main/{logo_option}.png" style="width:150px; position:absolute; top:20px; left:20px;">'

    # 배경 이미지 출력
    st.markdown(f"""
        <div style="position: relative;">
            <img src="https://raw.githubusercontent.com/Kjeung0310-netizen/poster-project/main/baseball.jpg" style="width:100%; border-radius:10px;">
            {logo_html}
        </div>
    """, unsafe_allow_html=True)
    
    # 노란 글씨 + 검은 테두리 스타일
    font_map = {"작게": "50px", "중간": "90px", "크게": "130px"}
    
    st.markdown(f"""
        <div style="
            text-align: center; 
            margin-top: -300px;
            font-size: {font_map[size_option]}; 
            font-weight: bold; 
            color: #FFFF00; 
            -webkit-text-stroke: 3px black; 
            text-shadow: 4px 4px 0px black;
        ">
            {user_text}
        </div>
    """, unsafe_allow_html=True)
