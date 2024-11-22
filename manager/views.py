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
    menu_name_from_form = request.POST['menu_name'] # 받아온 메뉴이름 변수에 담기
    if menu_name_from_form.strip()=='': # 제대로 된 값이 맞는지 검증해서 처리
        context = {"message":"메뉴 이름을 넣으셔야 됩니다."}
        return render(request, 'manager/menu_add_page.html', context)
    menu_price_from_form = request.POST['menu_price'] # 받아온 메뉴가격 변수에 담기
    # Menu 테이블에 가져온 값 저장하기
    Menu.objects.create(menu_name=menu_name_from_form, menu_price=menu_price_from_form)
    print(f"메뉴이름 : {menu_name_from_form}, 가격 : {menu_price_from_form} 이 추가되었습니다. ") # log 추가
    
    return render(request, 'manager/menu_add_page.html') # 이후 단계 페이지 설정

   
def menu_detail(request, menu_id):
    # print("menu_id : ",menu_id)
    menu = Menu.objects.get(pk=menu_id)
    context = {
       "menu_to_page" : menu
    }
    return render(request, 'manager/menu_detail.html', context)

def add_option(request, menu_id):
    menu = Menu.objects.get(pk=menu_id)
    context = {"menu":menu}
    return render(request, 'manager/add_option.html', context)

def add_option_data(request):
    menu_id_from_form = request.POST['menu_id']
    option_name_from_form = request.POST['option_name']
    option_price_from_form = request.POST['option_price']
    # DB Opion Table에 저장
    menu = Menu.objects.get(pk=menu_id_from_form)
    Option.objects.create(menu=menu, option_name=option_name_from_form, option_price=option_price_from_form)
    context = {"menu":menu}
    return render(request, 'manager/add_option.html', context) # option 추가 화면 보여주기