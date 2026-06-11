import streamlit as st
from PIL import Image
import io

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

# 사진 불러오기 (이름을 baseball.jpg로 맞췄습니다)
img = Image.open("baseball.jpg")

with st.sidebar:
    user_text = st.text_input("문구 입력:", "최원준 화이팅!")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")

col1, col2 = st.columns([1, 2])

with col2:
    st.image(img, use_container_width=True)
    font_map = {"작게": "30px", "중간": "60px", "크게": "90px"}
    
    st.markdown(f"""
        <div style="text-align: center; font-size: {font_map[size_option]}; font-weight: bold; color: white; text-shadow: 3px 3px 5px black; margin-top: -285
    px;">
            {user_text}
        </div>
    """, unsafe_allow_html=True)

    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    st.download_button("📥 이미지 저장", buf.getvalue(), "poster.jpg", "image/jpeg")
