#!/usr/bin/python
import argparse
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
    parser = argparse.ArgumentParser(description='Remove urls from Google using Webmaster Tools',
        add_help=False)
    # required arguments
    required = parser.add_argument_group('required arguments')
    required.add_argument("--login",
        required=True,
        help="Account used to authenticate you on Google Webmaster Tools",
        metavar="john.smith@gmail.com")
    required.add_argument("--password",
        required=True,
        help="Password used with your account",
        metavar="secret")
    required.add_argument("--domain",
        required=True,
        help="Domain to manage",
        metavar="http://example.com")
    required.add_argument("--file",
        required=True,
        help="List of urls",
        metavar="urls.txt")
    # optional arguments
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('-h', '--help',
        action='help',
        help="Show this help message and exit")

    args = parser.parse_args()

    browser = get_browser_instance()
    cj = cookielib.LWPCookieJar()
    browser.set_cookiejar(cj)

    wmt_url = "https://www.google.com/webmasters/tools/url-removal?hl=en&siteUrl=" + args.domain

    response = browser.open(wmt_url)
    browser.select_form(nr=0)
    browser['Email'] = args.login
    response = browser.submit()
    browser.select_form(nr=0)
    browser['Passwd'] = args.password
    response = browser.submit()

    with open(args.file, 'r') as f:
        content = f.read().splitlines()
        for url_to_remove in content:
          delete = "https://www.google.com/webmasters/tools/removals-request?hl=en&siteUrl="+ args.domain + "&urlt=" + args.domain + url_to_remove
          browser.open(delete)
          browser.select_form(nr=0)
          form = browser.form
          form.find_control("removalmethod").get("PAGE").selected=True
          response = browser.submit()
          print "submitted %s, %s" % (url_to_remove,response.code)
          sleep(2)
