from twilio.rest import Client
from secret import account_sid, auth_token
def sms(args):
    client = Client(account_sid, auth_token)
    if args is not None and len(args):
        if type(args) != str:
            client.messages.create(to="***REMOVED***", from_="***REMOVED***", body=' '.join(args))
        else:
            client.messages.create(to="***REMOVED***", from_="***REMOVED***", body=args)
    else:
        client.messages.create(to="***REMOVED***", from_="***REMOVED***", body='Job is Done!')

if __name__ == "__main__":
    from sys import argv
    sms(argv[1:])
