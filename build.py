#!/usr/bin/env python3
"""Generates the static pages (index, privacy, terms, support) from shared parts.
Run `python3 build.py` after editing; commit the generated .html files (GitHub Pages serves
them as they are, no build step)."""

APP_STORE_URL = "https://apps.apple.com/app/id<SCRAPSHOT_APP_ID>"   # placeholder until the listing is live
EMAIL = "support@munchmethod.com"
CONTROLLER = "Rahul Sagar"
EFFECTIVE = "9 October 2026"
SITE = "https://founder-edany.github.io/scrapshot-site"

NAV = [("index.html", "Home"), ("support.html", "Support"), ("privacy.html", "Privacy"), ("terms.html", "Terms")]


def page(file, title, description, body):
    nav = "".join(f'<a href="{href}"{" aria-current=\"page\"" if href == file else ""}>{label}</a>' for href, label in NAV)
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{SITE}/assets/og.jpg">
<meta property="og:type" content="website">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/LilitaOne-Regular.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header">
  <a class="brand" href="index.html" aria-label="Scrapshot home"><img src="assets/logo.webp" alt="Scrapshot" width="148" height="52"></a>
  <nav>{nav}</nav>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <p>© 2026 {CONTROLLER} · <a href="support.html">Support</a> <a href="privacy.html">Privacy</a> <a href="terms.html">Terms</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p class="note">Apple and the App Store are trademarks of Apple Inc.</p>
</footer>
</body>
</html>
"""


INDEX = f"""
<section class="card hero">
  <div>
    <img class="logo" src="assets/logo.webp" alt="Scrapshot" width="520" height="183">
    <p class="pitch"><b>Aim. Fire. Topple!</b> Blast towering stacks of junk off the table with a cannon:
    cans, crates, tyres, paint tins, glass bottles and gas cylinders that go <b>boom</b>.
    One good shot can bring the whole thing down.</p>
    <a class="badge" href="{APP_STORE_URL}" aria-label="Download Scrapshot on the App Store"><img src="assets/app-store-badge.svg" alt="Download on the App Store" width="168" height="56"></a>
    <p class="note">Coming soon to the App Store.</p>
  </div>
  <img class="art" src="assets/key-art.webp" alt="A cannon blasting a stack of cans off a table in a junkyard" width="752" height="1344" loading="eager">
</section>
<section class="card">
  <div class="features">
    <div><b>1,300+ levels</b>From a few cans to castles, walls and bridges of scrap.</div>
    <div><b>Real physics</b>Every stack wobbles, tips and crashes down for real.</div>
    <div><b>Hard &amp; Super Hard</b>Tougher levels with bigger stacks and fewer balls.</div>
  </div>
</section>
<section class="card">
  <h2>Help &amp; policies</h2>
  <p><a href="support.html">Support &amp; FAQ</a> · <a href="privacy.html">Privacy policy</a> · <a href="terms.html">Terms of use</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</section>
"""

PRIVACY = f"""
<article class="card narrow doc">
<h1>Privacy policy</h1>
<p><span class="effective">Effective {EFFECTIVE}</span></p>
<p>This policy explains what the Scrapshot game ("the app") does with information about you, in plain English.
The short version: <b>we don't ask who you are, there are no accounts, no tracking and no advertising networks.</b>
The only things that leave your device are the purchase records needed to sell and restore in-app purchases,
an optional backup of your progress in <i>your own</i> iCloud, and anonymous crash and device diagnostics
collected by the game engine's maker.</p>

<h2>Who is responsible</h2>
<p>The data controller is <b>{CONTROLLER}</b>, the developer and App Store seller of Scrapshot, based in the United Kingdom.
Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>What is collected, why, and the legal basis</h2>
<table class="data">
<thead><tr><th>What</th><th>Who receives it</th><th>Why</th><th>Legal basis (UK / EU GDPR)</th></tr></thead>
<tbody>
<tr><td><b>Purchase records</b>: a random anonymous app user ID created on your device, the products you bought,
App Store transaction IDs, price, currency and store country, purchase dates and the App Store receipt; plus
technical request details (app version, OS version, device model, language and IP address).</td>
<td>RevenueCat, Inc. (USA), our in-app purchase provider, and Apple</td>
<td>To process, verify and restore your purchases and unlock what you bought (e.g. No Ads).</td>
<td>Performance of a contract (Art. 6(1)(b)).</td></tr>
<tr><td><b>Crash and diagnostic data</b>: engine crash reports and stack traces, and anonymous hardware and
software details (device model, graphics chip, OS version, screen and memory).</td>
<td>Unity Technologies (the game engine's maker)</td>
<td>To find and fix crashes, and for Unity's hardware statistics.</td>
<td>Legitimate interests (Art. 6(1)(f)): keeping the app working.</td></tr>
<tr><td><b>Progress backup</b>: level reached, coins, fuel, settings, which items and tips you've seen, which
purchases have been delivered, and a random device ID.</td>
<td>Your own iCloud account (Apple). <b>We can't see it.</b></td>
<td>So your progress comes back if you reinstall or move to a new device.</td>
<td>Performance of a contract (Art. 6(1)(b)). Only if you're signed into iCloud.</td></tr>
<tr><td><b>Support emails</b>: your email address and what you write.</td>
<td>Us</td>
<td>To answer you.</td>
<td>Legitimate interests (Art. 6(1)(f)).</td></tr>
</tbody>
</table>
<p>We do <b>not</b> collect your name, email address (unless you email us), contacts, location, photos or your
advertising identifier, and we don't create accounts. The app makes no other network requests.</p>
<p>Some things are stored <b>only on your device</b> and never sent anywhere: your progress and settings,
your privacy choices, and (only if you allowed analytics) a local log of house-ad views and taps used to
rotate the game's own adverts.</p>

<h2>Advertising and your privacy choices</h2>
<p>Scrapshot currently shows only its own "house" adverts, bundled with the app; no advertising network
receives any data. On first launch the app asks for your choices about personalised ads and analytics, and you
can change them any time in <b>Settings → Privacy choices</b>. Buying <b>No Ads</b> (or the Starter bundle) turns
off pop-up adverts; optional reward videos stay available.</p>
<p><b>Ad networks will be added later.</b> When they are, this policy will be updated <i>before</i> the app
update that adds them, naming each network and what it receives, and your Privacy choices will control
whether ads are personalised.</p>

<h2>Third parties</h2>
<ul>
<li><b>Apple</b> (App Store payments, iCloud): <a href="https://www.apple.com/legal/privacy/">apple.com/legal/privacy</a>. Apple handles your payment details; we never see them.</li>
<li><b>RevenueCat, Inc.</b> (in-app purchases): <a href="https://www.revenuecat.com/privacy">revenuecat.com/privacy</a>. Optional device-identifier collection and SDK diagnostics are switched off.</li>
<li><b>Unity Technologies</b> (game engine diagnostics): <a href="https://unity.com/legal/privacy-policy">unity.com/legal/privacy-policy</a>.</li>
</ul>
<p>RevenueCat and Unity may process data outside the UK / EU (for example in the USA); they rely on approved
safeguards such as the UK International Data Transfer Addendum / EU Standard Contractual Clauses or the UK
Extension to the EU-US Data Privacy Framework.</p>
<p>We don't sell or share your personal information, and we don't use it for cross-app tracking or targeted advertising.</p>

<h2>How long we keep it</h2>
<ul>
<li>Purchase records: kept by RevenueCat for as long as needed to provide and restore purchases and to meet
tax and accounting duties, then deleted under RevenueCat's retention rules. We can delete them on request.</li>
<li>Diagnostics: kept by Unity under its retention policy.</li>
<li>iCloud backup: until you delete it (iPhone Settings → [your name] → iCloud → Manage Storage) or turn off iCloud for the app.</li>
<li>Support emails: up to 2 years after your issue is resolved.</li>
<li>On-device data: until you delete the app.</li>
</ul>

<h2>Children</h2>
<p>Scrapshot isn't directed at children under 13 and we don't knowingly collect personal information from them.
If you think a child has sent us personal information, email us and we'll delete it.</p>

<h2>Your rights</h2>
<p>Under UK and EU GDPR you can ask for access to your data, correction, deletion, restriction, portability,
and you can object to processing based on legitimate interests. California residents (CCPA) can ask to know
and delete personal information; we don't sell or share it. To use any right, email
<a href="mailto:{EMAIL}">{EMAIL}</a>. Because the app has no accounts, include your RevenueCat app user ID if
you have it, or the date and product of a purchase, so we can find your records. We'll reply within one month.
You can also complain to the UK Information Commissioner's Office (<a href="https://ico.org.uk">ico.org.uk</a>)
or your local data protection authority.</p>

<h2>Security</h2>
<p>Data in transit to RevenueCat, Unity and Apple is encrypted (HTTPS). Nothing is perfectly secure, but we
keep what we collect to the minimum the game needs.</p>

<h2>Changes</h2>
<p>We'll update this page when the app's data use changes (for example when ad networks are added), change the
effective date above, and mention significant changes in the app's release notes.</p>

<h2>Contact</h2>
<p>{CONTROLLER} · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</article>
"""

TERMS = f"""
<article class="card narrow doc">
<h1>Terms of use</h1>
<p><span class="effective">Effective {EFFECTIVE}</span></p>
<p>These terms are an agreement between you and <b>{CONTROLLER}</b> ("we", "us"), the developer of the Scrapshot
game ("the app"). By downloading or playing the app you agree to them. If you got the app from the App Store,
Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User Licence Agreement</a>
also applies; if anything here conflicts with it, Apple's terms win for the matters they cover.</p>

<h2>1. Your licence</h2>
<p>We give you a personal, non-exclusive, non-transferable, revocable licence to use the app on Apple devices
you own or control, for your own non-commercial entertainment. You may not copy, modify, reverse-engineer,
resell, rent or redistribute the app or its content, except as the law allows.</p>

<h2>2. Coins and other virtual items</h2>
<ul>
<li>Coins, fuel, extra balls and other in-game items are a limited licence to use features of the game.
They have <b>no cash or real-world value</b>, can't be exchanged for money and can't be transferred or sold.</li>
<li>Purchases of virtual items are <b>non-refundable</b>, except where the law requires or Apple decides
otherwise. Refund requests go through Apple: <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</li>
<li>We may change how virtual items work or their in-game prices (for example to balance the game). Items you
have already received won't be taken away except where they were obtained by mistake, fraud or a bug.</li>
</ul>

<h2>3. In-app purchases</h2>
<p>All purchases are made through Apple's App Store and processed by Apple; Apple's payment terms apply.
Non-consumable purchases (No Ads, the Starter bundle) can be restored on the same Apple ID with
<b>Settings → Restore purchases</b>. Consumable items (coin packs, the Rescue Pack) are used up and can't be
restored. Prices are shown in your local currency by the App Store.</p>

<h2>4. Acceptable use</h2>
<p>Don't cheat, hack, use bots or exploits, tamper with the app or its purchases, or use the app unlawfully. If
you do, we may refuse support or remove items obtained that way.</p>

<h2>5. Updates and availability</h2>
<p>We may update, change or stop offering the app or features at any time. Some features need an internet
connection (purchases) or an iCloud account (progress backup). We don't guarantee the app will always be
available or error-free.</p>

<h2>6. Disclaimer</h2>
<p>The app is provided "as is" and "as available". To the extent the law allows, we make no warranties beyond
those that can't be excluded by law. Nothing in these terms affects your statutory rights as a consumer, for
example under the UK Consumer Rights Act 2015 (digital content must be as described, fit for purpose and of
satisfactory quality).</p>

<h2>7. Limitation of liability</h2>
<p>We're not liable for losses that weren't foreseeable, for business losses, or for loss of virtual items or
progress, except where caused by our negligence or breach of these terms. Our total liability to you is limited
to the amount you paid for the app and in-app purchases in the 12 months before the claim. We don't exclude
liability for death or personal injury caused by negligence, for fraud, or anything else that can't be excluded
by law.</p>

<h2>8. Governing law</h2>
<p>These terms are governed by the laws of England and Wales, and the courts of England and Wales have
jurisdiction. If you live elsewhere in the UK or the EU, you also keep the protection of the mandatory laws of
your country and may bring proceedings there.</p>

<h2>9. Changes to these terms</h2>
<p>We may update these terms (for example when features are added). We'll change the effective date above and,
for significant changes, tell you in the app's release notes. Continuing to use the app means you accept the
updated terms.</p>

<h2>10. Contact</h2>
<p>{CONTROLLER} · <a href="mailto:{EMAIL}">{EMAIL}</a> · Privacy: see our <a href="privacy.html">privacy policy</a>.</p>
</article>
"""

SUPPORT = f"""
<article class="card narrow doc">
<h1>Support</h1>
<p>Stuck, lost something or found a bug? Email <a href="mailto:{EMAIL}">{EMAIL}</a> and we'll get back to you.
The quickest way is the <b>Support</b> button in the game's Settings: it opens an email with the app version
already filled in. It helps to mention your iPhone / iPad model and iOS version.</p>

<h2>Purchases</h2>
<details><summary>I bought something but didn't get it</summary>
<p>Purchases are delivered as soon as the App Store confirms them. If the app was closed or lost connection,
just open it again: anything paid for but not yet delivered is added automatically. If a purchase says
<i>pending</i> (for example waiting for a parent's approval with Ask to Buy), it's added once it's approved.</p></details>
<details><summary>How do I restore No Ads or the Starter bundle?</summary>
<p>Open <b>Settings → Restore purchases</b> while signed into the same Apple ID you bought with. The game tells
you what was restored. Coin packs and the Rescue Pack are used up when bought, so they can't be restored.</p></details>
<details><summary>How do I get a refund?</summary>
<p>Purchases go through Apple, so refunds are handled by Apple at
<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p></details>

<h2>Progress and iCloud</h2>
<details><summary>Is my progress backed up?</summary>
<p>Yes, if you're signed into iCloud on your device: your level, coins, settings and delivered purchases are
backed up to your own iCloud account automatically. Reinstall the app or set up a new device with the same
Apple ID and your progress comes back the next time you open the game.</p></details>
<details><summary>I lost my progress</summary>
<p>Check that you're signed into iCloud with the same Apple ID as before and that iCloud is turned on for apps,
then open the game again. If you play on two devices, the game keeps the furthest level and the higher coin
balance. Without iCloud, progress is stored only on the device and is lost if the app is deleted.</p></details>

<h2>Ads and No Ads</h2>
<details><summary>What does No Ads remove?</summary>
<p>No Ads (and the Starter bundle, which includes it) removes the pop-up adverts between levels. Optional
reward videos, which you choose to watch for coins or fuel, stay available.</p></details>
<details><summary>How do I change my privacy choices?</summary>
<p>In the game, open <b>Settings → Privacy choices</b>. See our <a href="privacy.html">privacy policy</a> for details.</p></details>

<h2>Contact</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
</article>
"""

PAGES = [
    ("index.html", "Scrapshot: aim, fire, topple!", "Blast towering stacks of junk off the table in Scrapshot, a physics cannon game for iPhone and iPad.", INDEX),
    ("privacy.html", "Privacy policy · Scrapshot", "What the Scrapshot game does with your information.", PRIVACY),
    ("terms.html", "Terms of use · Scrapshot", "The terms for playing Scrapshot.", TERMS),
    ("support.html", "Support · Scrapshot", "Help with purchases, progress, iCloud and ads in Scrapshot.", SUPPORT),
]

if __name__ == "__main__":
    for file, title, desc, body in PAGES:
        with open(file, "w", encoding="utf-8") as f:
            f.write(page(file, title, desc, body))
        print("wrote", file)
