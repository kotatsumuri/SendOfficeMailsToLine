from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FollowEvent,UnfollowEvent,JoinEvent,LeaveEvent
)

import csv
import pandas as pd
from info import getAccessToken,getChannelSecret

app = Flask(__name__)

line_bot_api = LineBotApi(getChannelSecret())
handler = WebhookHandler(getAccessToken())


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    #app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


'''
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
'''

@handler.add(FollowEvent)
def handle_follow(event):
    f = open('uid.csv','a')
    userId = event.source.user_id
    print(userId)
    print(userId,file = f)
    f.close()

@handler.add(UnfollowEvent)
def handle_unFolow(event):
    df = pd.read_csv('uid.csv',index_col=0)
    userId = event.source.user_id
    print(userId)
    print(df)
    df_new = df.drop(index = [userId])
    print(df_new)
    df_new.to_csv('uid.csv')

@handler.add(JoinEvent)
def handle_Join(event):
    f = open('gid.csv','a')
    groupId = event.source.group_id
    print(groupId,file = f)
    f.close()

@handler.add(LeaveEvent)
def handle_Leave(event):
    df = pd.read_csv('gid.csv',index_col=0)
    groupId = event.source.group_id
    df_new = df.drop(index = [groupId])
    df_new.to_csv('gid.csv')

if __name__ == "__main__":
    app.run()