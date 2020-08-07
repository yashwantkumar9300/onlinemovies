import http.client
import json

class Moviesmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")
        headers = {
                    'x-rapidapi-host': "imdb8.p.rapidapi.com",
                    'x-rapidapi-key': "4422ecdd22msh0284eaac7d64721p1d830ejsn5fc033392fd1"
                  }
        conn.request("GET", "/title/auto-complete?q=game%20of%20thr", headers=headers)
        res = conn.getresponse()
        data = res.read()
        x=data.decode("utf-8")
        print(type(x))
        dict_data = json.loads(x)
        json.dump(dict_data,open("app_admin/raw/movies.json","w"))

    def __call__(self,request, *args, **kwargs):
        response=self.get_response(request)
        return response

