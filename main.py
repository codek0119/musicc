import streamlit as st
import random

st.set_page_config(page_title="기분 따라 듣는 K-POP", page_icon="🎧", layout="centered")

st.title("🎶 오늘의 기분 따라 K-POP 추천")
st.write("당신의 **오늘 기분**을 선택하면 어울리는 한국 노래를 추천해드릴게요!")

# 기분별 한국 노래 데이터
emotion_music = {
    "행복해요 😊": [
        {"title": "볼빨간사춘기 - 여행", "url": "https://www.youtube.com/watch?v=9wRh1FHBozU"},
        {"title": "아이유 - 좋은 날", "url": "https://www.youtube.com/watch?v=jeqdYqsrsA0"},
    ],
    "슬퍼요 😢": [
        {"title": "이하이 - 한숨", "url": "https://www.youtube.com/watch?v=RIl2vRz0dqE"},
        {"title": "임재현 - 흔적", "url": "https://www.youtube.com/watch?v=UR3eV4gdc3Y"},
    ],
    "화나요 😠": [
        {"title": "방탄소년단 - MIC Drop", "url": "https://www.youtube.com/watch?v=kTlv5_Bs8aw"},
        {"title": "지코 - Okey Dokey", "url": "https://www.youtube.com/watch?v=Ycv5fNd4AeM"},
    ],
    "평온해요 😌": [
        {"title": "폴킴 - 모든 날, 모든 순간", "url": "https://www.youtube.com/watch?v=YQHsXMglC9A"},
        {"title": "멜로망스 - 선물", "url": "https://www.youtube.com/watch?v=oK0jUu4T7ME"},
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

