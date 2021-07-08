import logging

import requests
import sys

log = logging.getLogger('urllib3')
log.setLevel(logging.DEBUG)
fh = logging.FileHandler("requests.log")
log.addHandler(fh)


def get_repos(query, sort_order=None, ignore=None):
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    all_results = []
    ind = 1
    while True:
        try:
            url = f"https://api.github.com/search/repositories?q={query}&page={ind}&per_page=100"

            # if sort_order:
            #     url = f"https://api.github.com/search/repositories?q={query}+sort:name-{sort_order}&page={ind}&per_page=100"
            # if ignore:
            #     url = f"https://api.github.com/search/repositories?q={query}+sort:name-{sort_order}+NOT+{ignore}+in:name&page={ind}&per_page=100"
            print(url)
            response = requests.get(url, headers=headers)
            data = response.json()
            if len(data["items"]) == 0:
                break
            for i in range(len(data["items"])):
                all_results.append(data["items"][i])
            ind += 1
        except Exception as exc:
            print(url, response.text)

            raise exc
    if sort_order == "asc":
        all_results = sorted(all_results, key=lambda x: x["name"])
    if sort_order == "desc":
        all_results = sorted(all_results, key=lambda x: x["name"], reverse=True)
    if ignore:
        all_results = list(filter(lambda x: x["name"].lower().find(ignore.lower()) == -1, all_results))
    return all_results


def main():
    if len(sys.argv) < 2:
        raise Exception("Please enter query string")
    if len(sys.argv) > 4:
        raise Exception("Maximum number of parameters should be 3!")
    if len(sys.argv) > 2 and sys.argv[2].lower() not in ["desc", "asc"]:
        raise Exception("Sort order should be 'asc' or 'desc'!")
    repos = get_repos(*sys.argv[1:])
    # pp(repos)
    print("Number of retrieved repositories is", len(repos))
    for i in repos:
        print(i["name"])


if __name__ == "__main__":
    main()
