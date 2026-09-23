<!-- .github/templates/source/bug_report.yaml から自動生成されています。このファイルを直接編集しないでください。ソースを編集し、`python .github/templates/generate_issue_templates.py --write` を実行してください。 -->

---
name: "不具合・障害報告 (Bug Report)"
about: "システムの意図しない動作・エラー・障害を報告する場合"
title: "[Bug]: "
labels: "bug, priority-triage"
---

## 1. 事象の概要 (Summary)
<!-- 何が起きているかを簡潔に記述してください。 -->

## 2. 再現手順 (Steps to Reproduce)
<!-- 現象を確実に再現するための手順 -->
1.
2.
3.

## 3. 期待する挙動 vs 実際の挙動 (Expected vs Actual)
- **期待する動作 (Expected):**
- **実際の動作 (Actual):**

## 4. 発生環境 (Environment)
<!-- ITIL: インシデント特定に必要な構成要素 (CI) の記録 -->
- [ ] 本番環境 (Production) / [ ] ステージング環境 (Staging) / [ ] 開発・ローカル環境 (Dev/Local)

## 4-2. 発生環境の補足情報 (Additional Environment Details)
- **OS / ブラウザ / アプリバージョン:**
- **関連サービス / データベース:**

## 5. 影響範囲 (Impact)
<!-- ITIL: 優先度マトリクス判定用（入力） -->
- [ ] 全ユーザー / [ ] 特定のユーザー群 / [ ] 内部運用のみ

## 6. 緊急度 (Urgency)
<!-- ITIL: 優先度マトリクス判定用（入力） -->
- [ ] 即時対応が必要（サービス停止等） / [ ] 通常フローで対応可能

## 7. 優先度 (Priority)
<!-- ITIL V4 優先度マトリクス: 上記「影響範囲」×「緊急度」を掛け合わせた結果（出力）を記録してください。 -->
- [ ] P1: 緊急（即時対応） / [ ] P2: 高（当日〜翌営業日） / [ ] P3: 中（通常フロー） / [ ] P4: 低（計画的に対応）

## 8. ログ・証跡 (Logs & Screenshots)
<!-- スタックトレース、エラーログ、スクリーンショットを添付してください。 -->
<details><summary>エラーログを開く</summary>

```
(ここにログを貼り付け)
```

</details>

## 9. 仮説・回避策 (Hypothesis & Workaround)
- **原因の仮説:**
- **暫定回避策:**

## 10. 関連Problem / 既知のエラー (Related Problem / Known Error)
<!-- ITIL V4 Problem Management: 同種の事象が繰り返す場合は Problem Record を作成しリンクしてください（未作成の場合は空欄で構いません）。 -->
- 関連Problem: #

## 11. 完了条件 (Resolution Criteria)
- [ ] 原因の特定と恒久対策（コード修正）の完了
- [ ] 再現テストケースの作成とテスト通過
- [ ] 本番環境での修正確認
