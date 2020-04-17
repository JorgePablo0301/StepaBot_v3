import discogs_client
import parse_price_discog

#старый
import requests

class DcFindPrice():
    var_token = "xQUbJLOQvFlhicUHgtDnWUeMntwjiRyVuLoGavnm"
    var_artist = ''
    var_album = ''
    var_type = ''
    var_country = ''
    var_result = []
    var_name = ''
    pricemedian = ''
    pricelowest = ''
    pricehighest = ''
    data = ''
    print_data = ''
    PRINT_RESULT = 0
    title = ''
    year = '0'
    id = ''
    country = ''
    labels = ''
    master_lnk_string='release'
    def main_find(self):
        d = discogs_client.Client('JMoney/0.1', user_token=self.var_token)
        results = d.search(self.var_name, artist=self.var_artist, album=self.var_album, type=self.var_type, country=self.var_country)
        self.var_result = results.page(1)
        if self.PRINT_RESULT==1:
            print(self.var_result)

    def main_findprint(self):
        i = 0
        for x in self.var_result:
            #print(x.title, x.year, x.id, x.country, x.labels)
            self.title = x.title
            #self.year = x.year
            self.id = x.id
            #self.country = x.country
            #self.labels = x.labels
            self.data = str(x)
            #print(self.data[1:7].lower())
            if self.data[1:7].lower().__eq__('master'):
                self.master_lnk_string = 'master'
                #print(self.master_lnk_string)
            parser = parse_price_discog.DiscogParser()
            #parser.getLinks("https://www.discogs.com/release/" + str(x.id))
            strlink="https://www.discogs.com/"+self.master_lnk_string+"/" + str(x.id)
            #print(strlink)
            parser.getLinks(strlink)
            self.pricehighest = parser.pricenamehighest + parser.pricehighest
            self.pricemedian = parser.pricenamemedian + parser.pricemedian
            self.pricelowest = parser.pricenamelowest + parser.pricelowest
            self.print_data = self.data+"\n"+self.pricemedian+"\n"+self.title+"\n"+self.year+"\n"+str(self.id)+"\n"+self.country+"\n"+self.labels
            if self.PRINT_RESULT.__eq__(1):
                print(self.data)
                print(parser.pricenamehighest + parser.pricehighest)
                print(parser.pricenamemedian + parser.pricemedian)
                print(parser.pricenamelowest + parser.pricelowest)
            i = i+1
            if i>0:
              return

###################
# code
##################

dcfindprice = DcFindPrice()
dcfindprice.var_name = 'Queen Sheer Heart Attack us'
#dcfindprice.PRINT_RESULT = 1
dcfindprice.main_find()
dcfindprice.main_findprint()
print(dcfindprice.print_data)


