from django.urls import path
from . import views

urlpatterns = [
    # 메인 페이지를 upload_file 뷰로 설정
    path('', views.upload_file, name='home'),  
    path('about/', views.about, name='about'),
    path('api/', views.api, name='api'),
    path('upload/', views.upload_file, name='upload_file'),
    path('success/', views.upload_success, name='upload_success'),
    path('contactus/', views.contact_us, name='contact_us'),

]