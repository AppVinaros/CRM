import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / 'crm.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        origin TEXT,
        status TEXT,
        reason_baja TEXT,
        full_name TEXT,
        dni_nie TEXT,
        emails TEXT,
        province TEXT,
        city TEXT,
        address TEXT,
        postal_code TEXT,
        legal_form TEXT,
        company_name TEXT,
        commercial_name TEXT,
        nif TEXT,
        phones TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS domains (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        domain_name TEXT,
        date_added TEXT,
        type TEXT,
        migration_status TEXT,
        migration_date TEXT,
        server_user TEXT,
        server_password TEXT,
        domain_server TEXT,
        notes TEXT,
        FOREIGN KEY(client_id) REFERENCES clients(id)
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        state TEXT,
        employee TEXT,
        date TEXT,
        contact_name TEXT,
        issue TEXT,
        note TEXT,
        via TEXT,
        additional_notes TEXT,
        FOREIGN KEY(client_id) REFERENCES clients(id)
    )''')
    conn.commit()
    conn.close()


def add_client(**kwargs):
    conn = get_connection()
    c = conn.cursor()
    emails = json.dumps(kwargs.get('emails', []))
    phones = json.dumps(kwargs.get('phones', []))
    c.execute('''INSERT INTO clients (origin, status, reason_baja, full_name, dni_nie, emails,
        province, city, address, postal_code, legal_form, company_name, commercial_name,
        nif, phones) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
        kwargs.get('origin'),
        kwargs.get('status'),
        kwargs.get('reason_baja'),
        kwargs.get('full_name'),
        kwargs.get('dni_nie'),
        emails,
        kwargs.get('province'),
        kwargs.get('city'),
        kwargs.get('address'),
        kwargs.get('postal_code'),
        kwargs.get('legal_form'),
        kwargs.get('company_name'),
        kwargs.get('commercial_name'),
        kwargs.get('nif'),
        phones
    ))
    conn.commit()
    conn.close()


def list_clients():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT id, full_name, company_name FROM clients')
    rows = c.fetchall()
    conn.close()
    return rows


def add_domain(client_id, domain_name, **kwargs):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''INSERT INTO domains (client_id, domain_name, date_added, type, migration_status,
        migration_date, server_user, server_password, domain_server, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
        client_id,
        domain_name,
        kwargs.get('date_added'),
        kwargs.get('type'),
        kwargs.get('migration_status'),
        kwargs.get('migration_date'),
        kwargs.get('server_user'),
        kwargs.get('server_password'),
        kwargs.get('domain_server'),
        kwargs.get('notes')
    ))
    conn.commit()
    conn.close()


def add_ticket(client_id, **kwargs):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''INSERT INTO tickets (client_id, state, employee, date, contact_name,
        issue, note, via, additional_notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
        client_id,
        kwargs.get('state'),
        kwargs.get('employee'),
        kwargs.get('date'),
        kwargs.get('contact_name'),
        kwargs.get('issue'),
        kwargs.get('note'),
        kwargs.get('via'),
        kwargs.get('additional_notes')
    ))
    conn.commit()
    conn.close()


def list_open_tickets():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, client_id, state, note FROM tickets WHERE state != 'Finalizado'")
    rows = c.fetchall()
    conn.close()
    return rows


def search_clients(name=None, company=None, domain=None):
    conn = get_connection()
    c = conn.cursor()
    query = "SELECT DISTINCT clients.id, full_name, company_name FROM clients"
    joins = []
    conditions = []
    params = []
    if domain:
        joins.append("JOIN domains ON domains.client_id = clients.id")
        conditions.append("domains.domain_name LIKE ?")
        params.append(f"%{domain}%")
    if name:
        conditions.append("full_name LIKE ?")
        params.append(f"%{name}%")
    if company:
        conditions.append("company_name LIKE ?")
        params.append(f"%{company}%")
    if joins:
        query += " " + " ".join(joins)
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()
    return rows
