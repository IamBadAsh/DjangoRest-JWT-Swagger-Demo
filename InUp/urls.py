from django.urls import path
from .views.DeleteUser import DeleteUserApiview
from .views.UpdateUser import UpdateUserApiview

urlpatterns = [
    path('deleteUser/<int:pk>', DeleteUserApiview),
    path('updateUser/<int:pk>', UpdateUserApiview),
]