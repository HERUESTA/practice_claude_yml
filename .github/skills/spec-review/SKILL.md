---
name: spec-review
description: 仕様検討・要件整理を行うスキル。PBI_ISSUE_TEMPLATEに沿ってdocs/配下にmdファイルを作成する
---

## 概要

このスキルを使って、新機能の仕様検討・要件整理を対話形式で進めます。
`.github/ISSUE_TEMPLATE/PBI_ISSUE_TEMPLATE.md` を参照し、`docs/{機能名}.md` を作成します。

ISSUEの作成・更新は「issueを作成して」「issueを更新して」と話しかけることで実行できます。

## 手順

### ステップ1: 要望の理解

`.github/ISSUE_TEMPLATE/PBI_ISSUE_TEMPLATE.md` を読み込み、不明な点はユーザーに質問してください。

- タイトルはなんですか？

### ステップ2: ドキュメント作成

整理した内容を `PBI_ISSUE_TEMPLATE.md` のフォーマットに沿って `docs/{機能名}.md` に保存してください。

---

## 操作メニュー

### Issue 新規作成

「issueを作成して」と話しかけることで実行できます。
`docs/` 配下のmdファイルの内容を使って GitHub に PBI Issue を新規作成します。

1. 「ISSUEのタイトルを教えてください」とユーザーに質問する
2. 使用するmdファイルをユーザーに選択させる（`docs/` 配下のファイル一覧を提示）
3. 本文（mdファイルの内容）をユーザーに提示して確認を取る
4. 以下を実行する

```bash
gh issue create \
  --title "{タイトル}" \
  --label "PBI" \
  --body-file {mdファイルのパス}
```

### Issue 更新

「issueを更新して」と話しかけることで実行できます。
`docs/` 配下のmdファイルの内容で既存の GitHub Issue を更新します。

1. 「更新するISSUE番号を教えてください」とユーザーに質問する
2. 使用するmdファイルをユーザーに選択させる（`docs/` 配下のファイル一覧を提示）
3. 本文（mdファイルの内容）をユーザーに提示して確認を取る
4. 以下を実行する

```bash
gh issue edit {issue番号} \
  --body-file {mdファイルのパス}
```
