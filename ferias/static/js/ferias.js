/**
 * Este archivo tiene las funciones necesarias para que el filtro de busqueda
 * de la pagina ./ferias/tempaltes/ferias.html funcione correctamente.
 */

const x = document.getElementById("demo");
const lat = document.getElementById('lat');
const lon = document.getElementById('lon');
const radius = document.getElementById('radius');
const myForm = document.getElementById('buscador');
const provinciaSelect = document.getElementById('provincia');
const cantonSelect = document.getElementById('canton');
const distritoSelect = document.getElementById('distrito');
var distribucion_cr = {};
var currentProvincia = 0;
var totalFilters = 0;
var filtersUbicacionCount = 0;
var filtersComodidadesCount = 0;

provinciaSelect.addEventListener('change', (event) => getCantones(event.target.value));
cantonSelect.addEventListener('change', (event) => getDistritos(event.target.value));

setupForm();
setParamsFromQuery();

/**
 * Limpiar el select de cantones y distritos
 **/
function cleanCantones() {
    while (cantonSelect.firstChild) {
        cantonSelect.removeChild(cantonSelect.lastChild);
    }
    let optionElement = document.createElement('option');
    optionElement.value = -1;
    optionElement.innerHTML = "Seleccione un cantón";
    cantonSelect.appendChild(optionElement);
    cleanDistritos();
}

/**
 * Limpiar el select de distritos
 **/
function cleanDistritos() {
    while (distritoSelect.firstChild) {
        distritoSelect.removeChild(distritoSelect.lastChild);
    }
    let optionElement = document.createElement('option');
    optionElement.value = -1;
    optionElement.innerHTML = "Seleccione un distrito";
    distritoSelect.appendChild(optionElement);
}

/**
 * Cambiar los distritos segun la provincia y canton seleccionados.
 **/
function getDistritos(distrito) {
    if (distribucion_cr.length > 0) {
        cleanDistritos();
        let distritos = [];
        let cantones = distribucion_cr[currentProvincia].cantones;
        for (var i = 0; i < cantones.length; i++) {
            if(cantonSelect.value == cantones[i].nombre){
                distritos = cantones[i].distritos;
                break;
            }
        }
        for (var i = 0; i < distritos.length; i++) {
            var optionElmt = document.createElement('option');
            optionElmt.value = distritos[i];
            optionElmt.innerHTML = distritos[i];
            distritoSelect.appendChild(optionElmt);
        }
    }
}

/**
 * Cambiar los cantones segun la provincia.
 **/
function getCantones(provincia) {
    if (distribucion_cr.length > 0) {
        cleanCantones();
        currentProvincia = provincia;
        const cantones = distribucion_cr[currentProvincia].cantones;
        for (var i = 0; i < cantones.length; i++) {
            var optionElmt = document.createElement('option');
            optionElmt.value = cantones[i].nombre;
            optionElmt.innerHTML = cantones[i].nombre;
            cantonSelect.appendChild(optionElmt);
        }
        cleanDistritos();
    }
}

/**
 * Conseguir los datos de las provincias, cantones y distritos 
 **/
function setupForm() {
    $.ajax({
        url: base_url +'data/cr_distribucion.json',
        dataType: "json",
        success: function (data) {
            distribucion_cr = data;
            // Provincias
            for (var i = 0; i < distribucion_cr.length; i++) {
                var optionElmt = document.createElement('option');
                optionElmt.value = i;
                optionElmt.innerHTML = distribucion_cr[i].nombre;
                provinciaSelect.appendChild(optionElmt);
            }
        },
        async: false
    });
}

/***
 *  Cambiar valores de los filtros segun los parametros
 *  del URL
 **/
function setParamsFromQuery() {
    var params = {};
    window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value) {
        params[key] = value;
    });
    var allInputs = myForm.getElementsByTagName('input');
    for (var i = 0; i < allInputs.length; i++) {
        var input = allInputs[i];
        if (params[input.name] !== undefined) {
            input.value = params[input.name];
            if (input.name !== "lat" && input.name !== "lon" 
                && input.name !== "radius" && input.name !== "search")
            {
                filtersComodidadesCount++;
            }
        }
        if (lat.value !== '' && lon.value !== '' && radius.value !== '') {
            document.getElementById('radiusGroup').style.display = 'block';
            document.getElementById('radioText').innerHTML = radius.value / 1000;
        }
    }
    if (params['provincia'] !== undefined){
        provinciaSelect.value = decodeURIComponent(params['provincia']);
        getCantones(provinciaSelect.value);
        filtersUbicacionCount++;
    }
    if (params['canton'] !== undefined) {
        getCantones(provinciaSelect.value);
        cantonSelect.value = decodeURIComponent(params['canton']).replaceAll('+', ' ');
        getDistritos(cantonSelect.value);
        filtersUbicacionCount++;
    }
    if (params['distrito'] !== undefined) {
        getDistritos(cantonSelect.value);
        distritoSelect.value = decodeURIComponent(params['distrito']).replaceAll('+', ' ');
        filtersUbicacionCount++;
    }
    if(filtersComodidadesCount > 0){
        document.getElementById('badge-comodidades').innerHTML = filtersComodidadesCount;
        totalFilters += filtersComodidadesCount;
    }
    if (filtersUbicacionCount > 0) {
        document.getElementById('badge-ubicacion').innerHTML = filtersUbicacionCount;
        totalFilters += filtersUbicacionCount;
    }
    if(totalFilters > 0){
        document.getElementById('badge-filtros').innerHTML = totalFilters;
    }
}

/***
 *  Funcion para no enviar parametros vacios
 **/
myForm.addEventListener('submit', function () {
    var allInputs = myForm.getElementsByTagName('input');
    for (var i = 0; i < allInputs.length; i++) {
        var input = allInputs[i];
        if (input.name && !input.value) {
            input.name = '';
        }
    }
    if (lat.value === '' || lon.value === '') {
        radius.name = '';
    }
    if (provinciaSelect.value < 0){
        provinciaSelect.name = '';
    }
    if (cantonSelect.value < 0) {
        cantonSelect.name = '';
    }
    if (distritoSelect.value < 0) {
        distritoSelect.name = '';
    }
});

/***
 *  Funcion conseguir la posicion geografica
 **/
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Este navegador no soporta geolocalización.";
        alert("Este navegador no soporta geolocalización.");
    }
}

/***
 *  Mostrar coordenadas de la persona
 **/
function showPosition(position) {
    lat.value = position.coords.latitude;
    lon.value = position.coords.longitude;
    radius.value = 1000;
    document.getElementById('radiusGroup').style.display = 'block';
}

/***
*  Actualizar el valor del radio.
**/
function updateRadiusInput(val) {
    document.getElementById('radioText').innerText = val / 1000;
}

/**
 * Agregar al url la pagina de los resultados. 
 * Y abrir el enlace.
 **/
function getPage(page) {
    let url = new URL(window.location.href);
    url.searchParams.set('page', page);    
    window.open(url.href, "_self");
}

/***
 *  Limpiar los filtros de busqueda
 **/
function limpiarFiltros() {
    var allInputs = myForm.getElementsByTagName('input');
    for (var i = 0; i < allInputs.length; i++) {
        var input = allInputs[i];
        if (input.name !== 'search') {
            input.name = '';
        }
    }
    var allSelects = myForm.getElementsByTagName('select');
    for (var i = 0; i < allSelects.length; i++) {
        allSelects[i].name = '';
    }
}

/**
 * Hacer una búsqueda normal sin los parametros de
 * geolocalización.
 */
function normalSearch() {
    lat.name = '';
    lon.name = '';
    radius.name = '';
    myForm.submit();
}