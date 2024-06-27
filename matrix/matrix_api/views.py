from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import user


class user_handler (View):
    def get(self, request):
        email = request.GET.get('email')
        if email:
            user_obj = user.objects.filter(email=email).first()
            if user_obj != None:
                if user_obj.scanned == False:
                    user_obj.scanned = True
                    user_obj.save()
                    return HttpResponse('QR is scanned successfully')
                else:
                    return HttpResponse('QR is already scanned')
            else:
                return HttpResponse('Email not found')
    # Create your views here.
