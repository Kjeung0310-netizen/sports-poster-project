import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

with st.sidebar:
    user_text = st.text_input("응원 문구:", "원준아!")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")
    logo_option = st.selectbox("로고 선택", ["로고 없음", "KIA", "KT", "LG", "Samsung"])

# 1. 이미지 로드
img = Image.open("baseball.jpg").convert("RGBA")

# 2. 로고 합성
if logo_option != "로고 없음":
    logo = Image.open(f"{logo_option}.png").convert("RGBA")
    logo = logo.resize((200, 200))
    img.paste(logo, (50, 50), logo)

# 3. 글씨 합성 (정말 크게 그려서 보이게 만듦)
draw = ImageDraw.Draw(img)

# 기본 폰트 사용 시 크기 조절이 어려우므로, 
# 텍스트를 이미지 전체 크기에 맞춰 잘 보이게 그립니다.
w, h = img.size
# 위치를 (w/4, h/3)으로 잡고 더 크게 강조
draw.text((w/4, h/3), user_text, fill="white")
# 글씨를 5번 정도 덧그려서 두껍게 보이게 함
draw.text((w/4 + 2, h/3 + 2), user_text, fill="white")
draw.text((w/4 - 2, h/3 - 2), user_text, fill="white")

# 4. 출력 및 저장
final_img = img.convert("RGB")
st.image(final_img, use_container_width=True)

buf = io.BytesIO()
final_img.save(buf, format="JPEG")
st.download_button("📥 완성된 포스터 저장하기", buf.getvalue(), "poster.jpg", "image/jpeg")
