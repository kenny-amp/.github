# .github

kenny-amp organization の default community health files リポジトリです。個別リポジトリに同名ファイルが存在しない場合、このリポジトリの内容が組織共通のデフォルトとして適用されます。

## 含まれるもの
- [`.github/ISSUE_TEMPLATE/`](./.github/ISSUE_TEMPLATE/): 共通 Issue テンプレート5種類（feature_request / bug_report / task_maintenance / research_spike / problem_record）。Markdown版・YAML Forms版の両方を [`.github/templates/source/`](./.github/templates/) の単一ソースから生成
- [`.github/PULL_REQUEST_TEMPLATE.md`](./.github/PULL_REQUEST_TEMPLATE.md): 共通 PR テンプレート
- [`.github/workflows/`](./.github/workflows/): 各リポジトリから `workflow_call` で呼び出す再利用可能ワークフロー（静的解析 / シークレットスキャン / 依存関係レビュー / ラベル同期 / Issueテンプレートの生成物検証）
- [`labels.yml`](./labels.yml): Issueテンプレートが参照するラベルの唯一のソース。`reusable-label-sync.yml` 経由で各リポジトリに同期する
- [`SECURITY.md`](./SECURITY.md): 脆弱性報告方針
- [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md): 行動規範
- [`SUPPORT.md`](./SUPPORT.md): サポート窓口の案内
- [`CONTRIBUTING.md`](./CONTRIBUTING.md): 共通の開発参加ガイド

## 注意事項
リポジトリ側に同名ファイルが存在する場合はそちらが優先されます（例: `ai-tools` は独自の Issue テンプレート・PR テンプレートを持つ場合があります）。
