from django.urls import path
from rest_framework_swagger import views as swagger_views
from rest_framework_jwt import views as jwt_views
from . import views

urlpatterns = [
    path('docs/', swagger_views.get_swagger_view(title='API Docs')),
    path('token-auth/', jwt_views.obtain_jwt_token),
    path('posts/', views.post_list),
    path('posts/<int:post_id>/comments/', views.comment_create),
    path('posts/<int:post_id>/comments/<int:comment_id>/', views.comment_delete),
]
