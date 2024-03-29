from django.urls import path

from listapp.views import BuildingDetail

from listapp.views import CreateBuilding

from listapp.views import DeleteBuilding

from listapp.views import show_glass_list2

from listapp.views import CreateGlass

from listapp.views import ShowUserBuilding

from listapp.views import EnrollPicture

from listapp.views import BuildingDetail2

app_name = 'listapp'

urlpatterns = [
    path('building/detail/<int:pk>', BuildingDetail2.as_view()),
    path('building/create/<str:pk>', CreateBuilding.as_view()),
    path('building/delete/<int:pk>', DeleteBuilding.as_view()),
    path('building/list/<str:pk>', ShowUserBuilding.as_view()),
    path('picture/create/<str:pk>', EnrollPicture.as_view()),
    path('glass/list/<str:user_id>', show_glass_list2),
    path('glass/create/<str:pk>', CreateGlass.as_view()),
    path('imsi/<int:pk>', BuildingDetail.as_view())
]