import random
import string

from rest_framework import status, parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView
from rest_framework.compat import coreapi, coreschema
from account.models import Account
from account.api.serializers import RegistrationSerializer
from teams.models import Team
from teams.api.serializers import TeamAllSerializer
from players.api.serializers import PlayerAllSerializer


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


@api_view(['GET'])
def get_user_by_token_view(request, token):
    if request.method == 'GET':
        queryset = Token.objects.get(key=token)
        return Response({'user_id': queryset.user_id})


@api_view(['GET'])
def get_all_users_view(request):
    if request.method == 'GET':
        queryset = Account.objects.values('id', 'email')
        result = map(lambda item: dict(item, name=item.get('email').split('@')[0]), queryset)
        return Response({'users': result})


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


@api_view(['GET'])
@permission_classes((IsAdminUser, ))
def mass_population_view(request):
    if request.method == 'GET':
        queryset = Account.objects.values('id')
        team_data = []
        for query in queryset:
            for x in range(100):
                data = {'name': get_random_string(20), 'owner': query.get('id')}
                team_data.append(data)
        for team in team_data:
            serializer_team = TeamAllSerializer(data=team)
            if serializer_team.is_valid():
                serializer_team.save()
        queryset_team = Team.objects.values()
        player_data = []
        for query in queryset_team:
            for x in range(100):
                data = {'name': get_random_string(20), 'team': query.get('id'), 'owner': query.get('owner_id')}
                player_data.append(data)
        for player in player_data:
            serializer_player = PlayerAllSerializer(data=player)
            if serializer_player.is_valid():
                serializer_player.save()
        return Response({"response": "done"})


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'id': token.user_id})
