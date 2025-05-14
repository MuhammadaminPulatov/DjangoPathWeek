from django.http import HttpResponse

# def dushanba(request):
#     return HttpResponse('Dushanba')
# def seshanba(request):
#     return HttpResponse('Seshanba')
# def chorshanba(request):
#     return HttpResponse('Chorshanba')
# def payshanba(request):
#     return HttpResponse('Payshanba')
# def juma(request):
#     return HttpResponse('Juma')
# def shanba(request):
#     return HttpResponse('Shanba')
# def yakshanba(request):
#     return HttpResponse('Yakshanba')


def week(request, week_name):
    return HttpResponse(week_name)