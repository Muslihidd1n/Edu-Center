
from django.contrib import admin
from django.urls import path
from Tizim.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tizim),
    path('xona/', xona),
    path('yonalish/', yonalish),
    path('ustoz/', ustoz),
    path('guruh/', guruh),
    path('talaba/', talaba),
    path('tolov/', tolov),



    path('xona_update/<int:pk>/', xona_update),
    path('yonalish_update/<int:pk>/', yonalish_update),
    path('ustoz_update/<int:pk>/', ustoz_update),
    path('guruh_update/<int:pk>/', guruh_update),
    path('talaba_update/<int:pk>/', talaba_update),
    path('tolov_update/<int:pk>/', tolov_update),



    path('bitta_talaba/<int:pk>/', bitta_talaba),
    path('bitta_ustoz/<int:pk>/', bitta_ustoz),



    path('xona_ochir/<int:pk>/', xona_ochir),
    path('yonalish_ochir/<int:pk>/', yonalish_ochir),
    path('ustoz_ochir/<int:pk>/', ustoz_ochir),
    path('guruh_ochir/<int:pk>/', guruh_ochir),
    path('talaba_ochir/<int:pk>/', talaba_ochir),
    path('tolov_ochir/<int:pk>/', tolov_ochir),
]
