from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('store/new', views.new_book, name='new_book'),
    path('store/<int:book_id>', views.book_details, name='book_details'),
    path('store/<int:book_id>/edit', views.edit_book, name='edit_book'),
    path('store/<int:book_id>/delete', views.delete_book, name='delete_book'),
]
