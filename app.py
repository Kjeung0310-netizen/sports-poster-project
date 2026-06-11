import streamlit as st
import base64
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("⚾ 나만의 응원 포스터 제작기")

with st.sidebar:
    user_text = st.text_input("응원 문구:", "ex) 000(선수이름) 화이팅!")
    size_option = st.select_slider("글자 크기", options=["작게", "중간", "크게"], value="중간")
    logo_option = st.selectbox("로고 선택", ["로고 없음", "KIA", "KT", "LG", "Samsung"])

def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

bg_img = get_image_base64("baseball.jpg")
logo_html = ""
if logo_option != "로고 없음":
    logo_img = get_image_base64(f"{logo_option}.png")
    if logo_img:
        logo_html = f'<img src="data:image/png;base64,{logo_img}" style="width: 150px; position: absolute; top: 20px; left: 20px;">'

font_map = {"작게": "40px", "중간": "80px", "크게": "120px"}

# HTML 실행 강제화 (배열 고정 버전)
html_code = f"""
    <div style="position: relative; width: 100%; font-family: Arial, sans-serif;">
        <img src="data:image/jpeg;base64,{bg_img}" style="width: 100%; border-radius: 10px;">
        {logo_html}
        <div style="
            position: absolute; top: 55%; left: 50%; transform: translate(-50%, -50%); 
            text-align: center; font-size: {font_map[size_option]}; 
            font-weight: bold; color: white; -webkit-text-stroke: 2px black; 
            text-shadow: 4px 4px 0px black; white-space: nowrap;
        ">
            {user_text}
        </div>
    </div>
"""
components.html(html_code, height=700)

st.write("—")
with open("baseball.jpg", "rb") as f:
    st.download_button("📥 포스터 저장하기", f.read(), "poster.jpg", "image/jpeg")
