var message_socket = connect_to_socket('ws://localhost:3334/ws/chat/'+resource_name, function(event) {
    const message_text = JSON.parse(event.data);
    handle_messages(message_text);
    event.preventDefault();
});
message_socket.onclose = function(e) {
    message_socket = message_socket.reconnect();
};


function scroll_bottom() {
    const chat = document.getElementById("message-chat");
    chat.scrollBy(null, chat.scrollHeight);
}

function send_message(){
    const value = document.getElementById("message-to-send").value;
    message_socket.send(value);
    add_message(value, resource_name);
    document.getElementById("message-to-send").value = "";
    scroll_bottom();
}

function add_message(value, sender){
    const image = document.createElement("img");
    const message_text_element = document.createElement("div");
    message_text_element.classList.add("messagetext");

    if (sender == resource_name) {
        message_text_element.classList.add("fromplayer");
        image.classList.add("fromplayer");
    } else {value = "<b>"+sender+"</b>: "+value};
    message_text_element.innerHTML = value;

    const chat = document.getElementById("message-chat");
    if (chat.lastChild != null){
        if (chat.lastChild.classList.contains(sender)){
            if (sender == resource_name) {message_text_element.classList.add("fromplayer")};
            chat.lastChild.appendChild(message_text_element);
            return null;
        }
    }

    const message_element = document.createElement("li");
    message_element.classList.add("message");
    message_element.classList.add(sender);
    image.setAttribute("src", "https://uploads-ssl.webflow.com/63ef94743451bd743ebebef4/63f24302222b9bae30daeac8_44196.png");
    image.setAttribute("loading", "lazy");
    image.setAttribute("height", "30");
    image.setAttribute("alt", "");
    image.classList.add("perfil");
    message_element.appendChild(image);
    message_element.appendChild(message_text_element);

    chat.appendChild(message_element);
    event.preventDefault();
}


var input = document.getElementById("message-to-send");
input.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("send-message").click();
  }
});

function handle_messages(messages){
    messages.forEach((message) => {
        const sender = message["player"];
        const text = message["message"];
        add_message(text, sender);
    });
    scroll_bottom();
};