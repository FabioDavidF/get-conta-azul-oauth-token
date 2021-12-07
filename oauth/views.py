from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .utils import create_json_file
import urllib.parse
import requests
import os
import json


HASHED_CLIENT_CREDENTIALS = os.environ["HASHED_CONTA_AZUL_CLIENT_CREDENTIALS"]
CLIENT_ID = os.environ["CONTA_AZUL_CLIENT_ID"]
REDIRECT_URI = urllib.parse.quote_plus("http://localhost:8000/auth/get-token")
STATE = "random_string"


# Create your views here.
def authorize(request):
    url = f"https://api.contaazul.com/auth/authorize?redirect_uri={REDIRECT_URI}&client_id={CLIENT_ID}&scope=sales&state={STATE}"
    return HttpResponseRedirect(url)

def get_token(request):
    code = request.GET.get("code")
    state = request.GET.get("state")
    if state != STATE:
        return HttpResponse(status=401)

    url = f"https://api.contaazul.com/oauth2/token?grant_type=authorization_code&redirect_uri={REDIRECT_URI}&code={code}"
    headers = {
        "Authorization": f"Basic {HASHED_CLIENT_CREDENTIALS}"
    }
    response = requests.post(url, headers=headers)
    create_json_file(json.loads(response.content))
    return HttpResponse(200)