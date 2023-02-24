function mudar_modificador(modificador_element, mudanca_no_modificador) {
    var modificador;
    if (modificador_element.value != "") {
        modificador = parseInt(modificador_element.value);
    } else {modificador = 0};

    if (isNaN(modificador)) {
        window.location.reload();
    };
    modificador += mudanca_no_modificador;
    if (modificador == 0){
        modificador_element.value = "";
    } else {
        var sinal = "";
        if (modificador > 0) {sinal = "+"};
        modificador_element.value = sinal + modificador;
    };
};

cache_modificacao = {}

function novo_modificador(atributo_element, modificador_novo, origem){
    var cache_modificacao_atributo = cache_modificacao[atributo_element.id];
    if (cache_modificacao_atributo == undefined) {cache_modificacao_atributo = {}};

    var modificador_anterior = cache_modificacao_atributo[origem];
    if (modificador_anterior == undefined) {modificador_anterior = 0};

    const mudanca_no_modificador = modificador_novo - modificador_anterior;
    cache_modificacao_atributo[origem] = modificador_novo;
    cache_modificacao[atributo_element.id] = cache_modificacao_atributo;

    if (mudanca_no_modificador != 0) {
        const modificador_element = atributo_element.getElementsByTagName("input")[0];
        mudar_modificador(modificador_element, mudanca_no_modificador);
    };
};
