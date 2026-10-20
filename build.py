"""なかま星図の legal ページ（GitHub Pages 用）を生成する。使い方: python build.py"""
from pathlib import Path

APP = "なかま星図"
DEV = "時吉 悠介"
MAIL = "tokiyoshi.0410@gmail.com"
UPDATED = "2026年10月20日"
OUT = Path(__file__).resolve().parent

CSS = """
  :root { --bg:#F7F4EE; --card:#fff; --border:#E4DED3; --text:#23201C; --sub:#7A736A; --accent:#5B4BB7; }
  * { box-sizing: border-box; }
  body { margin:0; background:var(--bg); color:var(--text);
    font-family:-apple-system,BlinkMacSystemFont,"Hiragino Sans","Noto Sans JP",sans-serif; line-height:1.9; }
  .wrap { max-width:720px; margin:0 auto; padding:48px 20px 80px; }
  h1 { font-size:26px; margin:0 0 6px; }
  .updated, .lead { color:var(--sub); font-size:14px; margin:0 0 32px; }
  h2 { font-size:18px; margin:36px 0 10px; padding-top:20px; border-top:1.5px solid var(--border); }
  h2:first-of-type { border-top:none; padding-top:0; }
  p, li { font-size:15px; }
  ul { padding-left:22px; }
  .back { display:inline-block; margin-bottom:28px; color:var(--accent); text-decoration:none; font-weight:700; font-size:14px; }
  .note, .card { background:var(--card); border:1.5px solid var(--border); border-radius:14px; padding:18px 20px; margin-bottom:16px; }
  .card h2 { border:none; padding:0; margin:0 0 6px; font-size:17px; }
  .card p { margin:0; color:var(--sub); }
  .links a { display:inline-block; margin:0 16px 8px 0; font-weight:700; }
  details { background:var(--card); border:1.5px solid var(--border); border-radius:14px; padding:14px 18px; margin-bottom:10px; }
  summary { font-weight:700; cursor:pointer; }
  a { color:var(--accent); }
  footer { margin-top:48px; color:var(--sub); font-size:13px; }
"""


def page(file: str, title: str, body: str, back: bool = True) -> None:
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {APP}</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
{'  <a class="back" href="./">← ' + APP + '</a>' if back else ''}
{body}
  <footer>{APP} — 開発者: {DEV}</footer>
</div>
</body>
</html>
"""
    (OUT / file).write_text(html, encoding="utf-8", newline="\n")


page("index.html", APP, f"""
  <h1>{APP}</h1>
  <p class="lead">算命学と16タイプで、自分と仲間を読み解く iPhone アプリです。</p>
  <p class="links"><a href="privacy.html">プライバシーポリシー</a><a href="terms.html">利用規約</a><a href="support.html">サポート</a></p>
  <div class="card"><h2>できること</h2><p>生年月日から算命学の命式と人体星図を出し、仲間との相関図・二人の相性・チーム編成の分析を表示します。16タイプの簡易診断と組み合わせた分析もできます。</p></div>
  <div class="card"><h2>データは端末の中だけ</h2><p>アカウント登録は不要です。登録した名前や生年月日は利用者の端末の中だけに保存され、外部に送信されません。</p></div>
  <p>お問い合わせ: <a href="mailto:{MAIL}">{MAIL}</a></p>
""", back=False)

page("privacy.html", "プライバシーポリシー", f"""
  <h1>プライバシーポリシー</h1>
  <p class="updated">最終更新日: {UPDATED}</p>
  <div class="note"><p style="margin:0"><strong>要約:</strong> 本アプリは利用者の個人情報を収集しません。登録した名前や生年月日はすべて利用者の端末の中だけに保存され、開発者がそれを見ることはできません。</p></div>

  <h2>1. 収集しない情報</h2>
  <p>本アプリ「{APP}」（以下「本アプリ」）は、以下をはじめとする個人情報を開発者のサーバー等に収集・送信しません。</p>
  <ul>
    <li>本アプリに登録した名前・生年月日・性別・性格タイプ・答え合わせの記録</li>
    <li>氏名、メールアドレス、電話番号、住所</li>
    <li>位置情報、連絡先、写真など端末内の他のデータ</li>
    <li>広告識別子（IDFA）</li>
  </ul>
  <p>本アプリはアカウント登録機能を持たず、利用者を識別する仕組みもありません。</p>

  <h2>2. 端末内に保存される情報</h2>
  <p>以下の情報が利用者の端末の中だけに保存されます。アプリを削除すると端末から消去されます。</p>
  <ul>
    <li>登録したメンバーの名前（ニックネーム可）、生年月日、算命学の計算上の性別区分、16タイプ</li>
    <li>チーム編成と、答え合わせ（当たり・外れ）の記録</li>
    <li>アプリ内購入の購入状態</li>
  </ul>

  <h2>3. 他の人の情報を登録する場合</h2>
  <p>本アプリでは、自分以外の人（友人・同僚など）の名前と生年月日を登録できます。他の人の情報を登録する際は、必ず本人の了承を得てください。登録画面でも確認をお願いしています。ニックネームでの登録も可能です。</p>

  <h2>4. 画像の共有とバックアップ</h2>
  <p>相関図を画像で共有する機能では、画像に名前（ニックネーム）と関係が描かれます。生年月日は画像に含まれません。共有先は利用者が iOS の共有シートで選ぶもので、本アプリが自動で送信することはありません。</p>
  <p>バックアップの書き出しで作成されるファイルには、登録したすべての情報が含まれます。保存先は利用者が選びます。取り扱いにご注意ください。</p>

  <h2>5. アプリ内購入について</h2>
  <p>本アプリには「{APP} Pro」という買い切りのアプリ内購入があります。決済はすべて Apple の App Store を通じて行われ、本アプリが支払い情報を取得・保存することはありません。</p>

  <h2>6. アプリの更新について</h2>
  <p>本アプリは不具合修正などのため、起動時に更新の有無を確認することがあります。この通信では、更新の配信に必要な技術情報（アプリのバージョン、端末の種類、IP アドレス）が配信元のサーバーに渡ります。登録した情報が送信されることはなく、利用者個人の特定に用いられることもありません。</p>

  <h2>7. 第三者への提供</h2>
  <p>本アプリは、利用者に関する情報を第三者へ提供・販売しません。広告配信サービスおよびアクセス解析ツールを使用していません。</p>

  <h2>8. 本ポリシーの変更</h2>
  <p>本ポリシーを変更する場合は、本ページにて改定後の内容を掲載し、最終更新日を更新します。</p>

  <h2>9. お問い合わせ</h2>
  <p><a href="mailto:{MAIL}">{MAIL}</a></p>
""")

page("terms.html", "利用規約", f"""
  <h1>利用規約</h1>
  <p class="updated">最終更新日: {UPDATED}</p>

  <h2>1. 適用</h2>
  <p>本規約は、iPhone アプリ「{APP}」（以下「本アプリ」）の利用に関する条件を定めるものです。本アプリをダウンロードまたは使用した時点で、本規約に同意したものとみなします。</p>

  <h2>2. 本アプリの位置づけ</h2>
  <p>本アプリは、算命学（東洋の占術）と性格タイプの考え方を用いて、自分や仲間への理解を深めることを楽しむためのエンターテインメントです。表示される鑑定・相性・運勢・チームへの助言は、将来や性格を保証・断定するものではありません。</p>
  <p><strong>採用、人事評価、配属、昇進、取引の可否など、人に関する重要な判断には使用しないでください。</strong>生年月日に基づく情報で人を評価・選別することは、差別や不利益につながるおそれがあります。</p>

  <h2>3. 他の人の情報の登録</h2>
  <p>自分以外の人の名前や生年月日を登録する場合は、事前に本人の了承を得てください。了承を得ずに登録したことによって生じた問題について、開発者は責任を負いません。</p>

  <h2>4. 16タイプについて</h2>
  <p>本アプリの16タイプ（4つの軸による性格タイプ）の簡易診断・説明文・算命学との対応づけは本アプリ独自のものであり、MBTI® その他の公式な検査とは関係ありません。MBTI は Myers &amp; Briggs Foundation の登録商標です。</p>

  <h2>5. 利用料金</h2>
  <p>本アプリは無料でダウンロードできます。一部の機能は「{APP} Pro」を購入すると利用できます。Pro は買い切りで、継続的な課金は発生しません。購入手続きおよび返金は、すべて Apple の App Store を通じて行われます。</p>

  <h2>6. 計算について</h2>
  <p>算命学の命式は、高尾流の人体星図の配置と二十八元に基づいて計算しています。流派や計算方法によって結果が異なる場合があります。</p>

  <h2>7. 禁止事項</h2>
  <ul>
    <li>本アプリを逆コンパイル、逆アセンブル、その他の方法で解析すること</li>
    <li>本アプリの文章・データを無断で複製し、再配布または販売すること</li>
    <li>他の人を誹謗中傷する目的で本アプリの表示内容を利用すること</li>
    <li>法令または公序良俗に違反する行為</li>
  </ul>

  <h2>8. 免責事項</h2>
  <p>開発者は、本アプリの利用によって生じた損害について、法令で認められる範囲で責任を負いません。データは端末内にのみ保存されるため、端末の故障やアプリの削除によるデータの消失に備えて、バックアップ機能をご利用ください。本アプリの内容および機能は、予告なく変更されることがあります。</p>

  <h2>9. 本規約の変更</h2>
  <p>本規約を変更する場合は、本ページにて改定後の内容を掲載し、最終更新日を更新します。</p>

  <h2>10. お問い合わせ</h2>
  <p><a href="mailto:{MAIL}">{MAIL}</a></p>
""")

FAQ = [
    ("機種変更したら Pro が消えました", "アプリの「設定」タブ →「購入の復元・詳細」→「購入を復元する」を押してください。購入時と同じ Apple ID でサインインしていれば、追加のお支払いなしで元に戻ります。"),
    ("機種変更でメンバーのデータを引き継ぎたい", "旧端末で「設定」→「バックアップ」→「書き出す」を押し、ファイルアプリや iCloud Drive に保存してください。新端末で「ファイルから読み込む」を押してそのファイルを選ぶと引き継げます。データは端末の中だけに保存されているため、書き出さずにアプリを削除すると元に戻せません。"),
    ("Pro は月額ですか", "いいえ。一度のお支払いでずっと使える買い切りです。継続的な請求は発生しません。"),
    ("無料では何が使えますか", "メンバーの鑑定（本質・人体星図・人生の流れ・天中殺・五行バランス）、今日の運勢、相関図と画像共有、相性の点数、16タイプの簡易診断と算命学との比較、答え合わせ、チーム2つまでの編成が使えます。Pro にすると、相性の詳しい解説、今月・今年の運勢、大運、チームの進め方アドバイス、3つ以上のチーム作成が使えます。"),
    ("他のサイトや本と結果が違います", "算命学は流派によって人体星図の配置や蔵干（二十八元）の取り方が異なります。本アプリは高尾流の配置と一般的な二十八元の表を使っています。また、節入り日（月の変わり目）に生まれた方は、流派によって前の月として扱われることがあります。"),
    ("MBTI の結果と同じですか", "本アプリの16タイプは独自の簡易診断で、MBTI® 公式検査とは関係ありません。すでにご自身のタイプをご存じの場合は、鑑定ページで直接選ぶこともできます。"),
    ("会社のチームで使ってもいいですか", "メンバー同士の相互理解やチームづくりの話題として、本人の了承のうえでお使いください。採用・評価・配属などの判断には使わないでください。"),
]

page("support.html", "サポート", f"""
  <h1>サポート</h1>
  <p class="lead">よくあるご質問と、お問い合わせ先です。</p>
  {''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)}
  <h2>解決しない場合</h2>
  <p>下記までメールでご連絡ください。数日以内に返信します。<br><a href="mailto:{MAIL}">{MAIL}</a></p>
""")

print("ok", sorted(p.name for p in OUT.glob("*.html")))
