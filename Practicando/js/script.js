function agregarLineasHTML(cantidad) {
    // Selecciona el div donde se agregarán las líneas de HTML
    var tabla_contenedora = document.getElementById("tabla_contenedora");
    var header_tabla = document.getElementById("header_tabla");
    var fila_header_tr = document.getElementById("fila_header_tr");
    const letras = ["A", "B", "C", "D", "E"];

    // Bucle para crear 'cantidad' de líneas de HTML
    var letras_headers = "";

    for (var i = 1; i <= cantidad; i++) {
        letras_headers += `<th>${letras[i-1]}</th>`;

        var fila = document.createElement('tr'); // Crear fila

        for (var j = 0; j < cantidadColumnas; j++) {
            var celda = document.createElement('td'); // Crear celda
            celda.innerHTML = `Fila ${i+1} - Columna ${j+1}`; // Contenido de celda
            fila.appendChild(celda); // Añadir celda a la fila
        }

        tabla.appendChild(fila); // Añadir fila a la tabla
    }

    fila_header_tr.innerHTML += letras_headers;

}

// Llamada a la función con 5 como cantidad de líneas
agregarLineasHTML(5);
