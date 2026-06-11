import streamlit as st
from PIL import Image
import io

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

with st.sidebar:
    user_text = st.text_area("문구:", "최원준 멀티히트!")
    size_option = st.select_slider("크기", options=["작게", "중간", "크게"], value="중간")
    logo_option = st.selectbox("로고", ["로고 없음", "KIA", "KT", "LG", "Samsung"])

# 이미지 표시
col1, col2 = st.columns([1, 3])
with col2:
    st.image("baseball.jpg", use_container_width=True)
    
    # 여기서부터 텍스트 테두리 스타일 적용 (HTML/CSS)
    font_map = {"작게": "40px", "중간": "80px", "크게": "120px"}
    
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
            {user_text.replace('\n', '<br>')}
        </div>
    """, unsafe_allow_html=True)
