from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SeededVM(APIView):
    def get(self,request):
        res = requests.get('https://support.ringcentral.com/content/dam/support/us/en/ringex/seeded-content/voicemail-new-user.json')
        return Response(res.json(), status=status.HTTP_200_OK)