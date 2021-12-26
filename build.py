import json
import os
import sys
import shutil

PROFILE_PREFIX = "profile_"

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


def get_line(elements):
    t = """
<div class="line">\
{elements}
</div>"""
    return indent(t.format(elements="".join(elements)), 4)


def get_fav_element(item):
    t = """
<div class="fav-element">
    <a href="{link}">
        <div class="link-icon">
            <img class=\"icon\" src=\"{icon}\"/>
        </div>
    </a>
    <span class="link-label">{label}</span>
</div>"""
    return indent(t.format_map(item), 8)


def get_vertical_separator(item):
    t = """
<div class="vertical-separator">
</div>"""
    return indent(t.format_map(item), 8)


def get_text_element(item):
    t = """
<div class="text-element" style="width: {width}">
{value}
</div>"""
    return indent(t.format_map(item), 8)


def handle_item(item, profile):
    profile_name = PROFILE_PREFIX + profile
    if profile_name in item:
        for element in item[profile_name]:
            item[element] = item[profile_name][element]

    type = item.pop("type", None)
    function_name = "get_%s" % type.replace("-", "_")
    return getattr(sys.modules[__name__], function_name)(item)


def create(_input, _output, profile):
    with open(_input, "r") as i:
        data = json.load(i)

    body_components = []
    body_components.append(get_headline(data["meta"]["header"], 1))

    for line in data["data"]:
        for section in line:
            items = []
            body_components.append(get_headline(section, 2))
            for item in line[section]:
                items.append(handle_item(item, profile))
            body_components.append(get_line(items))

    map = {
        "components": "".join(body_components),
        "title": data["meta"]["title"]
    }
    html = html_main(map)

    with open(_output, "w") as o:
        o.write(html)


def create_assets(assets_dir, output_dir):
    shutil.copytree(assets_dir, output_dir + "/assets", dirs_exist_ok=True)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        s = ("Expecting exactly four arguments:\n"
             "    python build.py <input_file> <profile> <assets_dir> <output_dir>")
        print(s, sys.stderr)
        exit(1)
    input_file = sys.argv[1]
    profile = sys.argv[2]
    assets_dir = sys.argv[3]
    output_dir = sys.argv[4]

    create(input_file, output_dir + "/startpage.html", profile)
    create_assets(assets_dir, output_dir)
