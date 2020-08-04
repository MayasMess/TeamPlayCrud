from rest_framework import generics
from tabletoken.models import TableToken
from tabletoken.api.serializers import TableTokenSerializer


class TableTokenDetail(generics.RetrieveAPIView):
    queryset = TableToken.objects.all()
    serializer_class = TableTokenSerializer
