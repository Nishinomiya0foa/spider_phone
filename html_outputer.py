# -*- coding: utf-8 -*-

class outputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # fout = open('output.html', 'w', encoding='utf-8')
        #
        # fout.write("<html>")
        # fout.write("<body>")
        # fout.write("<table>")
        #
        # for data in self.datas:
        #     fout.write('<tr>')
        #     fout.write('<td>{}</td>'.format(data['url']))
        #     fout.write('<td>{}</td>'.format(data['title'].encode('utf-8').decode('utf-8')))
        #     fout.write('<td>{}</td>'.format(data['summary'].encode('utf-8').decode('utf-8')))
        #     fout.write('</tr>')
        #
        # fout.write("</table>")
        # fout.write("</body>")
        # fout.write("</html>")
        # fout.close()
        with open('output222.xlsx', 'a', encoding='utf-8') as fout:
            for data in self.datas:
                fout.writelines('{}\t'.format(data['url']))
                fout.writelines('{}\t'.format(data['title'].encode('utf-8').decode('utf-8')))
                fout.writelines('{}\n'.format(data['summary'].encode('utf-8').decode('utf-8')))