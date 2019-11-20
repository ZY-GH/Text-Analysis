import requests
import os
from lxml import etree
from random import choice
import time
with open('company_information.csv',encoding='UTF-8') as f:
    a = []
    for line in f:
        a.append(line.strip().split(','))

#修正第一项，去掉错误编码
a[0]=['600036','招商银行']

proxies = []
with open('host.txt','r') as f:
    lines = f.readlines()
    c = {}
    for line in lines:
        b = line.split('#')
        c[b[0]]=b[0]+'://'+b[1]
        proxies.append(c)
        c.clear()


#开始爬虫
base_url = 'http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/search/index.phtml?t1=2&symbol=%s'
headers_1 = {
    "Proxy-Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "DNT": "1",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    "Referer": "https://www.baidu.com/s?wd=%BC%96%E7%A0%81&rsv_spt=1&rsv_iqid=0x9fcbc99a0000b5d7&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&oq=If-None-Match&inputT=7282&rsv_t",
    "Accept-Charset": "gb2312,gbk;q=0.7,utf-8;q=0.7,*;q=0.7",
}  # 网上找的浏览器
headers_2 = {
    "Proxy-Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
    "Accept": "image/gif,image/x-xbitmap,image/jpeg,application/x-shockwave-flash,application/vnd.ms-excel,application/vnd.ms-powerpoint,application/msword,*/*",
    "DNT": "1",
    "Referer": "https://www.baidu.com/link?url=c-FMHf06-ZPhoRM4tWduhraKXhnSm_RzjXZ-ZTFnPAvZN",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
}  # window 7 系统浏览器
headers_3 = {
    "Proxy-Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "image/x-xbitmap,image/jpeg,application/x-shockwave-flash,application/vnd.ms-excel,application/vnd.ms-powerpoint,application/msword,*/*",
    "DNT": "1",
    "Referer": "https://www.baidu.com/s?wd=http%B4%20Pragma&rsf=1&rsp=4&f=1&oq=Pragma&tn=baiduhome_pg&ie=utf-8&usm=3&rsv_idx=2&rsv_pq=e9bd5e5000010",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.7,en;q=0.6",
}  # Linux 系统 firefox 浏览器
headers_4 = {
    "Proxy-Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Accept": "*/*",
    "DNT": "1",
    "Referer": "https://www.baidu.com/link?url=c-FMHf06-ZPhoRM4tWduhraKXhnSm_RzjXZ-ZTFnP",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.7,en;q=0.6",
}  # Win10 系统 firefox 浏览器
headers_5 = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://www.baidu.com/link?url=c-FMHf06-ZPhoRM4tWduhraKXhnSm_RzjXZ-",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.7,en;q=0.6",
    "Accept-Charset": "gb2312,gbk;q=0.7,utf-8;q=0.7,*;q=0.7",
}  # Win10 系统 Chrome 浏览器
headers_6 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "DNT": "1",
    "Referer": "https://www.baidu.com/s?wd=If-None-Match&rsv_spt=1&rsv_iqid=0x9fcbc99a0000b5d7&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rq",
    "Accept-Charset": "gb2312,gbk;q=0.7,utf-8;q=0.7,*;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
}

headers = choice([headers_1,headers_2,headers_3,headers_4,headers_5,headers_6])
for item in a[29:]:
    url = base_url % item[0]
    doc = requests.get(url,headers= headers,proxies = choice(proxies))
    #time.sleep(2)
    #print(doc.encoding)
    html = etree.HTML(doc.text.encode('ISO-8859-1'))

    #根据公司名称建立相应的子文件夹
    try:
        os.mkdir('%s'%item[1])
    except:
        pass
    #提取所有包办目标信息的节点，都存储在tr节点下，并且从第三个tr节点开始



    #获取所有2018年10月1号以后发出的研报的日期

    #获取研究报告的总页数


    second_html = etree.HTML(doc.text.encode('ISO-8859-1').decode('ISO-8859-1'))

    pages_num = second_html.xpath(
        "//div[@class='pagebox']//span[contains(@class,'pagebox_num')]//text()"
    )

    #print(pages_num)

    research_num_count = 1

    work_dir = os.getcwd()

    print(item[1]+'\t股票代码(%s)'% item[0]+'****其股票研究报告如下')
    if pages_num==[]:

        page_url = base_url % item[0]

        page_doc = requests.get(page_url,headers= headers,proxies = choice(proxies))

        #time.sleep(2)

        #print(page_doc.text.encode('ISO-8859-1').decode('ISO-8859-1')[:100])

        page_html = etree.HTML(page_doc.text.encode('ISO-8859-1').decode('gbk').encode('utf-8').decode('utf-8'))

        initial_tr_nodes = page_html.xpath('//div[@class="main"]//tr')[2:-1]
        #print(initial_tr_nodes)

        tr_nodes = []

        all_dates = []

        #获取2018年10月1日以前发布的研报的日期并且去掉2018年10月1日以后发布的研报的HTML节点
        for tr in initial_tr_nodes:
            date_lst = tr.xpath('./td[4]/text()')[0].strip().split('-')
            #print(date_lst)
            if int(date_lst[0])==2018:
                if int(date_lst[1])>=10:
                    continue
                else:
                    all_dates.append(tr.xpath('./td[4]//text()')[0].strip())
                    tr_nodes.append(tr)
            elif int(date_lst[0])<2018:
                all_dates.append(tr.xpath('./td[4]//text()')[0].strip())
                tr_nodes.append(tr)
        #num_of_research = len(all_dates)


        #获取目标研报的名字
        names_of_research = []
        for tr in tr_nodes:
            names_of_research.append(tr.xpath('./td[2]/a/text()')[0].strip())

        #获取目标研报的链接
        link_of_research = []

        for tr in tr_nodes:
            link_of_research.append(tr.xpath('./td[2]/a/@href')[0])

        #获取研究机构名称

        names_of_reseach_organization = []
        for tr in tr_nodes:
            names_of_reseach_organization.append(\
                        tr.xpath('./td[5]/a/div/span/text()')[0].strip())

        #以日期作为文件夹名创建机构名文件夹下子文件夹，并且在其中每个文件夹放入两个文件，一个文件存储日期机构，格式为csv格式，另一个存储内容，为txt格式

        count = 1

        cur_dir = work_dir+'\\'+item[1]

        for link in link_of_research:
            link_doc = requests.get(link,headers= headers,proxies = choice(proxies))
            #time.sleep(2)
            link_html = etree.HTML(link_doc.text.encode('ISO-8859-1').decode('gbk').encode('utf-8').decode('utf-8'))

            article = link_html.xpath('//p//text()')[0]
            try:
                new_chdir = all_dates[count - 1] + '(第%d份研报)' % research_num_count
                os.mkdir(os.path.join(cur_dir, new_chdir))
            except:
                pass

            os.chdir(cur_dir+'\\'+ new_chdir)

            #开始将目标数据写入文件当中

            #1.将研报内容写入txt文件当中,以研究机构名作为文件名

            with open(
                    names_of_reseach_organization[count - 1] + '.txt',
                    'w+',
                    encoding='UTF-8') as f:
                for par in link_html.xpath('//p//text()'):
                    f.write(par)
                    f.write('\n')

            #2.将研报日期，机构，标题写入一个csv文件当中，并且以研究机构作为名称

            with open(names_of_reseach_organization[count-1]+'.csv','w+',encoding='UTF-8') as f:
                f.write('日期')
                f.write(',')
                f.write('机构')
                f.write(',')
                f.write('标题')
                f.write('\n')
                f.write(all_dates[count-1])
                f.write(',')
                f.write(names_of_reseach_organization[count-1])
                f.write(',')
                f.write(names_of_research[count-1])
            os.chdir(work_dir)
            print(item[1] + '公司的第%d份研究报告' % research_num_count + '\t' +
              '%s' % names_of_research[count - 1] + '\t' +
              '%s' % names_of_reseach_organization[count - 1])
            count += 1
            research_num_count += 1
    else:

        for page in pages_num:


            page_url = base_url % item[0]+'&p=%s' % page

            page_doc = requests.get(page_url,headers= headers,proxies = choice(proxies))

            #time.sleep(2)

            #print(page_doc.text.encode('ISO-8859-1').decode('ISO-8859-1')[:100])

            page_html = etree.HTML(page_doc.text.encode('ISO-8859-1').decode('gbk').encode('utf-8').decode('utf-8'))

            initial_tr_nodes = page_html.xpath('//div[@class="main"]//tr')[2:-1]
            #print(initial_tr_nodes)

            tr_nodes = []

            all_dates = []

            #获取2018年10月1日以前发布的研报的日期并且去掉2018年10月1日以后发布的研报的HTML节点
            for tr in initial_tr_nodes:
                date_lst = tr.xpath('./td[4]/text()')[0].strip().split('-')
                #print(date_lst)
                if int(date_lst[0])==2018:
                    if int(date_lst[1])>=10:
                        continue
                    else:
                        all_dates.append(tr.xpath('./td[4]//text()')[0].strip())
                        tr_nodes.append(tr)
                elif int(date_lst[0])<2018:
                    all_dates.append(tr.xpath('./td[4]//text()')[0].strip())
                    tr_nodes.append(tr)
            #num_of_research = len(all_dates)


            #获取目标研报的名字
            names_of_research = []
            for tr in tr_nodes:
                names_of_research.append(tr.xpath('./td[2]/a/text()')[0].strip())

            #获取目标研报的链接
            link_of_research = []

            for tr in tr_nodes:
                link_of_research.append(tr.xpath('./td[2]/a/@href')[0])

            #获取研究机构名称

            names_of_reseach_organization = []
            for tr in tr_nodes:
                names_of_reseach_organization.append(\
                            tr.xpath('./td[5]/a/div/span/text()')[0].strip())

            #以日期作为文件夹名创建机构名文件夹下子文件夹，并且在其中每个文件夹放入两个文件，一个文件存储日期机构，格式为csv格式，另一个存储内容，为txt格式

            count = 1

            cur_dir = work_dir+'\\'+item[1]

            for link in link_of_research:
                link_doc = requests.get(link,headers= headers,proxies=choice(proxies))
                #time.sleep(2)
                link_html = etree.HTML(link_doc.text.encode('ISO-8859-1').decode('gbk').encode('utf-8').decode('utf-8'))

                article = link_html.xpath('//p//text()')[0]
                try:
                    new_chdir = all_dates[count - 1] + '(第%d份研报)' % research_num_count
                    os.mkdir(os.path.join(cur_dir, new_chdir))
                except:
                    pass

                os.chdir(cur_dir+'\\'+ new_chdir)

                #开始将目标数据写入文件当中

                #1.将研报内容写入txt文件当中,以研究机构名作为文件名

                with open(
                        names_of_reseach_organization[count - 1] + '.txt',
                        'w+',
                        encoding='UTF-8') as f:
                    for par in link_html.xpath('//p//text()'):
                        f.write(par)
                        f.write('\n')

                #2.将研报日期，机构，标题写入一个csv文件当中，并且以研究机构作为名称

                with open(names_of_reseach_organization[count-1]+'.csv','w+',encoding='UTF-8') as f:
                    f.write('日期')
                    f.write(',')
                    f.write('机构')
                    f.write(',')
                    f.write('标题')
                    f.write('\n')
                    f.write(all_dates[count-1])
                    f.write(',')
                    f.write(names_of_reseach_organization[count-1])
                    f.write(',')
                    f.write(names_of_research[count-1])
                os.chdir(work_dir)
                print(item[1] + '公司的第%d份研究报告' % research_num_count+'\t'+'%s' %names_of_research[count-1]+'\t'+'%s'%names_of_reseach_organization[count-1])
                count+=1
                research_num_count +=1
    print(item[1]+'公司的的数据已爬完'+'\t'+'总共有:%d份' %(research_num_count-1))
    #time.sleep(10)