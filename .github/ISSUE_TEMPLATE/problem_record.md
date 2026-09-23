<!-- .github/templates/source/problem_record.yaml から自動生成されています。このファイルを直接編集しないでください。ソースを編集し、`python .github/templates/generate_issue_templates.py --write` を実行してください。 -->

---
name: "問題記録 (Problem Record)"
about: "複数のインシデントに共通する根本原因を追跡・管理する場合"
title: "[Problem]: "
labels: "problem, root-cause"
---

## 1. 問題の概要 (Problem Summary)
<!-- ITIL V4 Problem Management: 繰り返し発生している事象・パターンを記述してください。 -->

## 2. 関連インシデント (Related Incidents)
<!-- この問題に関連する Bug Report のイシュー番号を列挙してください。 -->
- インシデント: #
- インシデント: #

## 3. 根本原因分析 (Root Cause Analysis)
<!-- ITIL V4 / ISO 12207 Problem Resolution: 根本原因の分析結果を記述してください。 -->

## 4. 既知のエラー登録 (Known Error Record)
<!-- 既知のエラー（Known Error）として記録する暫定回避策と影響範囲。KEDB（既知のエラーデータベース）に相当する情報です。 -->
- **暫定回避策 (Workaround):**
- **影響を受ける機能・サービス:**

## 5. 恒久対策 (Permanent Fix)
<!-- 恒久対策の内容、または対応する Task/Maintenance イシューへのリンクを記述してください。 -->
- 対応イシュー: #

## 6. ステータス (Problem Status)
<!-- ITIL V4 Problem Management のライフサイクル -->
- [ ] 調査中 (Under Investigation) / [ ] 既知のエラー (Known Error) / [ ] 恒久対策の実施中 (Fix in Progress) / [ ] 解決済み (Resolved) / [ ] クローズ (Closed)

## 7. 完了条件 (Acceptance Criteria)
- [ ] 根本原因分析（RCA）が文書化されていること
- [ ] 恒久対策が実施され、関連インシデントが再発していないこと
