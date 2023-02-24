var ficha_socket = connect_to_socket('ws://localhost:3334/ws/ficha/'+resource_name, function(event) {
    const jogador = JSON.parse(event.data);
    const atributos = jogador["atributos"];
    for (var atributo_nome in atributos){
        mudar_atributo(atributo_nome, atributos[atributo_nome]);
    };
    atualizaPericias(atributos);
    document.getElementById("defense").innerHTML = jogador["defesa"];
    document.getElementById("movimento").innerHTML = jogador["movimento"];
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
