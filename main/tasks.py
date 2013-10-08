#coding=utf8
from celery.task import task
import urllib
from django.core.mail import send_mail

def get_email(url):
    spl = url.split('/')
    email = None

    for res in spl:

        if '@' in res:
            email = res
            return email

    return email


def get_site(url):
    spl = url.split('/')
    site = None
    url_len = 0

    if '@' in url:

        for res in spl:

            if '@' in res:
                break
            else:
                url_len += len(res)+1

        if url_len > 0:
            site = 'http://%s' % url[:url_len]
            return site

    return site

@task
def parse_to_send(url):
    site = get_site(url)
    email = get_email(url)

    if site and email is not None:
        source = urllib.urlopen(site).read()
        send_mail('Site source', source , 'sudohq@gmail.com', [email])
        return True

    else:
        return False




