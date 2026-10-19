from pathlib import Path
from bs4 import BeautifulSoup
import gzip,json,html
R=Path('/home/user');path=R/'UK_Junior_Data_Analyst_Roadmap_Eastbourne.html'
base=R/'reference/roadmap_before_hindi.html.gz'
if not base.exists():base.write_bytes(gzip.compress(path.read_bytes()))
original=gzip.decompress(base.read_bytes()).decode();s=BeautifulSoup(original,'html.parser')
# Direct video pages and published descriptions checked 19 October 2026.
# These are language supports, not claims of complete syllabus equivalence.
choices={
'pCJ15nGFgVg':{'url':'https://www.youtube.com/watch?v=OX-iyb-21tk','title':'Excel fundamentals — Hindi / Hinglish','by':'Rishabh Mishra · ~1h16 · formulas, VLOOKUP and PivotTables; keep the Power Query and advanced-formula checkpoints.'},
'7mz73uXD9DA':{'url':'https://www.youtube.com/watch?v=7azCOKryADA','title':'SQL course — Hindi','by':'The iScale · ~4h51 · queries, joins, dates, CTEs and window functions; keep the short T-SQL bridge.'},
'QKIGsShyEsQ':{'url':'https://www.youtube.com/watch?v=E8ZDobnpQJ4','title':'SQL window functions — Hindi','by':'Data Prodigy · ~51 min · ranking, window frames and LAG/LEAD; use for this topic, not as the whole intermediate SQL course.'},
'FwjaHCVNBWA':{'url':'https://www.youtube.com/watch?v=bLz_aOtOpgc','title':'Power BI course — Hindi','by':'The iScale · ~12h full video; select relevant chapters and retain the modelling, DAX, security and refresh checkpoints.'},
'wUSDVGivd-8':{'url':'https://www.youtube.com/watch?v=YV0_puRO1u4&list=PLrN_S08trZepom2bLaBTt0QQt2XnmC7dc','title':'Python for data analysis — Hindi course','by':'freeCodeCamp Hindi · Aakash N S · six-part Zero to Pandas series (2020). Follow part numbers; use current pandas documentation for API changes.'}
}
count=0
for a in list(s.find_all('a',href=True)):
 key=next((k for k in choices if ('v='+k) in a['href']),None)
 if not key:continue
 d=choices[key]
 if 'resource' in a.get('class',[]):
  node=s.new_tag('a',href=d['url'],target='_blank',rel='noopener noreferrer');node['class']=['resource','hindi-option'];node.append(d['title']+' ↗');small=s.new_tag('small');small.string=d['by'];node.append(small)
 else:
  node=s.new_tag('span');node['class']=['hindi-option','hindi-inline'];link=s.new_tag('a',href=d['url'],target='_blank',rel='noopener noreferrer');link.string=d['title']+' ↗';node.append(link);small=s.new_tag('small');small.string=d['by'];node.append(small)
 a.insert_after(node);count+=1
note=s.new_tag('p',id='hindi-study-note');note['class']=['hindi-study-note'];note.string='Prefer Hindi explanations? Use the Hindi option for the topic you need—not a second compulsory course. Complete the same practice tasks and checkpoints whichever language you choose.'
s.select_one('#courses .note').insert_after(note)
style=s.new_tag('style',id='hindi-options-style');style.string='''.hindi-inline{display:block;margin:8px 0 12px;padding:10px 12px;background:#f1f5ee;border:1px solid #e1e8da;border-radius:8px;line-height:1.7}.hindi-inline>a{font-size:.78rem;font-weight:650}.hindi-inline>small{display:block;font-size:.68rem;color:#65756c;margin-top:3px}.course-links>.hindi-inline{flex-basis:100%;min-width:0;margin:0}.resource.hindi-option{background:#f1f5ee;border-color:#e1e8da}.hindi-study-note{font-size:.79rem;line-height:1.8;color:#61736b;margin:12px 0 20px}.hindi-option a,.hindi-option small{overflow-wrap:anywhere}@media(max-width:650px){.hindi-inline{padding:10px}.hindi-inline>a{font-size:.75rem}.hindi-inline>small{font-size:.67rem}}@media print{.hindi-inline{break-inside:avoid}.hindi-inline>a{font-size:8pt}.hindi-inline>small{font-size:7pt}.hindi-study-note{font-size:8pt}}''';s.head.append(style)
path.write_text(str(s));(R/'reference/hindi_learning_options.json').write_text(json.dumps({'checked':'2026-10-19','added_after_english_links':count,'choices':choices},indent=2))
# Ensure the change is strictly additive: remove new nodes and the DOM must match.
check=BeautifulSoup(path.read_text(),'html.parser')
for node in list(check.select('.hindi-option,#hindi-study-note,#hindi-options-style')):node.decompose()
assert str(check)==str(BeautifulSoup(original,'html.parser')),'Unexpected non-additive change'
assert count==15,count
print('Added',count,'Hindi resource entries after their English links; all other DOM content unchanged.')
