from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.api.serializers import RegistrationSerializer


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user."
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
            return Response(data)
        data = serializer.errors
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def logout_view(request, token):
    if request.method == 'DELETE':
        queryset = Token.objects.get(key=token)
        queryset.delete()
        return Response({'response': 'successfully deleted'})

