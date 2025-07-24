# CRM CLI

Este proyecto proporciona una peque\u00f1a aplicaci\u00f3n en l\u00ednea de comandos para gestionar
clientes, dominios y tickets. Utiliza SQLite y est\u00e1 implementado s\u00f3lo con la
biblioteca est\u00e1ndar de Python.

## Instalaci\u00f3n

No se necesitan dependencias externas. Para inicializar la base de datos ejecute:

```bash
python -m crm_app init
```

## Comandos principales

- `add_client` \u2013 A\u00f1ade un cliente.
- `list_clients` \u2013 Muestra los clientes registrados.
- `add_domain` \u2013 A\u00f1ade un dominio a un cliente.
- `add_ticket` \u2013 Registra un ticket asociado a un cliente.
- `list_tickets` \u2013 Lista los tickets que no est\u00e1n finalizados.
- `search` \u2013 Permite buscar clientes por nombre, empresa o dominio.

Ejemplo de uso para crear un cliente:

```bash
python -m crm_app add_client --full_name "Juan Perez" --company_name "Mi Empresa" \
  --emails juan@ejemplo.com --phones 123456789 --origin App --status Activo
```

Para ver los tickets abiertos:

```bash
python -m crm_app list_tickets
```
