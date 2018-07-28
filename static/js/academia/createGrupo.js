var proceso = new Object();
var table = new Array();
var numeroAsignaturas = 0;
proceso.asignatura = new Array();

//principal
$(document).ready(function(){


    $('#btnAsignaturaBuscar').submit(function(e){
        e.preventDefault();
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
              success: function(json){
                console.log(JSON.stringify(json))
                var html = ""
                if (json.length !=0) {
                  for (var i = 0; i < json.length; i++) {

                    html += 'Descripción: '+json[i].descripcion + '<br>';
                    if (json[i].estado_activo== true) {
                        html += 'Estado: Activo <br/>';
                    }else {
                        html += 'Estado: Inactivo <br/>';
                    }
                    html += 'ID Programa Académico: '+json[i].programaacademico + '<br>';
                    html += 'Nombre Programa Académico: '+json[i].programaacademico__descripcion + '<br>';
                    var fila = new Object();
                    /*Se establecen los valores que se llevaran a tablas*/
                    fila.descripcion = json[i].descripcion;
                    fila.estado_activo = json[i].estado_activo;
                    fila.programaacademico = json[i].programaacademico;
                    fila.programaacademico__descripcion = json[i].programaacademico__descripcion;
                    table.push(fila);
                        }//final for
                  $("#btnAsignaturaSeleccionar").attr("disabled", false);
                  $('#asignatura_list').html(html);
                }else{
                  html += '<strong>Asignatura con el código de busqueda no existe</strong><br>';
                  $('#asignatura_list').html(html);
                  $("#btnAsignaturaSeleccionar").attr("disabled", true);
                    }
                  }//final json
                })
                });


    $("#btnAsignaturaSeleccionar").click(function(){
        var d = table;
        var t = document.getElementById('tb-detalle').getElementsByTagName('tbody')[0];
        var rowCount = t.rows.length;
        var row = t.insertRow(rowCount);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        cell1.innerHTML = d[d.length-1].descripcion;
        if (d[d.length-1].estado_activo == true) {
            cell2.innerHTML = 'Activo';
        }else {
            cell2.innerHTML = 'Inactivo';
        }
        cell3.innerHTML = d[d.length-1].programaacademico__descripcion;
        cell4.innerHTML = '<td><input type="button" class="borrar" value="Eliminar" /></td>';
        proceso.asignatura.push({'id': d[d.length-1].id});
        numeroAsignaturas +=1;
        controAsignaturas(numeroAsignaturas);
    });


    $("#btnCerrarAsignatura").click(function(){
        $("#txtNombreAsignatura").val("");
    });


    $(document).on('click', '.borrar', function (event) {
         event.preventDefault();
         $(this).closest('tr').remove();
         numeroAsignaturas -= 1;
         controAsignaturas(numeroAsignaturas);
    });


    function controAsignaturas(asig){
        if (asig !=0){
            var htm = "";
            $("#btnAsignaturaSeleccionar").attr("disabled", true);
            $("#btnGuardar").attr("disabled", false);
            $("#txtNombreAsignatura").val("");
            $('#asignatura_list').html(htm);
        }else{
            $("#btnGuardar").attr("disabled", true);
        }
    };


})//principal
