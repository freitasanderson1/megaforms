$('#formQuestionario').on('submit', function(){
    event.preventDefault()
    console.log('Tentaram me enviar aqui ó')
})

$('.assoativa').on('input',function(){
    var id = $(this).attr("id")
    var value = $(this).val()

    $(this).val() > $(this).data('maxvalue') || $(this).val() <= 0 ? $(this).val(''): $(this).val() 

    $('.assoativa').each(function(index, item){
        if(this.id != id && $(this).val() == value){
            $(this).val('')
        }
    })
})