import streamlit as st
import os
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip

st.title("YouTube Automation for Senior Women’s Channel")

# User enters a topic
topic = st.text_input("Enter video topic:", "10 Things Every Senior Should Declutter")

if st.button("Generate Script"):
    script = f"Welcome! Today, we'll talk about {topic}. Let's dive in and discover some amazing insights!"
    st.text_area("Generated Script:", script)

    # Generate Voiceover
    tts = gTTS(script, lang="en")
    tts.save("voiceover.mp3")
    st.audio("voiceover.mp3", format="audio/mp3")

    # Create Video
    video = VideoFileClip("stock_video.mp4").subclip(0, 10)
    audio = AudioFileClip("voiceover.mp3")
    video = video.set_audio(audio)
    video.write_videofile("final_video.mp4", fps=24)

    st.video("final_video.mp4")

    # Download Video
    with open("final_video.mp4", "rb") as file:
        st.download_button("Download Video", file, file_name="final_video.mp4")
