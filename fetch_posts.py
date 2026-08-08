import json
from urllib.parse import urlencode
from urllib.request import urlopen

base_url = "https://masar-class-api.a-f-almatrafi.workers.dev/api/posts"
params = {"page": 1, "limit": 5}
url = f"{base_url}?{urlencode(params)}"

with urlopen(url, timeout=10) as resp:
    status = resp.status
    print(status)
    if status == 200:
        data = json.loads(resp.read().decode("utf-8"))["data"]
        for post in data:
            print(post["title"])
