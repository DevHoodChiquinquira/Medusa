const checkbox = document.getElementById('id_recursoTecnologico')

checkbox.addEventListener('change', (event) => {
  if (event.target.checked) {
    console.log('checked')
    $(formRecursoFisico).show();
    id_marca.required = true;
    id_modelo.required = true;
    id_numeroSerie.required = true;
    id_placaInventario.required = true;
  } else {
    console.log('not checked')
    $(formRecursoFisico).hide();
    id_marca.required = false;
    id_modelo.required = false;
    id_numeroSerie.required = false;
    id_placaInventario.required = false;
  }
})
