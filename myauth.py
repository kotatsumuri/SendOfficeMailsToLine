from O365 import Account

credentials = ('af50de44-9a4d-4d68-b7ed-e7ce28810582','W[+.nA7nq0MB0.Ach9-u1JjQqLN/UGEV')
account = Account(credentials)
account.authenticate(scopes = ['basic','message_all'])

