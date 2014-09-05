import httplib, random, string

urlString = '/oauth/v2/get_request_token?'

oauth_nonce = 'ce2130523f788f313f76314ed3965ea6'
oauth_timestamp = '1202956957'
oauth_consumer_key ='dj0yJmk9T1FhTzloOGN1c0FVJmQ9WVdrOWEyRldjRlJZTm1zbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wYw--'
oauth_signature_method='plaintext'
oauth_signature='2384b693f51c3d55d14aba3b7cf6b0067805879d%26'
oauth_version='1.0'
xoauth_lang_pref='"en-us"'
oauth_callback = 'oob'

s1 = 'oauth_nonce='+oauth_nonce
s2 = 'oauth_timestamp='+oauth_timestamp
s3 = 'oauth_consumer_key='+oauth_consumer_key
s4 = 'oauth_signature_method='+oauth_signature_method
s5 = 'oauth_signature='+oauth_signature
s6 = 'oauth_version='+oauth_version
s7 = 'xoauth_lang_pref='+xoauth_lang_pref
s8 = 'oauth_callback='+oauth_callback

urlString += s1+'&'+s2+'&'+s3+'&'+s4+'&'+s5+'&'+s6+'&'+s7+'&'+s8

domain = "api.login.yahoo.com"
print(domain+urlString)

conn = httplib.HTTPSConnection(domain)
conn.request("GET", urlString)
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print(data1)


