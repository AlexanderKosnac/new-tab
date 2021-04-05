import json
import os
import sys
import shutil


def indent(string, n):
    return string.replace("\n", "\n" + " " * n)


def html_main(map):
    t = """
<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="assets/stylesheet.css">
</head>
<body>
{components}
</body>
</html>"""
    return indent(t.format_map(map), 0)


def get_headline(text, level):
    return indent("\n<h{lvl}>{txt}</h{lvl}>".format(lvl=level, txt=text), 4)


def get_line(fav_elements):
    t = """
<div class="line">\
{elements}
</div>"""
    return indent(t.format(elements="".join(fav_elements)), 4)


def get_fav_element(link, icon, label):
    t = """
<div class="fav-element">
    <a href="{ln}">
        <div class="link-icon">
            <img class=\"icon\" src=\"{src}\"/>
        </div>
    </a>
    <span class="link-label">{lbl}</span>
</div>"""
    return indent(t.format(ln=link, src=icon, lbl=label), 8)


def create(_input, _output):
    with open(_input, "r") as i:
        data = json.load(i)

    body_components = []
    body_components.append(get_headline(data["meta"]["header"], 1))

    for line in data["data"]:
        for section in line:
            items = []
            body_components.append(get_headline(section, 2))
            for item in line[section]:
                items.append(get_fav_element(item["link"], item["icon"], item["label"]))
            body_components.append(get_line(items))

    map = {
        "components": "".join(body_components),
        "title": data["meta"]["title"]
    }
    html = html_main(map)

    with open(_output, "w") as o:
        o.write(html)


def create_assets(assets_dir, output_dir):
    shutil.copytree("assets", output_dir + "assets", dirs_exist_ok=True)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        s = ("Expecting exactly three arguments:\n"
             "    python create.py <input_file> <assets_dir> <output_dir>")
        print(s, sys.stderr)
        exit(1)
    input_file = sys.argv[1]
    assets_dir = sys.argv[2]
    output_dir = sys.argv[3]

    create(input_file, output_dir + "startpage.html")
    create_assets(assets_dir, output_dir)
