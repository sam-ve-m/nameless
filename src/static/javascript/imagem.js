var images_urls = {};

const self_image = document.getElementsByClassName("pearson")[0].getElementsByClassName("perfil")[0];
self_image.classList.add(resource_name+"_perfil_image")


var images_socket = connect_to_socket('ws://localhost:3334/ws/images/'+resource_name, function(event) {
    const images = JSON.parse(event.data);
    for (var image_id in images) {
        const image_url = location.origin+"/"+images[image_id];
        images_urls[image_id] = image_url;
        const image_elements = document.getElementsByClassName(image_id);
        for (var x = 0; x < image_elements.length; x++){
            const image_element = image_elements[x];
            image_element.setAttribute("src", image_url);
        };
    };
});
images_socket.onclose = function(e) {
    images_socket = images_socket.reconnect();
};


function change_image(image_id, content){
    images_socket.send(JSON.stringify({
        "image_id": image_id,
        "content": content
    }));
};

function set_image(character, image_element){
    const image_id = character+"_perfil_image";
    image_element.classList.add(image_id);
    var image_url = images_urls[image_id];
    if (image_url == undefined) {image_url = "https://uploads-ssl.webflow.com/63ef94743451bd743ebebef4/63f24302222b9bae30daeac8_44196.png"};
    image_element.setAttribute("src", image_url);
};
