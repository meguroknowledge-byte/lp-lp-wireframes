# LP Wireframes for GitHub Pages

GitHub Pages 用の LP ワイヤーフレーム置き場です。

## 使い方

1. このフォルダを GitHub リポジトリにします
2. `main` ブランチへ push します
3. GitHub の `Settings > Pages` で:
   Source: `Deploy from a branch`
   Branch: `main`
   Folder: `/ (root)`
4. 数分待つと公開 URL が発行されます

## 現在のページ

- `pages/magma-secret-ticket/`

## 今後 LP を追加する流れ

1. `pages/新しいLP名/` を作る
2. その中に `index.html` と `assets/` を置く
3. ルートの `index.html` にカードを追加する

## 補足

- GitHub Pages ではローカルの `file:///...` は使えないため、画像は各ページの `assets/` に置いて相対パスで参照します
- `_` から始まるファイルやフォルダもそのまま扱えるように `.nojekyll` を置いています
