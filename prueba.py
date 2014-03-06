import requests
from lxml import etree
from jinja2 import Template
import webbrowser
f = open('template.html','r')
web = open('web.html','w')

def direccion(orientacion):
	if (orientacion > 337.5 and orientacion <= 360) or (orientacion  >= 0 and orientacion < 22.5):
		return 'N'
	if orientacion >= 22.5 and orientacion <= 67.5:
		return 'NE'
	if orientacion > 67.5 and orientacion < 112.5:
		return 'E'
	if orientacion >= 112.5 and orientacion <= 157.5:
		return 'SE'
	if orientacion > 157.5 and orientacion < 202.5:
		return 'S'
	if orientacion >= 202.5 and orientacion <= 245.5:
		return 'SO'
	if orientacion > 245.5 and orientacion < 292.5:
		return 'O'
	if orientacion >= 292.5 and orientacion <= 337.5:
		return 'NO'


provincias = ['Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla']

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
	orientacion = float(orientacion.attrib["value"])
	orientacion = direccion(orientacion)
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
