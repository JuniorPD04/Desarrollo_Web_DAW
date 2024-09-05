function agregarLineasHTML(cantidad) {
    // Selecciona el div donde se agregarán las líneas de HTML
    var creacion_dinamica = document.getElementById("creacion_dinamica");
    var header_tabla = document.getElementById("header_tabla");
    
    // Bucle para crear 'cantidad' de líneas de HTML

    header_tabla.innerHTML += `<tr>
                        <th scope="col">First</th>
                        <th scope="col">Last</th>
                        <th scope="col">Handle</th>
                    </tr>`;

    for (var i = 1; i <= cantidad; i++) {
        // Crea una línea de HTML similar pero numerada
        var lineaHTML = `<p>Esta es la línea número ${i}</p>`;
        
        // Agrega la línea de HTML al div
        creacion_dinamica.innerHTML += lineaHTML;
    }
}

// Llamada a la función con 5 como cantidad de líneas
agregarLineasHTML(5);
