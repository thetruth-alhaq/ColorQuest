# -*- coding: utf-8 -*-
import io, re

# ---------- i18n.js ----------
p = "i18n.js"
s = io.open(p, encoding="utf-8").read()
pairs = [
    # pill_price styles
    ("$1 - ", "$0.99 - "), ("$1 -", "$0.99 -"), ("$1 ", "$0.99 "),
    ("$1-", "$0.99-"), ("$1.", "$0.99."), ("$1", "$0.99"),
    ("US$ 0.990.99", "US$ 0.99"),            # guard double-replace
    ("1 $ ", "0.99 $ "), ("1 $", "0.99 $"),  # de/fr/it "1 $"
    ("دولار واحد لمرة واحدة", "0.99$ لمرة واحدة"),
    ("دولار واحد،", "0.99$،"),
    ("এক ডলার", "০.৯৯ ডলার"),
    ("একবার -", "একবার -"),
    ("এক ডলার,", "০.৯৯ ডলার,"),
    ("एक डॉलर", "99 सेंट"),
    ("ایک ڈالر", "0.99 ڈالر"),
    ("один доллар", "99 центов"),
    ("один доллар,", "99 центов,"),
    ("ein Dollar", "99 Cent"),
    ("un dollar", "99 centimes"),
    ("un dollaro", "99 centesimi"),
    ("één dollar", "99 cent"),
    ("um dólar", "99 cêntimos"),
    ("un dólar", "99 céntimos"),
    ("bir dolar", "99 sent"),
    ("satu dolar", "99 sen"),
    ("one dollar", "99 cents"),
    ("One dollar", "99 cents"),
    ("1ドル", "99セント"),
    ("一美元", "0.99 美元"),
    ("1 دولار", "0.99 دولار"),
]
for a, b in pairs:
    s = s.replace(a, b)
io.open(p, "w", encoding="utf-8").write(s)

# ---------- index.html ----------
p = "index.html"
s = io.open(p, encoding="utf-8").read()
s = s.replace('"price": "1.00"', '"price": "0.99"')
s = s.replace("One dollar, no ads", "$0.99, no ads")
s = s.replace("$1 once", "$0.99 once")
s = s.replace("One dollar, yours forever", "$0.99, yours forever")
io.open(p, "w", encoding="utf-8").write(s)

# ---------- support.html (email) ----------
p = "support.html"
s = io.open(p, encoding="utf-8").read()
s = s.replace("support@colorquest.game", "support@learnvexo.com")
io.open(p, "w", encoding="utf-8").write(s)
print("done")
