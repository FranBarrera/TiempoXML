import requests
from lxml import etree
from jinja2 import Template
import webbrowser
f = open('template.html','r')
web = open('web.html','w')

provincias = ['Almeria','Cadiz','Cordoba','Huelva','Jaen','Malaga','Sevilla']

html=''
list_min = []
list_max = []
listspeed = []
listorientacion = []


for provincia in provincias:
	p = {'q':provincia ,'mode':'xml','units':'metric','lang':'sp'}
	r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=p)
	raiz = etree.fromstring(r.text.encode("utf-8"))
	city = raiz.find("city")
	speed = raiz.find("wind/speed")
	speed = speed.attrib["value"]
	temp_min = raiz.find("temperature")
	temp_min = int(float(temp_min.attrib["min"]))
	temp_max = raiz.find("temperature")
	temp_max = int(float(temp_max.attrib["max"]))
	orientacion = raiz.find("wind/direction")
	orientacion = orientacion.attrib["name"]
	list_min.append(temp_min)
	list_max.append(temp_max)
	listspeed.append(speed)
	listorientacion.append(orientacion)

for linea in f:
	html += linea

mitemplate = Template(html)
mitemplate = mitemplate.render(provincias=provincias,temp_min=list_min,temp_max=list_max,viento=listspeed,direccion=listorientacion)
web.write(mitemplate)

webbrowser.open('web.html')
