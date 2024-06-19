$( document ).ready(function() {
    var urlApiRelatorios = $('#urlApiRelatorios').val()
    
    var listExclude =[]
    $('.checkboxPessoa:checked').each(function(){listExclude.push(this.value)})
    
    chamarApiRelatorio(urlApiRelatorios,listExclude)

});

$('#recarregarRelatorio').on('click',function(){
    $('#collapsePessoas').toggleClass('d-none')
    $('#divLoading').removeClass('d-none')
    $('#containerRelatorio').empty()

    var urlApiRelatorios = $('#urlApiRelatorios').val()
    var listExclude =[]
    $('.checkboxPessoa:checked').each(function(){listExclude.push(this.value)})
    
    chamarApiRelatorio(urlApiRelatorios,listExclude)
})

async function chamarApiRelatorio(url,exclude=[]){
    var response = await fetch(url);
    
    let data = await response.json();

    insertRelatorio(data,exclude)
}

function insertRelatorio(data,exclude){

    // console.log(`Index: ${Object.getOwnPropertyNames(data)}`);
    // console.log(`Dados: ${data}`)
    console.log(data)

    var container = $('#containerRelatorio')

    $('#divLoading').addClass('d-none')
    container.empty().append(`
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
    
    
    // console.log(exclude)
    data.perguntas.forEach(pergunta => {
        // console.log(`Valor Antes: ${pergunta.respostas.length}`)
        var respostasFilter = pergunta.respostas.filter(r => exclude.includes(String(r.quemRespondeu.id)));

        pergunta.respostas = respostasFilter
        // console.log(`Valor Depois: ${respostasFilter.length}`)

    })

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

                    // console.log(dict)

                    pergunta.associacoes.map(function(e){
                        listData = []
                        pergunta.alternativas.map(function(a){
                            listData.push({
                                label: a.valor,
                                data:[dict[e.id][a.id]]
                            })
                        })
                        // console.log(e.valor,listData)

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
                    if(pergunta.correto[0]){
                        respostasCorretas = pergunta.correto[0].valor.split(',')
                        var lrc = []
                        // console.log(respostasCorretas)
                        pergunta.respostas.map(function(resp){
                            resp.valor.split(',').map(function(sr){
                                lrc.push(sr)
                            })
                        })

                        dictRespostasCorretas = {}
                        var trc = 0

                        respostasCorretas.map(function(rc){
                            var rdp = rc.split(':')
                            dictRespostasCorretas[rdp[0]] = {}
                            dictRespostasCorretas[rdp[0]]['totalRespostas'] = lrc.filter((l) => l.includes(`${rdp[0]}:`))
                            dictRespostasCorretas[rdp[0]]['respostasCorretas'] = lrc.filter((l) => l.includes(`${rdp[0]}:`)).filter((r)=> r.includes(`:${rdp[1]}`))

                        })

                        // console.log(lrc)
                        // console.log(pergunta.respostas.filter((p) => p.valor == pergunta.correto[0].valor).length)
                        // console.log(pergunta.correto[0].valor)

                        $(`#container-Pergunta-${pergunta.id}`).append(`
                            <div class="mx-1 text-dark">
                                Das <b>${pergunta.respostas.length}</b> respostas, 
                                <b>${pergunta.respostas.filter((p) => p.valor == pergunta.correto[0].valor).length}</b> destas estão na sequência correta. 
                                Representando <b>${((pergunta.respostas.filter((p) => p.valor == pergunta.correto[0].valor).length/pergunta.respostas.length)*100).toFixed(2)}%</b> de acerto.
                            </div>
                        `)

                        $(`#container-Pergunta-${pergunta.id}`).append(`
                            <hr>
                            <h4 class="fs-6 text-secondary text-center">
                                Disposição das respostas:
                            </h4>

                            ${pergunta.associacoes.map(function(associacao,index){                                
                                return `
                                    <div>
                                        <div class="d-flex flex-column">
                                            <p class="text-dark">${index+1}) ${associacao.valor}</p>
                                            ${pergunta.alternativas.map((alternativa) =>{
                                                // console.log(dictRespostasCorretas[alternativa.id]['respostasCorretas'])
                                                return `<span ${ dictRespostasCorretas[alternativa.id]['respostasCorretas'].filter((r) => r.includes(`${alternativa.id}:${associacao.id}`)).length > 0 ? 'class="fw-bold text-success"':''}>${alternativa.valor}: ${((lrc.filter((l) => l.includes(`${alternativa.id}:${associacao.id}`)).length/lrc.filter((l) => l.includes(`${alternativa.id}:`)).length)*100).toFixed(2)}%</span>`
                                            }).join('')}
                                            
                                        </div>
                                    </div>
                                    <hr>    
                                `
                            }).join(' ')}
                        `)

                        // $(`#container-Pergunta-${pergunta.id}`).append(`
                        //     <hr>
                        //     <h4 class="fs-6 text-secondary text-center">
                        //         Disposição das respostas:
                        //     </h4>

                        //     ${respostasCorretas.map(function(rc,index){
                        //         var rdp = rc.split(':')
                        //         dictRespostasCorretas[rdp[0]] = {}
                        //         dictRespostasCorretas[rdp[0]]['totalRespostas'] = lrc.filter((l) => l.includes(`${rdp[0]}:`))
                        //         dictRespostasCorretas[rdp[0]]['respostasCorretas'] = lrc.filter((l) => l.includes(`${rdp[0]}:`)).filter((r)=> r.includes(`:${rdp[1]}`))
                        //         perguntaRetorno = pergunta.associacoes.find((a) => a.id==rdp[1])

                        //         console.log(rdp[0],rdp[1],perguntaRetorno)
                                
                        //         return `
                        //             <div>
                        //                 <p class="text-dark">${index+1}) ${perguntaRetorno.valor}</p>
                        //                 <div class="d-flex justify-content-between">
                        //                     <span class="text-dark">Total de Respostas: <span class="fw-bold">${dictRespostasCorretas[rdp[0]]['totalRespostas'].length}</span></span>
                        //                     <span class="text-dark">Total de Respostas Corretas: <span class="fw-bold">${dictRespostasCorretas[rdp[0]]['respostasCorretas'].length}</span></span>
                        //                     <span class="text-dark">Porcentagem de Respostas Corretas: <span class="fw-bold">${((dictRespostasCorretas[rdp[0]]['respostasCorretas'].length/dictRespostasCorretas[rdp[0]]['totalRespostas'].length)*100).toFixed(2)}%</span></span>
                        //                 </div>
                        //             </div>
                        //             <hr>    
                        //         `
                        //     }).join(' ')}
                        // `)

                    }else{
                        $(`#container-Pergunta-${pergunta.id}`).append(`
                            <hr>
                            ${labelAcept ? '' : pergunta.associacoes.map(function(a,index){
                                return `<p>${index+1}) ${a.valor}</p>`
                            }).join(' ')}
                        `)
                        
                    }

                    break;
                
            }
            
        }

    });
}