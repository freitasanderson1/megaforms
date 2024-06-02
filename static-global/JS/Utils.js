$('.nav-link').on('click', function(){
    $('.nav-link, .active').removeClass('active')
    $(this).addClass('active')
})

$('#botao-sair').on('click', function(){
    $('#formSair').submit()
})