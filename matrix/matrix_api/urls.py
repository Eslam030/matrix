from django.urls import path
from .views import *

app_name = 'matrix_api'

urlpatterns = [
    path('scanUser/', user_scanner.as_view(), name='user'),
    path('image/', image_handler.as_view(), name='image'),
    path('user/', USER.as_view(), name='user'),
    path('sponsors/', SPONSORS.as_view(), name='sponsors'),
    path('communities_partners/', COMMUNITIES_PARTNERS.as_view(),
         name='communities_partners'),
    path('partners/', PARTNERS.as_view(), name='partners'),
    path('vips/', VIPS.as_view(), name='vips'),
    path('mentors', MENTORS.as_view(), name='mentors'),
    path('speakers', SPEAKERS.as_view(), name='speakers'),
    path('host_and_main_communities', HOST_AND_MAIN_COMMUNITIES.as_view(),
         name='host_and_main_communities'),
    path('load_data', Data.as_view(), name='load_data'),

]
