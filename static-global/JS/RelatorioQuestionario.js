$( document ).ready(function() {
    var urlApiRelatorios = $('#urlApiRelatorios').val()
    
    chamarApiRelatorio(urlApiRelatorios)

});

async function chamarApiRelatorio(slug){
    var response = await fetch(slug);
    
    let data = await response.json();

    insertRelatorio(data)
}

function insertRelatorio(data){

    // console.log(`Index: ${Object.getOwnPropertyNames(data)}`);
    // console.log(`Dados: ${data}`)

    var container = $('#containerRelatorio')

    container.empty()
    container.append(`
        <h1 class="text-info fs-4 fw-bold">
            Questionário: <span class="fs-5 fw-normal">${data.nome}</span>
        </h1>
        <h1 class="text-secondary fs-5">
            Descrição: <span class="fs-6">${data.descricao}</span>
        </h1>
        <hr>
        <div id="containerPerguntas">
        </div>
    `)

    data.perguntas.forEach(pergunta => {
        if(pergunta.ativo){

            switch(pergunta.tipo){
                case 0:

                    $('#containerPerguntas').append(`
                        <div id="container-Pergunta-${pergunta.id}">
                            <h1 class="fs-5 text-info text-center">
                                ${pergunta.descricao}
                            </h1>
                            <canvas>
                            </canvas>
                        </div>
                    `)

                    var ctx = $(`#container-Pergunta-${pergunta.id} canvas`)
                    var labels = ['']
                    var data = {
                        labels: labels,
                        datasets:
                            pergunta.alternativas.map(function(a){
                                return { 
                                    'label': a.valor,
                                    'data': [pergunta.respostas.filter((p) => p.valor==a.valor).length],
                                    'borderWidth': 1
                                }
                            })
                    }

                    new Chart(ctx, {
                        type: 'bar',
                        data: data,
                        options: {
                            scales: {
                                y: {
                                    beginAtZero: true
                                }
                            }
                        }
                    });
                    var totalRespostas = pergunta.respostas.length

                    $(`#container-Pergunta-${pergunta.id}`).append(`
                        <h4 class="fs-6 text-secondary text-center">
                            Disposição das respostas:
                        </h4>
                        <div class="d-flex justify-content-center perguntasDisposition">
                            ${ pergunta.alternativas.map(function(a){
                                return `<div class="mx-1 text-secondary"><b>${a.valor}:</b> ${((pergunta.respostas.filter((p) => p.valor==a.valor).length / totalRespostas) * 100).toFixed(2)}% </div>`
                            }).join(' ')}
                        </div>
                        <hr>
                    `)
                    break;

                case 1:

                    $('#containerPerguntas').append(`
                        <div id="container-Pergunta-${pergunta.id}">
                            <h1 class="fs-5 text-info text-center">
                                ${pergunta.descricao}
                            </h1>
                            <canvas>
                            </canvas>
                        </div>
                    `)
                    var ctx = $(`#container-Pergunta-${pergunta.id} canvas`)
                    var labels = ['']

                    pergunta.respostas.map(function(p){
                        p.valor = p.valor.split(',') 
                        return p.valor
                    })

                    var dict = {}
                    pergunta.alternativas.map(function(e){
                        dict[`${e.valor}`] = 0
                        pergunta.respostas.map(function(p){
                            if(p.valor.includes(e.valor)){
                                return dict[`${e.valor}`]++
                            }
                            else{
                                return dict[`${e.valor}`]
                            }
                        })
                        return 
                    })
                    var data = {
                        labels: labels,
                        datasets:
                            pergunta.alternativas.map(function(a){
                                return { 
                                    'label': a.valor,
                                    'data': [dict[`${a.valor}`]],
                                    'borderWidth': 1
                                }
                            })
                    }

                    new Chart(ctx, {
                        type: 'bar',
                        data: data,
                        options: {
                            scales: {
                                y: {
                                    beginAtZero: true
                                }
                            }
                        }
                    });

                    var totalRespostas = 0
                    pergunta.alternativas.map(function(a){
                        totalRespostas += dict[`${a.valor}`]
                    })

                    $(`#container-Pergunta-${pergunta.id}`).append(`
                        <h4 class="fs-6 text-secondary text-center">
                            Disposição das respostas:
                        </h4>
                        <div class="d-flex justify-content-center perguntasDisposition">
                            ${ pergunta.alternativas.map(function(a){
                                return `<div class="mx-1 text-secondary"><b>${a.valor}:</b> ${((dict[`${a.valor}`] / totalRespostas) * 100).toFixed(2)}% </div>`
                            }).join(' ')}
                        </div>
                        <hr>
                    `)

                    break;

                case 2:
                    $('#containerPerguntas').append(`
                        <div id="container-Pergunta-${pergunta.id}">
                            <h1 class="fs-5 text-info text-center">
                                ${pergunta.descricao}
                            </h1>
                        </div>
                    `)

                    $(`#container-Pergunta-${pergunta.id}`).append(`
                        <h4 class="fs-6 text-secondary text-center">
                            Disposição das respostas:
                        </h4>
                        <div class="d-flex flex-column">
                            ${ pergunta.respostas.map(function(a){
                                return `<div class="mx-1 text-secondary"><b>${a.quemRespondeu.nome} ${a.quemRespondeu.sobrenome}:</b> ${(a.valor)}`
                            }).join(' ')}
                        </div>
                        <hr>
                    `)
                    break;
                
                
            }
            
        }

    });
}