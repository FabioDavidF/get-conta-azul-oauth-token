from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import urllib.parse
import requests
import os


HASHED_CLIENT_CREDENTIALS = os.environ["bDlSNEZ1NXF0YUhMMW5oZlFoV2d2SzBFb0hFd0JqQm46U1JrVkRkOFJmZ1dEbXpqYzFqTVcxQXRXbmhKREl6eHc="]
REDIRECT_URI = urllib.parse.quote_plus("http://localhost:8000/auth/get-token")
CLIENT_ID = "l9R4Fu5qtaHL1nhfQhWgvK0EoHEwBjBn"
STATE = "faeiuhfekljefkljfdhjksghjka"



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
    print(response.json())
    return HttpResponse(200)   