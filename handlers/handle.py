from telebot import TeleBot
from telebot.types import Message
def message_handl(message:Message,bot:TeleBot):
    try:
        jsot=message.text.split('\n')
        print(jsot)
        data={
            'dat':jsot[0],
            'pair':jsot[2].split(":")[1],
            'type':jsot[3],
            'leverage':jsot[4].split(":")[1],
            'entry':jsot[5].split(":")[1],
            'targets':[float(jsot[7].split(":")[1]),float(jsot[8].split(":")[1]),float(jsot[9].split(":")[1]),float(jsot[10].split(":")[1]),float(jsot[11].split(":")[1]),float(jsot[12].split(":")[1]),float(jsot[13].split(":")[1])],
            'stoploss':jsot[15].split(":")[1]
            }
        print(data)
    except :
        return'not suitable formate'
    leverage=data['leverage'].split(" ")
    print(leverage[0])
    entry=data['entry'].split("-")
    pair=data['pair'][0:-5]
    try:
        if data['type']=="LONG":
            message1=f"✨{pair}/USDT\n\n🎗 Trade Type = {data['type']} 🟢\n\n💫 Leverage :- {leverage[2]}\n\n⚡️ Entry = [ {entry[0]} TO {entry[1] }]\n\n❌ StopLoss :- {data['stoploss']}\n\n❎ Take profit = [ {data['targets'][0]}, {data['targets'][1]} , {data['targets'][2]} , {data['targets'][3]} , {data['targets'][4]} , {data['targets'][5]} , {data['targets'][6]} ]"
        else:
            message1=f"✨{pair}/USDT\n\n🎗 Trade Type = {data['type']} 🔴\n\n💫 Leverage :- {leverage[2]}\n\n⚡️ Entry=[ {entry[0]} TO {entry[1] }]\n\n❌ StopLoss= {data['stoploss']}\n\n❎ Take profit=[ {data['targets'][0]}, {data['targets'][1]} {data['targets'][2]} {data['targets'][3]} {data['targets'][4]} {data['targets'][5]} {data['targets'][6]} ]"
    except Exception as e:
        print(e)
    try:
        message2=f"📍 {data['pair']}\n\n🏹 Signal Type:- {data['type']}\n\n💫Leverage: {data['leverage']}\n\n👉 Entry Targets:- {data['entry']}\n\n🎯 Profit Targets:\n1) {data['targets'][0]}\n2) {data['targets'][1]}\n3) {data['targets'][2]}\n4) {data['targets'][3]}\n5) {data['targets'][4]}\n6) {data['targets'][5]}\n7) {data['targets'][6]}\n\n🛑 Stop Target: {data['stoploss']} "
    except Exception as e:
        print(e)
    try:
        message3=f"⚡️💫 {data['pair']} 💫⚡️\n\n[{data['type']}]:{data['entry']}\n\n✨🎯 TARGETS ✨🎯\n\n1.Goal👉 {data['targets'][0]}\n2.Goal👉 {data['targets'][1]}\n3.Goal👉 {data['targets'][2]}\n4.Goal👉 {data['targets'][3]}\n5.Goal👉 {data['targets'][4]}\n6.Goal👉 {data['targets'][5]}\n7.Goal👉 {data['targets'][6]}\n\nSL🛑:- {data['stoploss']}\n\n🎗 LEVERAGE:- {data['leverage']}"
        
    except Exception as e:
        print(e)
    messages=[message1,message2,message3]
    for mese in messages:
        try:
            bot.send_message(message.chat.id,text=mese)
        except Exception as e:
            print(e)
