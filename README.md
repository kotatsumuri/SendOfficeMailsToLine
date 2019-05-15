# Send Office Mails To Line

## Send Office Mails To Line is 何 ?

学生メールに届いたクラス当てのメールをLINEのグループトークや個人トークに送信します。

設定したメールアドレス宛にメールが届いていれば**差出人**,**タイトル**,**本文**,**添付ファイルがあるか否か**を以下の様式でLINEBotが送信してくれます。

>from:差出人
>
>title:タイトル
>
>以下本文
>
>...
>
>...
>
>...
>
>...
>
>※添付ファイルがあります。(添付ファイルがある場合)

添付ファイルも送信したかったのですが，残念ながらLINE Messaging APIの仕様上できなかった。(Office 365 APIでは添付ファイルを落とすことが可能)

## 使い方

以下の環境で動作させています。

CentOS7

Python3.6.*

また以下のパッケージを使用してますのでインストールしてください。

```bash
pip install flask
pip install line-bot-api
pip install O365
```

Info.py内にLINEBotの**チャンネルシークレット**,**アクセストークン**,Office 365 APIの**クライアントID**,**クライアントシークレット**を記述してください。

```python
_ChannelSecret = "YourLINE_CHANNEL_SECRET"
_AccessToken = "YourACCESS_TOKEN"

_credentials = ('YourOFFICE_CLIENT_ID','YourCLIENT_SECRET')

_className = "転送したいメールアドレス"

def getChannelSecret():
    return _ChannelSecret

def getAccessToken():
    return _AccessToken

def getCredentials():
    return _credentials

def getClassName():
    return _className
```

Office 365 APIを使用するにはセッティングが必要なため，以下の記事を参考に行ってください。

**PythonのO365パッケージでメール一覧を取得する-Qiita @k8uwall**
https://qiita.com/k8uwall/items/4e98c0b8e615a2e51a79



-----

#####何かあればissueに書くか，直接お願いします。





