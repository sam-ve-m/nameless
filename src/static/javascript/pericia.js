function destaca_pericia (pericias_controle, pericias_box, pericia_selecionada, posicao_dessa_pericia) {
    const elemento_destacado = pericias_box.children[pericias_controle.selectedIndex];
    if (elemento_destacado != undefined){
        elemento_destacado.classList.remove("bold-text");
    };
    pericias_box.children[posicao_dessa_pericia].classList.add("bold-text");

    pericias_controle.selectedIndex = posicao_dessa_pericia;
    pericia_selecionada.innerHTML = pericias_controle.options[posicao_dessa_pericia].innerHTML;
    pericia_selecionada.click();
};
