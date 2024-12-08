# django import

from django.urls import path
from . import views

urlpatterns = [
    # path('search/<int:sim_id>/<int:category_id>/', views.NumberSearchView.as_view(), name='numbers_search'),
    path('ucell/', views.ucell_page, name='ucell'),
    path('beeline/', views.beeline_page, name='beeline'),
    path('uztelecom/', views.uzmobile_page, name='uztelecom'),
    path('humans/', views.humans_page, name='humans'),

    path('ucell_sim/', views.UcellSearchView.as_view(), name='ucell_search'),
    path('beeline_sim/', views.BelineSearchView.as_view(), name='beeline_search'),
    path('uzmobile_sim/', views.uztelecomSearchView.as_view(), name='uztelecom_search'),
    path('humans_sim/', views.humansSearchView.as_view(), name='humans_search'),

    # number detail
    path('number_detail/<str:number>/', views.NumberDetailView.as_view(), name='search_number_detail'),
]
