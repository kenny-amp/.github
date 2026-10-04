# Codex PR レビューの設定

Codex 標準の Automatic review を使うには、対象リポジトリを Codex に接続し、
<https://app.chatgpt.com/settings/code-review> でそのリポジトリを選択して
**Review code → Automatic review** を有効にします。
自分の PR も対象にする場合は **Personal preferences → Automatic review** と
**Review trigger** も確認します。

PR をレビュー可能にした後、Codex のレビューが投稿されたことを確認してください。
届かない場合は接続、リポジトリ設定、個人設定、trigger を確認します。
Codex のレビューは人間の approve の代わりにはなりません。

`approval_policy = "never"` と `sandbox_mode = "workspace-write"` は
Codex CLI のローカル作業設定です。GitHub PR の自動レビュー設定とは別です。
リポジトリが trusted のときに、そのリポジトリの `.codex/config.toml` が読み込まれます。

この `.github` リポジトリから自動的に継承されるのは GitHub が対応する共通ファイルだけです。
Codex のリポジトリ別設定、`.codex/config.toml`、`AGENTS.md` は継承されません。
新規リポジトリでは ai-commons の `devtools/setup/setup_repo_baseline.py` を使って
ローカル設定を配置し、この手順で Codex 側の設定を行ってください。

公式手順: <https://learn.chatgpt.com/docs/third-party/github>
