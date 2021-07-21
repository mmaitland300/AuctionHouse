from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("inactive", views.closed_listings, name="inactive"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("close/<int:listing_id>", views.close, name="close"),
    path("add_item/<int:listing_id>", views.add_item, name="add_item"),
    path("remove_item/<int:listing_id>", views.remove_item, name="remove_item"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("listing/<str:category>", views.category_listings, name="category_listings")

]
