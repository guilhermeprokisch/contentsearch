# views.py

from django.shortcuts import render, HttpResponse
import requests
import json
# Create your views here.


def index(request):

    parsedData = []
    jsonList = []
    buzzsumo = {}
    if request.method == 'POST':
        query = request.POST.get('query')
        req = requests.get('https://api.buzzsumo.com/search/articles.json?q=' + query +'&result_type=total&num_results=100&language=pt&api_key=EVbxwdk2TiIJB2T6ScnA_temp&begin_date=1462059921', verify=False)
        #VERIFICAR QUESTAO DO CERTIFICADO SSL    
        jsonList.append(json.loads(req.content.decode("utf-8")))
        jsonList = jsonList[0]['results']
    for data in jsonList:
        buzzsumo['published_date'] = data['published_date']
        buzzsumo['title'] = data['title']
        buzzsumo['url'] = data['url']
        #buzzsumo['thumbnail'] = data['thumbnail']
        buzzsumo['domain_name'] = data['domain_name']
        buzzsumo['total_shares'] = data['total_shares']
        buzzsumo['twitter_shares'] = data['twitter_shares']
        parsedData.append(buzzsumo.copy())
    return render(request, 'app/searchContent.html', {'data': parsedData})
