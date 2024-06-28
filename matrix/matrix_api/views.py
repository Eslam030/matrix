from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from django.conf import settings
from django.http import JsonResponse
from PIL import Image


class user_handler (View):
    def get(self, request):
        email = request.GET.get('email')
        operation = request.GET.get('operation')
        if email:
            obj = user.objects.filter(email=email).first()
            if obj == None:
                return JsonResponse({'error': 'Email not found'})
            if (operation == 'scan_qr'):
                if obj.scanned == False:
                    obj.scanned = True
                    obj.save()
                    return JsonResponse({'success': 'QR scanned successfully'})
                else:
                    return JsonResponse({'error': 'QR already scanned'})
        else:
            return JsonResponse({'error': 'Email not Provided'})


# the upcoming post method is used to add a new records to the database
@method_decorator(csrf_exempt, name='dispatch')
class USER (View):
    def post(self, request):
        email = request.POST.get('email')
        obj = user.objects.filter(email=email).first()
        if obj == None:
            obj = user(email=email)
            obj.save()
            return HttpResponse('User added successfully')
        else:
            return HttpResponse('User already exists')


@method_decorator(csrf_exempt, name='dispatch')
class SPONSORS (View):
    def post(self, request):
        name = request.POST.get('name')
        ProfileLink = request.POST.get('ProfileLink')
        Bio = request.POST.get('Bio')
        Image = request.FILES.get('Image')
        obj = sponsors.objects.filter(name=name).first()
        if obj == None:
            obj = sponsors(
                name=name, ProfileLink=ProfileLink, Bio=Bio, Image=Image)
            obj.save()
            return HttpResponse('Sponsor added successfully')
        else:
            return HttpResponse('Sponsor already exists')


@method_decorator(csrf_exempt, name='dispatch')
class COMMUNITIES_PARTNERS (View):
    def post(self, request):
        name = request.POST.get('name')
        ProfileLink = request.POST.get('ProfileLink')
        Bio = request.POST.get('Bio')
        Image = request.FILES.get('Image')
        obj = Communities_Partners.objects.filter(name=name).first()
        if obj == None:
            obj = Communities_Partners(
                name=name, ProfileLink=ProfileLink, Bio=Bio, Image=Image)
            obj.save()
            return HttpResponse('Community Partner added successfully')
        else:
            return HttpResponse('Community Partner already exists')


@method_decorator(csrf_exempt, name='dispatch')
class PARTNERS(View):
    def post(self, request):
        name = request.POST.get('name')
        ProfileLink = request.POST.get('ProfileLink')
        Bio = request.POST.get('Bio')
        Image = request.FILES.get('Image')
        obj = Partners.objects.filter(name=name).first()
        if obj == None:
            obj = Partners(
                name=name, ProfileLink=ProfileLink, Bio=Bio, Image=Image)
            obj.save()
            return HttpResponse('Partner added successfully')
        else:
            return HttpResponse('Partner already exists')


@method_decorator(csrf_exempt, name='dispatch')
class VIPS(View):
    def post(self, request):
        name = request.POST.get('name')
        ProfileLink = request.POST.get('ProfileLink')
        Bio = request.POST.get('Bio')
        Position = request.POST.get('Position')
        Image = request.FILES.get('Image')
        obj = Vips.objects.filter(name=name).first()
        if obj == None:
            obj = Vips(name=name, ProfileLink=ProfileLink,
                       Bio=Bio, Image=Image, Position=Position)
            obj.save()
            return HttpResponse('VIP added successfully')
        else:
            return HttpResponse('VIP already exists')


@method_decorator(csrf_exempt, name='dispatch')
class MENTORS (View):
    def post(self, request):
        name = request.POST.get('name')
        ProfileLink = request.POST.get('ProfileLink')
        Bio = request.POST.get('Bio')
        Image = request.FILES.get('Image')
        position = request.POST.get('position')
        Track = request.POST.get('Track')
        obj = Mentors.objects.filter(name=name).first()
        if obj == None:
            obj = Mentors(
                name=name, ProfileLink=ProfileLink, Bio=Bio, Image=Image, position=position, Track=Track)
            obj.save()
            return HttpResponse('Mentor added successfully')
        else:
            return HttpResponse('Mentor already exists')


@method_decorator(csrf_exempt, name='dispatch')
class SPEAKERS (View):
    def post(self, request):
        name = request.POST.get('name')
        Track = request.POST.get('Track')
        Type_of_Speaker = request.POST.get('Type_of_Speaker')
        Session_Title = request.POST.get('Session_Title')
        position = request.POST.get('position')
        ProfileLink = request.POST.get('ProfileLink')
        Bio = request.POST.get('Bio')
        Image = request.FILES.get('Image')
        Day = request.POST.get('Day')
        Time = request.POST.get('Time')
        Stage = request.POST.get('Stage')
        obj = Speaker.objects.filter(name=name).first()
        if obj == None:
            obj = Speaker(name=name, Track=Track, Type_of_Speaker=Type_of_Speaker, Session_Title=Session_Title,
                          position=position, ProfileLink=ProfileLink, Bio=Bio, Image=Image, Day=Day, Time=Time, Stage=Stage)
            obj.save()
            return HttpResponse('Speaker added successfully')
        else:
            return HttpResponse('Speaker already exists')


class HOST_AND_MAIN_COMMUNITIES (View):
    def post(self, request):
        name = request.POST.get('name')
        ProfileLink = request.POST.get('ProfileLink')
        community_type = request.POST.get('community_type')
        Image = request.FILES.get('Image')
        obj = Host_and_main_communities.objects.filter(name=name).first()
        if obj == None:
            obj = Host_and_main_communities(name=name, ProfileLink=ProfileLink,
                                            community_type=community_type, Image=Image)
            obj.save()
            return HttpResponse('Host and main community added successfully')
        else:
            return HttpResponse('Host and main community already exists')
# in the post we can erase csrf token


@ method_decorator(csrf_exempt, name='dispatch')
class image_handler (View):
    def get(self, request):
        path = request.GET.get('path')
        if path:
            total_dir = settings.BASE_DIR / path
            with open(total_dir, 'rb') as f:
                return HttpResponse(f.read(), content_type='image/jpeg')
        else:
            return JsonResponse({'error': 'Path not found'})

    def post(self, request):
        name = request.POST.get('name')
        model = request.POST.get('model')
        image = request.FILES.get('image')
        print(name, model, image)
        obj = None
        if model == 'sponsors':
            obj = sponsors.objects.filter(name=name).first()
        if obj != None:
            obj.Image = image
            obj.save()
            return HttpResponse('Image uploaded successfully')
        else:
            return HttpResponse('Email not found')
