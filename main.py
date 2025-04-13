import telebot, time, random
from telebot import types
from chk22 import *
from bin import *

admin_id = '6309252183'
token = "7754936482:AAGBhBbwy--kbszpT7og9BarbnrGpc__Kno"
bot = telebot.TeleBot(token, parse_mode="HTML")

allowed_users = [admin_id]  # قائمة لتخزين معرفات المستخدمين المسموح لهم

# Blacklisted BINs
blacklisted_bins = [
    "433333"
]

video_urls = [
    "https://t.me/reeetere/57"
]

def is_blacklisted(card_number):
    """Check if the card's BIN is in the blacklist"""
    for bin_prefix in blacklisted_bins:
        if card_number.startswith(bin_prefix):
            return True
    return False

def check_card(card, message):
    # First check if card is blacklisted
    card_number = card.split('|')[0].strip()
    if is_blacklisted(card_number):
        return "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌\n\n𝐂𝐚𝐫𝐝: <code>{}</code>\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: Blacklisted BIN - Card not checked".format(card)
    
    bot.send_chat_action(message.chat.id, 'typing')  # إشعار الكتابة
    processing_message = bot.send_message(message.chat.id, "Processing your request...😅")  # إرسال رسالة المعالجة
    start_time = time.time()
    brand, type, level, bank, country_name, country_flag = info(card)
    try:
        result = chk(card)
    except Exception as e:
        result = f"Error: {e}"
    elapsed_time = round(time.time() - start_time, 2)
    
    bot.delete_message(message.chat.id, processing_message.message_id)  # حذف رسالة المعالجة
    
    response = ""
    if 'charged' in result.lower():
        response = f"""
𝐂𝐇𝐀𝐑𝐆𝐄𝐃 🌶

𝐂𝐚𝐫𝐝: <code>{card}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: B3 1$
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {result}

𝐈𝐧𝐟𝐨: {brand} - {type} - {level}
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} {country_flag}

𝐓𝐢𝐦𝐞: {elapsed_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬
𝐁𝐲: <a href='tg://openmessage?user_id=6309252183'>JOO</a>
"""
    elif any(keyword in result for keyword in ['funds', 'OTP', 'Charged', 'Funds', 'INSUFFICIENT_FUNDS', 'postal', 'approved', 'Nice!', 'Approved', 'cvv: Gateway Rejected: cvv', 'does not support this type of purchase.', 'Duplicate', 'Successful', 'Authentication Required', 'successful', 'Thank You For Your Donation', 'confirmed', 'successfully']):
        response = f"𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅\n\n𝐂𝐚𝐫𝐝: <code>{card}</code>\n𝐆𝐚𝐭𝐞𝐰𝐚𝐲: B3 1$ 🔥\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {result}\n\n𝗜𝗻𝗳𝗼: {brand} - {type} - {level}\n𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} {country_flag}\n\n𝐓𝐢𝐦𝐞: {elapsed_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n𝐁𝐲: <a href='tg://openmessage?user_id=6309252183'>JOO</a>"
    else:
        response = f"𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌\n\n𝐂𝐚𝐫𝐝: <code>{card}</code>\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {result}\n\n𝗜𝗻𝗳𝗼: {brand} - {type} - {level}\n𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} {country_flag}\n\n𝐓𝐢𝐦𝐞: {elapsed_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬"
    
    return response

@bot.message_handler(commands=['start'])
def start_command(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "You are not authorized to use this bot.")
        return   
    video_url = random.choice(video_urls)
    bot.send_video(message.chat.id, video_url, caption="𝐉𝐮𝐬𝐭 𝐬𝐞𝐧𝐝 𝐲𝐨𝐮𝐫 𝐜𝐚𝐫𝐝 𝐢𝐧 𝐭𝐡𝐞 𝐟𝐨𝐫𝐦𝐚𝐭: number|mm|yy|cvv", parse_mode='Markdown', reply_to_message_id=message.message_id)

@bot.message_handler(commands=['chk'])
def chk_command(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "You are not authorized to use this bot.")
        return
    
    card_data = message.text.replace('/chk ', '').strip()
    
    if '|' in card_data:
        card_number = card_data.split('|')[0].strip()
        if is_blacklisted(card_number):
            bot.reply_to(message, "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌\n\n𝐂𝐚𝐫𝐝: <code>{}</code>\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: Blacklisted BIN - Card not checked".format(card_data), parse_mode='HTML')
            return
            
        bot.send_chat_action(message.chat.id, 'typing')
        result_message = check_card(card_data, message)
        bot.reply_to(message, result_message, parse_mode='HTML')
    else:
        bot.reply_to(message, "Please provide a valid card in the format: number|mm|yy|cvv", parse_mode='HTML')

@bot.message_handler(commands=['add_user'])
def add_user_command(message):
    if str(message.chat.id) != admin_id:
        bot.reply_to(message, "You are not authorized to add users.")
        return
    try:
        new_user_id = message.text.split()[1]
        allowed_users.append(new_user_id)
        bot.reply_to(message, f"User {new_user_id} has been added.")
    except IndexError:
        bot.reply_to(message, "Please provide a valid user ID.")

bot.infinity_polling()
