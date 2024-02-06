from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]


# from .views import create_book

# urlpatterns = [
    # path('create/', create_book, name='create_book'),
# ]


## Router 사용하지 않은 url 패턴 수동 정의

# from django.urls import path
# from .views import MyModelViewSet
# from django.urls import path

# mymodels_viewset = MyModelViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
# mymodel_detail_view = MyModelViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })

# urlpatterns = [
#     path('mymodels/', mymodels_viewset, name='mymodels-list'),
#     path('mymodels/<int:pk>', mymodel_detail_view, name="mymodels-detail"),
# ]
