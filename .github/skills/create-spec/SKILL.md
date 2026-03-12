---
name: spec-review
description: 仕様検討・要件整理を行うスキル。PBI_ISSUE_TEMPLATEに沿ってdocs/配下にmdファイルを作成する
---

## 概要

このスキルを使って、新機能の仕様検討・要件整理を **planMode** で対話形式に進めます。
`.github/ISSUE_TEMPLATE/PBI_ISSUE_TEMPLATE.md` のフォーマットを参照しながら `plan.md` に整理し、
確定後に `docs/{PBI名}.md` として保存します。

ISSUEの作成・更新は「issueを作成して」「issueを更新して」と話しかけることで実行できます。

## 手順

### ステップ1: テンプレート読み込み

`.github/ISSUE_TEMPLATE/PBI_ISSUE_TEMPLATE.md` を読み込む。

### ステップ2: PBIヒアリング

ユーザーに「PBI名はなんですか？」と1回だけ質問する。

### ステップ3: ドキュメント保存

`PBI_ISSUE_TEMPLATE.md` のフォーマットに沿って `docs/{PBI名}.md` に保存する。
不明な項目はコメントアウトのまま残してよい。

---

## 操作メニュー

### Issue 新規作成

「issueを作成して」と話しかけることで実行できます。
`docs/` 配下のmdファイルの内容を使って GitHub に PBI Issue を新規作成します。

1. 使用するmdファイルをユーザーに選択させる（`docs/` 配下のファイル一覧を提示）
2. 選択したmdファイルのファイル名（拡張子 `.md` を除く）を ISSUE タイトルとして使用する
3. 本文（mdファイルの内容）をユーザーに提示して確認を取る
4. 以下を実行する

```bash
gh issue create \
  --title "{mdファイル名}" \
  --label "PBI" \
  --body-file {mdファイルのパス}
```

### Issue 更新

「issueを更新して」と話しかけることで実行できます。
`docs/` 配下のmdファイルの内容で既存の GitHub Issue を更新します。

1. 「更新するISSUE番号を教えてください」とユーザーに質問する
2. 使用するmdファイルをユーザーに選択させる（`docs/` 配下のファイル一覧を提示）
3. 選択したmdファイルのファイル名（拡張子 `.md` を除く）を ISSUE タイトルとして使用する
4. 本文（mdファイルの内容）をユーザーに提示して確認を取る
5. 以下を実行する

```bash
gh issue edit {issue番号} \
  --title "{mdファイル名}" \
  --body-file {mdファイルのパス}
```
