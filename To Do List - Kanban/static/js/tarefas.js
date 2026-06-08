// Verifica se o usuário está logado ao carregar o HTML.
if (!localStorage.getItem("token")) {
    window.location.href = "../templates/index.html";
}

// Carrega os dados necessários ao abrir o HTML.
listar_tarefas();
carregar_status_tarefa();


// Função para carregar o select de status de tarefas.
async function carregar_status_tarefa() {

    try {

        // Envia a requisição para o backend.
        const resposta = await fetch("http://127.0.0.1:5000/api/status-tarefa", {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            }
        });

        const dados = await resposta.json();

        // Captura o select de status de tarefas.
        const select = document.getElementById("id-status-tarefa");
        select.innerHTML = `<option value="">Selecione um status</option>`;

        // Preenche o select com os status de tarefas retornados pelo backend.
        dados.forEach(function (status_tarefa) {

            select.innerHTML += `<option value="${status_tarefa.id}">${status_tarefa.nome}</option>`;

        });

    } catch {

        console.error("Não foi possível carregar os status de tarefas...");

    }

}


// Função para salvar uma nova tarefa.
async function salvar_tarefa() {

    // Captura os dados do formulário.
    const titulo = document.getElementById("titulo").value;
    const descricao = document.getElementById("descricao").value;
    const id_status_tarefa = document.getElementById("id-status-tarefa").value;
    const mensagem = document.getElementById("mensagem");

    // Extrai o ID do usuário logado a partir do token.
    const payload = JSON.parse(atob(localStorage.getItem("token").split(".")[1]));
    const id_usuario = payload.sub;

    try {

        // Envia os dados para o backend.
        const resposta = await fetch("http://127.0.0.1:5000/api/tarefas", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            },
            body: JSON.stringify({ titulo, descricao, id_usuario, id_status_tarefa })
        });

        const dados = await resposta.json();

        // Verifica se o cadastro foi bem-sucedido.
        if (resposta.ok) {

            // Exibe a mensagem de sucesso e limpa o formulário.
            mensagem.className = "alert alert-success";
            mensagem.textContent = dados.mensagem;
            cancelar();
            listar_tarefas();

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


// Função para listar todas as tarefas na tabela.
async function listar_tarefas() {

    try {

        // Envia a requisição para o backend.
        const resposta = await fetch("http://127.0.0.1:5000/api/tarefas", {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            }
        });

        const dados = await resposta.json();

        // Captura o corpo da tabela.
        const tabela = document.getElementById("tabela-tarefas");
        tabela.innerHTML = "";

        // Preenche a tabela com as tarefas retornadas pelo backend.
        dados.forEach(function (tarefa) {

            tabela.innerHTML += `
                <tr>
                    <td>${tarefa.titulo}</td>
                    <td>${tarefa.nome_status_tarefa}</td>
                    <td>${tarefa.descricao || "—"}</td>
                    <td>—</td>
                    <td>${tarefa.criado_em}</td>
                    <td>
                        <button class="btn btn-sm btn-warning">Editar</button>
                        <button class="btn btn-sm btn-danger">Excluir</button>
                    </td>
                </tr>
            `;

        });

    } catch {

        console.error("Não foi possível carregar as tarefas...");

    }

}


// Função para cancelar e limpar o formulário.
function cancelar() {

    // Limpa todos os campos do formulário.
    document.getElementById("id-tarefa").value = "";
    document.getElementById("titulo").value = "";
    document.getElementById("descricao").value = "";
    document.getElementById("id-status-tarefa").value = "";
    document.getElementById("arquivo").value = "";

}