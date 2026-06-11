import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

with st.sidebar:
    user_text = st.text_area("응원 문구 (줄바꿈 가능):", "네모 안에 공을 던져")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")
    logo_option = st.selectbox("로고 선택", ["로고 없음", "KIA", "KT", "LG", "Samsung"])

# 1. 이미지 로드
img = Image.open("baseball.jpg").convert("RGBA")

# 2. 로고 합성 (사진 위에 로고 그리기)
if logo_option != "로고 없음":
    logo = Image.open(f"{logo_option}.png").convert("RGBA")
    logo = logo.resize((150, 150))
    img.paste(logo, (50, 50), logo)

# 3. 텍스트 합성 (사진 위에 글씨 그리기)
draw = ImageDraw.Draw(img)
# 폰트 설정 (폰트 파일이 깃허브에 없으면 .load_default() 사용)
try:
    font_size = {"작게": 50, "중간": 90, "크게": 130}[size_option]
    font = ImageFont.truetype("NanumGothic.ttf", font_size)
except:
    font = ImageFont.load_default()

draw.multiline_text((img.width/4, img.height/3), user_text, font=font, fill="white", align="center")

# 4. 합성된 이미지를 RGB로 변환 (JPG 저장용)
final_img = img.convert("RGB")

# 5. 화면 표시 (이미 합성된 final_img를 보여줌)
st.image(final_img, use_container_width=True)

# 6. 저장 버튼 (이미 합성된 final_img를 저장함)
buf = io.BytesIO()
final_img.save(buf, format="JPEG")
st.download_button("📥 완성된 포스터 저장하기", buf.getvalue(), "poster.jpg", "image/jpeg")
user_text = st.text_area("응원 문구 (입력 후 아래 버튼 클릭!):", "원준아\n멀티히트 가자!")
submit = st.button("포스터에 적용하기") # 버튼 추가
