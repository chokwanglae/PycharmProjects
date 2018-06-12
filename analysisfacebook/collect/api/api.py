# fb_api wrapper function
from urllib.parse import urlencode
from .web_request import json_request
ACCESS_TOKEN="EAACEdEose0cBAAv1nDXWbDwFZAhHXRlZCc8CS43L0JaZAhZBhZCsEQJpOEiXRNxqymIBWqDbTUP2kNzrJJLaISJq0gFwLUCni8piZBu1QK4lVoUqqQZCkmlfanwc435ZA4nwC9LtZBSeXAvPpEqipqFiMlxaCvVW8GofZCfYl90G6DZBtvQbmz9LPgJ1K943uADEvOpSFTILj1XTQZDZD"
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"

def pd_gen_url(
        base =BASE_URL_FB_API,
        node='',
        **params):
    url='%s/%s/?%s' % (base, node, urlencode(params))
    return url

def pd_name_to_id(pagename):
    url = pd_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)
    return json_result.get("id")

def pd_fetch_posts(pagename, since, until):
    url = pd_gen_url(node=pd_name_to_id(pagename)+"/posts",
    fields='id, message, link, name, type, shares, reacticons, created_time, comments.limit(0).summary(true).limit(0).summary(true)',
    since = since,
    until= until,
    limit = 50,
    access_token=ACCESS_TOKEN)
    #json_result = json_request( url=url)


    isnext = True
    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else json_result.get('pasing')
        posts = None if json_result is None is None else json_result.get('data')


        URL = None if paging is None else paging.get("next")

        isnext = url is not None


        yield posts
