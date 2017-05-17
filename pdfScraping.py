#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pdfScraping.py
#  
#  Copyright 2017 raja <raja@raja-Inspiron-N5110>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  https://schoolofdata.org/2013/08/16/scraping-pdfs-with-python-and-the-scraperwiki-module/

import scraperwiki, urllib2, urlparse, lxml, os, sys, requests
from bs4 import BeautifulSoup

def get_pdf_links(url):
     
    # create response object
    r = requests.get(url)
     
    # create beautiful-soup object
    soup = BeautifulSoup(r.content,'html5lib')
     
    # find all links on web-page
    links = soup.findAll('a')
 
    # filter the link sending with .pdf
    pdf_links = [url + link['href'] for link in links if link['href'].endswith('pdf')]
 
    return pdf_links
   

def RequestSend(url):
#Get content, regardless of whether an HTML, XML or PDF file
    pageContent = urllib2.urlopen(url)
    return pageContent

def process2PDF(LocationOfFile):
#Use this to get PDF, covert to XML
    pdfToProcess = RequestSend(LocationOfFile)
    pdfToObject = scraperwiki.pdftoxml(pdfToProcess.read())
    return pdfToObject

def parse_HTML_tree(contentToParse):
#returns a navigatibale tree, which you can iterate through
    soup = BeautifulSoup(contentToParse,"lxml")
    return soup

url="http://www-personal.umich.edu/~csev/books/py4inf/media/"
pdflinks=get_pdf_links(url)
pdf = process2PDF('http://greenteapress.com/thinkstats/thinkstats.pdf')
pdfToSoup = parse_HTML_tree(pdf)
soupToArray = pdfToSoup.findAll('text')
"""for line in soupToArray:
	print line """
for link in pdflinks:
         
        # obtain filename by splitting url and getting 
        # last string
        file_name = link.split('/')[-1]  
for FN in file_name:
	print FN
