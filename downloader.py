#!/usr/bin/python
# -*- coding: utf-8 -*-

# 2012 (c) Suvorov Roman, windj007@gmail.com

import sys, re, requests



import browser_objects
import dom_builder

class Browser(object):
    __re_script_start       = re.compile(r"(<scrip[^>]*[^/]>)");
    __re_script_start_cdata = r'\1<!--'; #r'\1<![CDATA[';
    __re_script_end         = re.compile(r"</script>");
    __re_script_end_cdata   = r'--></script>';#r']]></script>';

    def __init__(self):
        self.__parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("dom"))

    def downloadHTML(self, url):
        return self.processHTMLtoHTML(self.__downloadImpl(url), url)

    def downloadDOM(self, url):
        return self.processHTMLtoDOM(self.__downloadImpl(url), url)

    def processHTMLtoDOM(self, page_html, url = ''):
        self.url = url
        self.page_html = page_html
        return self.processDOM(self.__parseHTML(page_html))

    def processHTMLtoHTML(self, page_html, url = ''):
        return self.__genHTML(self.processHTMLtoDOM(page_html, url))

    def processDOM(self, dom):
        self.dom = dom # save for further usage
        with PyV8.JSContext(browser_objects.Window(self)) as context:
            for script_tag in dom.getElementsByTagName("script"):
                if script_tag.hasAttribute('type') and script_tag.getAttribute('type') == 'text/javascript':
                    jscode = self.__downloadImpl(script_tag.getAttribute("src")) if script_tag.hasAttribute('src') else ''.join([child.data for child in script_tag.childNodes])
                    #if script_tag.hasAttribute('src'):
                        #print "********************external:\n" + script_tag.getAttribute("src")
                    #else:
                        #print "********************internal:\n" + ''.join([child.data for child in script_tag.childNodes])
                    context.eval(jscode)
        return dom

    def __parseHTML(self, html):
        #cdata_opened = Downloader.__re_script_start.sub(Downloader.__re_script_start_cdata, html)
        #cdata_closed = Downloader.__re_script_end.sub(Downloader.__re_script_end_cdata, cdata_opened)
        return dom_builder.HTMLtoDOM(html)

    def 

    def __genHTML(self, dom):
        return dom.toprettyxml(indent = "  ")

    def __downloadImpl(self, url):
        resp = requests.get(url)
        if resp.status_code < 400:
            return resp.text
        else:
            return ""

dl = Browser()
#dom = dl.downloadDOM("http://drugoi.livejournal.com/3713501.html?format=light")
#dom = dl.downloadDOM("http://www.google.com")
print dl.downloadHTML("http://jqueryui.com/demos/button/").encode('UTF-8')

#with PyV8.JSContext(Window(dom)) as cont:
#    cont.eval('window.getElementsByTagName("div")[0].innerHTML = "<p>test text</p>"')
    #print cont.eval('window.getElementsByTagName("title")[0].childNodes[0].data')

#print dom.getElementsByTagName("div")[0].toxml()