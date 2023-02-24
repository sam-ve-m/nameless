const resource_name = window.location.pathname.split("/")[2];

function connect_to_socket(url, on_message_function) {
  web_socket = new WebSocket(url);
  web_socket.onmessage = on_message_function;
  web_socket.reconnect = function() {
        var new_websocket = connect_to_socket(url, on_message_function);
        new_websocket.onclose = this.onclose;
        return new_websocket;
  };
  return web_socket
}

//
//var message_socket = connect_to_socket('ws://localhost:3334/ws/message/test', function(event) {
//    const message_text = event.data;
//    const message_element = document.createElement("h3");
//    message_element.innerHTML = message_text;
//    const chat = document.getElementById("box");
//    chat.appendChild(message_element);
////    Array.from(graphs.querySelectorAll("script")).forEach( oldScript => {
////        const newScript = document.createElement("script");
////        Array.from(oldScript.attributes).forEach( attr => newScript.setAttribute(attr.name, attr.value) );
////        newScript.appendChild(document.createTextNode(oldScript.innerHTML));
////        oldScript.parentNode.replaceChild(newScript, oldScript);
////    });
//    event.preventDefault();
//});
//message_socket.onclose = function(e) {
//    message_socket = message_socket.reconnect();
//};
//function send_socket(){
//    const value = document.getElementById("here").value;
//    message_socket.send(value);
//}
