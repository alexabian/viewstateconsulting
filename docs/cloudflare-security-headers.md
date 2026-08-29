# Recommended Cloudflare response headers

GitHub Pages cannot configure arbitrary response headers from this repository. The following values are recommendations for a Cloudflare Response Header Transform Rule and are **not deployed by this commit**.

| Header | Recommended value |
| --- | --- |
| `Strict-Transport-Security` | `max-age=31536000` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), payment=(), usb=()` |
| `Content-Security-Policy` | `default-src 'self'; base-uri 'self'; connect-src 'none'; font-src 'self'; form-action 'none'; frame-ancestors 'none'; img-src 'self'; object-src 'none'; script-src 'none'; style-src 'self'; upgrade-insecure-requests` |

Do not add `includeSubDomains` or submit the domain to the HSTS preload list until HTTPS support for every current and future subdomain has been confirmed.

After applying the Cloudflare rule, verify these headers independently on `https://viewstate.co/`. Cloudflare's managed `robots.txt` response may retain its own route-specific Content Security Policy.

## Cloudflare feature compatibility

The live deployment review found that Cloudflare currently injects its email-address protection script, Web Analytics beacon and a bot/challenge loader into the otherwise script-free repository HTML. Disable those Cloudflare features before applying the recommended `script-src 'none'` policy. If any must remain enabled, review the feature and define the narrowest compatible policy instead of weakening the CSP broadly.

Cloudflare also served the repository `robots.txt` in place of the zone's previous managed content-signals response, rather than prepending the managed block. For that reason, the repository does not ship a `robots.txt`; the zone-level managed response remains authoritative.
