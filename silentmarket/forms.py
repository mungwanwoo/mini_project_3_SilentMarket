from django import forms
from .models import User, Address, Category, Product, ProductImg

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password','name', 'phone_number']  # 필요한 필드만 추가
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '아이디를 입력하세요'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '비밀번호를 입력하세요'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '이름을 입력하세요'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '전화번호 (선택)'
            }),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['sido', 'sigungu', 'eup_myeon_dong', 'detail_address']
        widgets = {
            'sido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '시도'
            }),
            'sigungu': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '시군구'
            }),
            'eup_myeon_dong': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '읍면동'
            }),
            'detail_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '상세주소'
            }),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '카테고리명을 입력하세요'
            })
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'content', 'price', 'status', 'shipping_included', 'shipping_cost']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '상품명을 입력하세요'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': '상품 설명을 입력하세요'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '상품 가격을 입력하세요'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'shipping_included': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'shipping_cost': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '배송비를 입력하세요'
            }),
        }


class ProductImgForm(forms.ModelForm):
    class Meta:
        model = ProductImg
        fields = ['url']

        widgets = {
            'url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '이미지주소를 입력하세요'
            })
        }
