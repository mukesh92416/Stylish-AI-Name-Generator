from django.shortcuts import render

NORMAL = "abcdefghijklmnopqrstuvwxyz"

# ===== FONTS =====
FONTS = {
    "Bold": "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",
    "Script": "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",
    "Double": "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",
    "Gothic": "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷",
    "Wide": "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",
    "Bubble": "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ",
}

# ===== CATEGORY ORDER =====
CATEGORY_ORDER = [
    "royal",
    "gaming",
    "cute",
    "aesthetic",
    "fancy",
    "dark"
]

# ===== DECORATORS =====
DECORATORS = {
    "royal": [
        ("꧁ ", " ꧂"),
        ("『", "』"),
        ("【", "】"),
        ("★ ", " ★"),
        ("👑 ", " 👑"),
    ],
    "gaming": [
        ("🔥 ", " 🔥"),
        ("⚡ ", " ⚡"),
        ("🎮 ", " 🎮"),
    ],
    "cute": [
        ("💖 ", " 💖"),
        ("🎀 ", " 🎀"),
    ],
    "aesthetic": [
        ("🌸 ", " 🌸"),
        ("🦋 ", " 🦋"),
    ],
    "dark": [
        ("☠ ", " ☠"),
        ("😈 ", " 😈"),
    ],
    "fancy": [
        ("", ""),
    ],
}

# ===== EXTRA SYMBOL PATTERNS =====
PATTERNS = [
    lambda n: f"×͜× {n}",
    lambda n: f"{n}ツ",
    lambda n: f"乂{n}乂",
    lambda n: f"{n}々",
    lambda n: f"★{n}★",
    lambda n: f"彡{n}彡",
]

def stylize(text, font):
    result = ""
    for ch in text.lower():
        if ch in NORMAL:
            result += font[NORMAL.index(ch)]
        else:
            result += ch
    return result

def stylish_name(request):
    results = []
    name = ""

    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if name:
            seen = set()

            # ===== GENERATE IN ORDER =====
            for category in CATEGORY_ORDER:
                wrappers = DECORATORS.get(category, [])

                for font in FONTS.values():
                    base = stylize(name, font)

                    for left, right in wrappers:
                        styled = f"{left}{base}{right}"

                        if styled not in seen:
                            seen.add(styled)
                            results.append({
                                "text": styled,
                                "category": category
                            })

                    # add symbol styles in fancy
                    if category == "fancy":
                        for pattern in PATTERNS:
                            styled = pattern(base)

                            if styled not in seen:
                                seen.add(styled)
                                results.append({
                                    "text": styled,
                                    "category": "fancy"
                                })

    return render(request, "tools/stylish_name.html", {
        "results": results,
        "name": name
    })
