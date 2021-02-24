from django.contrib import admin
from django.urls import path
from django.urls import include

# from .views import startingPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('base_blog.urls'))  # This request will be processed by base_blog-application
]
