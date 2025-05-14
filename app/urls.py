from django.urls import path

from app.views import week


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
    path('<str:week_name>/',week)
]