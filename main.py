import streamlit as st
import random

st.set_page_config(page_title="기분 따라 듣는 K-POP", page_icon="🎧", layout="centered")

st.title("🎶 오늘의 기분 따라 K-POP 추천")
st.write("당신의 **오늘 기분**을 선택하면 어울리는 한국 노래를 추천해드릴게요!")

# 기분별 한국 노래 데이터
emotion_music = {
    "행복해요 😊": [
        {"title": "볼빨간사춘기 - 여행", "url": "https://www.youtube.com/watch?v=g6U2SS-ZMy8&list=RDg6U2SS-ZMy8&start_radio=1&pp=ygUG7Jes7ZaloAcB"},
        {"title": "아이유 - 좋은 날", "url": "https://www.youtube.com/watch?v=V6WWJNpIJN4&list=RDV6WWJNpIJN4&start_radio=1&pp=ygUJ7KKL7J2A64KgoAcB"},
    ],
    "슬퍼요 😢": [
        {"title": "이하이 - 한숨", "url": "https://www.youtube.com/watch?v=AT9e7H-X4Pg&list=RDAT9e7H-X4Pg&start_radio=1&pp=ygUG7ZWc7IiooAcB"},
        {"title": "헤이즈 - 비도 오고 그래", "url": "https://www.youtube.com/watch?v=aYDs3T-r__4&list=RDaYDs3T-r__4&start_radio=1&pp=ygUV67mE64-E7Jik6rOg6re4656Y7IScoAcB"},
    ],
    "화나요 😠": [
        {"title": "방탄소년단 - MIC Drop", "url": "https://www.youtube.com/watch?v=Zj3TcKZY648&list=RDZj3TcKZY648&start_radio=1&pp=ygUP66eI7J207YGs65Oc66GtoAcB"},
        {"title": "지코 - Okey Dokey", "url": "https://www.youtube.com/watch?v=pFOS5viKFjk&list=RDpFOS5viKFjk&start_radio=1&pp=ygUM7Jik7YKk64-E7YKkoAcB"},
    ],
    "평온해요 😌": [
        {"title": "폴킴 - 모든 날, 모든 순간", "url": "https://www.youtube.com/watch?v=nq0BYGyH2Do&list=RDnq0BYGyH2Do&start_radio=1&pp=ygUX66qo65OgIOuCoCDrqqjrk6DsiJzqsISgBwE%3D"},
        {"title": "멜로망스 - 선물", "url": "https://www.youtube.com/watch?v=wTCU8wOFq5E&list=RDwTCU8wOFq5E&start_radio=1&pp=ygUG7ISg66y8oAcB"},
    ],
}

# 사용자 기분 선택
emotion = st.selectbox("오늘 기분은?", list(emotion_music.keys()))

if st.button("추천 받기 🎵"):
    if emotion:
        song = random.choice(emotion_music[emotion])
        st.success(f"‘{emotion}’ 기분엔 이 노래 어때요?")
        st.markdown(f"**🎵 {song['title']}**")
        st.video(song["url"])
    else:
        st.warning("기분을 선택해주세요!")

