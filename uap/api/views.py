from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
from rest_framework import permissions

from .models import Alumno, Profesor
from .serializers import UserSerializer, GroupSerializer, AlumnoSerializer, ProfesorSerializer

# Create your views here.


class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)


class AlumnoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer


class ProfesorLista(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AlumnoLista(generics.ListCreateAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AlumnoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    permission_classes = (permissions.IsAuthenticated,)