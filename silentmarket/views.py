from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, AddressForm, CategoryForm, ProductForm, ProductImgForm
from .models import Category, Product, ProductImg, Address, User


# 메인 페이지
def index(request):
    category_list = Category.objects.all()
    products = Product.objects.all()
    user_id = request.session.get('user_id')  
    user = None
    if user_id:
        try:
            user = User.objects.get(id=user_id)  
        except User.DoesNotExist:
            pass
    context = {'category_list': category_list, 'products': products, 'user': user}
    return render(request, 'silentmarket/index.html', context)

# 회원가입
def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        address_form = AddressForm(request.POST)

        if user_form.is_valid() and address_form.is_valid():
            user = user_form.save()
            
            address = address_form.save(commit=False)
            address.user = user
            address.save()

            # 로그인 처리
            request.session['user_id'] = user.id
            return redirect('silentmarket:index')
    else:
        user_form = UserForm()
        address_form = AddressForm()

    return render(request, 'silentmarket/signup.html', {
        'user_form': user_form,
        'address_form': address_form
    })

# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if user.password==password:
                request.session['user_id'] = user.id
                return redirect('silentmarket:index')
            else:
                error_message = "아이디나 비밀번호가 잘못되었습니다."
                return render(request, 'silentmarket/login.html', {'error_message': error_message})
        except User.DoesNotExist:
            error_message = "아이디가 존재하지 않습니다."
            return render(request, 'silentmarket/login.html', {'error_message': error_message})

    return render(request, 'silentmarket/login.html')

# 로그아웃
def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('silentmarket:index')

# 카테고리 추가
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('silentmarket:index')
    else:
        form = CategoryForm()
    return render(request, 'silentmarket/add_category.html', {'form': form})
    

# 상품 등록
def add_product(request):
    user_id = request.session.get('user_id')
    
    if user_id:
        user = User.objects.get(id=user_id)

        if request.method == 'POST':
            # 상품 등록 처리
            product_form = ProductForm(request.POST)
            if product_form.is_valid():
                product = product_form.save(commit=False)
                product.user = user 
                product.save()

                # 이미지 등록 처리
                img_form = ProductImgForm(request.POST)
                if img_form.is_valid():
                    product_img = img_form.save(commit=False)
                    product_img.product = product
                    product_img.save()

                return redirect('silentmarket:product_detail', product_id=product.id)
        else:
            product_form = ProductForm()
            img_form = ProductImgForm()

        return render(request, 'silentmarket/add_product.html', {'form': product_form, 'img_form': img_form})
    
    return redirect('silentmarket:login')

# 상품 상세 페이지
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    product_imgs = ProductImg.objects.filter(product=product)
    user_id = request.session.get('user_id')
    user = None
    if user_id:
        try:
            user = User.objects.get(id=user_id)  
        except User.DoesNotExist:
            pass
    context = {
        'product': product,
        'product_imgs': product_imgs,
        'user': user
    }
    return render(request, 'silentmarket/product_detail.html', context)

def category_product_list(request, category_id):
    # category_id인 카테고리에 속한 포스트들의 리스트를 보여주기
    category = get_object_or_404(Category, id=category_id)
    category_list = Category.objects.all()

    products = Product.objects.filter(category=category)
    
    context = {
        'products':products,
        'category':category,
        'category_list':category_list
    }
    return render(request, 'silentmarket/index.html', context)
