#!/usr/bin/env python3
"""Add a persistent services index (with real links) to the bundled homepage.

Why: the homepage ships as a JSON-packed template that replaces documentElement on
boot, which wiped the static crawlable block — including its links to the six
service pages. Result: those pages were orphans for any JS-rendering crawler
(Bingbot renders JS). This edits the bundle's *own* markup so the links survive
hydration, and stays inside the site's design language.
"""
import json
import re
import sys

PATH = "index.html"
MARKER = 'id="vs-services-index"'

CSS = """
#vs-services-index{background:#0d1823;border-top:1px solid rgba(236,233,226,.16)}
#vs-services-index .vs-idx{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));column-gap:clamp(24px,4vw,64px)}
#vs-services-index .vs-row{border-top:1px solid rgba(236,233,226,.16)}
#vs-services-index a{display:flex;align-items:baseline;gap:16px;padding:20px 0;text-decoration:none;color:rgba(236,233,226,.92);font-family:'Bricolage Grotesque',system-ui,sans-serif;font-size:clamp(17px,1.6vw,21px);line-height:1.25;transition:color .18s ease,gap .18s ease}
#vs-services-index a:hover{color:oklch(0.78 0.15 60);gap:22px}
#vs-services-index .vs-n{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.12em;color:oklch(0.78 0.15 60);min-width:2ch}
#vs-services-index .vs-meta{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:rgba(236,233,226,.45)}
@media (max-width:640px){#vs-services-index .vs-idx{grid-template-columns:1fr}}
"""

SERVICES = [
    ("01", "Microsoft 365 consulting", "/microsoft-365-consulting-dubai/", "Tenant, security, licensing"),
    ("02", "IT infrastructure support", "/it-infrastructure-support-dubai/", "Networks, endpoints, backup"),
    ("03", "IT project management", "/it-project-management-dubai/", "Migrations, fit-out, rollout"),
    ("04", "Interim IT manager", "/it-interim-manager-dubai/", "Senior cover, month to month"),
    ("05", "Software asset management", "/software-asset-management-dubai/", "Audit, compliance, cost"),
    ("06", "AI consulting", "/ai-consulting-dubai/", "Pilots that reach production"),
]
SERVICES[3] = ("04", "Interim IT manager", "/interim-it-manager-dubai/", "Senior cover, month to month")


def build_block() -> str:
    rows = "\n".join(
        f'      <li class="vs-row"><a href="{href}"><span class="vs-n">{n}</span>'
        f'<span>{name}<span class="vs-meta" style="display:block;margin-top:6px">{meta}</span></span></a></li>'
        for n, name, href, meta in SERVICES
    )
    return f"""
<section id="vs-services-index" aria-labelledby="vs-services-heading" style="padding:clamp(56px,7vw,104px) clamp(20px,4vw,56px)">
  <style>{CSS}</style>
  <div style="max-width:1400px;margin:0 auto">
    <div class="vs-meta" style="margin-bottom:22px">Services / index</div>
    <h2 id="vs-services-heading" style="font-family:'Bricolage Grotesque',system-ui,sans-serif;font-weight:500;font-size:clamp(26px,3.4vw,44px);line-height:1.12;margin:0 0 clamp(28px,4vw,48px);color:#ece9e2;max-width:24ch">Every engagement, and where each one starts.</h2>
    <ul class="vs-idx">
{rows}
    </ul>
    <div style="display:flex;flex-wrap:wrap;gap:14px 40px;align-items:baseline;margin-top:clamp(32px,4vw,52px);padding-top:26px;border-top:1px solid rgba(236,233,226,.16)">
      <a href="mailto:contact@viewstate.co" style="font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:rgba(236,233,226,.72);text-decoration:none">contact@viewstate.co</a>
      <a href="https://bookings.cloud.microsoft/book/ViewstateConsulting@viewstate.co/" style="font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:oklch(0.78 0.15 60);text-decoration:none">Book a call</a>
      <span class="vs-meta">Dubai, UAE</span>
      <span class="vs-meta">Reviewed 27 October 2026</span>
    </div>
  </div>
</section>
"""


def main() -> int:
    src = open(PATH, encoding="utf-8").read()
    m = re.search(r'(?s)(<script type="__bundler/template">)(.*?)(</script>)', src)
    if not m:
        print("no template script found", file=sys.stderr)
        return 1
    html = json.loads(m.group(2))
    if MARKER in html:
        print("already present — nothing to do")
        return 0
    block = build_block()
    if "</body>" not in html:
        print("no </body> in template", file=sys.stderr)
        return 1
    html = html.replace("</body>", block + "</body>", 1)
    blob = json.dumps(html, ensure_ascii=False).replace("</", "<\\/")
    out = src[: m.start(2)] + blob + src[m.end(2):]
    open(PATH, "w", encoding="utf-8").write(out)
    print(f"inserted services index: template {len(html):,} chars, file {len(out):,} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
