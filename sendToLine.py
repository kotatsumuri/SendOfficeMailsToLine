# （1）必要なパッケージをインポート
from linebot import LineBotApi
from linebot.models import TextSendMessage,FileMessage
from linebot.exceptions import LineBotApiError

import csv

from info import getChannelSecret
 
# （2）LINE APIへ接続するための定数を定義。
LINE_CHANNEL_SECRET= getChannelSecret()
 
# LINE APIを定義。引数にアクセストークンを与える。
line_bot_api = LineBotApi(LINE_CHANNEL_SECRET)

def sendToLine(fromName,title,body,hasAttachments):
    with open('uid.csv') as fp:
        reader = csv.reader(fp)
        header = next(reader)
        ulst = []
        for row in reader:
            ulst.append(row[0])
        print(ulst)

    with open('gid.csv') as fp:
        reader = csv.reader(fp)
        header = next(reader)
        glst = []
        for row in reader:
            glst.append(row[0])
        print(glst)

    message = "from:" + fromName + "\n" + "title:" + title + "\n\n" + body
    
    if hasAttachments:
        message = message + "\n\n" + "※添付ファイルあり"
    
    try:
        # ラインユーザIDは配列で指定する。
        line_bot_api.multicast(
            ulst, TextSendMessage(text=message)
        )

        for groupId in glst:
            line_bot_api.push_message(
                groupId, TextSendMessage(text=message)
            )
    except LineBotApiError as e:
        # エラーが起こり送信できなかった場合
        print(e)

if __name__ == '__main__':
    testFrom = "川上　昌汰"
    testTitle = "テスト"
    testBody = "テストメールでございます。"
    hasAttachments = True

    sendToLine(testFrom,testTitle,testBody,hasAttachments)