#!/usr/bin/env python
import rethinkdb as r
import os

PROJECT_NAME=os.environ['HORIZON_PROJECT_NAME']

r.connect("rethinkdb", 28015).repl()
r.db_create(PROJECT_NAME).run()
r.db(PROJECT_NAME).table_create("cars", primary_key="car_no").run()
r.db(PROJECT_NAME).table_create("orders").run()
r.db(PROJECT_NAME).table_create("users").run()
r.db(PROJECT_NAME).table_create("hz_collections").run()
r.db(PROJECT_NAME).table_create("hz_groups").run()
r.db(PROJECT_NAME).table_create("hz_users_auth").run()

