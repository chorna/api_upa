from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token

from .models import Seccion, Alumno

# Create your tests here.


class LogInTest(TestCase):
    def setUp(self):
        self.base_url = '/api-v1/'
        self.credentials = {
            'username': 'apitest',
            'password': '1234',
            'is_active': True
            }
        user = get_user_model().objects.create_user(**self.credentials)
        response = self.client.post('/api-v1/login', self.credentials, follow=True)
        self.token = None
        if response.status_code == 200:
            self.token = Token.objects.get(user=user)

        s1 = {'codseccion': 'S1'}
        s2 = {'codseccion': 'S2'}
        seccion1 = Seccion.objects.create(**s1)
        secc2= Seccion.objects.create(**s2)

        alumno_1 = {'nombre':'jc', 'correo':'jc@vegusti.com', 'seccion': seccion1}
        alumno1 = Alumno.objects.create(**alumno_1)
        alumno_2 = {'nombre':'sergi', 'correo':'sergi@litho.com'}
        alumno2 = Alumno.objects.create(**alumno_2)

    def test_login(self):
        self.login_url = '%s%s' % (self.base_url, 'login')
        response = self.client.post(self.login_url, self.credentials, follow=True)
        self.assertTrue(response.status_code, 200)
        self.assertEqual(response.json(), {'token': self.token.key})

    def test_alumnos(self):
        self.alumnos_url = '%s%s' % (self.base_url, 'alumnos')
        response = self.client.get(self.alumnos_url)
        self.assertTrue(response.status_code, 401)

        header = {'content-type': "application/json",'HTTP_AUTHORIZATION': 'Token %s' % self.token.key}
        response = self.client.get(self.alumnos_url, **header)
        self.assertTrue(response.status_code, 200)
        self.assertTrue(len(response.data), 2)
        js = [{'id': 1, 'foto': None, 'nombre': 'jc', 'usuario': None, 'correo': 'jc@vegusti.com', 'seccion': 1},
              {'id': 2, 'foto': None, 'nombre': 'sergi', 'usuario': None, 'correo': 'sergi@litho.com', 'seccion': None}]
        self.assertEqual(response.json(), js)