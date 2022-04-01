

// const api_url = 'sismos_api/';
var prevApi = {};
const api_url = 'sismos_api/';
var data = undefined
// charge the api and populate the table and the map
if(map != undefined){
    map.remove()
}
async function get_datos(){
    const response = await fetch(api_url);
    const json = await response.json();
    let geo = JSON.stringify(json.geojson)
    
    if (data != geo){
        data = geo
        get_data(JSON.parse(data))
    } 
}
function get_data(data){
        if(map != undefined){
            map.remove()
        }
        let div_mapa = document.querySelector('#div-mapa')
        div_mapa.innerHTML=`<div id="map" class="map map-home" style="margin:12px 0 12px 0;height:400px;"></div>`
        
    
        var map = L.map('map').setView([18.476389, -69.893333], 6);    
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);
    
        // needed variables
        
        let tbody = document.querySelector('tbody')
        tbody.innerHTML = ''
        let activePopup=false;
    
        
        
        var geojsonLayer = L.geoJson(data,{
            style: function(feature){
                return feature.properties.estilos
            },

            onEachFeature: function (feature,layer){
                // creates tablerows element and populate from geojson
                let p = feature.properties
                let tbody = document.querySelector('tbody')
                let color = ''
                const tr = document.createElement('tr');
                tr.id = `tr${p.id[0]}`
                tr.className='tr-class'
                var latitud = String(p.latitud[0])
                if(latitud.length == 2){
                    latitud+= '.000'
                }else{
                    var l = 6 - latitud.length
                    for(var i = 0;i < l;i+=1){
                        latitud+='0'
                    }
                }
                var longitud = String(p.longitud[0])
                if(longitud.length==3){
                    longitud+='.000'
                }else{
                    var l = 7 - longitud.length
                    for (var i = 0; i < l; i+=1){
                        longitud+='0'
                    }
                }
                if(p.sentido[0]){
                    p.comentario[0]+=' (Sentido!)'
                    tr.style.color='red';
                }
                var mag = p.magnitud[0].toString()
                if(mag.length ==1){
                    mag = mag+'.0';
                }
                var prof = p.profundidad[0].toString()
                if(prof.search('[.]') == -1){
                    prof = prof + '.0';
                }
                tr.innerHTML=`
                            <td >${p.fecha[0]}</td>
                            <td >${p.hora[0]}</td>
                            <td >${latitud}</td>
                            <td >${longitud}</td>
                            <td >${prof}</td>
                            <td >${mag}</td>
                            <td >${p.comentario[0]}</td>`
                // addEventListener when click on tablerow
            
                tr.onclick = function(e){
                    // layer.openPopup()
                    console.log(e.target)

                    if (color != 'orange'){
                        clearInterval(interval)
                    }else{
                        color = ''
                    }
                    
                }
                // addEventListener when press mouse on tablerows
                tr.onmousedown= function(e){
                    // if(!activePopup){
                        color=e.target.parentNode.style.backgroundColor
                        // if (color != 'orange'){
                            layer.setStyle({fillColor:'black',color:'black'});
                        
                            e.target.parentNode.style.backgroundColor='orange'
                        
                            layer.openPopup();
                        // }
                        
                };
                // addEventListener when release mouse from tablerows
                tr.onmouseup= function(e){

                };
                tr.ondoublueclick=function(e){
                    interval = setInterval(get_datos,5000);
                }
                // add this tablerow to tbody in the table
                tbody.appendChild(tr)

                // add popup window to circleMarkers
                var mag = p.magnitud[0].toString()
                if(mag.length ==1){
                    mag = mag+'.0'
                }
                var prof = p.profundidad[0].toString()
                if(prof.search('[.]') == -1){
                    prof = prof + '.0'
                }
                var popupText = `<strong>Fecha: </strong>${p.fecha[0]}</br>
                                <strong>Hora: </strong>${p.hora[0]}</br>
                                <strong>Latitud: </strong>${p.latitud[0]}</br>
                                <strong>Longitud: </strong>${p.longitud[0]}</br>
                                <strong>Profundidad: </strong>${prof}</br>
                                <strong>Magnitud: </strong>${mag}</br>
                                <strong>Comentario: </strong>${p.comentario[0]}</br>
                                <a class='a-sismo' href="/sismo?id=${p.id[0]}&latitud=${p.latitud[0]}&longitud=${p.longitud[0]}">Mas informacion</a>`
                
                layer.bindPopup(popupText, {
                    offset: L.point(0, -10)
                });
                // turn tablerow and circleMarker color to default when close popup
                layer.on('popupclose',function(e){
                    let elem = document.querySelector(`#tr${p.id[0]}`);
                    elem.style.backgroundColor = color;
                    activePopup = false;
                    layer.setStyle(
                        p.estilos,
                    )
                    
                    interval = setInterval(get_datos,5000);
                })
                // turn tablerow color to orange and circleMarker color to black
                layer.on('click',function(e){
                    // if(!activePopup){
                        let elem = document.querySelector(`#tr${p.id[0]}`)

                        color = elem.style.backgroundColor
                        elem.scrollIntoView(false);
                        console.log(elem.style.top)
                        // elem.parentNode.parentNode.parentNode.scrollTop   )
                        
                        document.querySelector('html').scrollTop='100'
                        elem.style.backgroundColor = 'orange'
                        layer.setStyle({fillColor:'black',
                                    color:'black',
                                    fillOpacity:'1',
                                    });
                    clearInterval(interval)
                })

                
            },
            
            pointToLayer: function(feature,latlng){
                let l = L.circleMarker(latlng,{
                    radius:  feature.properties.magnitud[0]*2,
                });
                
                return l;
            },
        })
        geojsonLayer.addTo(map)
   
}
    get_datos(); 
    // periodic(get_data,5000)

    var interval = setInterval(get_datos,5000)

    

