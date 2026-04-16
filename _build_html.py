"""Convert report.qmd to a self-contained report.html using Python only."""
import base64, re, os
import markdown as md_lib

with open('report.qmd', encoding='utf-8') as f:
    raw = f.read()

body = re.sub(r'^---.*?---\s*', '', raw, flags=re.DOTALL)

def embed_image(m):
    path = m.group(1)
    if not os.path.exists(path):
        return m.group(0)
    with open(path, 'rb') as f:
        data = base64.b64encode(f.read()).decode()
    return f'![](data:image/png;base64,{data})'

body = re.sub(r'!\[\]\(([^)]+\.png)\)', embed_image, body)

details_blocks = {}

def stash_details(m):
    key = f'CODEBLOCK_{len(details_blocks)}_END'
    inner = m.group(1)
    code_m = re.search(r'```(?:python)?\n(.*?)```', inner, re.DOTALL)
    code_content = code_m.group(1).rstrip() if code_m else inner.strip()
    def esc(s):
        return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    html = (
        f'<div class="code-block">'
        f'<div class="code-label">Python</div>'
        f'<pre><code class="language-python">{esc(code_content)}</code></pre>'
        f'</div>'
    )
    details_blocks[key] = html
    return f'\n\n{key}\n\n'

body = re.sub(r'<details>(.*?)</details>', stash_details, body, flags=re.DOTALL)

toc_items = []
h2_count = [0]
h3_count = [0]

def make_anchor(text):
    return re.sub(r'[^a-z0-9-]', '', text.lower().replace(' ', '-'))

def add_heading_id(m):
    hashes = m.group(1)
    text   = re.sub(r'[*_`]', '', m.group(2).strip())
    anchor = make_anchor(text)
    if len(hashes) == 2:
        h2_count[0] += 1
        h3_count[0]  = 0
        num = f'{h2_count[0]}. '
        toc_items.append(f'<li><a href="#{anchor}">{num}{text}</a></li>')
        return f'<h2 id="{anchor}">{num}{text}</h2>'
    else:
        h3_count[0] += 1
        num = f'{h2_count[0]}.{h3_count[0]}. '
        toc_items.append(f'<li class="toc-sub"><a href="#{anchor}">{num}{text}</a></li>')
        return f'<h3 id="{anchor}">{num}{text}</h3>'

body_tagged = re.sub(r'^(#{2,3})\s+(.+)$', add_heading_id, body, flags=re.MULTILINE)
html_body = md_lib.markdown(body_tagged, extensions=['tables', 'fenced_code'])

for key, html in details_blocks.items():
    html_body = html_body.replace(f'<p>{key}</p>', html)
    html_body = html_body.replace(key, html)

toc_html = '<nav id="toc"><h2>Contents</h2><ul>' + ''.join(toc_items) + '</ul></nav>'

css = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    font-family: "Source Sans Pro", "Helvetica Neue", Arial, sans-serif;
    font-size: 16px; line-height: 1.7; color: #333; background: #fff;
}
#layout {
    display: flex; max-width: 1200px; margin: 0 auto;
    padding: 2rem 1rem; gap: 2.5rem;
}
#toc {
    flex: 0 0 210px; position: sticky; top: 2rem; align-self: flex-start;
    font-size: 0.88rem; border-right: 1px solid #e0e0e0;
    padding-right: 1.5rem; max-height: 90vh; overflow-y: auto;
}
#toc h2 { font-size: 0.8rem; text-transform: uppercase; letter-spacing: .08em;
           color: #888; margin-bottom: .6rem; font-weight: 600; }
#toc ul { list-style: none; }
#toc li { margin: .3rem 0; }
#toc li.toc-sub { padding-left: 1rem; }
#toc a { color: #555; text-decoration: none; }
#toc a:hover { color: #2c7bb6; }
#content { flex: 1; min-width: 0; }
#title-block {
    border-bottom: 2px solid #2c7bb6; margin-bottom: 2.5rem; padding-bottom: 1.2rem;
}
#title-block h1 { font-size: 1.9rem; color: #1a1a2e; line-height: 1.25; }
#title-block .subtitle { font-size: 1rem; color: #555; margin-top: .3rem; }
#title-block .authors { margin-top: .8rem; font-size: 0.95rem; color: #444; }
#title-block .date { font-size: 0.88rem; color: #888; margin-top: .2rem; }
h2 { font-size: 1.45rem; color: #1a1a2e; margin: 2.2rem 0 .7rem;
     border-bottom: 1px solid #e8e8e8; padding-bottom: .3rem; }
h3 { font-size: 1.15rem; color: #2c7bb6; margin: 1.6rem 0 .5rem; }
p { margin: .8rem 0; }
img { max-width: 100%; height: auto; display: block; margin: 1.2rem auto; border-radius: 4px; }
table { border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.92rem; }
th { background: #2c7bb6; color: #fff; padding: .5rem .8rem; text-align: left; }
td { padding: .45rem .8rem; border-bottom: 1px solid #e8e8e8; }
tr:nth-child(even) td { background: #f7f9fc; }
code { background: #f4f4f4; padding: .15em .35em; border-radius: 3px;
       font-family: "SFMono-Regular", Consolas, monospace; font-size: .88em; }
em { color: #555; }
strong { color: #1a1a2e; }
ul, ol { margin: .6rem 0 .6rem 1.5rem; }
li { margin: .3rem 0; }
.code-block {
    margin: .8rem 0 1.4rem; border: 1px solid #d0dce8;
    border-radius: 5px; overflow: hidden;
}
.code-label {
    background: #e8f0f8; color: #2c7bb6; font-size: 0.78rem;
    font-weight: 700; letter-spacing: .06em; text-transform: uppercase;
    padding: .3rem .8rem; border-bottom: 1px solid #d0dce8;
}
.code-block pre {
    margin: 0; padding: .9rem 1rem; background: #1e1e2e; overflow-x: auto;
}
.code-block pre code {
    background: none; color: #cdd6f4; font-size: 0.85rem;
    padding: 0; border-radius: 0;
    font-family: "SFMono-Regular", Consolas, monospace; line-height: 1.55;
}
@media (max-width: 768px) {
    #layout { flex-direction: column; }
    #toc { position: static; border-right: none; border-bottom: 1px solid #e0e0e0;
           padding-bottom: 1rem; padding-right: 0; max-height: none; }
}
@media print {
    #layout { flex-direction: column; gap: 0; padding: 0; }
    #toc { position: static; border-right: none; border-bottom: 1px solid #ccc;
           max-height: none; padding: 0 0 1rem 0; margin-bottom: 1.5rem;
           page-break-after: avoid; }
    #toc a { color: #333; }
    body { font-size: 12px; }
    h2 { font-size: 1.2rem; }
    h3 { font-size: 1rem; }
    img { max-width: 90%; page-break-inside: avoid; }
    .code-block { page-break-inside: avoid; }
    #title-block h1 { font-size: 1.5rem; }
}
"""

from datetime import date
title    = 'Electricity Demand Forecasting for Zurich (EWZ)'
subtitle = 'HSLU -- Applied Machine Learning and Predictive Modelling 1, FS26'
authors  = ['Paula Barghout', 'Elena Fuchs', 'Tamara Marcet']

title_block = f"""
<div id="title-block">
  <h1>{title}</h1>
  <div class="subtitle">{subtitle}</div>
  <div class="authors">{', '.join(authors)}</div>
  <div class="date">{date.today().strftime('%B %d, %Y')}</div>
</div>
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<div id="layout">
  {toc_html}
  <div id="content">
    {title_block}
    {html_body}
  </div>
</div>
</body>
</html>"""

with open('report.html', 'w', encoding='utf-8') as f:
    f.write(html)

size = os.path.getsize('report.html') / 1024 / 1024
print(f'Written report.html  ({size:.1f} MB)')
