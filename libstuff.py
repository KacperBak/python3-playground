import requests


def post_to_mailgun_api():
    sandbox= "sandboxe1234567890.mailgun.org"

    # email data
    email_from = """node 'host_name' <postmaster@{sandbox}>""".format(sandbox=sandbox)
    email_to = "Kacper Bak <test@kacperbak.de>"
    email_subject = "test"
    email_text = "text text text"
    payload = { "from": email_from, "to": email_to, "subject": email_subject, "text": email_text }

    # api
    key = "key-asdf1234asdf1234"
    url = """https://api.mailgun.net/v3/{sandbox}/messages""".format(sandbox=sandbox)
    r = requests.post(url, auth=('api', key), data=payload)
    print(r)