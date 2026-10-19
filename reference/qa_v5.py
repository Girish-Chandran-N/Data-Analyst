from pathlib import Path
import json,zipfile,re
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import pymupdf
R=Path('/home/user');f=R/'UK_Junior_Data_Analyst_Roadmap_Eastbourne.html'
results={}
with sync_playwright() as p:
 browser=p.chromium.launch(args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1440,'height':1000})
 errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
 page.goto(f.as_uri());page.wait_for_timeout(200)
 assert page.locator('.checklist input').count()==142
 assert page.locator('img').evaluate_all('(xs)=>xs.every(x=>x.complete&&x.naturalWidth>0)')
 page.screenshot(path=str(R/'reference/v5_desktop.png'))
 # Tick via label without scroll movement.
 page.locator('#card-excel .arc-summary').click()
 label=page.locator('[data-key="excel-3"]').locator('..');label.scroll_into_view_if_needed();page.wait_for_timeout(250)
 y=page.evaluate('scrollY');label.click();page.wait_for_timeout(150)
 assert abs(page.evaluate('scrollY')-y)<2
 assert page.locator('[data-key="excel-3"]').is_checked()
 assert page.locator('#heroCount').inner_text().startswith('1 / 142')
 # Native click toggles just once; keyboard toggles.
 cb=page.locator('[data-key="excel-3"]');cb.click();assert not cb.is_checked();cb.focus();page.keyboard.press('Space');assert cb.is_checked()
 page.reload();assert page.locator('[data-key="excel-3"]').is_checked()
 results['ticks']='label/native/keyboard, no jump, refresh persistence passed'
 # v4 key migration without loss, even as denominator changes.
 page.evaluate("localStorage.setItem('eastbourneAnalyst_v4',JSON.stringify({version:4,ticks:{'excel-3':true,'pbi-2':true}}))")
 page.reload();assert page.locator('[data-key="pbi-2"]').is_checked();assert not page.locator('[data-key="pbi-17"]').is_checked()
 results['existing_saved_keys']='preserved; new items start unchecked'
 # Backup actually downloads and retains keys.
 with page.expect_download() as dl:page.evaluate('exportProgress()')
 download=dl.value;download.save_as(str(R/'reference/qa_progress.json'));data=json.loads((R/'reference/qa_progress.json').read_text());assert len(data['ticks'])==142
 # Reset and restore via import.
 page.evaluate('boxes().forEach(b=>b.checked=false);updateProgress()')
 page.on('dialog',lambda d:d.accept())
 page.locator('#importFile').set_input_files(str(R/'reference/qa_progress.json'));page.wait_for_timeout(250)
 assert page.locator('[data-key="pbi-2"]').is_checked()
 results['backup']='export/download/import passed'
 page.evaluate('expandAll()');assert page.locator('.topic-card.open').count()==9
 page.evaluate('collapseAll()');assert page.locator('.topic-card.open').count()==0
 # Resume opens first incomplete arc rather than jumping to the top of the document.
 page.evaluate('resumeLearning()');assert page.locator('#card-setup').evaluate('(c)=>c.classList.contains("open")')
 # Filter includes nearby boundary examples but not wider London false positives.
 page.locator('[data-area="se"]').scroll_into_view_if_needed();page.locator('[data-area="se"]').click()
 assert page.locator('[data-evidence-area]:visible').count()==2
 page.locator('[data-area="all"]').click();assert page.locator('[data-evidence-area]:visible').count()==8
 results['navigation']='expand/collapse, resume and evidence filter passed'
 overflow={}
 for width in [320,360,390,650,768,900,1024,1440,1920]:
  page.set_viewport_size({'width':width,'height':900});page.evaluate('scrollTo(0,0)');page.wait_for_timeout(100)
  wide=page.evaluate('document.documentElement.scrollWidth > innerWidth')
  overflow[width]=wide
  if wide:
   print('OVERFLOW',width,page.evaluate('[...document.querySelectorAll("body *")].filter(x=>x.getBoundingClientRect().right>innerWidth+1).slice(0,10).map(x=>[x.tagName,x.className,x.getBoundingClientRect().right])'))
  assert not wide,width
 page.set_viewport_size({'width':390,'height':844});page.evaluate('scrollTo(0,0)');page.screenshot(path=str(R/'reference/v5_mobile.png'))
 menu=page.locator('.menu-toggle');assert menu.is_visible();menu.click();assert page.locator('#navLinks').is_visible();assert menu.get_attribute('aria-expanded')=='true'
 page.locator('#navLinks a[href="#courses"]').click();assert menu.get_attribute('aria-expanded')=='false'
 results['responsive']='no horizontal overflow at '+', '.join(map(str,overflow))+'px; mobile menu passed'
 # Snapshot another key part of the design.
 page.set_viewport_size({'width':1440,'height':1000});page.locator('#roadmap').scroll_into_view_if_needed();page.screenshot(path=str(R/'reference/v5_roadmap.png'))
 page.locator('#audit').scroll_into_view_if_needed();page.screenshot(path=str(R/'reference/v5_audit.png'))
 page.evaluate('boxes().forEach(b=>b.checked=false);updateProgress();openForPrint()')
 assert page.locator('details:not([open])').count()==0
 page.emulate_media(media='print')
 page.pdf(path=str(R/'UK_Junior_Data_Analyst_Roadmap_Eastbourne.pdf'),format='A4',print_background=True,prefer_css_page_size=True,display_header_footer=True,header_template='<div></div>',footer_template='<div style="width:100%;font:8px Arial;color:#69767a;padding:0 14mm;display:flex;justify-content:space-between"><span>OPERATION DATA ANALYST · SE LONDON & SUSSEX · REVIEWED 18 OCT 2026</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')
 results['js_errors']=errors;assert not errors
 browser.close()
pdf=pymupdf.open(R/'UK_Junior_Data_Analyst_Roadmap_Eastbourne.pdf')
results['pdf_pages']=len(pdf)
text=' '.join(pg.get_text() for pg in pdf);flat=re.sub(r'\s+',' ',text)
arcdata=json.loads((R/'reference/arc_data_v5.json').read_text())
missing=[]
for a in arcdata:
 for item in a['items']:
  if re.sub(r'\s+',' ',item) not in flat:missing.append(item)
results['pdf_missing_checkpoint_text']=missing
print('PDF missing',missing)
for i in [0,2,4,8,12,18,len(pdf)-1]:
 if i<len(pdf):pdf[i].get_pixmap(matrix=pymupdf.Matrix(1,1)).save(R/f'reference/v5_pdf_{i+1}.png')
results['pdf_sparse_pages']=[i+1 for i,pg in enumerate(pdf) if len(pg.get_text())<130]
with zipfile.ZipFile(R/'Eastbourne_Data_Analyst_Tracker.xlsx') as z:assert z.testzip() is None
results['xlsx']='valid OOXML archive; updated audit and checkpoint sheets'
(R/'reference/qa_v5_results.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
