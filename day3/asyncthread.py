import concurrent.futures
import urllib.request

URLS = [

    'http://www.foxnews.com',
    'https://www.cnn.com',
    'http://bbc.uk.com',
    'http://same-made-up-domain.com',
    'https://www.wp.pl',

]

def load_url(url,timeout):
    with urllib.request.urlopen(url,timeout=timeout) as conn:
        return conn.read()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = {executor.submit(load_url,url,60):url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]

        try:
            data = future.result()
        except Exception as ex:
            print(f"{url} generuje wyjątek: {ex}")
        else:
            print(f"{url} - strona ma rozmiar: {len(data)} bajtów")