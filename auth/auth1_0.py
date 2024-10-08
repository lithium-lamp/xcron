import time
import random
import hmac
import hashlib
import base64
import urllib.parse
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--envpath', action="store", dest='envpath', default='')
parser.add_argument('--crudtype', action="store", dest='crudtype', default='')
parser.add_argument('--baseurl', action="store", dest='baseurl', default='')
parser.add_argument('--token', action="store", dest='token', default='')
parser.add_argument('--accesstoken', action="store", dest='accesstoken', default='')
parser.add_argument('--tokensecret', action="store", dest='tokensecret', default='')
parser.add_argument('--accesstokensecret', action="store", dest='accesstokensecret', default='')
parser.add_argument('--variablename', action="store", dest='variablename', default='')

args = parser.parse_args()

# Timestamp and Nonce
TIMESTAMP = str(int(time.time()))
NONCE = ''.join([chr(random.randint(97, 122)) for i in range(32)])

# HMAC-SHA1 as the signature method
HMAC_METHOD = "HMAC-SHA1"
OAUTH_VERSION = "1.0"

# Twitter API endpoint
URL = args.baseurl

# Function to percent-encode parameters
def percent_encode(s):
    return urllib.parse.quote(s, safe='')

# Create the base string for signing
def create_base_string(method, url, params):
    # Sort the parameters
    sorted_params = '&'.join([f'{percent_encode(k)}={percent_encode(v)}' for k, v in sorted(params.items())])
    
    # Construct the base string
    base_string = f"{method.upper()}&{percent_encode(url)}&{percent_encode(sorted_params)}"
    return base_string

# Create the signing key
def create_signing_key(consumer_secret, token_secret):
    return f"{percent_encode(consumer_secret)}&{percent_encode(token_secret)}"

# Generate the HMAC-SHA1 signature
def generate_signature(base_string, signing_key):
    hashed = hmac.new(signing_key.encode(), base_string.encode(), hashlib.sha1)
    signature = base64.b64encode(hashed.digest()).decode()
    return signature

oauth_params = {
    'oauth_consumer_key': args.token,
    'oauth_token': args.accesstoken,
    'oauth_signature_method': HMAC_METHOD,
    'oauth_timestamp': TIMESTAMP,
    'oauth_nonce': NONCE,
    'oauth_version': OAUTH_VERSION,
}

base_string = ""

if args.crudtype == "POST":
    base_string = create_base_string(args.crudtype, URL, oauth_params)
elif args.crudtype == "DELETE":
    base_string = create_base_string(args.crudtype, URL, oauth_params)
elif args.crudtype == "UPDATE":
    base_string = create_base_string(args.crudtype, URL, oauth_params)
elif args.crudtype == "GET":
    base_string = create_base_string(args.crudtype, URL, oauth_params)
else:
    print("Invalid crudtype ", args.crudtype)
    exit(1)

signing_key = create_signing_key(args.tokensecret, args.accesstokensecret)

OAUTH_SIGNATURE = generate_signature(base_string, signing_key)

oauth_params['oauth_signature'] = OAUTH_SIGNATURE

authorization_header = (
    'OAuth ' +
    ', '.join([f'{percent_encode(k)}="{percent_encode(v)}"' for k, v in oauth_params.items()])
)

f = open(f"{args.envpath}", "w")
f.write(f"{args.variablename} = '{authorization_header}'")
f.close()