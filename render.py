from urllib.request import urlopen
import os
import json
import subprocess

root = os.path.dirname(__file__)

markdown = urlopen("https://raw.github.com/opmuse/opmuse/master/README.md").read()

html = urlopen("https://api.github.com/markdown", json.dumps({
    "text": markdown.decode('utf8'),
    "mode": "markdown"
}).encode('utf8')).read()

template = open('template.html', 'r').read()

with open(os.path.join(root, "public", "index.html"), "w") as index:
    index.write(template.replace('MARKDOWN', html.decode('utf8')))

subp = subprocess.Popen([
    os.path.join(root, "node_modules", "less", "bin", "lessc"),
    os.path.join(root, "main.less")
], stdout = subprocess.PIPE)

with open(os.path.join(root, "public", "css", "main.css"), "wb") as css:
    css.write(subp.stdout.read())

subp.wait()
