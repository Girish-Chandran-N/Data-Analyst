# UK Data Analyst Roadmap — Market, Course & Syllabus Audit
**Reviewed: 18 October 2026 · Target: South-East London, Brighton/Hove and the wider South East**

## Executive recommendation
Keep **Excel → SQL → Power BI → defensible projects**, with statistics, data quality and communication throughout. Keep Python/pandas as a useful later addition, but do not make every entry application wait for it. The previous plan had a sound stack but a genuine resource-to-syllabus mismatch: the old SQL link did not support all the CTE/window checkpoints. Power BI operational tasks also needed to be explicit.

No separate agent partners were available. This audit uses three passes by the same assistant: hiring relevance, curriculum alignment, and usability. It is not an independent panel review.

## Scope and limits
Eight purposefully chosen advert profiles were reviewed: five junior/entry-route examples and three experienced-role comparators. This is not a representative sample, vacancy census or a basis for skill-frequency percentages. Full text, employer search-index excerpts and unavailable pages are labelled below. Local SE London examples were experienced roles, so they do not establish a large junior market. Course review used published outlines, files and creator pages—not a minute-by-minute viewing of all videos.

## 1. Regional evidence and what it means
### 01. EDF — Reporting Analyst
- **Geography:** Brighton / Hove.
- **Level:** Entry-friendly reporting example; not explicitly titled junior.
- **Status:** Historical: advertised closing date 2 March 2026; direct fetch reached verification screen.
- **Evidence access:** Employer search-index excerpt; direct page access limited.
- **Signals:** Excel formulas and data manipulation; Power BI learning; accuracy, dashboards and stakeholder communication.
- **Decision for the roadmap:** Supports an Excel/reporting-first application route. No evidence that every entry role requires Python or SQL.
- **Source:** [1](https://careers.edfenergy.com/job/reporting-analyst-in-hove-jid-1596)

### 02. Legal & General — Data Analyst Apprenticeship 2026
- **Geography:** Hove.
- **Level:** Apprenticeship entry route.
- **Status:** Expired in indexed employer page; September 2026 intake. Direct fetch reached verification screen.
- **Evidence access:** Detailed employer search-index text; direct page access limited.
- **Signals:** Analysis, coding, visualisation, automation and non-technical communication; qualification, residency and right-to-work conditions.
- **Decision for the roadmap:** Add apprenticeships as an optional entry route. Check each future advert and current funding rules; do not generalise this advert's residency condition to every apprenticeship.
- **Source:** [1](https://careers.legalandgeneral.com/job/apprenticeship-data-analyst-hove-2026-in-brighton-and-hove-jid-6773)

### 03. Kreston Reeves — Junior Data Quality & Reporting Analyst
- **Geography:** Canterbury, Kent — adjacent-market comparator, not Brighton or SE London.
- **Level:** Junior, 12-month fixed term.
- **Status:** Employer page accessible with Apply Now on review date; recheck before applying.
- **Evidence access:** Full employer advert read.
- **Signals:** Advanced Excel, PivotTables, Power Query, formulas, cleansing, audit trails, GDPR, documentation and stakeholders; no explicit SQL/Python requirement in the read specification.
- **Decision for the roadmap:** Strengthen data-quality evidence, documented checks and privacy. Canterbury is a separate commute decision; no salary inferred from aggregator estimates.
- **Source:** [1](https://krestonreeves.pinpointhq.com/postings/60adaac6-a4bf-4a3d-b68c-8e8aff63d3f4)

### 04. Barts Health NHS Trust — Junior Information Analyst Returns
- **Geography:** Canary Wharf E14 — East London, not South-East London.
- **Level:** Band 5 junior.
- **Status:** NHS Jobs explicitly says closed; posted 29 September 2026.
- **Evidence access:** Full NHS Jobs advert and displayed person specification read.
- **Signals:** MS SQL Server and BI tools, reporting, quality and communication; NHS standard definitions and reporting knowledge essential; automation tools desirable; advert also lists Visual Basic/HTML among technology experience.
- **Decision for the roadmap:** Add a short SQL Server/T-SQL bridge and an optional NHS domain pack. A general portfolio does not automatically satisfy NHS essential criteria; do not turn one advert's legacy technologies into a universal syllabus.
- **Source:** [1](https://beta.jobs.nhs.uk/candidate/jobadvert/C9259-26-1692)

### 05. Seven Investment Management — Junior Data Analyst
- **Geography:** London / City — wider-London comparator, not verified SE London base.
- **Level:** Junior.
- **Status:** Employer URL now redirects to Vacancy not found; historical indexed specification only.
- **Evidence access:** Detailed employer search-index text; direct fetch confirmed vacancy-not-found redirect.
- **Signals:** Power BI, Excel, numerical and concise communication skills; Python highly beneficial; expected PL-300 within six-month probation; basic financial-services context.
- **Decision for the roadmap:** Keep Python as a useful differentiator. PL-300 can be employer-specific after hiring, not a universal prerequisite or a promised sponsored exam.
- **Source:** [1](https://careers.7im.co.uk/vacancies/588/junior-data-analyst.html)

### 06. Oxleas NHS Foundation Trust — Performance and Information Analyst
- **Geography:** Dartford DA2; trust serves Bexley, Bromley and Greenwich.
- **Level:** Experienced Band 7 — not junior.
- **Status:** NHS Jobs explicitly closed; posted 4 March 2026.
- **Evidence access:** Full advert duties and experience requirement read.
- **Signals:** Minimum three years SQL/database/warehouse experience; SQL, SSRS, Excel, Power BI; data quality and staff supervision.
- **Decision for the roadmap:** Local ecosystem signal only. Do not require three years' experience, stored procedures/triggers or people management before beginning junior applications.
- **Source:** [1](https://www.jobs.nhs.uk/candidate/jobadvert/C9277-26-0252)

### 07. Lewisham and Greenwich NHS Trust — Advanced Information Analyst
- **Geography:** Catford SE6 — South-East London.
- **Level:** Advanced Band 7 — not junior.
- **Status:** Advert closing date 17 May 2026; historical.
- **Evidence access:** Detailed NHS Jobs search result / person-specification text read.
- **Signals:** Advanced SQL and Excel, Python/R forecasting, Power BI/SSRS, NHS datasets and information governance; significant experience.
- **Decision for the roadmap:** Confirms relevant local stack but advanced forecasting, optimisation and expert SQL are later specialisms, not a junior baseline.
- **Source:** [2](https://www.jobs.nhs.uk/candidate/jobadvert/C9197-26-0415)

### 08. MetLife — Senior Data and Insights Analyst (body: Senior Data and Reporting Analyst)
- **Geography:** Brighton.
- **Level:** Senior — preferred 3–5+ years.
- **Status:** Employer page accessible; posted 2 October 2026; not counted as a junior opportunity.
- **Evidence access:** Full employer responsibilities and requirements read.
- **Signals:** Excel, Power Query, Power BI/DAX, SQL, governance, lineage, controlled change and automation; Python/Power Automate preferred; legacy VBA advantageous.
- **Decision for the roadmap:** Add lightweight report handover/change-log concepts now. Keep Power Automate, VBA and advanced platform engineering optional, not compulsory junior tools.
- **Source:** [24](https://www.metlifecareers.com/en_US/ml/JobDetail/Senior-Data-and-Reporting-Analyst/20930)

## 2. Course decisions
The core videos are free. Some creator problem packs, notes, certificates and newer datasets are paid; none are mandatory here. Microsoft PL-300 is a separate professional certification, not the same as a creator completion certificate.

### 01. Excel for Data Analytics — KEEP · SELECT CHAPTERS
- **Scope:** Formulas/functions, charts, tables, PivotTables, Power Query, Power Pivot and two projects are present in the published outline.
- **Study:** Prioritise chapters 2–5 and 7. Add UK date parsing, reconciliation, exception logs and a repeatable month-file refresh. Revisit basics only if your diagnostic fails.
- **Defer:** Solver, Scenario Manager, Goal Seek and deeper Power Pivot are useful later, not blockers before junior reporting applications.
- **Access/limits:** The creator lists free videos/files but paid supporter problems and certificates. If individual Excel files fail, download the repository ZIP or use the creator’s alternate file link.
- [Learning link](https://www.youtube.com/watch?v=pCJ15nGFgVg) · [Outline / creator files](https://github.com/lukebarousse/Excel_Data_Analytics_Course)

### 02. SQL foundations + selected intermediate — REPLACE SOLE RESOURCE
- **Scope:** The original 2018 freeCodeCamp course lists MySQL basics, joins, nested queries and database design. Its published chapters do not include CTEs or window functions.
- **Study:** Use Luke’s foundations course for analyst queries, CASE and CTEs. Supplement window/date/cleaning topics with selected Intermediate SQL lessons ↗ and the official T-SQL window lesson.
- **Defer:** Do not spend time on triggers, database administration or a second full beginner course. Keep one primary database and a short dialect bridge.
- **Access/limits:** PostgreSQL is the main course dialect. The free starter job dataset is historical 2023 data, not evidence of today’s London or Brighton market. Supporter exercises/certificates are paid.
- [Learning link](https://www.youtube.com/watch?v=7mz73uXD9DA) · [Outline / creator files](https://www.lukebarousse.com/sql)

### 03. Power BI for Data Analytics — KEEP + OPERATIONS PACK
- **Scope:** Published modules include Grand Tour, visualisations, Power Query and DAX, plus star-schema/dashboard projects.
- **Study:** Explicitly add workspace roles/access, gateway and scheduled refresh concepts, a Desktop RLS test, Performance Analyzer, mobile layout and accessibility. Use current Microsoft Learn guidance.
- **Defer:** Do not assume the creator’s “PL-300 aligned” description guarantees full current exam coverage. Newer exam topics need a separate exam checklist if you choose certification.
- **Access/limits:** Use the creator’s complete course-file link ↗ ; the repository warns that some large files are missing. Some Service exercises require a suitable account/licence; no paid sharing is required for the portfolio.
- [Learning link](https://www.youtube.com/watch?v=FwjaHCVNBWA) · [Outline / creator files](https://github.com/lukebarousse/PowerBI_Data_Analytics_Course)

### 04. Python for Data Analytics — KEEP · LATER IN SEQUENCE
- **Scope:** The outline covers basics, pandas, NumPy, Matplotlib, advanced cleaning/manipulation and a project.
- **Study:** Prioritise functions, dates, CSVs, missing values, groupby, merge validation, readable plots and reproducible export. Add one small test fixture and rerun from a clean environment.
- **Defer:** Defer deep OOP, machine learning, scraping and advanced plotting unless target roles justify them. Do not postpone Excel/BI applications until every Python chapter is complete.
- **Access/limits:** Use current notebooks when package APIs differ from the video. Free videos/code do not imply every practice problem or certificate is free.
- [Learning link](https://www.youtube.com/watch?v=wUSDVGivd-8) · [Outline / creator files](https://github.com/lukebarousse/Python_Data_Analytics_Course)

### 05. Statistics + official guidance — KEEP + APPLIED TASKS
- **Scope:** Khan Academy is a broad reference, not a role-specific analyst syllabus; use only the topics your checkpoint requires.
- **Study:** Practise denominators, weighted averages, percent vs percentage points, bias, uncertainty, correlation and plain-English communication on your own data.
- **Defer:** Do not add a full probability or data-science qualification. Introductory test reasoning is enough unless a role asks for deeper inference.
- **Access/limits:** Complement learning with ICO principles ↗ and the published methodology for the public dataset you use.
- [Learning link](https://www.khanacademy.org/math/statistics-probability) · [Outline / creator files](https://www.ons.gov.uk/)

## 3. Coverage matrix
| Skill group | Decision | Where | Proof |
|---|---|---|---|
| Excel formulas, lookups, pivots | Keep | Excel | Refreshable workbook, checked against raw totals. |
| Excel exceptions / combine files | Make explicit | Excel | Exceptions tab + source-file field + tested refresh. |
| SQL joins, NULLs, dates, CASE | Keep | SQL | Explain grain and reconcile joins. |
| CTEs and window functions | Fix resource mismatch | SQL | Selected intermediate lessons + 30-query project. |
| SQL Server / T-SQL | Add short bridge | SQL | Translate five queries; not another full database course. |
| Star schema / DAX / date table | Keep | Power BI | Validated model and five reconciled measures. |
| Refresh / gateway / workspace access | Add explicit tasks | Power BI | Explain setup and failure modes; use mock runbook if no Service account. |
| Row-level security / safe sharing | Add explicit tasks | Power BI | Desktop View as test and access explanation. |
| Performance / accessibility / mobile | Add explicit tasks | Power BI | One measured visual and a tested mobile layout. |
| Stats / denominators / uncertainty | Keep and apply | Statistics | One-page briefing with a limitation. |
| UK GDPR / responsible AI | Add explicit tasks | Statistics | Document permitted data use and independent validation. |
| Stakeholder question / acceptance checks | Add explicit tasks | Statistics / capstone | Two acceptance criteria and an external check; analytics practice, not BA training. |
| pandas / automation / tests | Keep and strengthen | Python | Known-output fixture + reproducible script. |
| Lineage / handover / change log | Add explicit tasks | Capstone | Owner, source, metric definitions, refresh, checks and version history. |
| Person-spec evidence / supporting statement | Add explicit tasks | Interview / job hunt | Map claims to criteria and record genuine gaps. |
| NHS domain definitions | Targeted optional pack | Job hunt / project | Read the NHS Data Dictionary and dataset methodology for the role. |
| Finance / retail context | Targeted practice | Portfolio | Metric glossary; label assumptions and synthetic data. |
| Power Automate / VBA / SSRS | Optional awareness | After core | Investigate only when repeated target adverts justify it. |
| ML / full-stack / cloud engineering | Deliberately excluded | Later specialisms | Not required by this reporting-first plan. No BA core. |

### Important completeness boundary
The revised plan covers the junior reporting/analytics groups identified in this sample. It does not claim to teach every employer’s proprietary system, NHS domain knowledge, advanced forecasting, legacy language or certification objective. A list of completed checkpoints is not proof of meeting every essential criterion.

### Optional PL-300 boundary
The official guide effective 20 April 2026 covers preparation (25–30%), modelling (25–30%), visualisation/analysis (25–30%), and management/security (15–20%). The roadmap now includes refresh/gateway concepts, access roles, RLS, performance and mobile/accessibility tasks. If taking the exam, review every current objective separately, including newer storage modes, calculation groups, visual calculations, Copilot features and sensitivity/governance topics. Do not buy platform capacity just to complete optional exercises. [Official guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300)

## 4. Keep the workload realistic
The plan still budgets 336 hours: 28 × 12. The 22 new checkpoints are integrated into existing projects, not 22 extra hours promised for free. Select relevant course chapters, skip duplicated lessons, and extend the calendar if a boss task needs longer. Five projects are a learning ladder; lead applications with your best three, not five equally polished case studies.

| Arc | Weeks | Learn | Build / applications | Review | Total hours |
|---|---|---:|---:|---:|---:|
| Setup, workflow & proof of work | 1 | 3 | 7 | 2 | 12 |
| Excel Pro & Power Query | 2–4 | 8 | 24 | 4 | 36 |
| SQL for reliable answers | 5–8 | 10 | 32 | 6 | 48 |
| Power BI, modelling & DAX | 9–13 | 12 | 40 | 8 | 60 |
| Statistics, quality & storytelling | 14–15 | 5 | 15 | 4 | 24 |
| Python, pandas & reproducibility | 16–19 | 10 | 32 | 6 | 48 |
| An end-to-end analytics capstone | 20–23 | 4 | 38 | 6 | 48 |
| SQL tests & interview confidence | 24–25 | 3 | 17 | 4 | 24 |
| Applications, referrals & feedback | 26–28 | 2 | 28 | 6 | 36 |

## 5. Practical recommendations
1. **Now:** keep improving Excel and start SQL; do not buy another full bootcamp. Use the diagnostic to avoid restarting skills you can already demonstrate.
2. **SQL:** switch the main foundation link to the analytics-focused PostgreSQL course, add selected intermediate window lessons, then a short T-SQL bridge for Microsoft-oriented roles. The old freeCodeCamp course remains a valid alternative for fundamentals, not a complete advanced path.
3. **Power BI:** treat a report as a small product: correct numbers, tested access, documented refresh, accessible layout and a runbook. A Desktop RLS mock is useful without a paid Service plan.
4. **Applications:** consider genuine Excel-led junior roles when you independently meet their criteria; broaden to SQL/BI roles as those deliverables become ready. Do not wait for a ceremonial week number.
5. **Geography:** create separate searches for SE London boroughs, Brighton/Hove, wider London and nearby Kent. Verify the office address, attendance requirement and your door-to-door travel costs. No assumed commute from Eastbourne or Bexley.
6. **Entry routes:** consider Data Technician or Data Analyst apprenticeships if eligible. Check each advert and current funding rules; one historical employer’s residency requirements do not establish a rule for everyone.
7. **Avoid misleading ads:** exclude self-funded training programmes from a vacancy count. Do not treat aggregator salary estimates, neighbouring-area search results or expired ads as verified local opportunities.
8. **Add later only if needed:** Power Automate, VBA, SSRS, Tableau, GA4, dbt/cloud and ML are not blanket requirements for this reporting-first path. Do not confuse an experienced-role wish list with your initial syllabus.

## 6. Website changes
- Retained the reference’s cream palette and exact original artwork.
- Rebuilt the hero into a desktop split layout with a calm progress dashboard and consistent tabular numerals.
- Added mobile menu, cleaner spacing, touch-friendly controls and a mobile-first stacked layout.
- Added desktop roadmap sidebar, Resume learning and consistent section/arc numbering.
- Added honest advert statuses, geographic filters, course decisions and the syllabus coverage matrix.
- Preserved stable existing checkpoint keys; the same local save format supports the 142-item syllabus. New items start unchecked, so completion percentage may drop without losing existing ticks.
- Updated the Excel tracker with 142 checkpoints, market evidence, coverage audit and study-budget sheets. HTML and Excel do not automatically sync.
- Browser QA and PDF output are checked separately; the PDF is static.

## 7. Source trail
- [Excel course outline](https://github.com/lukebarousse/Excel_Data_Analytics_Course) — Module list and file-download warning read; eight chapters plus projects. Paid problem packs/certificate distinguished on creator page.
- [SQL foundations](https://www.lukebarousse.com/sql) — Creator confirms free 4+ hour video and PostgreSQL project. Free dataset is historical 2023; supporter problems/certificate are paid.
- [Intermediate SQL](https://www.lukebarousse.com/int-sql) — Creator confirms free 6+ hour video, Contoso dataset and PostgreSQL workflow; use selected window/date/cleaning lessons, not another whole compulsory course.
- [Old SQL course](https://www.youtube.com/watch?v=HXV3zeQKqGY) — Published chapter list inspected: MySQL basics, joins, nested queries and schema design; no CTE/window-function chapters listed. Not a sufficient sole resource for the roadmap.
- [Power BI course outline](https://github.com/lukebarousse/PowerBI_Data_Analytics_Course) — Grand Tour, Visualizations, Power Query and DAX plus projects. Full files should be downloaded using creator's Google Drive link due to repository size limits. Do not infer complete Service/security or current exam coverage from the outline.
- [Python course outline](https://github.com/lukebarousse/Python_Data_Analytics_Course) — Basics, advanced pandas/Matplotlib and project. Use current notebooks; observed compatibility fixes mean copying older video syntax is not always sufficient.
- [Current PL-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300) — Skills as of 20 April 2026: prepare 25–30%, model 25–30%, visualize/analyze 25–30%, manage/secure 15–20%. Includes Service, gateway/refresh, roles/RLS, sensitivity, performance, mobile and accessibility; also newer exam-specific topics.
- [T-SQL learning path](https://learn.microsoft.com/en-us/training/paths/get-started-querying-with-transact-sql/) — Official search result identifies querying and modifying with T-SQL; used as bridge resource, not a replacement mandatory database course.
- [T-SQL window lesson](https://learn.microsoft.com/en-us/training/modules/write-queries-that-use-window-functions/) — Official learning objectives: OVER, ranking, aggregate and offset functions.
- [UK GDPR principles](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/) — Official principles include minimisation, accuracy, security, purpose/storage limitation and accountability. This roadmap is not legal training or legal advice.

UK salary context: [Prospects — Data analyst](https://www.prospects.ac.uk/job-profiles/data-analyst/), re-read 18 October 2026. Typical UK starting range £28,000–£32,000 is national guidance, not a Brighton or SE London guarantee.

This is a learning and job-search recommendation, not legal, immigration or financial advice and not a promise of employment.