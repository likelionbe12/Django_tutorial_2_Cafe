from django.urls import path
from . import views
app_name="manager"
urlpatterns = [    
    path('', views.index_view, name='manager_home'),
    path('menu_list_url/', views.menu_list, name="menu_list_page"),
    path('menu_add_url/',views.menu_add, name="menu_add_page"), # 메뉴 추가 페이지
    path('add_menu_data/', views.add_menu_data, name='add_menu_data')
]