from django.urls import path
from django.contrib.auth.views import LogoutView
from AppTuitlon import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('tuitlear/', views.tuitlear, name="Tuitlear"),
    path('tuitl/list', views.TuitlList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.TuitlDetalle.as_view(), name='Detail'),
    path(r'^borrar/(?P<pk>\d+)$', views.TuitlDelete.as_view(), name='Delete'),
    path('login', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='AppTuitlon/logout.html'), name='Logout'),
    path('register', views.register, name = 'Registrarse'),
    path("editUser", views.editUser, name='Editar Usuario'),
    path('addImg', views.addImg, name='Subir Avatar'),


]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)