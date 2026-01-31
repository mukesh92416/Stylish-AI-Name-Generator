from django.shortcuts import render


def stylish_name(request):

    name = ""
    results = []
    bios = []

    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if name:

            # ===== Font Variations =====
            fonts = [
                name,
                name.upper(),
                name.lower(),
                f"𝓜{name[1:]}" if len(name) > 1 else name,
                f"𝕸{name[1:]}" if len(name) > 1 else name,
                f"𝙈{name[1:]}" if len(name) > 1 else name,
                f"𝘔{name[1:]}" if len(name) > 1 else name,
                f"Ｍ{name[1:]}" if len(name) > 1 else name,
                f"Ⓜ{name[1:]}" if len(name) > 1 else name,
                f"🄼{name[1:]}" if len(name) > 1 else name,
            ]

            # ===== Decorations =====
            left_symbols = [
                "", "★ ", "🔥 ", "⚡ ",
                "👑 ", "💖 ", "🎮 ",
                "☠ ", "✦ ", "꧁ ",
                "◥ ", "༒ "
            ]

            right_symbols = [
                "", " ★", " 🔥", " ⚡",
                " 👑", " 💖", " 🎮",
                " ☠", " ✦", " ꧂",
                " ◤", " ༒"
            ]

            # ===== Patterns =====
            patterns = [
                lambda n: f"×͜× {n}",
                lambda n: f"{n}ツ",
                lambda n: f"乂{n}乂",
                lambda n: f"{n}々",
                lambda n: f"•{n}•",
                lambda n: f"★{n}★",
                lambda n: f"彡{n}彡",
                lambda n: f"✧{n}✧",
                lambda n: f"『{n}』",
                lambda n: f"【{n}】",
            ]

            seen = set()

            # Categories rotation
            categories = ["gaming", "cute", "royal", "dark", "fancy"]

            # ===== Generate styles =====
            for i, base in enumerate(fonts):

                category = categories[i % len(categories)]

                # Decoration styles
                for l in left_symbols:
                    for r in right_symbols:
                        styled = f"{l}{base}{r}"

                        if styled not in seen:
                            seen.add(styled)
                            results.append({
                                "text": styled,
                                "category": category
                            })

                # Pattern styles
                for pattern in patterns:
                    styled = pattern(base)

                    if styled not in seen:
                        seen.add(styled)
                        results.append({
                            "text": styled,
                            "category": category
                        })

            # Limit output for performance
            results = results[:500]

            # ===== Bio Generator =====
            bio_templates = [
                "🔥 Gamer {name}",
                "✨ Official {name}",
                "🎯 Headshot Lover",
                "🚀 Future Star",
                "💖 Living My Dream",
                "🎮 Gaming Zone",
                "👑 Born To Win",
                "💫 Stay Legendary",
            ]

            bios = [b.format(name=name) for b in bio_templates]

    return render(request, "tools/stylish_name.html", {
        "results": results,
        "bios": bios,
        "name": name
    })