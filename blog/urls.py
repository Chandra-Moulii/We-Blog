from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Landingpage"),
    path('Signup/', views.Signup, name="Signup" ),
    path('Login/', views.Login, name="Login" ),
    path('Logout/', views.Logout, name="Logout" ),
    path('Bloghome/', views.Bloghome, name="Bloghome" ),
    path('Myarticles/', views.Myarticles, name="Myarticles" ),
    path('Createpost/', views.Createpost, name="Createpost" ),
    path('Updatepost/<int:Author_id>', views.Updatepost, name="Updatepost" ),
    path('Deleteall/', views.Deleteall, name="Deleteall" ),
    path('Delete/<int:Article_id>', views.Delete, name="Deletepost" ),
    path('Profile/', views.Profile, name="Profile" ),
    path('Search/', views.Search, name="Search" ),
    path('Sort/', views.Sort, name="Sort" ),
    path('Sortmine/', views.Sortmine, name="Sortmine" ),
    path('Removepeofilepic/', views.Removeprofilepic, name="Removepicture" ),
    path('Detail/<int:Article_id>', views.detail, name="Detail" ),
    path('Updateprofile/', views.Updateprofile, name="Updateprofile" ),
    path('Authorpage/<int:Article_id>', views.Authorpage, name="Authorpage" ),
]
