import podcastindex
from os import environ
from dotenv import load_dotenv

load_dotenv()

config = {
    "api_key": environ.get("API_KEY", ""),
    "api_secret": environ.get("API_SECRET", ""),
}

index = podcastindex.init(config)


def search_podcasts(query):
    result = index.search(query)
    if result["status"]:
        return result["feeds"]


def get_episodes(feed_id=None, feed_url=None, itunes_id=None):
    result = None
    if feed_id:
        result = index.episodesByFeedId(feed_id)
    if feed_url:
        result = index.episodesByFeedUrl(feed_url)
    if itunes_id:
        result = index.episodesByItunesId(itunes_id)
    if result and result["status"]:
        return result["items"]


def get_episode(episode_id):
    result = index.episodeById(episode_id)
    if result["status"]:
        return result["episode"]


# results = search_podcasts("Indie Hackers")
# episodes = get_episodes(feed_url=results[0]["url"])
# episode = get_episode(episodes[0]["id"])
# print(episode)
