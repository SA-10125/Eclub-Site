from django.shortcuts import render, redirect
from .models import team_members, gallery_names
from django.contrib import messages #this is what we import to get flash messages.
from django.contrib.auth.models import User
#from .models import events
from django.contrib.auth import authenticate,login,logout #imported for the user login
from django.contrib.auth.decorators import login_required,user_passes_test #this is used to restrict pages that need login or a certain login.
from csv import reader #used to read from deleted_data.csv (an idea)


def render_simple_homepage(request):
    team = team_members.objects.all() #inlcudes images as byte64 (images are in static, can change later.)
    gallery_pics = gallery_names.objects.all() #is image loaction in static
    return render(request, 'temp_home.html', {"team_members": team, 'gallery':gallery_pics,})

#Have made the team members easy to change without need to edit the code/the html file as it no longer hard coded.
#This is a more flexible method. However, this may reduce efficieny as it needs an extra query to the database to get the team members

#I have also made the images byte64 encrypted strings. This is more efficient than fetching each image from the databse.
#Images need not be stored in the database. when a new member is added, one can simply use https://www.base64-image.de/ to byte64 encrypt the image into a string and add the string with the other details.
#the same byte64 encrypting has been done for the images in the gallery and for the cool bulb image.
#I have left the text on the blerb section hardcoded as it is unlikely to change and was increasing load time unnecesarily.

#TODO:
# I think speed can significantly be increased by rendering using static. but that isnt V friendly to admin, so try.
# #However, this may lead to client side rendering of images, will fix later.
#need to make the collab now button work.
#fix the events section.


#Heres the code I used to byte64 encrypt the images:
#import base64
#     for i in team:
#         i.image=encode_image_to_base64(i.imagepath)
#         i.save()
# def encode_image_to_base64(image_path):
#     try:
#         with open(image_path, "rb") as image_file:
#             return base64.b64encode(image_file.read()).decode("utf-8")
#     except:
#         return image_path
# #In the HTML, I loaded the images as: <img src="data:image/png;base64,{{ member.image }}" alt="{{ member.name }}" class="rounded-full mx-auto mb-4" width="200" height="200">


def login_page(request): #can add login feautures like error handling
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user=User.objects.filter(username=username)
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            referer = request.META.get('HTTP_REFERER')
            if referer:
                return redirect(referer)
            else:
                # Fallback to a specific URL, e.g., the home page
                return redirect('events')
        else:
            messages.info(request,'Username or password is incorrect.')
    return render(request,'login.html')

@login_required(login_url='login')
def logout_page(request):
    #consider general data record(logouts)?
    logout(request)
    return(redirect('home'))