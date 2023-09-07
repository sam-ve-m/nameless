var visible_characters_socket = connect_to_socket('ws://localhost:3334/ws/visible_characters/'+resource_name, function(event) {
    const visible_characters_ids = JSON.parse(event.data);
    const visible_characters = document.getElementById("visible-characters")
    while (visible_characters.children.length != 0) {
        visible_characters.removeChild(visible_characters.children[0]);
    };
    for (var i in visible_characters_ids) {
        const character_id = visible_characters_ids[i];
        const character_element = document.createElement("img");
        character_element.setAttribute("height", "30");
        character_element.classList.add("bigperfil");
        character_element.classList.add(character_id);
        set_image(character_id, character_element);
        visible_characters.appendChild(character_element);
    };
    event.preventDefault();
});
visible_characters_socket.onclose = function(e) {
    visible_characters_socket = visible_characters_socket.reconnect();
};
