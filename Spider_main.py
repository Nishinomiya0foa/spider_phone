from bs4 import BeautifulSoup
import url_manager,html_downloader,html_outputer,html_parser

class Spider_main(object):
    def __init__(self):
        self.urls = url_manager.url_manager()
        self.downloader = html_downloader.html_downloader()
        self.parser = html_parser.html_parser()
        self.outputer = html_outputer.outputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('The {} url: {}'.format(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count += 1

                if count == 10:
                    break
            except:
                print('craw failed!')
        self.outputer.output_html()



if __name__ == '__main__':
    root_url = 'http://detail.zol.com.cn/1213/1212228/param.shtml'
    # root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = Spider_main()
    obj_spider.craw(root_url)