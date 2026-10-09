function gerarEstrelas(qtd) {
    let sombras = [];
    for (let i = 0; i < qtd; i++) {
        const x = Math.floor(Math.random() * 2000);
        const y = Math.floor(Math.random() * 2000);
        sombras.push(`${x}px ${y}px #FFF`);
    }
    return sombras.join(', ');
}

document.getElementById('stars').style.boxShadow = gerarEstrelas(500);
document.getElementById('stars2').style.boxShadow = gerarEstrelas(150);
document.getElementById('stars3').style.boxShadow = gerarEstrelas(70);

document.querySelectorAll('.project-modal').forEach(modal => {
    const iframe = modal.querySelector('iframe');
    if (!iframe) return; // modal sem vídeo

    modal.addEventListener('show.bs.modal', () => {
        iframe.src = iframe.dataset.src;
    });

    modal.addEventListener('hidden.bs.modal', () => {
        iframe.src = '';
    });
});