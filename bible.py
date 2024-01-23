import urllib3

def get_link_to_number(num: int) -> str:
    hostname = f"https://www.biblestudy.org/bibleref/meaning-of-numbers-in-bible/{num}.html"
    http = urllib3.PoolManager()
    response = http.request('GET', hostname)

    if response.status == 200:
        return hostname
    else:
        return f"Failed loading number {num}. Status code: {response.status}"

print(get_link_to_number(input("Input a number: ")))
