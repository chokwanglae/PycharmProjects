from analysisfacebook import collect

if __name__ == '__main__':
    items = [

       {'pagename' : 'jtbcnews' , 'since' : '2017-01-01', 'until' : '2017-12-31'},
       {'pagename': 'chosun' , 'since' : '2017-01-01', 'until': '2017-12-31'}
    ]

    for item in items:
        collect.crawling(**item)

    #collect.crawling("jtbcnews", "2017-01-01", "2017-12-31")

    #데이터 분석(analize)


    #데이터 시각화 (visualize)


