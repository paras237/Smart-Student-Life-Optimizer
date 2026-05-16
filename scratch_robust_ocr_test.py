import re

sample_texts = [
    "object Oriented Programming With: Java: (PP)\nCourseCode  Attended/Pelivered. Percent\nELPYZ01B 27/24. WV",
    "CourseCode Attended/Delivered   Prent\nELPY20 13 Of 62.9 %.",
    "ELPY 2035 25/3. 80,65:-%",
    "Date. Structures (PR)\nCoursCode Attended /Delivered. Percent\nELPY 2038 t/2z 63.64 %",
    "Data Conumunication and. Networking . (PP)\nELPY206T 14/18 17.78:%",
    "Total Percentage, 209/280 TH.b4",
    "Operating Systems ~ (PP)\nELPY207T VGAN4, 19.68:%",
    "Verbal and: Quantitative: Reasoning (o1PAzozL)",
    "Machine Learning with Python (EIPYz0f3)\nELPY200B 12/18 66.67. %",
    "Internet of Things (E (PY2! 77).",
    "Internet.of Things : (PP)\nCourseCode Attended/Delivered Percent\nElPYZ170T 18728 b4..24-%",
    "Total Percentage. 209280 14.64. %",
]

def clean_text_line(line):
    # Remove common noisy unicode symbols from OCR
    l = re.sub(r'[~\^`<>\(\)]', ' ', line)
    # Collapse multiple spaces
    return ' '.join(l.split()).strip()

def fix_code(raw):
    # Replace space in code if it's in middle, e.g. ELPY 2038 -> ELPY2038
    c = raw.upper().replace(" ", "").strip()
    # ELPY, EIPY, E!PY, E|PY -> E1PY
    c = re.sub(r'^E[LI!\|]PY', 'E1PY', c)
    # 01PA fix
    c = re.sub(r'^[O]1PA', '01PA', c)
    c = re.sub(r'^0[LI!\|]PA', '01PA', c)
    
    # Replace trailing char O->0 if preceeded by digits
    c = c.replace('|', '1')
    return c

def extract_numbers_from_messy_fraction(txt):
    # Find patterns like "25/31", "18728" (which might be 18/28 if OCR missed separator)
    # Look for digits / digits
    m = re.search(r'(\d{1,3})\s*[/\|Iil1\\,:]+\s*(\d{1,3})', txt)
    if m:
        return int(m.group(1)), int(m.group(2))
    # Special: 209280 from the total percentage line
    m2 = re.search(r'(\d{3})(\d{3})', txt)
    if m2:
        return int(m2.group(1)), int(m2.group(2))
    return None, None

print("Running robust regex tests...\n")

for txt in sample_texts:
    line = clean_text_line(txt)
    print(f"ORIGINAL: {repr(txt)}")
    print(f"CLEANED : {repr(line)}")
    
    # Test Total Parser
    if "TOTAL PERCENTAGE" in line.upper() or "TOTAL" in line.upper() and ("PERCENT" in line.upper() or "PERCENTAGE" in line.upper()):
        print("-> DETECTED TOTAL LINE")
        num1, num2 = extract_numbers_from_messy_fraction(line)
        if num1 and num2:
            print(f"   Extracted Total: {num1} / {num2} = {round(num1/num2*100, 2)}%")
        continue

    # Look for code part anywhere
    # Find words that look like codes: typically starts with E1PY or variant
    code_match = re.search(r'([E0][A-Z0-9!\|]{3,4}\s*[A-Z0-9!\|]{3,5})', line.upper())
    if code_match:
        raw_code = code_match.group(1)
        fixed = fix_code(raw_code)
        print(f"-> CODE FOUND: {raw_code} -> Fixed: {fixed}")
        
        # Now look for fraction in same string after the code
        remainder = line.upper().split(raw_code)[-1]
        att, tot = extract_numbers_from_messy_fraction(remainder)
        if att and tot:
             print(f"   STATS FOUND: {att} / {tot}")
        else:
             print("   STATS NOT FOUND IN LINE")
    print("-" * 20)
