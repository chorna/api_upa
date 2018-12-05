from django.conf.urls import url, include
from django.urls import path

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'alumnos', views.AlumnoViewSet)
router.register(r'profesor_lista', views.ProfesorLista)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('login', views.login),
    path('alumnos', views.AlumnoLista.as_view()),
    path('alumno/<int:pk>/', views.AlumnoDetalle.as_view()),
    path('profesores', views.ProfesorLista.as_view()),
    path('profesor/<int:pk>/', views.ProfesorDetalle.as_view()),
    path('cursos', views.CursoLista.as_view()),
    path('curso/<int:pk>/', views.CursoDetalle.as_view()),
    path('notas', views.NotaLista.as_view()),
    path('nota/<int:pk>/', views.NotaDetalle.as_view()),
    path('notas/seccion/<int:pk>/', views.nota_seccion_lista),
    #path('notas/alumno/<int:pk>/', views.NotaAlumnoLista.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('sampleapi', views.sample_api)
]