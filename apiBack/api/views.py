# api/views.py
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import google.generativeai as genai

class ChatbotAPIView(APIView):
    def post(self, request):
        user_message = request.data.get('message')
        
        # Envoyer le texte à l'API de Google
        API_KEY = "AIzaSyAde0V4HHdCHOOJ4ZIR2Dx4mxGfc8QxS5w"  
        # url = f"https://api.example.com/v1/generative/{API_KEY}"  
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(user_message)
        
        return Response({"response": response.text}, status=status.HTTP_200_OK)


