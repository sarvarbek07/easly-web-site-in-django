# from .views import Detail,Blogview
from . views import *
from . import views
from django.urls import path
from django.conf.urls.static import static
from config.settings import MEDIA_ROOT,MEDIA_URL

urlpatterns=[

    path("",Blogview.as_view(),name="BV"),
    path('post/<int:pk>/',Detail.as_view(),name="detail"),
    path("post/new",views.addform,name="create"),
    
]+ static(MEDIA_URL,document_root=MEDIA_ROOT)