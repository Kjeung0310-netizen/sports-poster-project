import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

# 1. 사이드바 설정
with st.sidebar:
    user_text = st.text_input("응원 문구:", "최원준 화이팅!")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")
    # NC를 제외한 4개 구단
    logo_option = st.selectbox("로고 선택", ["로고 없음", "KIA", "KT", "LG", "Samsung"])

# 2. 이미지 작업
base_img = Image.open("baseball.jpg").convert("RGBA")
txt_layer = Image.new('RGBA', base_img.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(txt_layer)

# 글자 그리기
draw.text((base_img.width/3, base_img.height/2), user_text, fill="white")

# 로고 합성
if logo_option != "로고 없음":
    logo = Image.open(f"{logo_option}.png").convert("RGBA")
    logo = logo.resize((300, 300))
    txt_layer.paste(logo, (50, 50), logo)

# 3. 사진 위에 다 합치기
final_img = Image.alpha_composite(base_img, txt_layer).convert("RGB")

# 4. 화면 출력
st.image(final_img, use_container_width=True)

# 5. 저장 버튼
buf = io.BytesIO()
final_img.save(buf, format="JPEG")
st.download_button("📥 완성된 포스터 저장하기", buf.getvalue(), "poster.jpg", "image/jpeg")
