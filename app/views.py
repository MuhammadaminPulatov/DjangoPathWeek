from django.http import HttpResponse

from app.models import Task


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


def day_task(request, week_day):
    daily_task = Task.objects.get(day=week_day)
    return HttpResponse(f"{daily_task.task}")