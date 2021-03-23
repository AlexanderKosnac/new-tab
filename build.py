import json
import os
import sys
import shutil


def indent(string, n):
    return string.replace("\n", "\n" + " " * n)


def html_main(body_components):
    t = """
<html>
<head>
    <title>New Tab</title>
    <link rel="stylesheet" href="assets/stylesheet.css">
</head>
<body>
{comps}
</body>
</html>"""
    return indent(t.format(comps="".join(body_components)), 0)


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
    body_components.append(get_headline(data["meta"]["title"], 1))

    for line in data["data"]:
        for section in line:
            items = []
            body_components.append(get_headline(section, 2))
            for item in line[section]:
                items.append(get_fav_element(item["link"], item["icon"], item["label"]))
            body_components.append(get_line(items))
    html = html_main(body_components)

    with open(_output, "w") as o:
        o.write(html)


def create_assets(build_dir):
    shutil.copytree("assets", build_dir + "assets", dirs_exist_ok=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        s = ("Expecting exactly one parameter:\n"
             "    python create.py <input_file>")
        print(s, sys.stderr)
        exit(1)

    BUILD_DIR = "build/"
    if not os.path.exists(BUILD_DIR):
        os.mkdir(BUILD_DIR)

    create(sys.argv[1], BUILD_DIR + "startpage.html")
    create_assets(BUILD_DIR)


