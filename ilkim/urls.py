from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('index', views.index, name="success"),
    path('solidworks', views.solidworks, name="solidworks"),
    path('siemenx', views.siemennx, name="siemennx"),
    path('matlab',views.matlab,name="matlab"),
    path('python',views.pythondef,name="python"),
    path('ansys',views.ansysdef,name="ansys"),
    path('gui',views.guidef,name="gui"),
    path('gamedevelop',views.gamedevelopdef,name="gamedevelop"),
    path('grafiktasarlama',views.graphic,name="grafiktasarlama"),
    path('incele/<slug:slug>/<int:id>',views.latest,name="incele"),
]