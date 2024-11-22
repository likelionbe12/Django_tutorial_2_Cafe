from django.shortcuts import render
from .models import Menu, Option
# Create your views here.
def index_view(request):
    return render(request, 'manager/index.html')

def menu_list(request): # Menu Table을 조회해서 메뉴 리스트를 전달해주겠습니다.
    menus = Menu.objects.all()
    context = {
        "menus_to_page" :menus,
        "cafe_name":"사나리아"
    }
    return render(request, 'manager/menu_list_page.html',context)

def menu_add(request):
    return render(request, 'manager/menu_add_page.html')

def add_menu_data(request):
    menu_name_from_form = request.POST['menu_name']
    menu_price_from_form = request.POST['menu_price']
    # if menu_name_from_form: & menu_price_from_form>0:
    Menu.objects.create(menu_name=menu_name_from_form, menu_price=menu_price_from_form)
    print(f"메뉴이름 : {menu_name_from_form}, 가격 : {menu_price_from_form} 이 추가되었습니다. ")
    
    return render(request, 'manager/menu_add_page.html')






