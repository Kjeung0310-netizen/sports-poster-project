import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

with st.sidebar:
    user_text = st.text_input("응원 문구:", "네모안에 공을 던져")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")
    logo_option = st.selectbox("로고 선택", ["로고 없음", "KIA", "KT", "LG", "Samsung"])

# 1. 이미지 로드
img = Image.open("baseball.jpg").convert("RGBA")

# 2. 로고 합성
if logo_option != "로고 없음":
    logo = Image.open(f"{logo_option}.png").convert("RGBA")
    logo = logo.resize((150, 150))
    img.paste(logo, (50, 50), logo)

# 3. 이미지에 글씨 직접 그리기 (PIL 사용)
draw = ImageDraw.Draw(img)
# 폰트 사이즈 설정
font_sizes = {"작게": 40, "중간": 80, "크게": 120}
# 시스템 기본 폰트 사용 (한글 지원을 위해 별도 파일이 없으면 기본 폰트)
font = ImageFont.load_default() 

# 텍스트 그리기 (위치: 사진 정중앙)
draw.text((img.width/4, img.height/2), user_text, fill="white")

# 4. 출력 및 저장
final_img = img.convert("RGB")
st.image(final_img, use_container_width=True)

buf = io.BytesIO()
final_img.save(buf, format="JPEG")
st.download_button("📥 완성된 포스터 저장하기", buf.getvalue(), "poster.jpg", "image/jpeg")
