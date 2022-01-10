// En este archivo están variables/funciones que se utilizarán en toda
// la página.

//===================== GENERICO ===========================

// Habilitar Tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
});

//===================== HORARIOS ===========================

// Diccionario para convertir los dias
const dias_dict = {
    'L': 'Lunes',
    'K': 'Martes',
    'M': 'Miércoles',
    'J': 'Jueves',
    'V': 'Viernes',
    'S': 'Sábado'
}

/**
 * Convertir una hora (string) en formato de 24 horas a formato de 12 horas (am/pm)
 */
function convertToAMPM(timeString) {
    const timeStr = new Date('1970-01-01T' + timeString + 'Z')
        .toLocaleString('es-CR', { timeZone: 'UTC', hour12: true, hour: 'numeric', minute: 'numeric' });
    return timeStr;
}