document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('nav button');
    const sections = document.querySelectorAll('main .tab');
    const searchInput = document.getElementById('search');

    // Switch tabs
    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const tab = btn.getAttribute('data-tab');
            sections.forEach(sec => {
                sec.hidden = sec.id !== tab;
            });
        });
    });

    // Load client data
    fetch('php/get_clients.php')
        .then(res => res.json())
        .then(data => {
            window.clients = data.clients;
            renderClients(data.clients);
        });

    // Search functionality
    searchInput.addEventListener('input', () => {
        const term = searchInput.value.toLowerCase();
        const filtered = window.clients.filter(c =>
            c.nombre.toLowerCase().includes(term) ||
            c.empresa.toLowerCase().includes(term) ||
            c.dominios.some(d => d.nombre.toLowerCase().includes(term))
        );
        renderClients(filtered);
    });
});

function renderClients(list) {
    const container = document.getElementById('cliente-list');
    container.innerHTML = '';
    list.forEach(cliente => {
        const div = document.createElement('div');
        div.className = 'cliente';
        div.innerHTML = `
            <h3>${cliente.nombre} (${cliente.empresa})</h3>
            <p>Dominios: ${cliente.dominios.map(d => d.nombre).join(', ')}</p>
        `;
        container.appendChild(div);
    });
}
