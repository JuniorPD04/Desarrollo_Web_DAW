function agregarLineasHTML(cantidad) {
    // Selecciona el div donde se agregarán las líneas de HTML
    var creacion_dinamica = document.getElementById("creacion_dinamica");
    var header_tabla = document.getElementById("header_tabla");
    var fila_header_tr = document.getElementById("fila_header_tr")
    
    // Bucle para crear 'cantidad' de líneas de HTML

    for (var i = 1; i <= cantidad; i++) {
        var lineaHTML1 = `<th>${i}</th>`;
        fila_header_tr.innerHTML += lineaHTML1;

        // Crea una línea de HTML similar pero numerada
        var lineaHTML2 = `<p>Esta es la línea número ${i}</p>`;
        
        // Agrega la línea de HTML al div
        creacion_dinamica.innerHTML += lineaHTML2;
    }

}

// Llamada a la función con 5 como cantidad de líneas
agregarLineasHTML(6);
