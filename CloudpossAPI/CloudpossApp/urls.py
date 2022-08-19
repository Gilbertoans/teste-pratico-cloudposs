from django.conf.urls import url
from CloudpossApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
  url('Clientes',views.CloudpossAPI),
  url('Clientes',views.CloudpossAPI),

  url(r'^Clientes/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)