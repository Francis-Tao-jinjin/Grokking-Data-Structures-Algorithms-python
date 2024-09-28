import requests
from requests.exceptions import RequestException
import re

def get_url(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except RequestException as e:
        print(f"Error: {e}")
        return None
    
    try:
        with open(output_file, 'w') as f:
            f.write(response.text)
    except IOError as e:
        print(f"Error: {e}")
        return None
    # return re.search(r"<title>(.*)</title>", response.text).groups()

# print(get_url("https://www.google.com", "output.html"))
get_url("https://api.github.com/events", "events.json")