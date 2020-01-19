from googleapiclient.discovery import build
from load_env import load_env

env = load_env()
CSE_ID = env["CSE_ID"]
CSE_API_KEY = env["CSE_API_KEY"]

# CSE_ID = "000675681608306227788:0mtlptlp0qh"
# CSE_API_KEY = "AIzaSyDVbEiJ3oRTvd9-QuroIspTURNWscrPicw"


def custom_search(term):
    resource = build("customsearch", 'v1', developerKey=CSE_API_KEY).cse()
    res = resource.list(q=term, cx=CSE_ID).execute()
    return res
