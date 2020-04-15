#< / ul >
#< ul
#
#
#class ="last" >
#
#< li
#
#
#class ="last_sold" >
#
#< h4 > Last
#Sold: < / h4 >
#< a
#href = "/sell/history/7499354" > 03
#Mar
#20 < / a >
#< / li >
#< li >
#< h4 > Lowest: < / h4 >
#€16.68
#< / li >
#< li >
#< h4 > Median: < / h4 >
#€31.66
#< / li >
#< li >
#< h4 > Highest: < / h4 >
#€90.00
#< / li >
#< / ul >

from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse


class DiscogParser(HTMLParser):
    FLAG_H4_STARTTAG = 0
    pricename = ""
    pricevalue = ""
    pricehighest = ""
    pricelowest = ""
    pricemedian = ""
    pricenamehighest = "Highest:"
    pricenamelowest = "Lowest:"
    pricenamemedian = "Median:"

    # FLAG_H4_STARTTAG = 1 <li>
    # FLAG_H4_STARTTAG = 2 <li> && <h4>
    # FLAG_H4_STARTTAG = 3 <li> && <h4> && </h4>
    # FLAG_H4_STARTTAG = 4 <li> && <h4> && </h4> && </li>

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        if (self.FLAG_H4_STARTTAG == 3):
            if tag == "li":
                self.FLAG_H4_STARTTAG = 4

        if (self.FLAG_H4_STARTTAG == 2):
            if tag == "h4":
                self.FLAG_H4_STARTTAG = 3


    def handle_data(self, data):
        #print("Encountered some data  :", data)
        if (self.FLAG_H4_STARTTAG == 2):
            self.pricename = data
            #print(self.pricename+"**************")
        if (self.FLAG_H4_STARTTAG == 3):
            self.pricevalue = data
            self.pricevalue = self.pricevalue.replace(" ","")
            self.pricevalue = self.pricevalue.replace("\n", "")
            #print(self.pricename+self.pricevalue)
            if self.pricename == self.pricenamehighest:
                self.pricehighest = self.pricevalue
            if self.pricename == self.pricenamelowest:
                self.pricelowest = self.pricevalue
            if self.pricename == self.pricenamemedian:
                self.pricemedian = self.pricevalue

    def handle_starttag(self, tag, attrs):
        #print("Encountered an start tag :", tag)
        if (self.FLAG_H4_STARTTAG==1):
            if tag == "h4":
                self.FLAG_H4_STARTTAG = 2
                #print("lower")
            else:
                self.FLAG_H4_STARTTAG = 0

        if tag == "li":
            self.FLAG_H4_STARTTAG = 1

    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-Type') == 'text/html; charset=utf-8':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")

            self.feed(htmlString)
            return htmlString, self.links
        else:
            return "", []



def spider(url):
    FLAG_H4_STARTTAG = 0
    parser = DiscogParser()
    parser.getLinks("https://www.discogs.com/Queen-Queen-II/release/7499354")
    print(parser.pricenamehighest+parser.pricehighest)
    print(parser.pricenamemedian+parser.pricemedian)
    print(parser.pricenamelowest+parser.pricelowest)

#code
#spider("https://www.discogs.com/Queen-Queen-II/release/7499354")
