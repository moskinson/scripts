import mechanize
import time
from urlparse import urlparse
import cookielib
import urllib2
from time import sleep


def get_browser_instance():
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.addheaders = [('User-agent', 'Mozilla/5.0 Compatible')]
        browser.set_handle_redirect(True)

        return browser


if __name__ == '__main__':

    browser = get_browser_instance()
    cj = cookielib.LWPCookieJar()
    browser.set_cookiejar(cj)

    google_user = "email"
    google_password = "password"
    wmt_domain_to_manage = "http://www.mydomain.com/"
    wmt_url = "https://www.google.com/webmasters/tools/url-removal?hl=en&siteUrl=" + wmt_domain_to_manage

    response = browser.open(wmt_url)
    browser.select_form(nr=0)
    browser['Email'] = google_user
    browser['Passwd'] = google_password
    response = browser.submit()

    file_with_url = open("urls_to_remove.wmt_test")
    urls_to_remove = file_with_url.readlines().pop().split(" ")
    file_with_url.close()

    for url_to_remove in urls_to_remove:
        borrar = "https://www.google.com/webmasters/tools/removals-request?hl=en&siteUrl="+ wmt_domain_to_manage + "&urlt=https://www.unience.com" + url_to_remove
        browser.open(borrar)
        browser.select_form(nr=0)
        form = browser.form
#        form.find_control("removalmethod").get("PAGE_CACHE").selected=True
        response = browser.submit()
        print "submitted %s, %s" % (url_to_remove,response.code)
        sleep(2)


