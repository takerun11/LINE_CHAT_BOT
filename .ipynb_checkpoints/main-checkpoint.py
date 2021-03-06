import json
from linebot import LineBotApi
from linebot.models import TextSendMessaga 

file = open('info.json', 'r')
info = json.load(file)

CANNNEL_ACCESS_TOKEN = info['CANNNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CANNNEL_ACCESS_TOKEN)

def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text='おはよう')
    line_bot_api.push_message(USER_ID, messages=messages)
    
if __name__ == "__name__":
    main()