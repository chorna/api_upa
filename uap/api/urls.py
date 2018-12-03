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
    #path('', include(router.urls)),
    path('logins', views.ExampleView.as_view()),
    path('alumnos', views.AlumnoLista.as_view()),
    path('alumnos_detalle/<int:pk>/', views.AlumnoDetalle.as_view()),
    path('profesores', views.ProfesorLista.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url('alumnos/', views.AlumnoViewSet),
]