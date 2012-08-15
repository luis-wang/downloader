#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.dom
from bs4 import BeautifulSoup

def createElement(source, doc)
    #if isinstance(source, bs4.Tag)
    res = doc.createElement(source.name)
    for attr in source:
        res.setAttribute(attr, source[attr])
    return res

def bs4toDOM(src_root, res_doc, cur_root):
    # copy children
    for child in src_root.contents:
        cur_root.appendChild(createElement(child, res_doc))
        bs4toDOM(child, res_doc, cur_root.childNodes[-1])

def HTMLtoDOM(html):
    root_source = BeautifulSoup(html)
    dom_impl = xml.dom.getDOMImplementation('4DOM')
    root_target = dom_impl.createDocument("", "", dom_impl.createDocumentType('html', '', 'http://www.w3.org/TR/html4/strict.dtd'))
    bs4toDOM(root_source, root_target)
    return root_target

