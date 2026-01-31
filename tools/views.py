from django.shortcuts import render

NORMAL = "abcdefghijklmnopqrstuvwxyz"

UNICODE_FONTS = {
    "Bold": "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",
    "Italic": "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻",
    "Bold Italic": "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯",
    "Script": "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",
    "Fancy": "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏",
    "Double": "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",
    "Gothic": "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷",
    "Bubble": "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ",
}

DECORATORS = [
    ("", ""),
    ("★ ", " ★"),
    ("✿ ", " ✿"),
    ("꧁ ", " ꧂"),
    ("『", "』"),
    ("【", "】"),
    ("𓆩 ", " 𓆪"),
    ("⚡ ", " ⚡"),
    ("♛ ", " ♛"),
    ("☠ ", " ☠"),
    ("ツ ", " ツ"),
    ("乂 ", " 乂"),
    ("♡ ", " ♡"),
    ("💖 ", " 💖"),
    ("💫 ", " 💫"),
    ("🔥 ", " 🔥"),
    ("🎀 ", " 🎀"),
    ("🦋 ", " 🦋"),
    ("🌸 ", " 🌸"),
    ("⚔ ", " ⚔"),
    ("👑 ", " 👑"),
    ("💎 ", " 💎"),
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
        seen = set()
        count = 1

        if name:
            for font in UNICODE_FONTS.values():
                base = stylize(name, font)
                for left, right in DECORATORS:
                    styled = f"{left}{base}{right}"
                    if styled not in seen:
                        seen.add(styled)
                        results.append({
                            "style": f"Style {count}",
                            "text": styled
                        })
                        count += 1
                    if count >= 300:
                        break
                if count >= 300:
                    break

    return render(request, "tools/stylish_name.html", {
        "results": results,
        "name": name
    })
