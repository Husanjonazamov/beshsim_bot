from django.urls import path
from . import views

urlpatterns = [
    # kampayniyalar ro'yhati
    path('', views.sim_list, name='sims'),
    # tariflar ro'yhati
    path('<int:sim_id>/', views.category_list, name='categories'),
    # kampaniya bo'yicha tariflarni chiqarish
    path('<int:sim_id>/category/<int:category_id>/', views.number_list, name='numbers'),
    # foydalanuvchi o'zi yoqgan raqamni qidirish uchun 
    path('<int:sim_id>/category/<int:category_id>/search/', views.search_numbers, name='search_numbers'),
    # ortga qaytish uchun 
    path('<int:sim_id>/previous-page/', views.previous_page, name='previous_page'),  # sim_id argumentini qo'shildi
    # foydalanuvchi o'ziga yoqgan raqam haqida malumot olish
    path('number/<int:number_id>/', views.number_detail, name='number_detail'),
    path('add-numbers/', views.add_number, name='add-numbers'),
   
]


