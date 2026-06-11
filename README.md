⚾ 나만의 응원 포스터 제작기 (Sports Poster Maker)
이 프로젝트는 파이썬(Streamlit)을 활용하여 사용자가 원하는 응원 문구를 입력하고, 야구장 배경 이미지와 구단 로고를 선택하여 나만의 응원 포스터를 제작하고 즉시 다운로드할 수 있는 웹 애플리케이션입니다.

🚀 주요 기능
실시간 응원 문구 입력: st.text_input을 통해 응원 문구를 입력하면 실시간으로 포스터에 반영됨.
구단 로고 및 글자 크기 조절: 사이드바 메뉴를 통해 구단 로고 선택 및 3단계 글자 크기 조절 기능 제공.
포스터 파일 저장: st.download_button을 통해 제작된 응원 포스터를 이미지 파일로 즉시 다운로드 가능.
반응형 UI: 사이드바와 메인 화면 분리를 통해 사용자 중심의 직관적인 디자인 구성.
🛠 사용 기술 및 도구
Framework: Streamlit
Library: Pillow (이미지 처리), Base64 (이미지 인코딩), IO (데이터 입출력)
Deployment: GitHub, Streamlit Community Cloud
AI Tool: chat gpt (코드 구조 설계, 배포 에러 디버깅 및 문서 작성 지원)
🌐 접속 및 실행 방법
본 프로젝트는 Streamlit Cloud에 배포되어 있어 별도의 설치 없이 아래 링크에서 바로 접속 가능합니다.

웹 앱 주소: https://sports-poster-project-vpyu5app5qncf9cc5e9h5mj.streamlit.app/
🛠 개선 기록 (AI 활용 및 디버깅)
레이아웃 밀림 현상 해결: 초기 코드에서 이미지와 텍스트가 별도로 출력되던 문제를 해결하기 위해, HTML의 position: relative와 absolute 속성을 활용하여 배경 이미지 위에 로고와 텍스트를 고정적으로 배치하도록 구조를 변경함.
디자인 커스텀: 야구장 배경에서 가장 가독성이 좋은 흰색 글씨와 검은색 외곽선(-webkit-text-stroke) 조합을 선택하여 디자인을 구성하였으며, 로고 위치를 좌측 상단(top: 50px)으로 직접 조정하여 깔끔한 레이아웃을 구현함.
