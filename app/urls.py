from django.urls import path

from app.views import day_task

# from app.views import dushanba,seshanba,chorshanba,payshanba,juma,shanba,yakshanba

# urlpatterns = [
#     path('dushanba/',dushanba),
#     path('seshanba/',seshanba),
#     path('chorshanba/',chorshanba),
#     path('payshanba/',payshanba),
#     path('juma/',juma),
#     path('shanba/',shanba),
#     path('yakshanba/',yakshanba),
# ]

urlpatterns = [
     path('<str:week_day>/',day_task)
]