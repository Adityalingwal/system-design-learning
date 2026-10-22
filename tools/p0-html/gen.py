import re, html, json, os
# Rebuilds reference/p0-practice.html from the two P0 md files. Run only when those md files change:
#   python3 tools/p0-html/gen.py
HERE=os.path.dirname(os.path.abspath(__file__))
REF=os.path.join(HERE,'..','..','reference')
SRC=os.path.join(REF,'p0-model-answers.md')
OUT=os.path.join(REF,'p0-practice.html')
lines=open(SRC,encoding='utf-8').read().split('\n')

def inline(s):
    s=html.escape(s,quote=False)
    codes=[]
    def c(m): codes.append(m.group(1)); return '\x00%d\x00'%(len(codes)-1)
    s=re.sub(r'`([^`]+)`',c,s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?!\*)',r'<em>\1</em>',s)
    # .md links open blank in a browser -> show plain text; keep other links
    s=re.sub(r'\[([^\]]+)\]\(([^)]+\.md)\)',r'\1',s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
    s=re.sub(r'\x00(\d+)\x00',lambda m:'<code>'+codes[int(m.group(1))]+'</code>',s)
    return s

def cells(l): return [x.strip() for x in l.strip().strip('|').split('|')]

def render_answer(al):
    out=[];i=0
    al=[l for l in al if l.strip()]
    if al and al[0].startswith('A:'): al[0]=al[0][2:].strip()
    first=True
    while i<len(al):
        l=al[i]
        if l.startswith('|'):
            rows=[]
            while i<len(al) and al[i].startswith('|'): rows.append(al[i]);i+=1
            head=cells(rows[0]); body=[cells(r) for r in rows[2:]]
            t='<div class="tw"><table><thead><tr>'+''.join('<th>%s</th>'%inline(h) for h in head)+'</tr></thead><tbody>'
            for r in body: t+='<tr>'+''.join('<td>%s</td>'%inline(x) for x in r)+'</tr>'
            out.append(t+'</tbody></table></div>');continue
        if re.match(r'^\d+\. ',l):
            items=[]
            while i<len(al) and re.match(r'^\d+\. ',al[i]): items.append(re.sub(r'^\d+\. ','',al[i]));i+=1
            out.append('<ol>'+''.join('<li>%s</li>'%inline(x) for x in items)+'</ol>');continue
        m=re.match(r'^\*([A-Za-z ]+?)(?: \([^)]*\))?:\*',l)
        if m:
            cls=m.group(1).split()[0].lower()
            out.append('<div class="line %s">%s</div>'%(cls,inline(l)))
        elif first: out.append('<p class="core">%s</p>'%inline(l))
        elif l.startswith('→'): out.append('<p class="arrow">%s</p>'%inline(l))
        else: out.append('<p>%s</p>'%inline(l))
        first=False;i+=1
    return '\n'.join(out)

sections=[];cur=None;q=None;intro=[];related=''
i=0
for l in lines:
    m=re.match(r'^## (\d+)\. (.+)$',l)
    if m:
        cur={'n':int(m.group(1)),'title':m.group(2),'qs':[],'foot':[]};sections.append(cur);q=None;continue
    if cur is None:
        if l.startswith('# ') or not l.strip() or l.startswith('---'): continue
        if l.startswith('Related:'): related=l
        else: intro.append(l)
        continue
    if l.startswith('---'): q=None;cur=None if False else cur; 
    if l.startswith('**Q:'):
        q={'q':re.match(r'^\*\*Q: (.*)\*\*$',l).group(1),'a':[]};cur['qs'].append(q);continue
    if l.startswith('---'): q=None;continue
    if l.startswith('**Next:**'): continue
    if l.startswith('Full section list'): cur['foot'].append(l);q=None;continue
    if q is not None: q['a'].append(l)


def md_blocks(ls):
    out=[];i=0
    def is_special(l):
        return (l.startswith('```') or l.startswith('#') or l.startswith('> ') or l.startswith('|') or l.startswith('- ')
                or re.match(r'^\d+\. ',l) or l.strip()=='---')
    while i<len(ls):
        l=ls[i]
        if not l.strip(): i+=1;continue
        if l.startswith('```'):
            i+=1;buf=[]
            while i<len(ls) and not ls[i].startswith('```'): buf.append(ls[i]);i+=1
            i+=1
            out.append('<pre class="diagram" tabindex="0">%s</pre>'%html.escape('\n'.join(buf),quote=False));continue
        m=re.match(r'^(#{1,4}) (.*)$',l)
        if m:
            lv=len(m.group(1));tg='h2' if lv==1 else 'h%d'%lv;out.append('<%s class="mdh mdh%d">%s</%s>'%(tg,lv,inline(m.group(2)),tg));i+=1;continue
        if l.strip()=='---': out.append('<hr>');i+=1;continue
        if l.startswith('> '):
            b=[]
            while i<len(ls) and ls[i].startswith('> '): b.append('<p>%s</p>'%inline(ls[i][2:]));i+=1
            out.append('<blockquote>%s</blockquote>'%''.join(b));continue
        if l.startswith('|'):
            rows=[]
            while i<len(ls) and ls[i].startswith('|'): rows.append(ls[i]);i+=1
            head=cells(rows[0]);body=[cells(r) for r in rows[2:]]
            t='<div class="tw"><table><thead><tr>'+''.join('<th>%s</th>'%inline(h) for h in head)+'</tr></thead><tbody>'
            for r in body: t+='<tr>'+''.join('<td>%s</td>'%inline(x) for x in r)+'</tr>'
            out.append(t+'</tbody></table></div>');continue
        if l.startswith('- '):
            it=[]
            while i<len(ls) and ls[i].startswith('- '): it.append(ls[i][2:]);i+=1
            out.append('<ul>'+''.join('<li>%s</li>'%inline(x) for x in it)+'</ul>');continue
        if re.match(r'^\d+\. ',l):
            it=[]
            while i<len(ls) and re.match(r'^\d+\. ',ls[i]): it.append(re.sub(r'^\d+\. ','',ls[i]));i+=1
            out.append('<ol>'+''.join('<li>%s</li>'%inline(x) for x in it)+'</ol>');continue
        p=[]
        while i<len(ls) and ls[i].strip() and not is_special(ls[i]): p.append(inline(ls[i]));i+=1
        if not p: p=[inline(l)];i+=1
        out.append('<p>%s</p>'%'<br>'.join(p))
    return '\n'.join(out)

def build_notes():
    ls=open(os.path.join(REF,'p0-notes.md'),encoding='utf-8').read().split('\n')
    # split by "## "
    idx=[k for k,l in enumerate(ls) if re.match(r'^## ',l)]
    html_out='<div class="intro">'+md_blocks(ls[:idx[0]])+'</div>'
    for a,b in zip(idx,idx[1:]+[len(ls)]):
        m=re.match(r'^## (\d+)\. (.+)$',ls[a]);n=int(m.group(1))
        body=ls[a+1:b]
        html_out+='<section id="s%d" class="sec" style="--c:%s"><h2><span class="num">%d</span>%s</h2>%s</section>'%(n,colors[n-1],n,inline(m.group(2)),md_blocks(body))
    return html_out

short={1:'Design process',2:'Requirements',3:'Trade-offs',4:'Bottlenecks',5:'Failure thinking',6:'10x & YAGNI',7:'Estimation',8:'Design doc'}
colors=['#2F6FEB','#1E9E6A','#E0870B','#8B5CF6','#E5484D','#0E9AA7','#C2478A','#6B7A90']
nq=0;notes='';prac='';toc='';chips='<button class="chip on" data-f="all">All</button>'
for s in sections:
    k=s['n'];col='--c:%s'%colors[k-1]
    toc+='<a href="#s%d" style="%s"><i></i>%d %s</a>'%(k,col,k,short[k])
    chips+='<button class="chip" data-f="%d" style="%s"><i></i>%s</button>'%(k,col,short[k])
    notes+='<section id="s%d" class="sec" style="%s"><h2><span class="num">%d</span>%s</h2>'%(k,col,k,html.escape(s['title']))
    for qq in s['qs']:
        nq+=1;a=render_answer(qq['a']);qh=inline(qq['q'])
        notes+='<article class="qa"><h3 class="q">%s</h3><div class="a">%s</div></article>'%(qh,a)
        prac+=('<div class="card" id="c%d" data-sec="%d" data-i="%d" tabindex="0" role="button" aria-expanded="false" style="%s">'
               '<div class="tag">%d · %s</div><div class="q">%s</div><div class="a">%s</div>'
               '<div class="marks"><button class="mk y" data-m="y">Got it ✓</button><button class="mk n" data-m="n">Missed ✗</button></div></div>')%(nq,k,nq,col,k,short[k],qh,a)
    for f in s['foot']: notes+='<p class="foot">%s</p>'%inline(f)
    notes+='</section>'
sub=' '.join(intro)
TOTAL=nq
page=open(os.path.join(HERE,'tpl.html'),encoding='utf-8').read()
page=(page.replace('%%SUB%%',inline(sub)).replace('%%REL%%',inline(related)).replace('%%TOC%%',toc)
 .replace('%%CHIPS%%',chips).replace('%%NOTES%%',build_notes()).replace('%%PRAC%%',prac).replace('%%TOTAL%%',str(TOTAL)))
open(OUT,'w',encoding='utf-8').write(page)
print('questions',nq,[len(s['qs']) for s in sections])
