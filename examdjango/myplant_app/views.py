from django.shortcuts import render, redirect

from examdjango.myplant_app.forms import ProfileForm, PlantForm, DeletePlantForm, EditProfileForm
from examdjango.myplant_app.models import Profile, Plant


def home_page(request):
    profile = Profile.objects.first()
    context = {'profile': profile}

    return render(request, template_name='home-page.html', context=context)


def create_profile_page(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileForm()

    context = {'form': form}

    return render(request, template_name='create-profile.html', context=context)


def profile_details_page(request):
    profile = Profile.objects.first()
    all_plants = len(Plant.objects.all())

    context = {'profile': profile,
               'all_plants': all_plants
               }

    return render(request, template_name='profile-details.html', context=context)


def edit_profile_page(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        context = {'form': EditProfileForm(initial=profile.__dict__)}
        return render(request, 'edit-profile.html', context)
    else:
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile-details-page')
        else:
            context = {'form': form}
            return render(request, 'edit-profile.html', context)


def delete_profile_page(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()

    if request.method == 'POST':
        profile.delete()
        plants.delete()

        return redirect('home-page')

    return render(request, 'delete-profile.html')


def catalogue_page(request):
    plants = Plant.objects.all()
    context = {'plants': plants}

    return render(request, template_name='catalogue.html', context=context)


def create_plant_page(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')

    else:
        form = PlantForm()

    context = {'form': form}

    return render(request, template_name='create-plant.html', context=context)


def plant_details_page(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    context = {'plant': plant}

    return render(request, template_name='plant-details.html', context=context)


def edit_plant_page(request, plant_id):
    plant = Plant.objects.get(id=plant_id)

    if request.method == "GET":
        context = {'form': PlantForm(initial=plant.__dict__)}
        return render(request, 'edit-plant.html', context)

    else:
        form = PlantForm(request.POST, instance=plant)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            context = {'form': form}
            return render(request, 'edit-plant.html', context)


def delete_plant_page(request, plant_id):
    plant = Plant.objects.get(id=plant_id)

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    form = DeletePlantForm(instance=plant)
    context = {'form': form}

    return render(request, 'delete-plant.html', context)




