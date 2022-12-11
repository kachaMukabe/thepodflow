import requests
import time
from os import environ
from dotenv import load_dotenv

load_dotenv()

headers = {
    "Authorization": environ.get("ASSEMBLY_API_KEY"),
    "Content-Type": "application/json",
}


def transcribe(url):
    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

    json = {"audio_url": url, "iab_categories": True, "auto_chapters": True}

    response = requests.post(transcript_endpoint, json=json, headers=headers)

    polling_endpoint = transcript_endpoint + "/" + response.json()["id"]
    return polling_endpoint


def get_status(polling_endpoint):
    polling_response = requests.get(polling_endpoint, headers=headers)
    status = polling_response.json()["status"]
    return status, polling_response.json()


pe = transcribe("https://share.transistor.fm/s/cc6dba56")

status, _ = get_status(pe)
while status != "completed":
    print(status)
    status, res = get_status(pe)
    if status == "completed":
        print(res)
    time.sleep(2)
