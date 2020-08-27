from __future__ import absolute_import
from twilio.rest import Client
from .secret import account_sid, auth_token, to_number, from_number

def send_message(args):
    client = Client(account_sid, auth_token)
    if args is not None and len(args):
        if type(args) != str:
            client.messages.create(to=to_number, from_=from_number, body=' '.join(args))
        else:
            client.messages.create(to=to_number, from_=from_number, body=args)
    else:
        client.messages.create(to=to_number, from_=from_number, body='Job is Done!')

if __name__ == "__main__":
    from sys import argv
    send_message(argv[1:])
