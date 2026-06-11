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
txt_layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(txt_layer)

# 2. 로고 합성 (좌표 50, 50)
if logo_option != "로고 없음":
    logo = Image.open(f"{logo_option}.png").convert("RGBA")
    logo = logo.resize((200, 200))
    txt_layer.paste(logo, (50, 50), logo)

# 3. 글씨 합성 (테두리 효과 포함)
font_size = {"작게": 60, "중간": 100, "크게": 180}[size_option]
font = ImageFont.load_default() # 기본 폰트

# 테두리 만들기 (글씨를 5번씩 그려서 테두리 효과)
x, y = img.width/4, img.height/2
for adj in range(-3, 4):
    draw.text((x+adj, y), user_text, fill="black", font=font)
    draw.text((x, y+adj), user_text, fill="black", font=font)
draw.text((x, y), user_text, fill="white", font=font)

# 4. 이미지 합치기
final_img = Image.alpha_composite(img, txt_layer).convert("RGB")

# 5. 화면 표시 및 저장 버튼 (이제 글씨와 로고가 박힌 채로 저장됨!)
st.image(final_img, use_container_width=True)

buf = io.BytesIO()
final_img.save(buf, format="JPEG")
st.download_button("📥 로고/글씨 포함해서 저장하기", buf.getvalue(), "poster.jpg", "image/jpeg")
