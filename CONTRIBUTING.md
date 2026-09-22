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
用途に応じて [Issue テンプレート](./.github/ISSUE_TEMPLATE/) を使い分けてください。
- `feature_request.md`: 機能追加・仕様変更
- `bug_report.md`: 不具合・障害報告
- `task_maintenance.md`: リファクタリング・技術改善
- `research_spike.md`: 技術調査・PoC

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

## 行動規範
すべての参加者は [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) を遵守してください。
