from django.urls import path, include, re_path
from rest_framework import routers

from .views import (
    CreateUserView, CreateTokenView, ManageUserView, UserViewSet, 
    ChangePasswordView,UserImageUpdateView,DepartmentViewset,AssetTypeViewset,AssetViewset,
    OfficetViewset,AssetHistoryViewset
    # AttachmentViewSet, ImageUpdateView, 
    )


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('offices', OfficetViewset)
router.register('departments', DepartmentViewset)
router.register('categories', AssetTypeViewset)
router.register('assets', AssetViewset)
router.register('history', AssetHistoryViewset)


urlpatterns = [
    path('', include(router.urls)),
    #path('upload/', FileList.as_view()),
    path('user/create/', CreateUserView.as_view(), name='create'),
    path('user/token/', CreateTokenView.as_view(), name='token'),
    path('user/me/', ManageUserView.as_view(), name='me'),
    path('user/change-password/', ChangePasswordView.as_view(), name='password-change'),
    path("users/<int:id>/image/", UserImageUpdateView.as_view(), name="user-image-update"),
]