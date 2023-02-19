
from django.contrib import admin
from django.urls import path
from app1 import views
# hello subu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:id>/',views.view,name="view")
]
