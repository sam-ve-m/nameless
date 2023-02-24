function closeAllSelect(element) {
    var visible_dropdowns = document.getElementsByClassName("dropdown");
    var visible_dropdowns_length = visible_dropdowns.length;
    for (var i = 0; i < visible_dropdowns_length; i++) {
        var visible_dropdown = visible_dropdowns[i];
        if (element != visible_dropdown) {
            visible_dropdown.classList.add("hide-dropdown")
        };
    };
};

function atualizaPericias(atributos) {
    for(var atributo in atributos){
        const atributo_element = document.getElementById(atributo);

        const pericias_controle = document.createElement("select");
        pericias_controle.setAttribute("style", "display: none;");

        const pericia_selecionada = document.createElement("div");
        pericia_selecionada.setAttribute("class", "expertiseselected");
        pericia_selecionada.setAttribute("style", "cursor: pointer;");

        const pericias_box = document.createElement("div");
        pericias_box.setAttribute("class", "dropdown expertskills hide-dropdown");

        var pericias = atributos[atributo]["pericias"];
        if (pericias == undefined) {pericias = []};
        var posicao_da_pericia = 0;

        for (var pericia in pericias) {
            const posicao_dessa_pericia = posicao_da_pericia;
            posicao_da_pericia++;

            const id_da_pericia = pericias[pericia]["id"];
            const nome_da_pericia = pericias[pericia]["nome"];
            const modificador_da_pericia = pericias[pericia]["modificador"];

            const pericia_element = document.createElement("div");
            pericia_element.setAttribute("class", "expertskill "+atributo+"color");
            pericia_element.setAttribute("style", "cursor: pointer;");
            pericia_element.innerHTML = nome_da_pericia;
            pericia_element.addEventListener("click", function(e) {
                novo_modificador(atributo_element, modificador_da_pericia, "pericia");
                destaca_pericia(pericias_controle, pericias_box, pericia_selecionada, posicao_dessa_pericia);
            });

            pericias_box.appendChild(pericia_element);

            const pericia_controle_element = document.createElement("option");
            pericia_controle_element.setAttribute("value", id_da_pericia);
            pericia_controle_element.innerHTML = nome_da_pericia;

            pericias_controle.appendChild(pericia_controle_element);
        }
        pericia_selecionada.addEventListener("click", function(event) {
            event.stopPropagation();
            closeAllSelect(pericias_box);
            pericias_box.classList.toggle("hide-dropdown");
        });

        const pericias_element_wrapper = atributo_element.getElementsByClassName("expertise")[0];
        novo_modificador(atributo_element, 0, "pericia")
        while (pericias_element_wrapper.children.length != 0) {
            pericias_element_wrapper.removeChild(pericias_element_wrapper.children[0]);
        };

        pericias_element_wrapper.appendChild(pericias_controle);
        pericias_element_wrapper.appendChild(pericia_selecionada);
        pericias_element_wrapper.appendChild(pericias_box);

        var ultima_pericia_selecionada = atributos[atributo]["ultima_pericia_selecionada"];
        if (ultima_pericia_selecionada == undefined) {ultima_pericia_selecionada = -1};
        pericias_controle.selectedIndex = ultima_pericia_selecionada;
        pericias_box.children[0].click();
    };
};
document.addEventListener("click", closeAllSelect);
