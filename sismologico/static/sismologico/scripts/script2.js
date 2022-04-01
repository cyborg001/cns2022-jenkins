
let div_datos = document.querySelector('.sidenav-content');
// div_datos.innerHTML='hola mundo'
let p_sismo = document.querySelector('.p-sismo');
console.log(p_sismo.id)
let api = 'sismo_api/';
var data = {};
async function  get_sismo(id){  
    console.log(id)
    if(map2 != undefined){
        map2.remove();
    }
    let div_mapa2 = document.querySelector('#div-mapa2')
    div_mapa2.innerHTML=`<div id="map2" class="map map-home" style="margin:12px 0 12px 0;height:400px;"></div>`
    

    

    const response = await fetch(`sismo_api/${id}`);
    const data = await response.json();
    const properties = data.sismo.features[0].properties

    // create the map with initial view from sismo coordinates
    const ll = data.sismo.features[0].geometry.coordinates
    const coord = [ll[1],ll[0]]
    var myIcon = L.icon({
        iconUrl: 'icon.png',
        iconSize: [38, 95],
        iconAnchor: [22, 94],
    })
    var map2 = L.map('map2').setView(coord, 8);    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map2);
    
        var geojsonLayer = L.geoJson(data.sismo,{
            style: function(feature){
                return feature.properties.estilos
            },
    
            onEachFeature: function (feature,layer){
                // creates tablerows element and populate from geojson
                let p = feature.properties

                // add popup window to circleMarkers
                var popupText = `<h4 class='text-center'><strong>Locacion</strong><h4></br>
                                <strong>Latitud: </strong>${p.latitud[0]}</br>
                                <strong>Longitud: </strong>${p.longitud[0]}</br>`
                layer.bindPopup(popupText)
                // turn tablerow and circleMarker color to default when close popup
                layer.on('popupclose',function(e){
                    
                })
                // turn tablerow color to orange and circleMarker color to black
                layer.on('click',function(e){

                })
    
                
            },
            pointToLayer: function(feature,latlng){
                    let l = L.marker(latlng,{});
                
                return l;
            },
        })
        geojsonLayer.addTo(map2)
    // create the list of properties
    
    const ul = document.createElement('ul')
    ul.className='sismo-ul'
    console.log(properties)
    p_sismo.innerHTML=`<h3>Sismo ocurrido en: ${properties.fecha[0]} ${properties.hora[0]}</h3>`
    let scie_data=`<p><pre><b>${properties.data_estaciones[0].slice(0,80)}</b></pre></p>`
    //  properties.data_estaciones[0].forEach((row){
    //    scie_data+= `<pre>${row}</pre><br>`,
    // });
    var numlineas = properties.data_estaciones[0].length % 80
    // for (let i=1;i<numlineas;i++){
    scie_data+=`<p><pre>${properties.data_estaciones[0].slice(80)}</pre></p>`
        // }
        
        
        
    
    var mag = properties.magnitud[0].toString()
    if(mag.length ==1){
        mag = mag+'.0'
    }
    var prof = properties.profundidad[0].toString();
    if(prof.search('[.]') == -1){
        prof = prof + '.0'
    }
    let datos = `<li><b>Fecha:</b> ${properties.fecha[0]}</li> <br>
                <li><b>Hora:</b> ${properties.hora[0]}</li> <br>
                <li><b>Latitud:</b> ${properties.latitud[0]}</li> <br>
                <li><b>Longitud:</b> ${properties.longitud[0]}</li> <br>
                <li><b>Profundidad:</b> ${prof}</li> <br>
                <li><b>Magnitud:</b> ${mag}</li> <br>
                <li><b>Comentario:</b> ${properties.comentario[0]}</li>`
    ul.innerHTML=datos
    div_datos.appendChild(ul)
    let data2 = document.querySelector('.data2')
    let title = `<h1>Datos Tecnicos</h1><br>`
    let title_data= document.createElement('div')
    let sentido= properties.sentido[0] ? 'Si' : 'No'
    var magC = properties.magC[0].toString()
    if(magC.length ==1){
        magC = magC+'.0'
    }
    var magL = properties.magL[0].toString()
    if(magL.length ==1){
        magL = magL+'.0'
    }
    var magW = properties.magW[0].toString()
    if(magW.length ==1){
        magW = magW+'.0'
    }
    var rms = properties.rms[0].toString()
    if(rms.length == 1){
        rms = rms+'.0'
    }
    var analista = properties.analista[0]
    var strFocal = properties.strFocal[0]
    var strGap = properties.strGap[0]
    let datos2 = `<li><b>Analista:</b> ${analista}</li> <br>
                    <li><b>Magnitud Coda:</b> ${magC}</li> <br>
                    <li><b>Magnitud Local:</b> ${magL}</li> <br>
                    <li><b>Magnitud Momento:</b> ${magW}</li> <br>
                    <li><b>Rms:</b> ${rms}</li> <br>
                    <li><b>Sentido:</b> ${sentido}</li> <br>
                    <li><b>Gap Info:</b> ${strGap}</li><br>
                    <li><b>Focal Info:</b> ${strFocal}</li><br>`
    title_data.innerHTML= title + datos2 + scie_data
    data2.appendChild(title_data)
    console.log(scie_data)


}   

get_sismo(p_sismo.id)