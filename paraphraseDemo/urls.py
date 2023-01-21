from django.contrib import admin
from django.urls import path,include
from .views import index,paraphraseText,summarizeText
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

path("",index,name="index"),
path('paraphraseText',paraphraseText,name="paraphraseText"),
path('summarizeText',summarizeText,name="summarizeText")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
