import requests
from lxml import etree


provincias = ['Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','sevilla']



for provincia in provincias:
	p = {'q':provincia,'mode':'xml','units':'metric','lang':'es'}
	r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=p)


raiz = etree.fromstring(r.text.encode("utf-8"))

city = raiz.find("city")

print city.attrib["name"]