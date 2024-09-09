function obtenerValores() {
    let filas = document.getElementById("nroFilas").value;
    let columnas = document.getElementById("nroColumnas").value;

    agregarLineasHTML(filas, columnas);
}

function esconder() {
    let filas = document.querySelectorAll("table tr");

    // Recorrer todas las filas
    filas.forEach((fila, indexFila) => {
        let celdas = fila.querySelectorAll("td, th");

        // Recorrer todas las celdas dentro de una fila
        celdas.forEach((celda, indexCelda) => {

            // Ocultar todas las celdas excepto las de la primera fila (indexFila == 0) y la primera columna (indexCelda == 0)
            if (indexFila > 0 && indexCelda > 0) {
                celda.style.visibility = "hidden"; // Ocultar celdas
            }
        });
    });
}

function agregarLineasHTML(cantidad_filas, cantidad_columnas) {
    if ((cantidad_filas > 0 && cantidad_filas <= 5) && (cantidad_columnas > 0 && cantidad_columnas <= 5)) {

        var tabla_contenedora = document.getElementById("tabla_contenedora");
        tabla_contenedora.innerHTML = "";
        const letras = ["A", "B", "C", "D", "E"];
        var numeros = [];

        while (numeros.length <= (Math.trunc(cantidad_filas * cantidad_columnas / 2) - 1)) {
            numeroAleatorio = Math.floor(Math.random() * 12) + 1;
            if (!numeros.includes(numeroAleatorio)) {
                numeros.push(numeroAleatorio);
            }
        }

        numeros = numeros.concat(numeros);
        numeros = numeros.sort(() => Math.random() - 0.5);

        var header_tabla = document.createElement("thead");
        var body_tabla = document.createElement("tbody");

        var letras_headers = "<tr>";

        tabla_contenedora.appendChild(header_tabla);
        tabla_contenedora.appendChild(body_tabla);

        for (var i = 0; i <= cantidad_columnas; i++) {
            if (i === 0) {
                letras_headers += `<th></th>`;
            } else {
                letras_headers += `<th>${letras[i - 1]}</th>`;
            }
        }
        letras_headers += "</tr>";
        header_tabla.innerHTML = letras_headers;

        var numero_index = 0;
        var veces = 0;
        for (var i = 0; i <= cantidad_filas - 1; i++) {
            var fila = document.createElement('tr');
            for (var j = 0; j <= cantidad_columnas; j++) {
                var celda = document.createElement('td');
                if (j === 0) {
                    celda.innerHTML = `<strong>${i + 1}</strong>`;
                    fila.appendChild(celda);
                } else {
                    if (numero_index === numeros.length) {
                        celda.id = `${letras[j - 1]}${i + 1}`;
                        celda.textContent = `COMODIN`;
                    } else {
                        celda.id = `${letras[j - 1]}${i + 1}`;
                        celda.textContent = `${numeros[numero_index]}`;
                        numero_index++;
                    }
                }
                fila.appendChild(celda);
            }

            body_tabla.appendChild(fila);
        }

        setTimeout(esconder, 3000);

    } else {
        alert('No se permite esa cantiadad de filas o columnas');
    }
}

function valoresId() {
    let id_1 = document.getElementById("primera").value.toUpperCase();
    let id_2 = document.getElementById("segunda").value.toUpperCase();

    verificarValor(id_1, id_2);
}

var contador = 0;

function verificarValor(id_1, id_2) {
    const celda_1 = document.getElementById(id_1);
    const celda_2 = document.getElementById(id_2);

    if (celda_1 && celda_2) {
        if (celda_1.textContent === "COMODIN") {
            celda_1.style.visibility = "visible";
            celda_1.style.backgroundColor = "green";
            alert("Has encontrado comodin");
        } else if (celda_2.textContent === "COMODIN") {
            celda_2.style.visibility = "visible";
            celda_2.style.backgroundColor = "green";
            alert("Has encontrado comodin");
        } else {
            if (celda_1.textContent === celda_2.textContent && id_1 !== id_2) {
                alert("Muy bien");
                celda_1.style.visibility = "visible";
                celda_2.style.visibility = "visible";
                celda_1.style.backgroundColor = "green";
                celda_2.style.backgroundColor = "green";
            } else {
                if (contador<10) {
                    alert(`Error. Los valores fueron: ${celda_1.textContent} y ${celda_2.textContent} te quedan: ${(10 - contador)} intentos`);
                }
                contador++;
                if (contador >= 10) {
                    let respuesta = confirm("No tienes más intentos, ¿Quieres continuar?");
                    if (respuesta) {
                        contador = 0;
                        obtenerValores();
                    } else {
                        alert("Has cancelado.");
                    }
                }
            }
        }
    } else {
        alert("Una o ambas celdas no existen");
    }
}