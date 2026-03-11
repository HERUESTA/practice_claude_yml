# AI指示書 (AI Instructions)

## コード共通化に関する指示 (Code Commonalization Instructions)

- ワークフローファイル内の重複する設定は共通化すること
- 複数のワークフローで同じpermissions設定が使われている場合は、再利用可能なコンポーネントやComposite Actionとして抽出すること
- checkout stepの設定（fetch-depth: 1など）が複数箇所で重複している場合は統一すること
- GitHub Actions における composite actions や reusable workflows を活用して重複コードを削減すること
- 設定の一貫性を保つため、共通パラメータはテンプレート化すること