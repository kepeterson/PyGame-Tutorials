import httplib, random, string, urllib, keys

urlString = '/oauth/v2/get_request_token?'

oauth_nonce = 'ce2130523f788f313f76314ed3965ea6'
oauth_timestamp = '1202956957'
oauth_consumer_key = keys.CONSUMER_KEY
oauth_signature_method='plaintext'
#consumer secret (with %26 at end)
oauth_signature=keys.CONSUMER_SECRET
oauth_version='1.0'
xoauth_lang_pref='"en-us"'
oauth_callback = 'oob'

nonce = 'oauth_nonce='+oauth_nonce
timestamp = 'oauth_timestamp='+oauth_timestamp
consumerKey = 'oauth_consumer_key='+oauth_consumer_key
sigMethod = 'oauth_signature_method='+oauth_signature_method
sig = 'oauth_signature='+oauth_signature
version = 'oauth_version='+oauth_version
lang = 'xoauth_lang_pref='+xoauth_lang_pref
callback = 'oauth_callback='+oauth_callback

urlString += nonce+'&'+timestamp+'&'+consumerKey+'&'+sigMethod+'&'\
             +sig+'&'+version+'&'+lang+'&'+callback

domain = "api.login.yahoo.com"
print(domain+urlString)

conn = httplib.HTTPSConnection(domain)
conn.request("GET", urlString)
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()

responses=data1.split('&')

newStr = responses[3].replace('xoauth_request_auth_url=',"")
newStr = urllib.unquote(newStr)

token = responses[0].replace('oauth_token=',"")

tokenSecret = responses[1].replace('oauth_token_secret=',"")

print(newStr)

verifier = raw_input("Input code: ")
verifier = 'oauth_verifier='+verifier
token = 'oauth_token='+token

tokenURL = '/oauth/v2/get_token?'
tokenURL += consumerKey+'&'+sigMethod+'&'+version+'&'+verifier+'&'+token\
           +'&'+timestamp+'&'+nonce+'&'+sig+tokenSecret

conn.request("GET", tokenURL)
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()

print(data1)

API = {'format':'json',
       'view':'compact',
       'oauth_consumer_key':oauth_consumer_key,
       'oauth_nonce':oauth_nonce,
       'oauth_signature_method':'HMAC-SHA1',
       'oauth_timestamp':'1219450170',
       'oauth_token':'PLACEHOLDER',
       'oauth_version':'1.0',
       'oauth_signature':'PLACEHOLDER'}

conn2 = httplib.HTTPConnection(domain)
conn2.request("GET", API, body = None, headers = '')
