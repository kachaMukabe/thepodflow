import streamlit as st
import time
from podcast import search_podcasts, get_episodes
from assemblyai import transcribe, get_status


query = st.text_input("Search")


def get_transcription(url):
    polling_endpoint = transcribe(url)
    status, _ = get_status(polling_endpoint)
    while status != "completed":
        status, response = get_status(polling_endpoint)
        if status == "completed":
            st.write(response)
        time.sleep(2)


if query:
    results = search_podcasts(query)

    for result in results:
        st.write(result["title"])
        with st.expander("Episodes"):
            episodes = get_episodes(feed_id=result["id"])
            for episode in episodes:
                st.write(episode["title"])
                if st.button("Get Transcription", key=episode["id"]):
                    get_transcription(episode["enclosureUrl"])
