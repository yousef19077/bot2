import telebot, time, threading, random, requests
import json
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from telebot import types
from chk22 import *
from bin import *

admin_id = '6309252183'
token = "8162909867:AAGOp5nw_d9CMXGrqGS6Zig3XFyXw8m8mKQ"
bot = telebot.TeleBot(token, parse_mode="HTML")

# تحميل قائمة المستخدمين المسموح لهم من ملف JSON
def load_allowed_users():
    try:
        with open("allowed_users.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # إذا كان الملف غير موجود أو يحتوي على خطأ، نعيد قائمة فارغة

allowed_users = load_allowed_users()

# إضافة دالة لإعادة التشغيل اليدوي
@bot.message_handler(commands=['restart'])
def restart(message):
    if str(message.chat.id) == admin_id:  # التأكد من أن الأمر فقط للمسؤول
        bot.send_message(message.chat.id, "Bot is restarting... 🔄")
        time.sleep(2)  # الانتظار لبضع ثوانٍ قبل إعادة التشغيل
        os.execv(sys.executable, ['python'] + sys.argv)  # إعادة تشغيل البوت
    else:
        bot.send_message(message.chat.id, "You are not authorized to restart the bot.")

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

def check_card(card, message):
    bot.send_chat_action(message.chat.id, 'typing')  # إشعار الكتابة
    processing_message = bot.send_message(message.chat.id, "Processing your request...😅")  # إرسال رسالة المعالجة
    start_time = time.time()
    brand, type, level, bank, country_name, country_flag = info(card)
    try:
        result = vbv(card)
    except Exception as e:
        result = f"Error: {e}"
    elapsed_time = round(time.time() - start_time, 2)
    
    bot.delete_message(message.chat.id, processing_message.message_id)  # حذف رسالة المعالجة
    
    response = ""
    if any(keyword in result for keyword in ['challenge required', 'OTP', 'Charged', 'Challenge Required', 'avs', 'postal', 'approved', 'Nice!', 'Approved', 'cvv: Gateway Rejected: cvv', 'does not support this type of purchase.', 'Duplicate',  'Authentication Required', 'Thank you', 'confirmed']):
        response = f"𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅\n\n𝐂𝐚𝐫𝐝: <code>{card}</code>\n𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree otp 🔥\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {result}\n\n𝗜𝗻𝗳𝗼: {brand} - {type} - {level}\n𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} {country_flag}\n\n𝐓𝐢𝐦𝐞: {elapsed_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n𝐁𝐲: <a href='tg://openmessage?user_id=6309252183'>JOO</a>"
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
            bot.send_chat_action(message.chat.id, 'typing')  # إشعار الكتابة قبل كل عملية فحص
            start_time = time.time()
            brand, type, level, bank, country_name, country_flag = info(card)
            try:
                result = vbv(card)
            except Exception as e:
                bot.send_message(admin_id, f"An error occurred: {e}")
                result = "ERROR"
            elapsed_time = round(time.time() - start_time, 2)
            print(result)
            card = card.replace('\n', '')
                
            if any(keyword in result for keyword in ['Challenge Required', 'OTP', 'Charged', 'Funds', 'challenge required', 'postal', 'approved', 'Nice!', 'Approved', 'cvv: Gateway Rejected: cvv', 'does not support this type of purchase.', 'Duplicate', 'Authentication Required', 'Thank you', 'confirmed']):
                live += 1
                bot.reply_to(message, f'𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅\n\n𝐂𝐚𝐫𝐝: <code>{card}</code>\n𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree otp🔥\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {result}\n\n𝗜𝗻𝗳𝗼: {brand} - {type} - {level}\n𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} {country_flag}\n\n𝐓𝐢𝐦𝐞: {elapsed_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n𝐁𝐲: <a href=\"tg://openmessage?user_id=6309252183\">JOO</a>', parse_mode='HTML')
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
            a6 = types.InlineKeyboardButton(f"𝐓𝐨𝐭𝐚𝐥 🍬 : {total}", callback_data='6')
            stop_button = types.InlineKeyboardButton("𝐒𝐭𝐨𝐩", callback_data=f'stop_process_{process_id}')
            buttons.add(a1, a2, a3, a4, a5, a6, stop_button)
            
            bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=send.message_id, reply_markup=buttons)

            for _ in range(5):
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

    if message.document.mime_type == 'text/plain':
        process(message)

# جعل البوت يعمل باستمرار حتى مع إعادة التشغيل
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)
