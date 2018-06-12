from analysisfacebook.collect.api import web_request as wr
import analysisfacebook.collect.api as pdapi
url= 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'

def pd_gen_url(url):
    url = pdapi.pdpd_gen_url('http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',

    YM = '{0:04d}{1:02d}'.format(2017, 1),
    SIDO = '서울특별시',
    GUNGU = '',
    RES_NM = '',
    numOfRows = 50,
    _type = 'json',
    pageNo = 50)
    servicekey='FPy5uacbvV8XJ75rPgupzqA3BehQdF29Ge3RqAxe0WYLTFraOAgoRP53UFZ011EuiiL7fxS%2B56ouKNOTrk%2FytQ%3D%3D'

    print(url)
def success_fetch_user_list(response):
    print(response)

def error_fetch_user_list(e):
    print(e)

wr.json_request(url=url, success= success_fetch_user_list,
                error= error_fetch_user_list)
'''
json_result = wr.json_request(url)
print(json_result)
'''