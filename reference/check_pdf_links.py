import requests,fitz,json,concurrent.futures
urls={
'excel':'https://www.customguide.com/cheat-sheet/excel-cheat-sheet.pdf',
'sql':'https://www.sqltutorial.org/wp-content/uploads/2016/04/SQL-cheat-sheet.pdf',
'windows':'https://learnsql.com/blog/sql-window-functions-cheat-sheet/Window_Functions_Cheat_Sheet.pdf',
'powerbi':'https://www.dataquest.io/wp-content/uploads/2025/01/Power-BI-Cheat-Sheet.pdf',
'python':'https://github.com/ehmatthes/pcc_3e/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc.pdf',
'pandas':'https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf',
'git':'https://education.github.com/git-cheat-sheet-education.pdf'}
def check(item):
 k,u=item
 try:
  r=requests.get(u,timeout=35);d={'url':u,'status':r.status_code,'pdf':r.content[:5]==b'%PDF-','bytes':len(r.content),'content_type':r.headers.get('content-type')}
  if d['pdf']:
   p=fitz.open(stream=r.content,filetype='pdf');d['pages']=len(p);d['sample']=p[0].get_text()[:180]
  return k,d
 except Exception as e:return k,{'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:results=dict(ex.map(check,urls.items()))
open('reference/shortcut_link_checks.json','w').write(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
