import re

def fix_code(raw):
    c = raw.upper().replace('|', '1')
    c = re.sub(r'^O(\d)', r'0\1', c)
    return c

text = """Object Oriented Programming with Java - (PP)
E1PY201B 23/29 79.31%
Object Oriented Programming with Java - (PR)
Course Code Attended/Delivered. Percent.
Data Structures. (E1PY203B)
E1PY203B 26/31 83.87 %
Data Structures: - (PR)
Course Code Attended/Delivered Percent
Data Communication and Networking - (PP)
E1PY206T 15/18 83.33 %
Verbal and Quantitative Reasoning - (PR)
O1PA202L 30/32 93.75 %
Machine Learning with Python - (PP)
E1PY210B 25/31 80.65 %
Machine Learning with Python - (PR).
E1PY210B 14/16 87.5 %
Artificial Intelligence Generative Al. -- (PP)
E1PY213T 24/29 82.76 %
Internet of Things: - (PP)
E1PY217T 25/27 92.59 %
Trainirig-l - (PR)
E1PY218L 6/7 85.71 %
Total Percentage 239/277 86.28 %"""

subjects = []
current_type = 'Unknown'
current_name = ''

for line in text.splitlines():
    line = line.strip()
    if not line: continue
    if re.search(r'course\s*code|attended.*delivered|from.*date|to.*date|home|scan\s*qr', line, re.IGNORECASE):
        continue

    type_match = re.search(r'[-\u2013]?\s*\(?(PP|PR)\)?\s*\.?\s*$', line, re.IGNORECASE)
    if type_match:
        current_type = type_match.group(1).upper()
        name_part = re.sub(r'\s*[-\u2013]?\s*\(?(PP|PR)\)?\s*\.?\s*$', '', line, flags=re.IGNORECASE)
        name_part = re.sub(r'[^\w\s]', ' ', name_part).strip()
        if len(name_part) > 4: current_name = name_part
        continue

    m = re.match(r'^([A-Z0-9|]{5,10})\s+(\d{1,3})/(\d{1,3})\s+(\d{1,3}(?:\.\d+)?)\s*%', line, re.IGNORECASE)
    if m:
        code = fix_code(m.group(1))
        att, tot, pct = int(m.group(2)), int(m.group(3)), float(m.group(4))
        if 0 < att <= tot <= 400 and 0 <= pct <= 100:
            subjects.append({'code': code, 'type': current_type, 'att': att, 'tot': tot, 'pct': pct})
        continue

    m2 = re.search(r'([A-Z0-9|]{5,10})\s+(\d{1,3})/(\d{1,3})(?:\s+(\d{1,3}(?:\.\d+)?)\s*%?)?', line, re.IGNORECASE)
    if m2:
        code = fix_code(m2.group(1))
        att, tot = int(m2.group(2)), int(m2.group(3))
        pct = float(m2.group(4)) if m2.group(4) else round(att/tot*100, 1) if tot else 0
        if 0 < att <= tot <= 400 and 0 <= pct <= 100:
            subjects.append({'code': code, 'type': current_type, 'att': att, 'tot': tot, 'pct': pct})

print(f"{'Code':<12} {'Type':<7} {'Att/Tot':<10} {'Pct'}")
print("-" * 38)
for s in subjects:
    print(f"{s['code']:<12} {s['type']:<7} {s['att']}/{s['tot']:<8} {s['pct']}%")
print(f"\nTotal rows parsed: {len(subjects)}")
