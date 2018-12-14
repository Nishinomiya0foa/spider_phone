import urllib.request

class html_downloader(object):
    """下载器"""
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if response.getcode()!= 200:
            return None

        return response.read()