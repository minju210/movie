def req(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "8faa3d66c8782fa7c4375f358b18faa6"
    url = f"{base_url}?key={key}&targetDt={dt}"
    print(url)

req()

