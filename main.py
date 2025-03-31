import telebot, time, threading, random
from telebot import types
from chk22 import *
from bin import *

admin_id = '6309252183'
token = "8162909867:AAGOp5nw_d9CMXGrqGS6Zig3XFyXw8m8mKQ"
bot = telebot.TeleBot(token, parse_mode="HTML")

allowed_users = [admin_id]  # قائمة لتخزين معرفات المستخدمين المسموح لهم

# Blacklisted BINs
blacklisted_bins = [
    "423223", "411773", "461046", "440393", "546993",
    "401159", "525346", "475833", "418914", "493728",
    "477213", "401378", "405482", "406068", "456933",
    "459661", "519535", "487917", "596610", "544679",
    "531389", "535925", "539374", "548793", "517040",
    "439701", "520353", "525855", "532775", "534183",
    "520636"
]

video_urls = [
    "https://t.me/O_An6/106",
    "https://t.me/O_An6/110",
    "https://t.me/O_An6/111",
    "https://t.me/O_An6/112",
    "https://t.me/O_An6/113",
    "https://t.me/O_An6/114",
    "https://t.me/O_An6/118",
    "https://t.me/O_An6/119",
    "https://t.me/O_An6/120",
    "https://t.me/O_An6/121",
    "https://t.me/O_An6/123",
    "https://t.me/O_An6/124",
    "https://t.me/O_An6/126",
    "https://t.me/O_An6/129",
    "https://t.me/O_An6/131",
    "https://t.me/O_An6/132",
    "https://t.me/O_An6/133",
    "https://t.me/O_An6/136",
    "https://t.me/O_An6/137",
    "https://t.me/O_An6/208",
    "https://t.me/O_An6/717",
    "https://t.me/O_An6/722"
]

stop_processes = {}

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
    if any(keyword in result for keyword in ['funds', 'OTP', 'Charged', 'Funds', 'INSUFFICIENT_FUNDS', 'postal', 'approved', 'Nice!', 'Approved', 'cvv: Gateway Rejected: cvv', 'does not support this type of purchase.', 'Duplicate', 'Successful', 'Authentication Required', 'successful', 'Thank You For Your Donation', 'confirmed', 'successfully']):
        response = f"𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅\n\n𝐂𝐚𝐫𝐝: <code>{card}</code>\n𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree Charge 🔥\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {result}\n\n𝗜𝗻𝗳𝗼: {brand} - {type} - {level}\n𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} {country_flag}\n\n𝐓𝐢𝐦𝐞: {elapsed_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n𝐁𝐲: <a href='tg://openmessage?user_id=6309252183'>JOO</a>"
    else:
        response = f"𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌\n\n𝐂𝐚𝐫𝐝: <code>{card}</code>\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {result}\n\n𝗜𝗻𝗳𝗼: {brand} - {type} - {level}\n𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} {country_flag}\n\n𝐓𝐢𝐦𝐞: {elapsed_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬"
    
    return response

def process(message):
    bot.send_chat_action(message.chat.id, 'typing')  # إشعار الكتابة
    video_url = random.choice(video_urls)
    process_id = hash(message)
    stop_processes[process_id] = False
    dd = 0
    live = 0
    risko = 0
    blacklisted = 0
    send = bot.send_video(message.chat.id, video_url, caption="𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐂𝐚𝐫𝐝𝐬...⌛", parse_mode='Markdown', reply_to_message_id=message.message_id)
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = f"combo_{message.chat.id}.txt"
    
    try:
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)
    except Exception as o:
        bot.send_message(admin_id, f"An error occurred: {o}")
        return

    with open(file_name, 'r') as file:
        lino = file.readlines()
        total = len(lino)

        for card in lino:
            if stop_processes.get(process_id):
                bot.edit_message_caption(chat_id=message.chat.id, message_id=send.message_id, caption="𝐒𝐭𝐨𝐩𝐩𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲")
                return
                
            card = card.strip()
            if not card:
                continue
                
            # Extract card number (first part before |)
            try:
                card_number = card.split('|')[0].strip()
            except:
                continue
                
            # Check if card is blacklisted
            if is_blacklisted(card_number):
                blacklisted += 1
                buttons = types.InlineKeyboardMarkup(row_width=1)
                a1 = types.InlineKeyboardButton(f"{card}", callback_data='1', align_center=True)
                a2 = types.InlineKeyboardButton(f"BLACKLISTED BIN", callback_data='2')
                a3 = types.InlineKeyboardButton(f"𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅ : {live}", callback_data='3')
                a4 = types.InlineKeyboardButton(f"𝐑𝐢𝐬𝐤 ❌️ : {risko}", callback_data='4')
                a5 = types.InlineKeyboardButton(f"𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌ : {dd}", callback_data='5')
                a6 = types.InlineKeyboardButton(f"𝐁𝐥𝐚𝐜𝐤𝐥𝐢𝐬𝐭𝐞𝐝 ⚠️ : {blacklisted}", callback_data='7')
                a7 = types.InlineKeyboardButton(f"𝐓𝐨𝐭𝐚𝐥 🍬 : {total}", callback_data='6')
                stop_button = types.InlineKeyboardButton("𝐒𝐭𝐨𝐩", callback_data=f'stop_process_{process_id}')
                buttons.add(a1, a2, a3, a4, a5, a6, a7, stop_button)
                bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=send.message_id, reply_markup=buttons)
                continue
                
            bot.send_chat_action(message.chat.id, 'typing')  # إشعار الكتابة قبل كل عملية فحص
            start_time = time.time()
            brand, type, level, bank, country_name, country_flag = info(card)
            try:
                result = chk(card)
            except Exception as e:
                bot.send_message(admin_id, f"An error occurred: {e}")
                result = "ERROR"
            elapsed_time = round(time.time() - start_time, 2)
            print(result)
                
            if any(keyword in result for keyword in ['funds', 'OTP', 'Charged', 'Funds', 'avs', 'postal', 'approved', 'Nice!', 'Approved', 'cvv: Gateway Rejected: cvv', 'does not support this type of purchase.', 'Duplicate', 'Successful', 'Authentication Required', 'successful', 'Thank you', 'confirmed', 'successfully']):
                live += 1
                bot.reply_to(message, f'𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅\n\n𝐂𝐚𝐫𝐝: <code>{card}</code>\n𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree Charge 🔥\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {result}\n\n𝗜𝗻𝗳𝗼: {brand} - {type} - {level}\n𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} {country_flag}\n\n𝐓𝐢𝐦𝐞: {elapsed_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n𝐁𝐲: <a href="tg://openmessage?user_id=6309252183">JOO</a>', parse_mode='HTML')
            elif 'RISK' in result:
                risko +=1
            else:
                dd +=1

            buttons = types.InlineKeyboardMarkup(row_width=1)
            a1 = types.InlineKeyboardButton(f"{card}", callback_data='1', align_center=True)
            a2 = types.InlineKeyboardButton(f"{result}", callback_data='2')
            a3 = types.InlineKeyboardButton(f"𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅ : {live}", callback_data='3')
            a4 = types.InlineKeyboardButton(f"𝐑𝐢𝐬𝐤 ❌️ : {risko}", callback_data='4')
            a5 = types.InlineKeyboardButton(f"𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌ : {dd}", callback_data='5')
            a6 = types.InlineKeyboardButton(f"𝐁𝐥𝐚𝐜𝐤𝐥𝐢𝐬𝐭𝐞𝐝 ⚠️ : {blacklisted}", callback_data='7')
            a7 = types.InlineKeyboardButton(f"𝐓𝐨𝐭𝐚𝐥 🍬 : {total}", callback_data='6')
            stop_button = types.InlineKeyboardButton("𝐒𝐭𝐨𝐩", callback_data=f'stop_process_{process_id}')
            buttons.add(a1, a2, a3, a4, a5, a6, a7, stop_button)
            
            bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=send.message_id, reply_markup=buttons)

            for _ in range(21):
                if stop_processes.get(process_id):
                    bot.edit_message_caption(chat_id=message.chat.id, message_id=send.message_id, caption="𝐒𝐭𝐨𝐩𝐩𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲")
                    return
                time.sleep(1)

    bot.edit_message_caption(chat_id=message.chat.id, message_id=send.message_id, caption="𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲")

@bot.callback_query_handler(func=lambda call: call.data.startswith('stop_process'))
def stop_process_callback(call):
    process_id = call.data.split('_')[-1]
    stop_processes[int(process_id)] = True
    bot.answer_callback_query(call.id, "Process will be stopped.")
    
@bot.message_handler(content_types=["document"])
def main(message):
    if str(message.chat.id) not in allowed_users:  # التحقق إذا كان المستخدم مسموحًا له
        bot.reply_to(message, "You are not authorized to use this bot.")
        return
    threading.Thread(target=process, args=[message]).start()

@bot.message_handler(commands=['start'])
def start_command(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "You are not authorized to use this bot.")
        return   
    video_url = random.choice(video_urls)
    bot.send_video(message.chat.id, video_url, caption="𝐉𝐮𝐬𝐭 𝐬𝐞𝐧𝐝 𝐲𝐨𝐮𝐫 𝐜𝐨𝐦𝐛𝐨", parse_mode='Markdown', reply_to_message_id=message.message_id)

@bot.message_handler(commands=['chk'])
def chk_command(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "You are not authorized to use this bot.")
        return
    
    card_data = message.text.replace('/chk ', '').strip()  # الحصول على بيانات البطاقة من نص الرسالة بعد "/qw"
    
    if '|' in card_data:  # تحقق إذا كانت الرسالة تحتوي على تفاصيل البطاقة
        # First check if card is blacklisted
        card_number = card_data.split('|')[0].strip()
        if is_blacklisted(card_number):
            bot.reply_to(message, "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌\n\n𝐂𝐚𝐫𝐝: <code>{}</code>\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: Blacklisted BIN - Card not checked".format(card_data), parse_mode='HTML')
            return
            
        bot.send_chat_action(message.chat.id, 'typing')  # إشعار الكتابة
        result_message = check_card(card_data, message)  # فحص البطاقة باستخدام الدالة check_card
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
