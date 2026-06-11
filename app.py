import streamlit as st
from PIL import Image
import io

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

with st.sidebar:
    user_text = st.text_input("응원 문구를 입력하세요!", "최원준 화이팅!")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")

col1, col2 = st.columns([1, 2])

with col2:
    st.image("baseball.jpg", use_container_width=True)
    font_map = {"작게": "30px", "중간": "60px", "크게": "90px"}
    
    st.markdown(f"""
        <div style="position: relative;">
            <div style="
                position: absolute;
                top: -300px;
                width: 100%;
                font-size: {font_map[size_option]}; 
                font-weight: bold; 
                color: white; 
                text-shadow: 3px 3px 5px black;
                text-align: center;
            ">
                {user_text}
            </div>
        </div>
    """, unsafe_allow_html=True)

    buf = io.BytesIO()
    img = Image.open("baseball.jpg")
    img.save(buf, format="JPEG")
    st.download_button("📥 포스터 파일 저장하기", buf.getvalue(), "poster.jpg", "image/jpeg")
