# Especificación de referencia para la base de datos de ferias del agricultor

- [Definiciones de términos](#terminos)
- [Tipos de campos](#tipos)
- [Definiciones de campos](#definiciones)
    - [Ferias](#ferias)
    - [Horarios](#horarios)
    - [Productos](#productos)

## Definiciones de términos <a name="terminos"></a>

Esta sección define los términos que se utilizan en este documento.

- **Conjunto de datos** (*dataset*): un conjunto completo de archivos definidos por esta especificación. La alteración del conjunto de datos crea una nueva versión del conjunto de datos.
- **Registro** (*record*): una estructura de datos básica compuesta por varios valores de campo diferentes que describen una sola entidad (por ejemplo, agencia de tránsito, parada, ruta, etc.). Representado, en una tabla, como una fila.
- **Campo** (*field*): propiedad de un objeto o entidad. Representado, en una tabla, como una columna.
- Valor de campo (*field value*): una entrada individual en un campo. Representado, en una tabla, como una sola celda.
- **Obligatorio** (*required*): el campo debe incluirse en el conjunto de datos y debe proporcionarse un valor en ese campo para cada registro.
- **Opcional** (*optional*): el campo puede omitirse del conjunto de datos.
- **Obligatorio condicional** (*conditionally required*): el campo o archivo es obligatorio en determinadas condiciones, que se describen en la descripción del campo o del archivo. Fuera de estas condiciones, este campo o archivo es opcional.

## Tipos de campos <a name="tipos"></a>

- **Color**: un color codificado como un número hexadecimal de seis dígitos. Consulte https://htmlcolorcodes.com para generar un valor válido (el "#" inicial no está incluido). Ejemplo: FFFFFF para blanco, 000000 para negro o 0039A6.
- **Código de moneda**: un código de moneda alfabético ISO 4217. Para obtener la lista de la moneda actual, consulte https://en.wikipedia.org/wiki/ISO_4217#Active_codes. Ejemplo: CAD para dólares canadienses, EUR para euros o JPY para yenes japoneses.
- **Fecha**: día en formato AAAAMMDD. Ejemplo: 20180913 para el 13 de septiembre de 2018.
- **Correo electrónico**: una dirección de correo electrónico. Ejemplo: example@example.com
- **Enum**: una opción de un conjunto de constantes predefinidas definidas en la columna "Descripción". Ejemplo: el campo `provincia` contiene un 1 para San José, un 2 para Alajuela...
- **ID**: un valor de campo de ID es un ID interno, que no debe mostrarse a los usuarios y es una secuencia de cualquier carácter UTF-8. Se recomienda utilizar solo caracteres ASCII imprimibles. Los ID definidos en una tabla a menudo se hacen referencia en otra tabla.
- **Código de idioma**: un código de idioma IETF BCP 47. Para obtener una introducción al IETF BCP 47, consulte http://www.rfc-editor.org/rfc/bcp/bcp47.txt y http://www.w3.org/International/articles/language-tags/.Ejemplo: *en* para inglés, *en-US* para inglés americano o *de* para alemán.
- **Latitud**: latitud WGS84 en grados decimales. El valor debe ser mayor o igual a -90.0 y menor o igual a 90.0. Ejemplo: 41.890169 para el Coliseo de Roma.
- **Longitud**: longitud WGS84 en grados decimales. El valor debe ser mayor o igual a -180.0 y menor o igual a 180.0. Ejemplo: 12.492269 para el Coliseo de Roma.
- **Flotante no negativo**: un número de punto flotante (es decir, decimal) mayor o igual que 0.
- **Entero no negativo**: un número entero mayor o igual que 0.
- **Número de teléfono**: un número de teléfono.
- **Hora**: hora en el formato *HH:MM:SS* (también se acepta *H:MM:SS*). Ejemplo: 14:30:00 para las 2:30 p.m.
- **Texto**: una cadena de caracteres UTF-8, cuyo objetivo es mostrarse y que, por lo tanto, debe ser legible por humanos.
- **Zona horaria**: zona horaria TZ de https://www.iana.org/time-zones. Los nombres de las zonas horarias nunca contienen el carácter de espacio, pero pueden contener un guión bajo. Consulte http://en.wikipedia.org/wiki/List_of_tz_zones para obtener una lista de valores válidos. Ejemplo: Asia/Tokio, América/Los_Angeles o África/El_Cairo.
- **URL**: una URL completa que incluye `http://` o `https://`, y cualquier carácter especial en la URL debe tener un escape correcto. Consulte el siguiente http://www.w3.org/Addressing/URL/4_URI_Recommentations.html para obtener una descripción de cómo crear valores de URL completos.

## Definiciones de los campos <a name="definiciones"></a>

En la columna "Obligatorio" están las opciones **R** (requerido), **O** (opcional) y **RC** (requerido condicionalmente).

### Ferias <a name="ferias"></a>

Información general básica de cada feria, incluyendo ubicación e infraestructura.

| Campo           | Tipo   | Obligatorio | Descripción                                                                                          |
|-----------------|--------|-------------|------------------------------------------------------------------------------------------------------|
| `feria_id`      | ID     | R           | Un identificador de tres letras mayúsculas para la feria. Ejemplo: CUR para la Feria de Curridabat.  |
| `codigo_url`    | Texto  | R           | Un nombre que será usado en la URL de cada feria. Ejemplo: "zapote" para https://ejemplo.com/zapote. |
| `nombre`        | Texto  | R           | Nombre oficial de la feria. Ejemplo: Mercado Libre de Guadalupe.                                     |
| `conocido_como` | Texto  | O           | Nombre común de la feria. Ejemplo: Feria de Guadalupe.                                               |
| `provincia`     | Entero | R           | 1 - San José, 2 - Alajuela, 3 - Cartago, 4 - Heredia, 5 - Guanacaste, 6 - Puntarenas, 7 - Limón.     |

### Horarios <a name="horarios"></a>

Tabla de horarios de cada feria.

| Campo         | Tipo   | Obligatorio | Descripción                                                                            |
|---------------|--------|-------------|----------------------------------------------------------------------------------------|
| `feria_id`    | ID     | R           | Un ID de la tabla de ferias que indica a cuál corresponde el horario.                  |
| `dia_inicio`  | Entero | R           | 1 - lunes, 2 - martes, 3 - miércoles, 4 - jueves, 5 - viernes, 6 - sábado, 7 - domingo |
| `hora_inicio` | Hora   | R           | HH:MM                                                                                  |
| `dia_final`   | Entero | R           | 1 - lunes, 2 - martes, 3 - miércoles, 4 - jueves, 5 - viernes, 6 - sábado, 7 - domingo |
| `hora_final`  | Hora   | R           | HH:MM                                                                                  |

### Productos <a name="productos"></a>

Lista de productos disponibles en las ferias.