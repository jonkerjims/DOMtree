import os

import geoip2.database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
print(BASE_DIR)
def IPsearch(ip):

    # client = geoip2.webservice.Client(651126, 'Pc3DOQ2YnPga')
    #
    # response = client.insights(ip)
    reader = geoip2.database.Reader(os.path.join(BASE_DIR,'GeoLite2-City.mmdb'))
    response = reader.city(ip)  # 有多种语言，我们这里主要输出英文和中文print("你查询的IP的地理位置是:")
    address = response.country.names["zh-CN"]+';'+response.subdivisions.most_specific.names["zh-CN"]+';'+response.city.names["zh-CN"]
    position = (response.location.longitude,response.location.latitude)

    return address,position