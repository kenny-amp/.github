# コントリビューションガイド

kenny-amp organization 配下のリポジトリにおける共通の開発参加ガイドです。個別リポジトリに独自の `CONTRIBUTING.md` がある場合はそちらを優先してください。

## ブランチ戦略
- `main`: 常にデプロイ可能な状態を維持する保護ブランチ
- 作業ブランチ: `feat/<概要>` / `fix/<概要>` / `chore/<概要>` / `docs/<概要>` の命名規則を推奨
- `main` への直接 push は禁止。必ず Pull Request 経由でマージする

## コミットメッセージ規約
[Conventional Commits](https://www.conventionalcommits.org/) に準拠してください。

```
<type>(<scope>): <summary>

[optional body]

[optional footer]
```

| type | 用途 |
| --- | --- |
| feat | 新機能の追加 |
| fix | 不具合修正 |
| docs | ドキュメントのみの変更 |
| refactor | 挙動を変えないコード改善 |
| test | テストの追加・修正 |
| chore | ビルド・補助ツール・依存関係の変更 |
| ci | CI/CD 設定の変更 |

## Issue の作成
用途に応じて [Issue テンプレート](./.github/ISSUE_TEMPLATE/) を使い分けてください。各テンプレートは Markdown版（`*.md`）と YAML Forms版（`*_form.yml`、末尾に `[フォーム版]`）の両方を用意しています。
- `feature_request`: 機能追加・仕様変更
- `bug_report`: 不具合・障害報告
- `task_maintenance`: リファクタリング・技術改善
- `research_spike`: 技術調査・PoC
- `problem_record`: 複数インシデントに共通する根本原因の追跡（ITIL Problem Management）

テンプレートの中身を変更する場合は `.github/ISSUE_TEMPLATE/*.md` / `*_form.yml` を直接編集せず、[`.github/templates/source/`](./.github/templates/source/) のソースYAMLを編集して `python .github/templates/generate_issue_templates.py --write` を実行してください（生成物はCIで最新かどうか検証されます）。

### ラベル
Issueテンプレートが参照するラベル（`bug`, `feature`, `priority-triage` 等）は [`labels.yml`](./labels.yml) を唯一のソースとして管理しています。各リポジトリで `.github/workflows/reusable-label-sync.yml` を呼び出すワークフローを設定し、ラベルを同期してください（未同期の場合、テンプレート指定のラベルはIssue作成時にサイレントに無視されます）。

## Pull Request の作成
- [PR テンプレート](./.github/PULL_REQUEST_TEMPLATE.md) に沿って記載してください
- 1 PR = 1 目的を原則とし、レビューしやすい粒度に分割してください
- CI（lint / secret-scan 等）がすべて通過していることを確認してください
- 破壊的変更を含む場合は PR 本文とドキュメントに明記してください

## レビュー方針
- レビュアーは最低 1 名の承認を必須とします（CODEOWNERS 設定がある場合はそれに従う）
- セキュリティ・CI 設定に関わる変更は管理者権限を持つレビュアーの承認を必須とします
- レビュー指摘には可能な限り 2 営業日以内に対応してください

## コーディング規約 / 静的解析
各リポジトリの `.pre-commit-config.yaml` またはドキュメントに従ってください。共通の静的解析・セキュリティスキャンは組織共通の再利用可能ワークフロー（[`.github/workflows/`](./.github/workflows/)）を各リポジトリから呼び出すことで自動実行できます。

## 新規リポジトリへの再利用可能ワークフロー導入手順
本リポジトリ（`kenny-amp/.github`）が提供する再利用可能ワークフローを新しいリポジトリに導入する際の手順です。`kenny-amp/ai-tools` と `kenny-amp/ai-common-projects` が導入済みなので、実例としても参照してください。

### 前提条件
- `kenny-amp/.github` は public リポジトリです。再利用可能ワークフロー（`workflow_call`）は public な提供元であればどのリポジトリからでも呼び出せるため、呼び出し元リポジトリ側で追加の権限設定は不要です。
  - 提供元を private に戻す場合は、提供元の Settings → Actions → General → **Access** で呼び出し元リポジトリを明示的に許可する必要があります（この設定が漏れると、対象ワークフローが 1 つもジョブを起動しない `startup_failure` になります）。
- `label-sync` は `labels.yml` を `raw.githubusercontent.com` 経由で取得します。この方式は private リポジトリのファイルを取得できないため、`kenny-amp/.github` は public のまま維持してください。

### 各ワークフローの導入
呼び出し例は各再利用可能ワークフロー自身の先頭コメントにも記載しています（[`reusable-lint.yml`](./.github/workflows/reusable-lint.yml) / [`reusable-secret-scan.yml`](./.github/workflows/reusable-secret-scan.yml) / [`reusable-dependency-review.yml`](./.github/workflows/reusable-dependency-review.yml) / [`reusable-label-sync.yml`](./.github/workflows/reusable-label-sync.yml)）。

| ワークフロー | 呼び出し元ファイル | 導入前の確認事項 |
| --- | --- | --- |
| `reusable-lint.yml` | `.github/workflows/lint.yml` | リポジトリ直下に `.pre-commit-config.yaml` が存在すること。存在しない場合は即座に失敗するため、用意できるまで導入を見送ってください。 |
| `reusable-secret-scan.yml` | `.github/workflows/secret-scan.yml` | 必須ではありませんが、誤検知を除外するため `.gitleaks.toml` の用意を推奨します。未設置でも既定ルールで動作します。 |
| `reusable-dependency-review.yml` | `.github/workflows/dependency-review.yml` | リポジトリの Settings → Code security and analysis → **Dependency graph** が有効であること。未確認の間は呼び出し元ジョブに `if: false` を付けて無効化しておいてください。 |
| `reusable-label-sync.yml` | `.github/workflows/label-sync.yml` | 呼び出し元ジョブに **`permissions: issues: write` を明示すること**（後述）。 |

`label-sync.yml` の呼び出し例（`permissions` の明示が必須）:
```yaml
name: label-sync

on:
  workflow_dispatch:
  schedule:
    - cron: "0 4 * * 1"  # 毎週月曜 13:00 JST

jobs:
  sync:
    permissions:
      issues: write
    uses: kenny-amp/.github/.github/workflows/reusable-label-sync.yml@main
```

### 既知の落とし穴
- **`permissions` の伝播**: 再利用可能ワークフローが要求する権限（例: `issues: write`）は、呼び出し元のジョブでも明示的に許可する必要があります。省略するとリポジトリの既定権限（read のみ）でキャップされ、`startup_failure`（ジョブが1つも起動しない）になります。エラーメッセージも残らないため気づきにくい点に注意してください。
- **`workflow_call` の解決失敗**: 提供元リポジトリが private かつ Access 設定で許可されていない場合も同様に `startup_failure` になります（`referenced_workflows: []` でジョブが0件）。
- **`raw.githubusercontent.com` は private リポジトリを認証なしで取得できない**: `label-sync` の `labels.yml` 取得はこの方式のため、`kenny-amp/.github` を private に戻すとダウンロードが 404 になります。
- **`gh` CLI と対象リポジトリの自動判定**: `actions/checkout` を実行しないワークフロー内で `gh` コマンドを使う場合、`.git` が存在せず対象リポジトリを自動判定できないため `GH_REPO` 環境変数（または `--repo` フラグ）を明示する必要があります（`reusable-label-sync.yml` 内では対応済みのため、呼び出し元では意識不要です）。
- **Repository Rulesets の必須ステータスチェック × `paths` フィルタは組み合わせ禁止**: `paths` フィルタ付きのワークフローを必須チェックに指定すると、対象外のファイルしか変更しないPRではジョブ自体が起動せず、そのチェックが永久に「Expected — Waiting」のままとなりマージ不可になります（2026-09-25、Dependabotの`actions/setup-python`更新PRで実害。`verify-issue-templates.yml`から`paths`フィルタを削除して解消）。必須チェックにする対象のワークフローには `paths` フィルタを付けないでください。
- **private リポジトリでの有料プラン要件**: `dependency-review-action` は private リポジトリで GitHub Advanced Security（有料）が必須、Repository Rulesets（ブランチ保護）は private リポジトリで GitHub Pro（有料）が必須です。いずれも Dependency Graph の有効化だけでは不十分で、無料枠の private リポジトリでは利用できません（`ai-tools` / `ai-common-projects` での検証で確認済み）。

## 行動規範
すべての参加者は [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) を遵守してください。
