#!/usr/bin/python
# -*- coding: utf-8 -*-

# 2012 (c) Suvorov Roman, windj007@gmail.com

import re
import PyV8

from urlparse import urlparse
from datetime import datetime

import logging

class BrowserObject(PyV8.JSClass):
    def __init__(self, browser):
        super(BrowserObject, self).__init__()
        self.browser = browser

class History(BrowserObject):
    def __init__(self, browser):
        super(History, self).__init__(browser)
        self.length = 0

    def back(self):
        pass
    def forward(self):
        pass
    def go(self, target):
        pass

class Location(BrowserObject):
    __re_netloc = re.compile(r"^([^:]+):?(\d+)?")
    def __init__(self, browser):
        super(Location, self).__init__(browser)
        parsed = urlparse(browser.url)
        netloc_parsed = Location.__re_netloc.match(parsed.netloc).groups('')
        self.hash = "#" + parsed.fragment
        self.host = parsed.netloc
        self.hostname = netloc_parsed[0]
        self.href = browser.url
        self.pathname = parsed.path
        self.port = netloc_parsed[1]
        self.protocol = parsed.scheme + ":"
        self.search = "?" + parsed.query
    def assign(self, url):
        pass
    def reload(self):
        pass
    def replace(self, url):
        pass

class Navigator(BrowserObject):
    def __init__(self, browser):
        super(Navigator, self).__init__(browser)
        self.appCodeName = "Mozilla"
        self.appName = "Netscape"
        self.appVersion = "5.0 (X11; Linux x86_64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.75 Safari/537.1"
        self.cookieEnabled = False # maybe worth enabling it
        self.onLine = True
        self.platform = "Linux"
        self.userAgent = self.appCodeName + "/" + self.appVersion
    def javaEnabled(self):
        return True
    def taintEnabled(self):
        return None

class Screen(BrowserObject):
    def __init__(self, browser):
        super(Screen, self).__init__(browser)
        availHeight = 1024
        availWidth = 1024
        colorDepth = 24
        height = 1024
        pixelDepth = 24
        width = 1024

class Document(BrowserObject, xml.dom.minidom.Document):
    def __init__(self, browser):
        super(Document, self).__init__(browser)
        self.anchors = [a for a in browser.dom.getElementsByTagName('a') if a.hasAttribute('name') and a.getAttribute('name')]
        self.applets = browser.dom.getElementsByTagName('applet')
        self.body = browser.dom.getElementsByTagName('body')[0]
        self.cookie = []
        self.domain = browser.window.location.hostname
        self.forms = browser.dom.getElementsByTagName('form')
        self.images = browser.dom.getElementsByTagName('img')
        self.lastModified = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.links = [a for a in browser.dom.getElementsByTagName('a') if a.hasAttribute('href') and a.getAttribute('href')]
        self.readyState = True
        self.referrer = ""
        self.title = browser.dom.getElementsByTagName('title')[0].childNodes[0].nodeValue
        self.URL = browser.url
    def close(self):
        pass
    def getElementsByName(self, name):
        return self.browser.dom.getElementsByName(name)
    def open(self, mime, replace):
        pass
    def write(self, *args):
        pass
    def writeln(self, *args):
        pass

class Window(BrowserObject):
    def __init__(self, browser):
        super(Window, self).__init__(browser)
        browser.window      = self
        self.window         = self
        self.closed         = False
        self.defaultStatus  = ""
        self.frames         = [self] + browser.dom.getElementsByTagName('frame') + browser.dom.getElementsByTagName('iframe') # TODO: implement frames right
        self.length         = len(self.frames)
        self.innerHeight    = 1024
        self.innerWidth     = 1024
        self.name           = "some window"
        self.opener         = None
        self.outerHeight    = 1024
        self.outerWidth     = 1024
        self.pageXOffset    = 0
        self.pageYOffset    = 0
        self.parent         = None
        self.screenLeft     = 0
        self.screenTop      = 0
        self.screenX        = 0
        self.screenY        = 0
        self.status         = "don't worry be happy"
        self.top            = self
        self.screen         = Screen(browser)
        self.location       = Location(browser)
        self.navigator      = Navigator(browser)
        self.history        = History(browser)
        self.document       = Document(browser)
    def alert(self, msg):
        logging.warning(msg)
    def blur(self):
        pass
    def clearInterval(self, interval_id):
        pass
    def clearTimeout(self, timeout_id):
        pass
    def close(self):
        pass
    def confirm(self, msg):
        logging.info("Confirm was requested: " + msg)
        return True
    def focus(self):
        pass
    def moveBy(self, x, y):
        pass
    def moveTo(self, x, y):
        pass
    def open(self, URL, name, specs, replace):
        pass
    def print_(self):
        pass
    def prompt(self, msg, defaultText):
        return defaultText
    def resizeBy(self, w, h):
        pass
    def resizeTo(self, w, h):
        pass
    def scroll(self, *args):
        pass
    def scrollBy(self, x, y):
        pass
    def scrollTo(self, x, y):
        pass
    def setInterval(self, code, msec, lang='JavaScript'):
        pass
    def setTimeout(self, code, msec, lang='JavaScript'):
        pass
