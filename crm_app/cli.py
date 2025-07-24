import argparse
import json
from datetime import datetime
from . import database as db


def cmd_init(args):
    db.init_db()
    print("Database initialized")


def cmd_add_client(args):
    emails = args.emails.split(',') if args.emails else []
    phones = args.phones.split(',') if args.phones else []
    db.add_client(
        origin=args.origin,
        status=args.status,
        reason_baja=args.reason_baja,
        full_name=args.full_name,
        dni_nie=args.dni_nie,
        emails=emails,
        province=args.province,
        city=args.city,
        address=args.address,
        postal_code=args.postal_code,
        legal_form=args.legal_form,
        company_name=args.company_name,
        commercial_name=args.commercial_name,
        nif=args.nif,
        phones=phones
    )
    print("Client added")


def cmd_list_clients(args):
    rows = db.list_clients()
    for r in rows:
        print(r)


def cmd_search(args):
    rows = db.search_clients(name=args.name, company=args.company, domain=args.domain)
    for r in rows:
        print(r)


def cmd_add_domain(args):
    db.add_domain(
        client_id=args.client_id,
        domain_name=args.domain_name,
        date_added=args.date_added or datetime.now().strftime('%Y-%m-%d'),
        type=args.type,
        migration_status=args.migration_status,
        migration_date=args.migration_date,
        server_user=args.server_user,
        server_password=args.server_password,
        domain_server=args.domain_server,
        notes=args.notes
    )
    print("Domain added")


def cmd_add_ticket(args):
    db.add_ticket(
        client_id=args.client_id,
        state=args.state,
        employee=args.employee,
        date=args.date or datetime.now().strftime('%Y-%m-%d'),
        contact_name=args.contact_name,
        issue=args.issue,
        note=args.note,
        via=args.via,
        additional_notes=args.additional_notes
    )
    print("Ticket added")


def cmd_list_tickets(args):
    rows = db.list_open_tickets()
    for r in rows:
        print(r)


parser = argparse.ArgumentParser(description='Simple CRM CLI')
subparsers = parser.add_subparsers(dest='command')

p_init = subparsers.add_parser('init')
p_init.set_defaults(func=cmd_init)

p_add_client = subparsers.add_parser('add_client')
p_add_client.add_argument('--origin')
p_add_client.add_argument('--status')
p_add_client.add_argument('--reason_baja')
p_add_client.add_argument('--full_name')
p_add_client.add_argument('--dni_nie')
p_add_client.add_argument('--emails')
p_add_client.add_argument('--province')
p_add_client.add_argument('--city')
p_add_client.add_argument('--address')
p_add_client.add_argument('--postal_code')
p_add_client.add_argument('--legal_form')
p_add_client.add_argument('--company_name')
p_add_client.add_argument('--commercial_name')
p_add_client.add_argument('--nif')
p_add_client.add_argument('--phones')
p_add_client.set_defaults(func=cmd_add_client)

p_list_clients = subparsers.add_parser('list_clients')
p_list_clients.set_defaults(func=cmd_list_clients)

p_search = subparsers.add_parser('search')
p_search.add_argument('--name')
p_search.add_argument('--company')
p_search.add_argument('--domain')
p_search.set_defaults(func=cmd_search)

p_add_domain = subparsers.add_parser('add_domain')
p_add_domain.add_argument('client_id', type=int)
p_add_domain.add_argument('domain_name')
p_add_domain.add_argument('--date_added')
p_add_domain.add_argument('--type')
p_add_domain.add_argument('--migration_status')
p_add_domain.add_argument('--migration_date')
p_add_domain.add_argument('--server_user')
p_add_domain.add_argument('--server_password')
p_add_domain.add_argument('--domain_server')
p_add_domain.add_argument('--notes')
p_add_domain.set_defaults(func=cmd_add_domain)

p_add_ticket = subparsers.add_parser('add_ticket')
p_add_ticket.add_argument('client_id', type=int)
p_add_ticket.add_argument('--state')
p_add_ticket.add_argument('--employee')
p_add_ticket.add_argument('--date')
p_add_ticket.add_argument('--contact_name')
p_add_ticket.add_argument('--issue')
p_add_ticket.add_argument('--note')
p_add_ticket.add_argument('--via')
p_add_ticket.add_argument('--additional_notes')
p_add_ticket.set_defaults(func=cmd_add_ticket)

p_list_tickets = subparsers.add_parser('list_tickets')
p_list_tickets.set_defaults(func=cmd_list_tickets)


def main():
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
