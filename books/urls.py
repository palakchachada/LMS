from django.urls import path,include
from .views import *

urlpatterns = [
    path("",home, name="home"),
    path("login/",login_page, name="login"),
    path("profile/",profile, name='profile'),
    path("register/",register, name="register"),
    path("add_books/",add_books, name="add_books"),
    path("edit_book/<slug:isbn>/",edit_book,name='edit_book'),
    path("delete_book/<slug:isbn>/",delete_book, name='delete_book'),
    path("book_details/",book_details,name="book_details"),
    path("logout/",logout_page,name="logout"),

]