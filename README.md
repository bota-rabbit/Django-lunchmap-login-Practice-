# 🥗 Django LunchMap Login Practice

PAIZAラーニングで学んだ、Django を使ってランチのお店を地図上に表示する練習プロジェクトです。  
ログイン機能を備え、ユーザーごとにお気に入りの店舗を記録できます。  
データを触りながら、Webアプリの動作・UI・認証の流れを理解するための作品です。

---

## 🔥 主なポイント

- Django 認証機能（login / logout / signup）
- 店舗の登録・編集・削除
- ログインユーザーごとのデータ管理  
- Map表示は **API使用をやめ、iFrameベースに変更**  APIはお金かかるし……
- UIは **Bootstrap5にアップグレード済み**

---

## 🧪 使用技術

| カテゴリ | 使用技術 |
|---|---|
| Backend | Django / Python |
| Frontend | **Bootstrap5** / HTML / CSS |
| Map表示 | Google Map iFrame 埋め込み |
| DB | SQLite (デフォルト) |

---

## 📂 機能

- ユーザー登録 & ログイン必須
- 飲食店データの新規追加 / 編集 / 削除
- マップでの位置確認（iFrame）
- UIをBootstrap5化し、表示を調整

```bash
python manage.py runserver
