from django.db import models
from django.contrib.auth.models import AbstractUser

# 유저 테이블
class User(AbstractUser):
    #전화번호
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    name=models.CharField(max_length=5)
    def __str__(self):
        return self.username

# 주소 테이블 
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    #특별시,도
    sido = models.CharField(max_length=100, verbose_name="시도")
    # 시 군 구
    sigungu = models.CharField(max_length=100, verbose_name="시군구")
    # 읍 명 동
    eup_myeon_dong = models.CharField(max_length=100, verbose_name="읍면동")
    #상세 주소
    detail_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="상세주소")
    #주소 등록일
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일")
    
    def __str__(self):
        return f"{self.sido} {self.sigungu} {self.eup_myeon_dong} {self.street_address}"

    class Meta:
        verbose_name = "주소"
        verbose_name_plural = "주소 목록"
        ordering = ["sido", "sigungu", "eup_myeon_dong"]

# 카테고리 테이블
class Category(models.Model):
    # 카테고리 제목
    name = models.CharField(max_length=100, unique=True, verbose_name='카테고리')
    # 카테고리 생성일
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = '카테고리 목록'
        ordering = ['name']

# 상품 테이블
class Product(models.Model):
    # 유저
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 상품명
    title = models.CharField(max_length=255,verbose_name='상품명')
    # 상품설명
    content = models.TextField(verbose_name='상품설명')
    # 상품 가격
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='상품 가격')
    # 상품 카테고리
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    # 상품 등록일
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='등록일')
    # 업데이트날짜
    update_at = models.DateTimeField(auto_now=True,verbose_name='업데이트날짜')
    # 판매상태
    status = models.CharField(max_length=50,choices=[('판매 중', '판매 중'), ('판매완료', '판매완료')],verbose_name='판매상태')
    # 배송비 포함 여부
    shipping_included = models.BooleanField(default=False,verbose_name='배송비 포함 여부')
    # 배송비
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=0, default=3500,verbose_name='배송비')

    def __str__(self):
        return self.title

    def get_final_price(self):
        if self.shipping_included:
            return self.price
        return self.price + self.shipping_cost

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '상품 목록'
        ordering = ['-create_at']
        indexes = [
            models.Index(fields=['-create_at'])
        ]

# 상품 이미지 테이블
class ProductImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.TextField(verbose_name='이미지주소')

    def __str__(self):
        return f"img for {self.product.title}"

# 결제 테이블
class Payment(models.Model):
    #구매자
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='구매자')  
    # 구매한 상품
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    # 판매자
    seller = models.ForeignKey(User, related_name='sold_products', on_delete=models.CASCADE)  
    # 결제 금액
    amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='결제 금액')  
    # 결제 일시
    payment_date = models.DateTimeField(auto_now_add=True,verbose_name='결제 일시')  
    # 결제 상태
    status = models.CharField(max_length=50, choices=[('결재 대기중', '결재 대기중'), ('결재완료', '결재완료')], default='결재 대기중',verbose_name='결제 상태') 


    def __str__(self):
        return f"Payment of {self.amount} by {self.user.username} for {self.product.title}"

    class Meta:
        verbose_name = '결제'
        verbose_name_plural = '결제 내역'
        ordering = ['-payment_date']
