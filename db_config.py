POSTGRES = {
    'user': 'rdquispe',
    'pw': 'espiritumistico',
    'db': 'backend_flask',
    'host': '127.0.0.1',
    'port': '5432',
}

DB_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
