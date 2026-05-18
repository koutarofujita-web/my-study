# DAY4: nginxでオリジナルホームページを作成

nginxのデフォルト設定をカスタマイズし、自分で作成したオリジナルのHTML/CSSコードをWebサーバーから配信する実験を行いました。

## 実際に作成したHTML/CSSコード

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ようこそNginxへ！</title>
    <style>
        body {
            font-family: sans-serif;
            text-align: center;
            padding-top: 50px;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.1em;
            color: #333;
            line-height: 1.6;
            max-width: 600px;
            margin: 10px auto;
            text-align: left;
        }
        a {
            color: #0066cc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <h1>こんにちは、コウタの世界！</h1>

    <p>このページを見れば、nginxは正常にインストールされて動作しています。ウェブサーバー、リバースプロキシについてはさらに設定が必要です。APIゲートウェイ、ロードバランサー、コンテンツキャッシュ、その他の機能。</p>

</body>
</html>
