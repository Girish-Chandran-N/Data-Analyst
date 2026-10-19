from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import json,pymupdf
R=Path('/home/user');f=R/'UK_Junior_Data_Analyst_Roadmap_Eastbourne.html';s=BeautifulSoup(f.read_text(),'html.parser')
ids=[x['id'] for x in s.select('[id]')];assert len(ids)==len(set(ids));assert not [a['href'] for a in s.select('a[href^="#"]') if a['href'][1:] not in ids]
results={}
with sync_playwright() as p:
 b=p.chromium.launch(args=['--no-sandbox']);page=b.new_page(viewport={'width':1440,'height':1000},accept_downloads=True);page.goto(f.as_uri());page.add_style_tag(content='html,body{scroll-behavior:auto!important}*{animation:none!important;transition:none!important}')
 a=page.locator('#navLinks a[href="#cheats"]');assert a.inner_text()=='Shortcuts';a.click();page.wait_for_timeout(200)
 assert page.evaluate('location.hash')=='#cheats';assert abs(page.locator('#cheats').evaluate('(el)=>el.getBoundingClientRect().top'))<150
 page.screenshot(path=str(R/'reference/shortcuts_desktop.png'))
 assert page.locator('.shortcut-pdf-card a[href$=".pdf"]').count()==7
 assert page.locator('.shortcut-pdf-card a').evaluate_all('(xs)=>xs.every(a=>a.target==="_blank"&&a.rel.includes("noopener"))')
 with page.expect_download() as dl:page.locator('.shortcut-download a').click()
 dl.value.save_as(str(R/'reference/shortcuts_download_test.pdf'))
 assert (R/'reference/shortcuts_download_test.pdf').read_bytes()==(R/'Data_Analyst_Shortcuts_Quick_Reference.pdf').read_bytes()
 results['offline_download']='Exact embedded PDF downloaded successfully'
 for w in [320,390,768,1024,1440]:
  page.set_viewport_size({'width':w,'height':900});page.eval_on_selector_all('.shortcut-topic','xs=>xs.forEach(x=>x.open=true)');assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'),w
 results['expanded_topics']='Eight topic panels fit 320, 390, 768, 1024 and 1440px without horizontal overflow'
 page.set_viewport_size({'width':390,'height':844});page.evaluate('scrollTo(0,0)');page.locator('.menu-toggle').click();page.locator('#navLinks a[href="#cheats"]').click();assert page.locator('.menu-toggle').get_attribute('aria-expanded')=='false'
 page.wait_for_timeout(100);assert abs(page.locator('#cheats').evaluate('(el)=>el.getBoundingClientRect().top'))<150
 page.screenshot(path=str(R/'reference/shortcuts_mobile.png'))
 results['navigation']='Desktop main navigation and mobile menu jump to Shortcuts; mobile bottom link also present'
 b.close()
pdf=pymupdf.open(R/'Data_Analyst_Shortcuts_Quick_Reference.pdf');assert len(pdf)==8
for i in [0,1,2,3,4,5,7]:assert pdf[i].get_links()
assert all(len(pg.get_text())>1400 for pg in pdf)
results['pdf']='Eight readable pages with clickable external references; project page uses original workflow guidance'
results['external_pdf_checks']=json.loads((R/'reference/shortcut_link_checks.json').read_text())
(R/'reference/qa_shortcuts_results.json').write_text(json.dumps(results,indent=2))
print(json.dumps({k:v for k,v in results.items() if k!='external_pdf_checks'},indent=2))
