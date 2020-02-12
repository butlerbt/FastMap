import geocoder
import pandas as pd
import folium
import selenium.webdriver

def geo_locate(location):
    """
    Get geocoordinates for mapbox registered locations
    """
    loc = geocoder.osm(location)
    return loc

def render_map(location, aerial = True):
    """
    Render folium map for geocoded location
    
    aerial dictates if custom mapbox tiles are used
    """

    # loc = geo_locate(location)
    # location = [loc.lat, loc.lng]


    if aerial:
        m = folium.Map(location,
        zoom_start=18, max_zoom=40,
        tiles= 'https://api.mapbox.com/styles/v1/butlerbt/ck6h2wkc107jz1io8zgoqee80/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiYnV0bGVyYnQiLCJhIjoiY2s2aDJqNzl2MDBqdDNqbWlzdWFqYjZnOCJ9.L4RJNdK2aqr6kHcHZxksXw',
        attr='Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        zoom_control = False, )
        m.save('aerial_map.html')
    else:
        m = folium.Map(location,
        zoom_start=18, max_zoom=40,
        zoom_control = False)
        m.save('basic_map.html')
    return m


def capture_map():
    """
    Use Selenium and PhantomJS to capture image of rendered map.
    """
    driver = selenium.webdriver.PhantomJS('phantomjs-2.1.1-macosx/bin/phantomjs')
    driver.set_window_size(512, 512)  # choose a resolution
    driver.get('aerial_map.html')
    # You may need to add time.sleep(seconds) here
    driver.save_screenshot('static/images/screenshot.png')




