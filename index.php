<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRM</title>
    <link rel="stylesheet" href="public/css/style.css">
</head>
<body>
    <header>
        <h1>CRM</h1>
        <input type="text" id="search" placeholder="Buscar clientes...">
    </header>
    <nav>
        <button data-tab="clientes">Clientes</button>
        <button data-tab="tickets">Tickets abiertos</button>
        <button data-tab="calendario">Calendario de renovaciones</button>
        <button data-tab="migraciones">Migraciones</button>
    </nav>
    <main>
        <section id="clientes" class="tab">
            <h2>Clientes</h2>
            <div id="cliente-list"></div>
        </section>
        <section id="tickets" class="tab" hidden>
            <h2>Tickets abiertos</h2>
            <div id="ticket-list"></div>
        </section>
        <section id="calendario" class="tab" hidden>
            <h2>Calendario de renovaciones</h2>
            <div id="calendario-list"></div>
        </section>
        <section id="migraciones" class="tab" hidden>
            <h2>Migraciones</h2>
            <div id="migraciones-list"></div>
        </section>
    </main>
    <script src="public/js/app.js"></script>
</body>
</html>
