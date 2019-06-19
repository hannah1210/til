from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('',views.index, name="index"),
    path('new/',views.new, name='new'),
    path('<int:board_pk>/',views.detail, name='detail'),
    path('<int:board_pk>/edit/',views.edit, name='edit'),
    path('<int:board_pk>/delete/',views.delete, name='delete'),
    path('<int:board_pk>/comments/',views.comment_create, name='comments'),
    path('<int:board_pk>/<int:comment_pk>/edit/',views.comment_edit, name='comments_edit'),
    path('<int:board_pk>/<int:comment_pk>/delete/',views.comment_delete, name='comments_delete')
]