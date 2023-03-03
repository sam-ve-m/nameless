var ficha_socket = connect_to_socket('ws://localhost:3334/ws/ficha/'+resource_name, function(event) {
    const jogador = JSON.parse(event.data);
    const atributos = jogador["atributos"];
    if (atributos != undefined){
        for (var atributo_nome in atributos){
            mudar_atributo(atributo_nome, atributos[atributo_nome]);
        };
        atualizaPericias(atributos);
    }
    if (jogador["defesa"] != undefined){
        mudar_defesa(jogador["defesa"]);
    };
    if (jogador["movimento"] != undefined){
        mudar_movimento(jogador["movimento"]);
    };
    if (jogador["vida"] != undefined){
        mudar_vida(jogador["vida"]);
    };
    if (jogador["esforco"] != undefined){
        mudar_esforco(jogador["esforco"]);
    };
});
ficha_socket.onclose = function(e) {
    ficha_socket = ficha_socket.reconnect();
};

function mudar_atributo(nome, atributo){
    const atributo_element = document.getElementById(nome);
    const valor = atributo_element.getElementsByClassName("attrnum")[0];
    valor.innerHTML = atributo["valor"];

    const modificador_atual = atributo["modificador"];
    novo_modificador(atributo_element, modificador_atual, "bruto");
}


function mudar_defesa(valor){
    document.getElementById("defense").innerHTML = valor;
};

function mudar_movimento(valor){
    document.getElementById("movimento").innerHTML = valor;
};


function mudar_vida(valor){
    const status_element = document.getElementsByClassName("statuses")[0].children[0];
    mudar_status(valor, status_element);
};

function mudar_esforco(valor){
    const status_element = document.getElementsByClassName("statuses")[0].children[1];
    mudar_status(valor, status_element);
};


function mudar_status_maximo(valor, elemento){
    mudar_valor(elemento.getElementsByClassName("statustotal")[0], valor);
};


function mudar_status_atual(valor, elemento){
    mudar_valor(elemento.getElementsByClassName("statusactive")[0], valor);
};


function mudar_status(valor, elemento){
    if (valor["atual"] != undefined){
        mudar_status_atual(elemento, valor["atual"]);
    };
    if (valor["maximo"] != undefined){
        mudar_status_maximo(elemento, valor["maximo"]);
    };
};

function mudar_valor(valor, elemento){
    elemento.innerHTML = valor;
};