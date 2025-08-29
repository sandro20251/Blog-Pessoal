document.addEventListener('DOMContentLoaded', function () {

    let tituloAtualizar = document.querySelector('.jsTituloPostagemA');
    let categoriaAtualizar = document.querySelector('.jsCategoriaPostagemA');
    let conteudoAtualizar = document.querySelector('.jsConteudoPostagemA');
    let idAtualizar = document.querySelector('.jsIdPostagemA')
    document.addEventListener('click', function (e) {
        const btnAtualizar = e.target.closest('.jsBtnAtualizar');
        if (btnAtualizar) {
            const atualizarPostagem = document.querySelector('#jsAtualizarPostagem');
            atualizarPostagem.classList.toggle('hide');
            idAtualizar.value = btnAtualizar.dataset.id;
            tituloAtualizar.value = btnAtualizar.dataset.titulo;
            categoriaAtualizar.value = btnAtualizar.dataset.categoria;
            conteudoAtualizar.value = btnAtualizar.dataset.conteudo;

        }
    })
})



