import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

# 1. 왼쪽 사이드바: 입력과 버튼
with st.sidebar:
    st.header("설정")
    input_text = st.text_area("응원 문구 (줄바꿈 가능):", "제발 네모안에 공을 던져")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")
    logo_option = st.selectbox("로고 선택", ["로고 없음", "KIA", "KT", "LG", "Samsung"])
    
    # 적용 버튼 추가 (이걸 눌러야 화면이 바뀜)
    apply_btn = st.button("포스터에 적용하기")

# 2. 메인 화면
col1, col2 = st.columns([1, 3])

with col2:
    # 기본 이미지 로드
    img = Image.open("baseball.jpg").convert("RGBA")
    
    # 로고 합성
    if logo_option != "로고 없음":
        logo = Image.open(f"{logo_option}.png").convert("RGBA")
        logo = logo.resize((200, 200))
        img.paste(logo, (50, 50), logo)
    
    # 텍스트 합성 (적용 버튼을 눌렀을 때만 반영)
    if apply_btn:
        draw = ImageDraw.Draw(img)
        try:
            font_size = {"작게": 50, "중간": 90, "크게": 130}[size_option]
            font = ImageFont.truetype("NanumGothic.ttf", font_size)
        except:
            font = ImageFont.load_default()
        draw.multiline_text((img.width/4, img.height/3), input_text, font=font, fill="white", align="center")
    
    # 결과 출력 및 저장
    final_img = img.convert("RGB")
    st.image(final_img, use_container_width=True)
    
    buf = io.BytesIO()
    final_img.save(buf, format="JPEG")
    st.download_button("📥 완성된 포스터 저장하기", buf.getvalue(), "poster.jpg", "image/jpeg")
