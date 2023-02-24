var dados_socket = connect_to_socket('ws://localhost:3334/ws/dados/'+resource_name, function(event) {
    const resultado_do_dado = JSON.parse(event.data);
    const message = resultado_do_dado["mensagem"];
    const sender = message["player"];
    const text = message["message"];
    add_message(text, sender);
    scroll_bottom();
    event.preventDefault();
});
dados_socket.onclose = function(e) {
    dados_socket = dados_socket.reconnect();
};


function roll_dice(atributo){
    const atributo_element = document.getElementById(atributo);
    const nome_atributo = atributo_element.getElementsByClassName("attrname")[0].innerHTML;
    const pericia = atributo_element.getElementsByClassName("expertiseselected")[0].innerHTML;
    const modificador = atributo_element.getElementsByClassName("bonus")[0].value;
    const rodar = {
        "atributo": nome_atributo,
        "pericia": pericia,
        "modificador": modificador
    }
    dados_socket.send(JSON.stringify(rodar));
}
