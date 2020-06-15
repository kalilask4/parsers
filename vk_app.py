import requests
import time


def get_count_posts():
    # https://api.vk.com/method/wall.get?access_token=a1b42744a1b42744a1b4274443a1c6b8adaa1b4a1b42744ff539e2e241551e4694a2ac9&v=5.110&domain=php2all
    url = 'https://api.vk.com/method/wall.get'
    token = 'a1b42744a1b42744a1b4274443a1c6b8adaa1b4a1b42744ff539e2e241551e4694a2ac9'
    version = 5.21
    domain = 'php2all'
    count = 100
    offset = 0
    posts = []

    while offset < 1000:
        response = requests.get(url,
                                params={'access_token': token,
                                        'v': version,
                                        'domain': domain,
                                        'count': count,
                                        'offset': offset})
        data = response.json()['response']['items']
        offset += 100
        posts.extend(data)
        time.sleep(0.5)
        return posts
    
posts = get_count_posts()

print(1)
