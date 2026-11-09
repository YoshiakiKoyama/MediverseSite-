from django.contrib import admin
from django.urls import path, include

# Main URL routing for the website
urlpatterns = [

    # Django admin page
    path("admin/", admin.site.urls),

    # Routes requests to the beatmaps app
    path("", include("beatmaps.urls")),

    path("", include("accounts.urls")),

]