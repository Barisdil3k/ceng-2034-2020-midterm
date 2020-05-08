# This program sends requests to a few URLs and checks the status code returned by them (using threads)

from threading import Thread

import requests

# an array of URLs
urls = ['https://api.github.com', 'http://bilgisayar.mu.edu.tr/',
        'https://www.python.org/', 'http://akrepnalan.com/ceng2034',
        'https://github.com/caesarsalad/wow']


def url_is_valid(_url: str) -> None:
    # make a request to the URL
    response = requests.get(url=_url)

    # assign the status code to another variable
    code = response.status_code

    # if status code is 2xx
    if code // 100 == 2:  # or 'code in range(200, 300)'
        print(f"URL: {_url}", f"Status: {code} (Successful)",
              sep='\n')
    else:
        print(f"URL: {_url}",
              f"Status: {code} (Failed)",
              sep='\n')


if __name__ == '__main__':
    # create an empty list to store threads
    threads = []

    # for each URL in the URL array
    for url in urls:
        # create a Thread
        t = Thread(target=url_is_valid, args=[url])

        # start it
        t.start()

        # append it to the threads array
        threads.append(t)

    for thread in threads:
        # wait until each thread terminates
        thread.join()

    print("\nCompleted.")
