class url_manager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def get_new_url(self):
        """从url管理器中获取一个新的url"""
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        """向管理器中添加一个url"""
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        """判断管理器中是否有新的待爬去的url"""
        return len(self.new_urls) != 0

    def add_new_urls(self, urls):
        """向管理器中添加一系列urls"""
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)