from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import AllowAny

from .models import Alumno, Profesor, Curso, Nota
from .serializers import (UserSerializer, GroupSerializer, AlumnoSerializer,
                          ProfesorSerializer, CursoSerializer, NotaSerializer)

# Create your views here.


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)

    from rest_framework.authtoken.models import Token
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=status.HTTP_200_OK)


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


class ProfesorDetalle(generics.RetrieveUpdateDestroyAPIView):
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


class CursoLista(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CursoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (permissions.IsAuthenticated,)


class NotaLista(generics.ListCreateAPIView):
    queryset = Nota.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (permissions.IsAuthenticated,)


class NotaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    permission_classes = (permissions.IsAuthenticated,)


class NotaSeccionLista(generics.ListCreateAPIView):
    queryset = Nota.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (permissions.IsAuthenticated,)

@csrf_exempt
@api_view(["GET"])
def nota_seccion_lista(request):
    seccion_id = request.GET.get('pk', None)
    data = []
    if seccion_id is not None:
        for nota in Nota.objects.filter(seccion_id=seccion_id):
            data.append({
                'alumno': nota.alumno.nombre,
                'nota': nota.nota
                })
    return Response(data, status=status.HTTP_200_OK)
    