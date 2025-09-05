document.addEventListener('DOMContentLoaded', function () {

    let tituloAtualizar = document.querySelector('.jsTituloPostagemA');
    let conteudoAtualizar = document.querySelector('.jsConteudoPostagemA');
    let idAtualizar = document.querySelector('.jsIdPostagemA');
    let idCategoriaAtualizar = document.querySelector('#idCategoria');
    let nomeCategoria = document.querySelector('#nomeCategoria');



    document.addEventListener('click', function (e) {
        const btnAtualizar = e.target.closest('.jsBtnAtualizar');
        if (btnAtualizar) {
            const atualizarPostagem = document.querySelector('#jsAtualizarPostagem');
            atualizarPostagem.classList.toggle('hide');
            idAtualizar.value = btnAtualizar.dataset.id;
            tituloAtualizar.value = btnAtualizar.dataset.titulo;
            conteudoAtualizar.value = btnAtualizar.dataset.conteudo;

        }

        const btnAddComentario = e.target.closest('.jsBtnComentario');
        if (btnAddComentario) {
            const comentario = document.querySelector('#jsAddComentario');
            comentario.classList.toggle('hide');
        }

        const btnCategoriaAtualziar = e.target.closest('.jsCategoriaAtualizar')
        if (btnCategoriaAtualziar) {
            const atualizarCategoria = document.querySelector('#atualizarCategoriajs');
            atualizarCategoria.classList.toggle('hide');

            idCategoriaAtualizar.value = btnCategoriaAtualziar.dataset.id;
            nomeCategoria.value = btnCategoriaAtualziar.dataset.nome;
            console.log(idCategoriaAtualizar);
        }

    })

})



