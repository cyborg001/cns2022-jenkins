# capstone
Final proyect for the Web Programming with Python and Javascript course.
user: administrador, contrasena: analisisuasd
INTRODUCTION

My final proyects is an app wich allows a seismic center to post seismic events in a the webpage. It shows a table of last 20 earthquakes happended, you can click on each earthquakes to see its properties and at same time you can see the point in the map where earthquake occured, it also works if you click on each eartquake in the map then you can see its properties and the earthquake will be shown in the table.

This app in the backend is constantly waiting for a new file named hyp.out wich is a file created by a program that parses a file outputed bye another program called Seisan.

The webapp also shows data from the institution that is analizing the eartquakes.

PASSING THE REQUIREMENTS

I believe this project satisfies the distinctiveness and complexity requirements because of the following: 

1- It's completly differet from any other project.
2- It has 3 Models: User, Sismo and Article.
3- It was designed and implemented by me using Python and JavaScript.
4- It was created using Django framework.
5- It's mobile responsive.

The file contained in this projects are the folowings:

1- models.py: it containt the models that represent the database. these models are:
    User, Sismo and Article.
2- urls.py: it has every url need to call the pages and apis in the project.
3- views.py: here you can see the logic of the backend created with Python 3.8. it started running
    a thread in background withs is constantly listen for a file to appears in any custom path tha you may find ok. Every 5 seconds it veryfied if the file hyp.out has been created then it uses it and delete it.

4- in templates/sismologico you will find 5 html files: base_legal.html, index.html, layout.html,   quienes.html, and sismo.html. in these page appears all the content of the app.

5- in static/sismologico youl find fhe following carpets: css wich containt the styles.css file, images where there are all the images needed in the app, leaflet has the leaflet lybraries need for the map to function, and scrips where you find the scrips which makes the frontend, these scripts are named script1 and script2.  

UNDERSTANDING views.py
 views.py is the main of the app and it containt all the functions needed in the backend, these functions are:

- ejecucion_horaria(segundos,path)

    segundos is the time for the thread to sleep and path is the path where the hyp.out file is created.

    this function is created because of the needless of the app for be constantly waiting for the hyp.out file to be created, whe its files appears this function will extract from the file the data corresponding for the last earthquake to be adde to the database and whowed in the table and map. so it returns the sismo object. and deletes the hyp.out to wait for the next event to ocurres. it maked thise process every 5 seconds.

- hilo.start
    starts the thread ejecucion_horaria. and set the time to 5 seconds.

- set_estilo(fecha,hora):
    fecha and hora are string and are extrated from the hyp.out file in ejecucion_horaria function.

    base on the date when the event happend it will computes the difference between the time when event happend and the now time.
    base on this difference it computes the colors of the circleMarkers in the map.

- index(request):
    this function creates the articles that will be posted in the carousel. and sends the user to the index.html page
  
- sismo_api(request,sismo_id):
    sismo_id is a string to be converted to integer to create the sismo object that will be shown in sismo.html page
    it returns the api, a json object in the geoJson format.

- sismos_api(request):
    this functions works when the api is called by and ajax function in the frontend. it returns a api geoJson object.

- parse_geojson(sismos):
    it is used internaly in the sismo_api function to parse the sismos objects and parse it into a geojson object

- sismo(request):
    its accept a GET method and gets id, fecha and hora from the frontend, in the 'mas informacion' link when you click on a earthquake
    these data will be used in script2 to call for the sismo_api/<int:num>
    and sends user to the sismo.html webpage.

- quienes(request):
    send user to static page quienes.html

- base_legal(request):
    send user to static page base_legal.html

UNDERSTANDING script1.js

    in script1 we found the async function get_data(). this function creates the map(from leaflet), and call for the api, if the api response is success then it gets a geojson object wich has all the features for every las 20 earthquakes. with this data the map is populated and the talbe too.

UNDERSTANDING script2.js

    in script2.js you'll find the async function get_sismo(id).
    this function receives a  parameter id which represents the id of the earthquake to analize, it also populates a list with the data returned from the promise, and populate the map for this only earthquake.




