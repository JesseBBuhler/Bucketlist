from django.shortcuts import render

from django.http import HttpResponse
from django.utils.regex_helper import contains
from .models import Country, Bucketlist, Traveler


# Create your views here.

def indexPageView(request) :
    return render(request, "travelTemplates/index.html")

def addPageView(request) :
    context = {
        "countries" : Country.objects.all().order_by('country_name'),
    }
    return render(request, "travelTemplates/add.html", context)

def searchPageView(request, code):
    context = {
        "code": code,
    }
    return render(request, "travelTemplates/search.html", context)

def viewPageView(request, id):
    # if new first and last name, add new user to system. Get id of new user, go to view page for the new user
    # if existing user, get id of user, go to view page for the existing user
    #travelerid = id
    bucketlist = Bucketlist.objects.filter(traveler=id)
    context = {
        "traveler": Traveler.objects.get(id=id),
        "bucketlist" : bucketlist
    }
    return render(request, "travelTemplates/view.html", context)

def addHandler(request):
    first_name = request.POST["first_name"].title()
    last_name = request.POST["last_name"].title()
    country_id = request.POST["country"]
    description = request.POST["description"]
    try:
        traveler = Traveler.objects.get(first_name=first_name, last_name=last_name)
    except:
        traveler = Traveler()
        traveler.first_name = first_name
        traveler.last_name = last_name
        traveler.save()

    try: 
        Bucketlist.objects.get(traveler=traveler, place=Country.objects.get(id=country_id))
        print("Item exists!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    except:
        bucketItem = Bucketlist()
        bucketItem.traveler = Traveler.objects.get(id=traveler.id)
        bucketItem.place = Country.objects.get(id=country_id)
        bucketItem.description = description
        bucketItem.save()
    return viewPageView(request, traveler.id)

def searchHandler(request):
    first_name = request.POST["first_name"].title()
    last_name = request.POST["last_name"].title()
    try:
        traveler = Traveler.objects.get(first_name=first_name, last_name=last_name)
    except:
        return searchPageView(request, 1)
    return viewPageView(request, traveler.id)

def deleteHandler(request, id):
    traveler = Bucketlist.objects.get(id=id).traveler.id
    Bucketlist.objects.get(id=id).delete()
    return viewPageView(request, traveler)

def updateHandler(request):
    id = request.POST["traveler_id"]
    #country = request.POST["3"]
    for record in Bucketlist.objects.filter(traveler=id) :
        record.visited = False
        record.save()

    for key, value in request.POST.items():
        if key == "traveler_id" or key == "csrfmiddlewaretoken":
            pass
        else :
            record = Bucketlist.objects.get(place=key, traveler=id)
            record.visited = True
            record.save()
        #print('Key: %s' % (key) ) 
        print(key)
     #print(f'Key: {key}') in Python >= 3.7
        #print('Value %s' % (value) )
    
    return viewPageView(request, id)
