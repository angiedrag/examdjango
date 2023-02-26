from django.urls import path
from examdjango.myplant_app.views import home_page, create_profile_page, edit_profile_page, delete_profile_page, \
    profile_details_page, catalogue_page, create_plant_page, edit_plant_page, delete_plant_page, plant_details_page


urlpatterns = [
    path('', home_page, name='home-page'),
    path('create/', create_profile_page, name='create-profile-page'),
    path('edit/', edit_profile_page, name='edit-profile-page'),
    path('delete/', delete_profile_page, name='delete-profile-page'),
    path('details/', profile_details_page, name='profile-details-page'),
    path('catalogue/', catalogue_page, name='catalogue'),
    path('create/', create_plant_page, name='create-plant-page'),
    path('edit/<int:plant_id>', edit_plant_page, name='edit-plant-page'),
    path('delete/<int:pk>', delete_plant_page, name='delete-plant-page'),
    path('details/<int:pk>', plant_details_page, name='plant-details-page'),
]






