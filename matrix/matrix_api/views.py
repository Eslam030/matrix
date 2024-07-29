from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from django.conf import settings
from django.http import JsonResponse
from PIL import Image
from django.urls import reverse
from django.shortcuts import redirect
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from io import BytesIO
import os
import requests
import validators


class user_scanner (View):
    def get(self, request):
        email = request.GET.get('email')
        if email:
            obj = user.objects.filter(email=email).first()
            if obj == None:
                return JsonResponse({'error': 'Email not found'})
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

    def get(self, request):
        email = request.GET.get('email')
        if email:
            obj = user.objects.filter(email=email).first()
            if obj == None:
                return JsonResponse({'error': 'Email not found'})
            else:
                return JsonResponse({'success': 'Found'})
        else:
            return JsonResponse({'error': 'Email not Provided'})

# for the next we will get all the data


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

    def get(self, request):
        sponsor = sponsors.objects.all().values()
        return JsonResponse(list(sponsor), safe=False)


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

    def get(self, request):
        community_partner = Communities_Partners.objects.all().values()
        return JsonResponse(list(community_partner), safe=False)


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

    def get(self, request):
        partner = Partners.objects.all().values()
        return JsonResponse(list(partner), safe=False)


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

    def get(self, request):
        vip = Vips.objects.all().values()
        return JsonResponse(list(vip), safe=False)


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

    def get(self, request):
        mentor = Mentors.objects.all().values()
        return JsonResponse(list(mentor), safe=False)


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

    def get(self, request):
        speaker = Speaker.objects.all().values()
        # make some transformation on the date
        return JsonResponse(list(speaker), safe=False)


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

    def get(self, request):
        host_and_main_community = Host_and_main_communities.objects.all().values()
        return JsonResponse(list(host_and_main_community), safe=False)


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
        obj = None
        if model == 'sponsors':
            obj = sponsors.objects.filter(name=name).first()
        if obj != None:
            obj.Image = image
            obj.save()
            return HttpResponse('Image uploaded successfully')
        else:
            return HttpResponse('Email not found')


class Data (View):
    SHEET_ID = "1dBPUuzZy6cRKYqsdlMYxILs3ryrYLgzePcoE85j4UcM"
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    RANGE = "Sponsors!F3:F3"

    speaker_types = {
        'Talks': Speaker.Speaker_Types.Talks,
        'Panels': Speaker.Speaker_Types.Panels,
        'Career Circles': Speaker.Speaker_Types.Career_Circles,
        'Mentorships': Speaker.Speaker_Types.Mentorship,
        'Workshops': Speaker.Speaker_Types.Workshops,
        '': None
    }

    stages = {
        'Primary': Speaker.stages.Primary,
        'Secondary': Speaker.stages.Secondary,
        'Workshop': Speaker.stages.Workshop,
        'Mentorship': Speaker.stages.Mentorship,
        'Career Circles': Speaker.stages.Career_Circles,
        '': None
    }

    days = {
        'Day 1 , July 31': Speaker.Days.Day1,
        'Day 2 , August 1': Speaker.Days.Day2,
        'Day 3 , August 2': Speaker.Days.Day3,
        '': None
    }

    community_type = {
        'Host': Host_and_main_communities.Types.Host,
        'Main': Host_and_main_communities.Types.Main_Community,
        '': None
    }

    def check_link(self, link):
        if validators.url(link):
            return link
        return ''

    def handle_row(self, row, size):
        while len(row) < size:
            row.append('')
        return row

    def handle_row_data(self, row):
        for i in range(len(row)):
            row[i] = row[i].strip()
        return row

    def handle_image(self, col, path, name):
        if col == '':
            return ''
        response = requests.get(col)
        try:
            img = Image.open(BytesIO(response.content))
            # save the image by the type of the image and the name of the image
            # the type is dynamic by the fetched data
            ty = img.format
            if not os.path.exists(settings.BASE_DIR / 'matrix_api' / path / f'{name}.{img.format}'):
                os.makedirs(os.path.dirname(settings.BASE_DIR /
                            'matrix_api' / path / f'{name}.{img.format}'), exist_ok=True)
            img.save(settings.BASE_DIR / 'matrix_api' /
                     path / f'{name}.{img.format}')
            return str(settings.BASE_DIR / 'matrix_api' / path / f'{name}.{img.format}')
        except Exception as e:
            return None

    def sheetHandler(self, sheet_name, row):
        row = self.handle_row_data(row)
        if sheet_name == "Sponsors":
            row = self.handle_row(row, 4)
            row[1] = self.check_link(row[1])
            row[2] = self.check_link(row[2])
            obj = sponsors.objects.filter(name=row[0]).first()
            if obj == None:
                row[1] = self.check_link(row[1])
                obj = sponsors(
                    name=row[0], ProfileLink=row[2], Bio=row[3], Image=self.handle_image(row[1], 'sponsor_images', row[0]))
                obj.save()
            else:
                obj.name = row[0]
                obj.ProfileLink = row[2]
                obj.Bio = row[3]
                obj.Image = self.handle_image(row[1], 'sponsor_images', row[0])
                obj.save()

        if sheet_name == "Communities Partners":
            # Communities_Partners_images
            row = self.handle_row(row, 4)
            obj = Communities_Partners.objects.filter(name=row[0]).first()
            row[1] = self.check_link(row[1])
            row[2] = self.check_link(row[2])
            if obj == None:
                obj = Communities_Partners(
                    name=row[0], ProfileLink=row[2], Bio=row[3], Image=self.handle_image(row[1], 'Communities_Partners_images', row[0]))
                obj.save()
            else:
                obj.name = row[0]
                obj.ProfileLink = row[2]
                obj.Bio = row[3]
                obj.Image = self.handle_image(
                    row[1], 'Communities_Partners_images', row[0])
                obj.save()
        if sheet_name == "Partners":
            # Partners_images
            row = self.handle_row(row, 4)
            obj = Partners.objects.filter(name=row[0]).first()
            row[1] = self.check_link(row[1])
            row[2] = self.check_link(row[2])
            if obj == None:
                obj = Partners(
                    name=row[0], ProfileLink=row[2], Bio=row[3], Image=self.handle_image(row[1], 'Partners_images', row[0]))
                obj.save()
            else:
                obj.name = row[0]
                obj.ProfileLink = row[2]
                obj.Bio = row[3]
                obj.Image = self.handle_image(
                    row[1], 'Partners_images', row[0])
                obj.save()

        if sheet_name == "Vips":
            # Vips_images
            row = self.handle_row(row, 5)
            obj = Vips.objects.filter(name=row[0]).first()
            row[1] = self.check_link(row[1])
            row[3] = self.check_link(row[3])
            if obj == None:
                obj = Vips(name=row[0], ProfileLink=row[3],
                           Bio=row[4], Image=self.handle_image(row[1], 'Vips_images', row[0]), position=row[2])
                obj.save()
            else:
                obj.name = row[0]
                obj.ProfileLink = row[3]
                obj.Bio = row[4]
                obj.Image = self.handle_image(row[1], 'Vips_images', row[0])
                obj.Position = row[2]
                obj.save()

        if sheet_name == "Mentors":
            # Mentors_images
            row = self.handle_row(row, 6)
            obj = Mentors.objects.filter(name=row[0]).first()
            row[1] = self.check_link(row[1])
            row[3] = self.check_link(row[3])
            if obj == None:
                obj = Mentors(name=row[0], ProfileLink=row[3],
                              Bio=row[5], Image=self.handle_image(row[1], 'Mentors_images', row[0]), position=row[2], Track=row[4])
                obj.save()
            else:
                obj.name = row[0]
                obj.ProfileLink = row[3]
                obj.Bio = row[5]
                obj.Image = self.handle_image(row[1], 'Mentors_images', row[0])
                obj.position = row[2]
                obj.Track = row[4]
                obj.save()
        if sheet_name == "Speakers":
            # Speaker_images
            row = self.handle_row(row, 11)
            obj = Speaker.objects.filter(name=row[0]).first()
            row[6] = self.check_link(row[6])
            row[7] = self.check_link(row[7])
            if row[9] == '':
                row[9] = None
            if obj == None:
                obj = Speaker(name=row[0], Track=row[1], Type_of_Speaker=self.speaker_types[row[2]], Session_Title=row[3], position=row[4], ProfileLink=row[7],
                              Bio=row[5], Image=self.handle_image(row[6], 'Speaker_images', row[0]), Day=self.days[row[8]], Time=row[9], Stage=self.stages[row[10]])
                obj.save()
            else:
                if row[9] == '':
                    row[9] = None
                obj.name = row[0]
                obj.Track = row[1]
                obj.Type_of_Speaker = self.speaker_types[row[2]]
                obj.Session_Title = row[3]
                obj.position = row[4]
                obj.ProfileLink = row[7]
                obj.Bio = row[5]
                obj.Image = self.handle_image(row[6], 'Speaker_images', row[0])
                obj.Day = self.days[row[8]]
                obj.Time = row[9]
                obj.Stage = self.stages[row[10]]
                print(obj.Time)
                print(obj)
                obj.save()

        if sheet_name == "Emails":
            row = self.handle_row(row, 1)
            obj = user.objects.filter(email=row[0]).first()
            if obj == None:
                obj = user(email=row[0])
                obj.save()

        if sheet_name == "Host & Main Communities ":
            row = self.handle_row(row, 4)
            if row[0] == "":
                return

            obj = Host_and_main_communities.objects.filter(name=row[0]).first()
            if obj == None:
                img = None
                row[3] = self.check_link(row[3])
                obj = Host_and_main_communities(
                    name=row[0], ProfileLink=self.check_link(row[2]), community_type=self.community_type[row[1]], Image=self.handle_image(row[3], 'Host_and_main_communities_images', row[0]))
                obj.save()
            else:
                # delete the old image
                if obj.Image != '':
                    os.remove(settings.BASE_DIR / obj.Image.path)
                obj.Image.delete()
                obj.name = row[0]
                obj.ProfileLink = self.check_link(row[2])
                obj.community_type = self.community_type[row[1]]
                row[3] = self.check_link(row[3])
                obj.Image = self.handle_image(
                    row[3], 'Host_and_main_communities_images', row[0])
                obj.save()

    def read_sheet(self, sheet_id, range_name, creds):
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=sheet_id, range=range_name)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print(f"No data found. in {range_name.split("!")[0]}")
            return
        data = []
        for row in values:
            self.sheetHandler(range_name.split("!")[0], row)

    def post(self, request):
        creds = None
        if os.path.exists(settings.BASE_DIR / "matrix_api/token.json"):
            creds = Credentials.from_authorized_user_file(
                settings.BASE_DIR / "matrix_api/token.json", self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    settings.BASE_DIR / 'matrix_api/credentials.json', self.SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(settings.BASE_DIR / "matrix_api/token.json", "w") as token:
                token.write(creds.to_json())

        sheets = ['Sponsors', 'Communities Partners', 'Partners', 'Vips', 'Mentors', 'Speakers', 'Emails',
                  'Host & Main Communities ']

        sheets = ['Speakers']
        response = {
            'errors': []
        }
        for sheet in sheets:
            if sheet == 'Emails':
                self.RANGE_NAME = f"{sheet}!A3:A"
            else:
                self.RANGE_NAME = f"{sheet}!A2:K"
            try:
                self.read_sheet(
                    self.SHEET_ID, self.RANGE_NAME, creds)
            except Exception as ex:
                response['errors'].append(str(ex))
        if response['errors'] == []:
            response['success'] = 'Data added successfully'
        print(response)
        return JsonResponse(response, safe=False)
