# app.py

import streamlit as st
from music_data import emotion_music
import random

st.set_page_config(page_title="기분 음악 추천기", page_icon="🎧", layout="centered")

st.title("🎶 오늘의 기분 음악 추천기")
st.write("당신의 **오늘 기분**은 어떤가요? 아래에서 선택해 주세요.")

# 사용자 기분 선택
emotion = st.selectbox("기분 선택", list(emotion_music.keys()))

# 음악 추천 버튼
if st.button("음악 추천받기 🎵"):
    if emotion:
        song = random.choice(emotion_music[emotion])
        st.success(f"'{emotion}' 기분에 어울리는 음악은:")
        st.markdown(f"**{song['title']}**")
        st.video(song["url"])
    else:
        st.warning("기분을 먼저 선택해 주세요.")



# music_data.py

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
