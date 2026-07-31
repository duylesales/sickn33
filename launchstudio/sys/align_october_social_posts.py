import os, glob, re

october_dir = '/Users/duyle/sickn33/launchstudio/2026/october-2026'
articles = sorted(glob.glob(f'{october_dir}/[0-9][0-9]-*.md'))
articles = [f for f in articles if not f.endswith('-social.md') and not f.endswith('-social_dutch.md') and not f.endswith('_dutch.md')]

def clean_text(t):
    return re.sub(r'\s+', ' ', t).strip()

def process_article(fpath):
    base = os.path.basename(fpath).replace('.md', '')
    with open(fpath, 'r', encoding='utf-8') as fp:
        content = fp.read()
        
    t_match = re.search(r'^Title:\s*(.*)$', content, re.MULTILINE)
    title = t_match.group(1).strip() if t_match else base
    
    idx = content.lower().find('real example')
    if idx == -1:
        return
    ex_text = content[idx:]
    
    # Subtitle
    sub_m = re.search(r'###\s*(.*)', ex_text)
    subtitle = sub_m.group(1).strip() if sub_m else ''
    
    # Extract paragraphs
    paras = [p.strip() for p in ex_text.split('\n\n') if p.strip() and not p.strip().startswith('#') and not p.strip().startswith('---')]
    
    # First story paragraph is usually after 'Real example' heading
    story_p = ''
    for p in paras:
        if p.lower() != 'real example' and not p.startswith('###') and not p.startswith('**Result:') and not p.startswith('**Cost'):
            story_p = p
            break
            
    res_m = re.search(r'\*\*Result:\*\*\s*(.*)', ex_text)
    result_text = res_m.group(1).strip() if res_m else ''
    
    cost_m = re.search(r'\*\*Cost & Timeline:\*\*\s*(.*)', ex_text)
    cost_text = cost_m.group(1).strip() if cost_m else ''
    
    # Extract name/entity
    # Look for capitalized name or Agency name in first sentence
    name = 'The Founder'
    if 'Dr. Visser' in story_p:
        name = 'Dr. Visser'
    elif 'Dr. Aris' in story_p:
        name = 'Dr. Aris'
    elif 'Studio Vorm' in story_p:
        name = 'Studio Vorm'
    elif 'CreativeFlow' in story_p:
        name = 'CreativeFlow'
    elif 'Digital Bloom' in story_p:
        name = 'Digital Bloom'
    else:
        m_name = re.search(r'^([A-Z][a-z]+(?: [A-Z][a-z]+)?),', story_p)
        if m_name:
            name = m_name.group(1)
        else:
            m_name2 = re.search(r'([A-Z][a-z]+) (?:ran|built|launched|founded|owns|created)', story_p)
            if m_name2:
                name = m_name2.group(1)
                
    # Extract tool used
    tools = re.findall(r'\*\*(Cursor|Bolt|Bolt\.new|Lovable|Bubble|v0|Supabase|OpenAI|ChatGPT|Next\.js|DALL-E|Midjourney)\b.*?\*\*', ex_text, re.IGNORECASE)
    tool_name = tools[0] if tools else 'AI builders'
    if tool_name.lower() == 'bolt.new':
        tool_name = 'Bolt.new'
        
    return {
        'base': base,
        'title': title,
        'subtitle': subtitle,
        'story': story_p,
        'result': result_text,
        'cost': cost_text,
        'name': name,
        'tool': tool_name
    }

parsed_count = 0
for fpath in articles:
    info = process_article(fpath)
    if info:
        parsed_count += 1

print(f'Successfully parsed metadata for {parsed_count} / 60 articles.')
