from urllib.request import Request, urlopen
from datetime import *
import sys
import json

#def print_error(error):
  #  print('%s %s' % (e, datetime.now()), file=sys.stdout)


def html_request(url= '' ,encoding='utf-8', success= None , error=lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)
        html = resp.read().decode(encoding)


        print('%s: success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:
            return html

        success(html)

    except Exception as e:
        if callable (error) is True:
            error(e)


def json_request(url=' ', encoding = 'utf-8', success = None, error = lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)):


    try:
        request = Request(url)
        resp = urlopen(request)
        resp_body = resp.read().decode(encoding)

        json_result = json.loads(resp_body)

        print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:
            return json_result

        success(json_result)

    except Exception as e:
        if callable(error) is True:
            error(e)

