from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('redirprofile/', views.redirProfile),
    path('dekonekte/', views.dekonekte, name='dekonekte'),
    path('konekte/', views.koneksyon, name ='konekte'),
    path('enskri/', views.inscrire,name='inscrire'),
    path('profile/<str:user>', views.showProfile),
    path('new-project/', views.newProject,name='newProject'),
    path('project/<str:slug>', views.showProject),
    path('project/<str:slug>/<str:prouser>', views.showProject),
    path('new-profile/', views.newProfile),
    path('modify-profile/<int:user>', views.modifyProfile),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
