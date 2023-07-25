from django.urls import path
from.import views

urlpatterns = [
    path('', views.country),
    path('India/', views.India),
    path('Australia/', views.Australia),
    path('America/', views.America),

    path('India/Gujarat/', views.Gujarat),
    path('India/Maharashtra/', views.Maharashtra),
    path('India/Karnataka/', views.Karnataka),

    path('Australia/newsouthwales/', views.newsouthwales),
    path('Australia/Queensland/', views.Queensland),
    path('Australia/SouthAustralia/', views.SouthAustralia),
    path('Australia/Tsamnia', views.Tsamnia),

]