import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='the URL of the target', required=True)

args = parser.parse_args()


Response = requests.get(args.url)

print (f"Response headers: {Response.headers}")

print (f"Cookies: {Response.cookies.get_dict()}")
