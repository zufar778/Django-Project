from django.contrib import admin
from django.urls import path
from main.views import home,cards,about, detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="Home_page_111"),
    path('about/', about, name="About page"),
    path('cards/', cards, name="Cards_Page"),
    path('detail/<int:id>/', detail, name="detail")
    # path('cards/<int:id>/<str:text>/<slug:slug>/', cards)
]
