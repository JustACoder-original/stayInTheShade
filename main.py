# from keys import googleMapsKey
# import requests
import folium
from folium import plugins
import webbrowser

m = folium.Map(tiles="OpenStreetMap", location=(39.50, -98.35), zoom_start=5).add_child(
    folium.ClickForMarker()
)
plugins.Geocoder().add_to(m)

m.save("map.html")
webbrowser.open("map.html")
# payload = {"location.latitude":"35.2368689", "location.longitude":"-80.80209479999999", "radius_meters":"50", "view":"FULL_LAYERS", "requiredQuality":"BASE", "key":googleMapsKey}
# r = requests.get("https://solar.googleapis.com/v1/dataLayers:get", params=payload)
