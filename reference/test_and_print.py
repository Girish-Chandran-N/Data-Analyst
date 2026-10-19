import json
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path('/home/user')
url=(root/'UK_Junior_Data_Analyst_Roadmap_Eastbourne.html').as_uri()
with sync_playwright() as p:
 browser=p.chromium.launch(args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(url);page.wait_for_timeout(300)
 print('loaded',page.title())
 print('images',page.locator('img').evaluate_all('(ims)=>ims.map(i=>({ok:i.complete&&i.naturalWidth>0,src:i.alt}))'))
 page.screenshot(path=str(root/'reference/desktop.png'),full_page=False)
 # Row-label click must toggle once, save and preserve scroll position.
 page.locator('#card-excel .arc-summary').click();page.locator('[data-key="excel-3"]').scroll_into_view_if_needed();page.wait_for_timeout(400)
 y1=page.evaluate('scrollY');page.locator('[data-key="excel-3"]').locator('..').click();page.wait_for_timeout(300);y2=page.evaluate('scrollY')
 assert page.locator('[data-key="excel-3"]').is_checked()
 assert abs(y1-y2)<2,(y1,y2)
 print('label toggle + no scroll jump',y1,y2)
 # Native checkbox and keyboard also work once.
 page.locator('[data-key="excel-3"]').click();assert not page.locator('[data-key="excel-3"]').is_checked()
 page.locator('[data-key="excel-3"]').focus();page.keyboard.press('Space');assert page.locator('[data-key="excel-3"]').is_checked()
 page.reload();assert page.locator('[data-key="excel-3"]').is_checked();print('persistence ok')
 page.evaluate('expandAll()');assert page.locator('.topic-card.open').count()==9
 page.evaluate('collapseAll()');assert page.locator('.topic-card.open').count()==0
 print('expand / collapse ok')
 # Test import/export helpers and storage failures.
 state=page.evaluate('saveState()');assert state['version']==4 and state['ticks']['excel-3'] is True
 page.evaluate('boxes().forEach(b=>b.checked=false);updateProgress();')
 page.set_viewport_size({'width':390,'height':844});page.evaluate('window.scrollTo(0,0)');page.wait_for_timeout(300)
 page.screenshot(path=str(root/'reference/mobile.png'),full_page=False)
 assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),page.evaluate('[document.documentElement.scrollWidth,innerWidth]')
 print('mobile horizontal overflow none')
 page.set_viewport_size({'width':1200,'height':900})
 page.evaluate('openForPrint()');page.emulate_media(media='print')
 page.pdf(path=str(root/'UK_Junior_Data_Analyst_Roadmap_Eastbourne.pdf'),format='A4',print_background=True,prefer_css_page_size=True,display_header_footer=True,header_template='<div></div>',footer_template='<div style="width:100%;font-size:8px;color:#797381;padding:0 14mm;display:flex;justify-content:space-between"><span>OPERATION DATA ANALYST · EASTBOURNE</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',margin={'top':'16mm','bottom':'16mm','left':'14mm','right':'14mm'})
 print('page errors',errors)
 assert not errors
 browser.close()
import pymupdf
pdf=pymupdf.open(root/'UK_Junior_Data_Analyst_Roadmap_Eastbourne.pdf')
print('PDF pages',len(pdf))
print('Text chars per page',[len(p.get_text()) for p in pdf])
for n in [0,1,2,4,5,10,15,len(pdf)-1]:
 if n<len(pdf):pdf[n].get_pixmap(matrix=pymupdf.Matrix(1,1)).save(root/f'reference/output_page_{n+1}.png')
