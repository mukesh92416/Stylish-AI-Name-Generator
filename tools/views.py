from django.shortcuts import render

# Unicode maps
def convert(text, normal, styled):
    result = ""
    for ch in text:
        if ch.lower() in normal:
            index = normal.index(ch.lower())
            result += styled[index]
        else:
            result += ch
    return result


def stylish_name(request):
    styled_names = []

    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if name:
            normal = "abcdefghijklmnopqrstuvwxyz"

            styles = {
                "Cursive": "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",
                "Bold": "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",
                "Double": "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",
                "Wide": "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",
                "Small Caps": "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ",
            }

            for style_name, styled_chars in styles.items():
                styled = convert(name, normal, styled_chars)
                styled_names.append(styled)

    return render(request, "tools/stylish_name.html", {
        "styled_names": styled_names
    })
