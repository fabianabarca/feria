/**
 * Este archivo tiene las funciones necesarias para que la lista de productos
 * de la pagina ./ferias/tempaltes/list_productos.html funcione correctamente.
 */

var list_products = [];
var total = 0;
const list_name = "milista";

//Ref: https://developer.mozilla.org/es/docs/Web/API/Window/localStorage
if (!window.localStorage.getItem(list_name)) {
  //Crear localstorage
  window.localStorage.setItem(list_name, JSON.stringify(list_products));
} else {
  //Conseguir localstorage
  list_products = JSON.parse(window.localStorage.getItem(list_name));
}

/**
 * Conseguir un producto dado su identidicador unico (ID)
 * @param {int} idIdentificador del producto que queremos conseguir
 * @returns object Producto
 */
function getProduct(id_product) {
  let product = null;
  if (list_products && list_products.length > 0) {
    product = list_products.find((p) => p.producto.id == id_product);
  }
  return product;
}

/**
 * Modificar/Agregar un producto de la lista
 * @param {json} product Json que representa un producto
 * @returns true se pudo modificar/agregar el producto, false en caso contrario
 */
function setProduct(product) {
  product = JSON.parse(product.replaceAll("'", '"'));
  let done = false;
  if (list_products && list_products.length > 0) {
    for (var i = 0; i < list_products.length && !done; i++) {
      if (
        list_products[i] &&
        list_products[i].producto.id === product.producto.id
      ) {
        if (list_products[i].quantity >= 1) {
          list_products[i].quantity += product.quantity;
        } else {
          list_products[i].quantity = product.quantity;
        }

        done = true;
      }
    }
    if (!done) {
      list_products.push(product);
      done = true;
    }
  } else {
    list_products.push(product);
    done = true;
  }
  drawList();
  return done;
}

/**
 * Eliminar un producto dado su identidicador unico (ID)
 * @param {int} idIdentificador del producto que queremos eliminar
 * @returns true se pudo eliminar el producto, false en caso contrario
 */
function removeProduct(id_product) {
  let done = false;
  for (var i = 0; i < list_products.length && !done; i++) {
    if (
      list_products[i] &&
      list_products[i].producto.id === parseInt(id_product)
    ) {
      list_products.splice(i, 1);
      drawList();
      done = true;
    }
  }
  return done;
}

/**
 * Guardar lista de productos
 */
function saveList() {
  if (list_products) {
    window.localStorage.setItem(list_name, JSON.stringify(list_products));
  }
}

/**
 * Modificar la cantidad de un producto
 * @param {int} id ID del producto a modificar
 * @param {bool} isMinus Verificar si es suma o resta
 */
function updateQuantity(id, isMinus = false) {
  let product = getProduct(id);
  if (isMinus) {
    product.quantity -= 1;
    if (product.quantity <= 0) {
      removeProduct(id);
    }
  } else {
    product.quantity += 1;
  }
  drawList();
}

/**
 * Calcular el valor total de la lista
 */
function calculate() {
  total = 0;
  if (list_products && list_products.length > 0) {
    list_products.forEach((product) => {
      total += product.producto.precio * product.quantity;
    });
  }
}

/**
 * (Re)Dibujar la lista de productos y la guarda
 */
function drawList() {
  calculate();
  let total_span = document.getElementById("total");
  total_span.innerHTML = "₡ " + total;
  let list = document.getElementById("list-products");
  list.innerHTML = "";
  let newElements = "";
  if (list_products && list_products.length > 0) {
    list_products.forEach((product) => {
      newElements +=
        '<label class="list-group-item d-flex justify-content-start align-items-center">';
      newElements +=
        '<img src="' +
        product.producto.imagen +
        '" class="img-circle me-2" width="40"/>';
      newElements +=
        '<div class="flex-grow-1"> <b>' +
        product.producto.nombre_comun +
        "</b><br>";
      newElements +=
        '<figcaption class="figure-caption">' +
        product.producto.nombre_cientifico +
        "</figcaption></div>";
      newElements +=
        "<b>₡ " +
        product.producto.precio +
        " x " +
        product.quantity +
        "&nbsp;&nbsp;</b>";
      newElements +=
        '<div class="btn-group" role="group" aria-label="Agregar o quitar producto">';
      newElements +=
        '<button type="button" class="btn btn-info" onclick="updateQuantity(' +
        product.producto.id +
        ')">+</button>';
      newElements +=
        '<button type="button" class="btn btn-info" onclick="updateQuantity(' +
        product.producto.id +
        ', true)">-</button></div>';
      newElements +=
        '<button type="button" class="btn btn-danger" onclick="removeProduct(' +
        product.producto.id +
        ')"><i class="bi bi-trash"></i></button>';
      newElements += "</label>";
    });
  }
  list.innerHTML = newElements;
  saveList();
}

/**
 * Copiar en el clipboard la lista
 * @param {htmlElement} context Elemento donde el tooltip se mostrara
 */
function copyToClipboard(context) {
  let title = "La lista esta vacia";
  if (list_products && list_products.length > 0) {
    let listCopied = "Posible total: ₡" + total + "\n\n";

    list_products.forEach((product) => {
      listCopied +=
        "-" +
        product.producto.nombre_comun +
        " x " +
        product.quantity +
        " = " +
        "₡ " +
        product.producto.precio * product.quantity;
      listCopied += "\n";
    });

    navigator.clipboard.writeText(listCopied);
    title = "Se copió la lista!";
  }
  //Usando los tooltips de boostrap 5
  let tooltip = new bootstrap.Tooltip(context, {
    title: title,
  });
  //Deshabilitar el tooltip usa vez el usuario lo ha visto
  //https://getbootstrap.com/docs/5.0/components/tooltips/#events
  context.addEventListener("hidden.bs.tooltip", function () {
    tooltip.disable();
  });

  tooltip.show();
}

/**
 * Borrar lista
 */
function deleteList() {
  window.localStorage.removeItem(list_name);
  list_products = [];
  drawList();
}

drawList();
