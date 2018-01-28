from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, CotacaoRequestSerializer
from quickstart.models import CotacaoRequest
from rest_framework.decorators import list_route

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CotacaoRequestViewSet(viewsets.ModelViewSet):
    queryset = CotacaoRequest.objects.all()
    serializer_class = CotacaoRequestSerializer
    """ordering_fields = ('publicacao', 'nota')"""

    @list_route(methods=['post'])
    
    def SendCotacaoRequest(self, request):
        name = request.POST['name']
        email = request.POST['email']
        vehicle_type = request.POST['vehicle_type']
        board_number = request.POST['board_number']


        if(nome is not None and email is not None and vehicle_type is not None and board_number is not None):
            cotacao_request = None
            try:
                cotacao_request = CotacaoRequest(name=name, email=email, vehicle_type=vehicle_type, board_number=board_number)
                cotacao_request.save()
            except:
                return Response(resposta, status = status.HTTP_500_OK)

        return Response(resposta, status = status.HTTP_200_OK)