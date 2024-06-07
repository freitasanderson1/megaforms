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
    console.log(data)

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
    perguntasAssociativas = data.perguntas.filter(pergunta => pergunta.tipo === 3)
    
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
                                if(a.valor){
                                    return `<div class="mx-1 text-secondary"><b>${a.quemRespondeu.nome} ${a.quemRespondeu.sobrenome}:</b> ${(a.valor)}</div>`
                                }
                            }).join(' ')}
                        </div>
                        <hr>
                    `)
                    break;
                case 3:
                    var canvasWidth = (1068 / 100) * (100/pergunta.alternativas.length);

                    // console.log(canvasWidth)

                    $('#containerPerguntas').append(`
                        <div id="container-Pergunta-${pergunta.id}">
                            <h1 class="fs-5 text-info text-center">
                                ${pergunta.descricao}
                            </h1>
                            <div id="container-canvas-${pergunta.id}" class="d-flex justify-content-between" style="width:100%;">
                                
                            </div>
                        </div>
                    `)

                    pergunta.associacoes.forEach((a) => {
                      $(`#container-canvas-${pergunta.id}`).append(
                        `<canvas id="canvas-${a.id}" width="${canvasWidth}" height="534"></canvas>`
                      )
                    })

                    // console.log(pergunta)

                    // console.log(pergunta.alternativas.length)
                    // console.log(pergunta.associacoes)
                    
                    var dict = {}
                    var listData = []
                    var labelAcept = true

                    pergunta.respostas.forEach((resposta, index) =>{
                        pergunta.associacoes.forEach((l) => {
                            dict[l.id] = {}
                            pergunta.alternativas.forEach((l2) =>{
                                dict[l.id][l2.id] = 0
                            })
                        })
                    })

                    pergunta.respostas.forEach((resposta, index) =>{            
                        rS = resposta.valor.split(',')
                        rS.forEach((r)=>{
                            if(r){
                                rdp = r.split(':')
                                dict[rdp[1]][rdp[0]]++
                            }
                        })

                    })

                    console.log(dict)

                    pergunta.associacoes.map(function(e){
                        listData = []
                        pergunta.alternativas.map(function(a){
                            listData.push({
                                label: a.valor,
                                data:[dict[e.id][a.id]]
                            })
                        })
                        console.log(e.valor,listData)

                        e.valor.length > 50 ? labelAcept = false : labelAcept = true

                        var data = {
                            labels:[e.valor.length > 50 ? e.valor.substr(0, 50) + '...': e.valor],
                            datasets:listData
                        }

                        new Chart($(`#canvas-${e.id}`), {
                            type: 'bar',
                            data: data,
                            options: {
                                responsive: false,
                                maintainAspectRatio: false,
                                scales: {
                                    y: {
                                        beginAtZero: true
                                    },
                                }
                            }
                        })

                    })

                    $(`#container-Pergunta-${pergunta.id}`).append(`
                        <hr>
                        ${labelAcept ? '' : pergunta.associacoes.map(function(a,index){
                            return `<p>${index+1}) ${a.valor}</p>`
                        }).join(' ')}
                    `)

                    break;

                
                
            }
            
        }

    });
}