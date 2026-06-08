// Verifica se o usuário está logado ao carregar o HTML.
if (!localStorage.getItem("token")) {
    window.location.href = "../templates/index.html";
}

// Carrega a lista de status de tarefas ao abrir o HTML.
listar_status_tarefa();


// Função para salvar um novo status de tarefa.
async function salvar_status_tarefa() {

    // Captura os dados do formulário.
    const nome = document.getElementById("nome").value;
    const mensagem = document.getElementById("mensagem");

    try {

        // Envia os dados para o backend.
        const resposta = await fetch("http://127.0.0.1:5000/api/status-tarefa", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            },
            body: JSON.stringify({ nome })
        });

        const dados = await resposta.json();

        // Verifica se o cadastro foi bem-sucedido.
        if (resposta.ok) {

            // Exibe a mensagem de sucesso e limpa o formulário.
            mensagem.className = "alert alert-success";
            mensagem.textContent = dados.mensagem;
            cancelar();
            listar_status_tarefa();

            setTimeout(function () {
                mensagem.className = "";
                mensagem.textContent = "";
            }, 4000);

        } else {

            // Exibe a mensagem de erro retornada pelo backend.
            mensagem.className = "alert alert-danger";
            mensagem.textContent = dados.erro;

            setTimeout(function () {
                mensagem.className = "";
                mensagem.textContent = "";
            }, 4000);

        }

    } catch {

        // Exibe a mensagem de erro caso o backend não esteja disponível.
        mensagem.className = "alert alert-warning";
        mensagem.textContent = "Não foi possível atender sua requisição no momento. Tente mais tarde...";

        setTimeout(function () {
            mensagem.className = "";
            mensagem.textContent = "";
        }, 4000);

    }

}


// Função para listar todos os status de tarefas na tabela.
async function listar_status_tarefa() {

    try {

        // Envia a requisição para o backend.
        const resposta = await fetch("http://127.0.0.1:5000/api/status-tarefa", {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            }
        });

        const dados = await resposta.json();

        // Captura o corpo da tabela.
        const tabela = document.getElementById("tabela-status-tarefa");
        tabela.innerHTML = "";

        // Preenche a tabela com os status de tarefas retornados pelo backend.
        dados.forEach(function (status_tarefa) {

            tabela.innerHTML += `
                <tr>
                    <td>${status_tarefa.nome}</td>
                    <td>
                        <button class="btn btn-sm btn-warning">Editar</button>
                        <button class="btn btn-sm btn-danger">Excluir</button>
                    </td>
                </tr>
            `;

        });

    } catch {

        console.error("Não foi possível carregar os status de tarefas...");

    }

}


// Função para cancelar e limpar o formulário.
function cancelar() {

    // Limpa todos os campos do formulário.
    document.getElementById("id-status-tarefa").value = "";
    document.getElementById("nome").value = "";

}