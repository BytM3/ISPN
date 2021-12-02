import time,shutil,folium,webbrowser
import os.path 
import phonenumbers as ph ##--import the phonenumbers works on phone numbers
from phonenumbers import timezone,geocoder,carrier
from phonenumbers.phonenumberutil import country_code_for_region ##--import country_code_for_region to find the region the phone number belongs to  
from opencage.geocoder import OpenCageGeocode ##--Convert coordinates to and from places
from folium import plugins
import datetime as dt 
from rich.progress import track
from rich.console import Console
console=Console()

def his_pn(pn,loc,html): ##--phn history
    f=open('his\his_pn.txt','a')
    f.write("IP adress: "+str(pn)+" located in: "+str(loc)+"--HTML file:"+str(html)+"--Date\Time: "+str(dt.datetime.now())+"\n")
    f.close()
def Y_N(): ##--Menu
    console.print("\n[[red]TYPE [b]YES[/][/]] [b][red]IF you know[/][/] [blue]the country-code[/] ")
    console.print("[[red]TYPE [b]NO [/][/]] [b][red]IF you don't know[/][/] [blue]the country-code[/] ")
def check_file(file): ##--check file existing in a dirc
    os.chdir('.\HTML\ph')
    return os.path.isfile(file) ##-- True = exist // False = do not exist 
def get_number(): ##get the phone number.
    Y_N()
    T=input('\nYOUR answer: ').upper() ##--Convert the word entirely to uppercase
    while True:
        if (T=='NO'): ##--if you don't know the country code
            cd=input('Enter region (EXP:TN=>Tunisia):').upper() ##--enter the region name. 
            ##--print(country_code_for_region(cd)) ##--here i could've used the country code directly without print it out.
            num=input('\nnumber: ') ##-- the phone number+country code
            number=('+'+str(country_code_for_region(cd))+num)  ##--the international form of the phone number
            break
        elif (T=='YES'): ##--if you know you know .
            num=input('\nnumber:')
            number=('+'+num)
            break
        else:
            Y_N()
            T=input('\nYOUR answer: ').upper()
    return number ##--return the number  
def valid(numb): ##--check if the number valid or not
    valid = ph.is_valid_number(ph.parse(numb))
    return valid
def get_info(numb): ##get information on the phone number
    pep=ph.parse(numb) ##--get basic details on the number.
    location=geocoder.description_for_number(pep,"en") ##--get location from the number.
    timeZone = timezone.time_zones_for_number(pep) ##--get the timezone from the phone location
    console.print("[b][bright_red]location :----------[/][/]",location)
    console.print("[b][bright_red]service provider :--[/][/]",carrier.name_for_number(pep,"en"))##--this will print the service provider name (like:ooreedoo...).
    console.print("[b][bright_red]Timezone:-----------[/][/]",end="")
    print(timeZone)
    his_pn(numb,location)    
def location(numb,parent): ##--give the exact location on map using: numb=>phone number.
    key='dbe5321bd0034e5a83e9a728794bd3c1'
    location=geocoder.description_for_number(ph.parse(numb),"en") ##--get location from the number.
    geo=OpenCageGeocode(key)
    res=geo.geocode(str(location)) ##--get basic details on the geo-location.
    lat = res[0]['geometry']['lat'] ##--latitude.on.map
    lng = res[0]['geometry']['lng'] ##--longitude.on.map
    map=folium.Map(location=[lat,lng],zoom_start=10) ##--zooms in on the phone location on map => not specific loc
    folium.TileLayer('Stamen Terrain').add_to(map)
    folium.TileLayer('Stamen Toner').add_to(map)
    folium.LayerControl().add_to(map)
    map.add_child(plugins.MiniMap())    
    folium.Circle(radius=10000,
                   location=[lat,lng],
                   fill=True,
                   popup=numb,
                   tooltip='<strong>Click here to see</strong>',
                   ).add_to(map) ##--mark the phone location on map => specific loc
    phd=numb+'.html'
    his_pn(numb,location,phd)
    map.save(phd) ##--save the map as an html file 
    webbrowser.open(phd) ##--open the map on net automatically
    print()
    for i in track(range(10),description="Saving MAP..."):
        i=i
        time.sleep(0.5)
    if check_file(phd):
        os.remove(phd)
        os.chdir(parent)
        shutil.move(phd,'.\HTML\ph')
    else:
        os.chdir(parent)
        shutil.move(phd,'.\HTML\ph')
def help_reg(): ##--helps
    console.print('[[b][red]Ctrl+click[/]] to open[/]: [blue3]https://www.nationsonline.org/oneworld/countries_of_the_world.htm[/]')
