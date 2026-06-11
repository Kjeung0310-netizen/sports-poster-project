import streamlit as st
import base64
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

with st.sidebar:
    user_text = st.text_input("응원 문구:", "네모안에 공을 던져")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")
    logo_option = st.selectbox("로고 선택", ["로고 없음", "KIA", "KT", "LG", "Samsung"])

def get_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_image_base64("baseball.jpg")
logo_html = ""
if logo_option != "로고 없음":
    logo_img = get_image_base64(f"{logo_option}.png")
    logo_html = f'<img src="data:image/png;base64,{logo_img}" style="width: 150px; position: absolute; top: 20px; left: 20px;">'

font_map = {"작게": "40px", "중간": "80px", "크게": "120px"}

# 폰트 스타일을 'Arial, sans-serif'로 지정하여 깔끔하게 변경
html_code = f"""
    <div style="position: relative; width: 100%; font-family: Arial, sans-serif;">
        <img src="data:image/jpeg;base64,{bg_img}" style="width: 100%; border-radius: 10px;">
        {logo_html}
        <div style="
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); 
            width: 100%; text-align: center; font-size: {font_map[size_option]}; 
            font-weight: bold; color: #FFFF00; -webkit-text-stroke: 2px black; 
            text-shadow: 4px 4px 0px black;
        ">
            {user_text}
        </div>
    </div>
"""

# 높이를 사진 비율에 맞춰 700 정도로 넉넉하게 주었습니다.
components.html(html_code, height=700)
