$('.associativa').on('input',function(){
    var id = $(this).attr("id")
    var value = $(this).val()
    var questao = $(this).data('item')

    $(this).val() > $(this).data('maxvalue') || $(this).val() <= 0 ? $(this).val(''): $(this).val() 

    // $(`.associativa[data-item="${questao}"]`).each(function(index, item){
    //     if(this.id != id && $(this).val() == value){
    //         $(this).val('')
    //     }
    // })
})