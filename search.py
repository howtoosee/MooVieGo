from googleapiclient.discovery import build

env = {}


with open(".env", 'r') as file:
    contents = file.read().split()
    for line in contents:
        k, v = line.split("=")
        env[k] = v


def custom_search(term):
    resource = build("customsearch", 'v1', developerKey=env['CSE_API_KEY']).cse()
    res = resource.list(q=term, cx=env['CSE_ID']).execute()
    return res

