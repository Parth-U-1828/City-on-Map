from django.shortcuts import render
from geopy.geocoders import Nominatim
from folium import *

def home(request):
	if request.GET.get("city"):
		try:
			city = request.GET.get("city")
			geolocator = Nominatim(user_agent="MyApp")
			location = geolocator.geocode(city)

			loc = [location.latitude,location.longitude]
			f = Figure(width=600,height=600)
			thane = Map(location=loc,zoom_start=15).add_to(f)
			Marker(loc,tooltip=city).add_to(thane)
			thane_html=thane._repr_html_()
			return render(request,"home.html",{"msg":thane_html})
	
		except Exception as e:
			msg = "issue" + str(e)
			return render(request,"home.html",{"msg":msg})

	else:
		return render(request,"home.html")
