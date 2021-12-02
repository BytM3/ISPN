import geocoder,folium,webbrowser,time,shutil,os 
from folium import plugins
import datetime as dt
from rich.progress import track
from rich.console import Console
console=Console()

def his_ip(ip,loc,html): ##--ip history
    f=open('his\his_ip.txt','a')
    f.write("IP adress: "+str(ip)+"located in: "+str(loc)+"--HTML file: "+str(html)+"--Date\Time: "+str(dt.datetime.now())+"\n")
    f.close()
def check_file(file): ##--check file existing True=exist
    os.chdir('.\HTML\isp')
    return os.path.isfile(file) ##-- True = exist // False = do not exist
def verif_ip(isp): ##--verif if ip is correct 
    p=0
    ver=False
    for i in range(len(isp)):
        if isp[i]=='.':
            p+=1
    if p==3 :
        ver=True
    return ver
def Loc(parent): ##--nat-ip location
    isp=input('\nIP-adress:')
    while True:
        if verif_ip(isp)==True:
            g = geocoder.ip(isp) ##--give details on the isp adress 
            address=g.latlng ##--give the lattitude and the longitude of an ip adress on map
            ##--still not sure about it.but,it works just fine :)
            if (address!=[]):
                isd=isp+'.html'
                his_ip(isp,g.city,isd)
                map=folium.Map(address,zoom_start=10) ##--creating the map
                folium.TileLayer('Stamen Terrain').add_to(map) ##--just for show
                folium.TileLayer('Stamen Toner').add_to(map)
                folium.LayerControl().add_to(map)
                map.add_child(plugins.MiniMap())
                folium.Marker(address,
                              popup=isp,
                              tooltip='<strong>Click here to see</strong>',
                              icon=folium.Icon(color='blue',prefix='glyphicon',icon='off')).add_to(map) ##--mark the location of the ISP 
                map.save(isd)
                webbrowser.open(isd) ##--open the map on net automatically
                print()
                for i in track(range(10),description="Saving MAP..."):
                    i=i
                    time.sleep(0.5)
                if check_file(isd):
                    os.remove(isd)
                    os.chdir(parent)
                    shutil.move(isd,'.\HTML\isp')
                    break
                else:
                    os.chdir(parent)
                    shutil.move(isd,'.\HTML\isp')
                    break
            else: ##--if the ip adress do not exist the program will ask for a restart
                console.print('IP adress NOT valid.',style="bold white on red3")
                isp=input('\nRe-enter ISP-adress:')
        else:
            isp=input('\nRe-enter ISP-adress:')