from urllib.request import urlopen


def load_file_from_url(file_path: str):
    try:
        with open(file_path) as f:
            content = f.readline()
            return content
    except FileNotFoundError:
        print("the file {0} couldn\'t be found".format(file_path));

        exit(2)


def load_page(url: str):
    respone = urlopen(url)
    html = respone.read().decode('utf-8')
    return

def scrape_page(page_contents: str):
    # TODO: analyze the text
    pass
