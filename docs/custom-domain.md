# Custom domain: scrapshot.munchmethod.com

**Live since 2026-10-09**: DNS CNAME added, custom domain set on the repo, HTTPS enforced.
The github.io URLs redirect to it.

1. DNS (at munchmethod.com's DNS provider) - one record:

   | Type | Name / Host | Value / Target | TTL |
   |---|---|---|---|
   | CNAME | `scrapshot` | `founder-edany.github.io` | 3600 (or Auto) |

   (Not the repo name: GitHub routes by the custom domain configured on the repo.)

2. Once `dig +short scrapshot.munchmethod.com` returns `founder-edany.github.io.`, turn the
   custom domain on (this also writes the CNAME file to the branch):

       gh api -X PUT repos/founder-edany/scrapshot-site/pages -f cname=scrapshot.munchmethod.com
       # after the certificate is issued (minutes to an hour):
       gh api -X PUT repos/founder-edany/scrapshot-site/pages -F https_enforced=true

   It isn't switched on yet on purpose: with a custom domain set, GitHub redirects the
   github.io URLs to it, so before the DNS record exists the site (and the links in the game)
   would break. After the switch, the old github.io links keep working (they redirect).

3. Optional: verify the domain for the account (Settings > Pages > Verified domains) to stop
   anyone else claiming it.
