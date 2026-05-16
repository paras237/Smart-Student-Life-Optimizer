import re
import pandas as pd

text = """Timetable Details
Date	Time	Faculty Name	Slot
Mon	12:00 - 12:50	Singh Akhilesh Kumar	Data Structures (PP)
E1PY203B-Section-8 (GU_C-515)
Mon	13:45 - 14:35	Kumar Dr. Ankit	Artificial Intelligence Generative AI (PP)
E1PY213T-Section-8 (GU_C-414)
Mon	14:35 - 15:25	Sharma Dr. Sanjiv	Machine Learning with Python (PP)
E1PY210B-Section-8 (GU_C-414)
Mon	15:30 - 16:20	Singh Akhilesh Kumar	Data Structures (PP)
E1PY203B-Section-8 (GU_C-414)
Mon	16:20 - 17:10	Sharma Dr. Sanjiv	Machine Learning with Python (PP)
E1PY210B-Section-8 (GU_C-414)
Mon	17:10 - 18:00	Kumar Arun	Object Oriented Programming with Java (PP)
E1PY201B-Section-8 (GU_C-414)
Tue	13:45 - 14:35	Sinha Kaushlendra Kumar	Internet of Things (PP)
MCA2-IoT6 (GU_C-416)
Tue	14:35 - 15:25	Raj Vishal	Verbal and Quantitative Reasoning (PR)
MCA2_SEC8_P2 (GU_C-416)
Tue	15:30 - 16:20	Raj Vishal	Verbal and Quantitative Reasoning (PR)
MCA2_SEC8_P2 (GU_C-416)
Tue	16:20 - 17:10	Sharma Dr. Sanjiv	Machine Learning with Python (PR)
MCA2_SEC8_P2 (GU_C-407)
Tue	17:10 - 18:00	Sharma Dr. Sanjiv	Machine Learning with Python (PR)
MCA2_SEC8_P2 (GU_C-407)
Wed	10:15 - 11:05	Singh Akhilesh Kumar	Data Structures (PR)
MCA2_SEC8_P2 (GU_C-408)
Wed	11:05 - 11:55	Singh Akhilesh Kumar	Data Structures (PR)
MCA2_SEC8_P2 (GU_C-408)
Wed	13:45 - 14:35	Sinha Kaushlendra Kumar	Internet of Things (PP)
MCA2-IoT6 (GU_C-416)
Wed	14:35 - 15:25	Singh Akhilesh Kumar	Data Structures (PP)
E1PY203B-Section-8 (GU_C-416)
Wed	15:30 - 16:20	Kumar Vipin	Verbal and Quantitative Reasoning (PR)
MCA2_SEC8_P2 (GU_C-416)
Wed	16:20 - 17:10	Kumar Vipin	Verbal and Quantitative Reasoning (PR)
MCA2_SEC8_P2 (GU_C-416)
Wed	17:10 - 18:00	Tyagi Mohini	Operating Systems (PP)
E1PY207T-Section-8 (GU_C-416)
Thu	12:00 - 12:50	Chourasiya Rajiv	Training-I (PR)
MCA2_SEC8_P2 (GU_C-513)
Thu	13:45 - 14:35	Sinha Kaushlendra Kumar	Internet of Things (PP)
MCA2-IoT6 (GU_C-416)
Thu	14:35 - 15:25	Kumar Dr. Ankit	Artificial Intelligence Generative AI (PP)
E1PY213T-Section-8 (GU_C-416)
Thu	15:30 - 16:20	Mishra Dr. Pawan	Data Communication and Networking (PP)
E1PY206T-Section-8 (GU_C-416)
Thu	16:20 - 17:10	Kumar Arun	Object Oriented Programming with Java (PR)
MCA2_SEC8_P2 (GU_C-407)
Thu	17:10 - 18:00	Kumar Arun	Object Oriented Programming with Java (PR)
MCA2_SEC8_P2 (GU_C-407)
Sun	12:00 - 12:50	Kumar Arun	Object Oriented Programming with Java (PP)
E1PY201B-Section-8 (GU_C-311)
Sun	13:45 - 14:35	Mishra Dr. Pawan	Data Communication and Networking (PP)
E1PY206T-Section-8 (GU_C-414)
Sun	14:35 - 15:25	Tyagi Mohini	Operating Systems (PP)
E1PY207T-Section-8 (GU_C-414)
Sun	15:30 - 16:20	Kumar Arun	Object Oriented Programming with Java (PP)
E1PY201B-Section-8 (GU_C-414)
Sun	16:20 - 17:10	Sharma Dr. Sanjiv	Machine Learning with Python (PP)
E1PY210B-Section-8 (GU_C-414)
Sun	17:10 - 18:00	Kumar Dr. Ankit	Artificial Intelligence Generative AI (PP)
E1PY213T-Section-8 (GU_C-416)"""

day_map = {'Mon':'Monday','Tue':'Tuesday','Wed':'Wednesday',
           'Thu':'Thursday','Fri':'Friday','Sat':'Saturday','Sun':'Sunday'}
name_to_code = {
    'Data Structures':                       'E1PY203B',
    'Artificial Intelligence Generative AI': 'E1PY213T',
    'Machine Learning with Python':          'E1PY210B',
    'Object Oriented Programming with Java': 'E1PY201B',
    'Internet of Things':                    'E1PY217T',
    'Verbal and Quantitative Reasoning':     '01PA202L',
    'Operating Systems':                     'E1PY207T',
    'Data Communication and Networking':     'E1PY206T',
    'Training-I':                            'E1PY218L',
    'Training I':                            'E1PY218L',
}

rows, unmatched = [], []
lines = [l.rstrip() for l in text.strip().splitlines()]
i = 0
while i < len(lines):
    parts    = lines[i].split('\t')
    day_abbr = parts[0].strip()
    if day_abbr in day_map and len(parts) >= 4:
        day     = day_map[day_abbr]
        tp      = re.split(r'\s*-\s*', parts[1].strip())
        t_start = tp[0].strip()
        t_end   = tp[1].strip() if len(tp) > 1 else ''
        faculty = parts[2].strip()
        slot    = parts[3].strip()
        type_m  = re.search(r'\(([A-Z]{2})\)\s*$', slot)
        stype   = type_m.group(1) if type_m else 'PP'
        sname   = re.sub(r'\s*\([A-Z]{2}\)\s*$', '', slot).strip()
        scode   = name_to_code.get(sname, '')
        if not scode: unmatched.append(sname)
        section = room = ''
        if i + 1 < len(lines):
            nxt     = lines[i + 1].strip()
            nxt_day = nxt.split('\t')[0]
            is_new  = nxt_day in day_map and len(nxt.split('\t')) >= 4
            is_hdr  = bool(re.search(r'date|time|faculty|timetable', nxt, re.IGNORECASE))
            if nxt and not is_new and not is_hdr:
                rm = re.search(r'\(([^)]+)\)\s*$', nxt)
                if rm:
                    room    = rm.group(1).strip()
                    section = re.sub(r'\s*\([^)]+\)\s*$', '', nxt).strip()
                else:
                    section = nxt
                i += 1
        rows.append({'day':day,'time_start':t_start,'time_end':t_end,
                     'subject_code':scode,'subject_name':sname,
                     'subject_type':stype,'section':section,
                     'room':room,'faculty':faculty})
    i += 1

print(f"{'Day':<12} {'Time':<14} {'Code':<12} {'Type':<5} {'Room':<10} {'Faculty'}")
print("-"*75)
for r in rows:
    print(f"{r['day']:<12} {r['time_start']}-{r['time_end']:<8} {r['subject_code']:<12} {r['subject_type']:<5} {r['room']:<10} {r['faculty']}")
print(f"\nTotal: {len(rows)} rows")
if unmatched:
    print(f"Unmatched: {set(unmatched)}")
else:
    print("All subject codes matched ✓")
