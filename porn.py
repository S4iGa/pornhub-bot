from pornhub_api import PornhubApi
import asyncio
from pornhub_api.backends.aiohttp import AioHttpBackend
import random
import pprint

api = PornhubApi()

def getEroVideo(words):
    data = api.search.search(
        words,
        ordering="mostviewed",
        period="weekly",
        tags=["japanese"],
    )
    videos =data.videos
    return videos
