"""Build the linked System Context document using Graphviz (standard library only)."""
from pathlib import Path
import subprocess
import html


ROOT = Path(__file__).resolve().parents[1]
components = [
('C01','Kund:innen','Nutzen FinSec zur Verwaltung ihrer verbundenen Bankkonten.','Extern: Geräte und eigenes Verhalten liegen außerhalb von FinSec; FinSec verantwortet sichere Authentisierung, Sitzungen und Datenübertragung.'),
('C02','Web-Frontend','Bietet die browserbasierte Oberfläche mit eingeschränktem Funktionsumfang.','FinSec verantwortet die Webanwendung und ihre sichere Kommunikation; der genaue Funktionsumfang ist noch offen.'),
('C03','Mobile App (geplant)','Bietet auf dem persönlichen Mobilgerät den vollen geplanten Funktionsumfang.','FinSec verantwortet App-Code, lokale Datenverarbeitung und Kommunikation; Betriebssystem und Gerät liegen außerhalb seiner Kontrolle. Plattform und Realisierungstermin sind offen.'),
('C04','Anwendungslogik','Steuert Anwendungsfälle einschließlich Nutzer- und Zugriffsverwaltung.','FinSec verantwortet Autorisierung, Sitzungsprüfung, fachliche Regeln und die sichere Koordination der Backend-Bereiche.'),
('C05','Finanzdatenverarbeitung','Klassifiziert, aggregiert und analysiert Finanzdaten für Auswertungen und Sparhinweise.','FinSec verantwortet korrekte und zweckgebundene Verarbeitung sowie den Schutz der verarbeiteten Daten.'),
('C06','Bankanbindung','Ruft autorisierte Kontodaten autonom ab und leitet Zahlungsaufträge an Banken weiter.','FinSec verantwortet Einwilligungs- und Berechtigungsprüfung, geschützte Zugangsmittel sowie sichere API-Aufrufe und Antwortverarbeitung.'),
('C07','Datenbank','Speichert Nutzer-, Verbindungs- und Finanzdaten für FinSec.','FinSec verantwortet Zugriffsschutz, Datenminimierung, Aufbewahrung, Löschung und die Absicherung von Speicherung und Sicherungen.'),
('C08','Bank 1','Stellt Kontodaten und Zahlungsdienste einer angebundenen EU-Bank bereit.','Extern: Die Bank verantwortet ihre Systeme und die Ausführung von Zahlungen; FinSec verantwortet seine Integrationsseite.'),
('C09','Bank 2','Stellt Kontodaten und Zahlungsdienste einer weiteren angebundenen EU-Bank bereit.','Extern: Verantwortung wie C08; die Bank bleibt eine eigenständige externe Partei.'),
('C10','Bank n','Steht stellvertretend für weitere angebundene EU-Banken.','Extern: Verantwortung wie C08; n bezeichnet die Erweiterbarkeit und keine konkrete Bank.'),
]
flows=[]
def flow(i,a,b,title,desc,resp):
    flows.append((i,a,b,title,desc,resp))
for i,target in [('F01','C02'),('F02','C03')]:
    flow(i,'C01',target,'Nutzung & Rückmeldungen','Hin: Anmeldedaten, Kontoverknüpfung, Abfragen und – soweit unterstützt – Überweisungsdaten. Zurück: Kontoinformationen, Auswertungen und Auftragsstatus.','FinSec verantwortet geschützte Übertragung, sichere Endpunkte und Eingabeprüfung; Kundengeräte bleiben extern.')
for i,src in [('F03','C02'),('F04','C03')]:
    flow(i,src,'C04','Anfragen & Ergebnisse','Hin: Anmeldeanfrage, Sitzungsnachweis, Datenabfragen und unterstützte Überweisungsaufträge. Zurück: Anmeldeergebnis, Finanzdaten, Auswertungen und Auftragsstatus.','Vollständig FinSec: Authentisierung, Autorisierung, Vertraulichkeit und Integrität der Kommunikation.')
flow('F05','C04','C05','Analyseauftrag & Auswertung','Hin: Analyseauftrag und zulässige Finanzdaten. Zurück: Klassifikation, Aggregate, Auswertungen und Sparhinweise.','Vollständig FinSec; Zugriff und Zweckbindung müssen auch zwischen internen Bereichen gelten.')
flow('F06','C04','C06','Bankauftrag & Ergebnis','Hin: autorisierte Kontoabrufe und Zahlungsaufträge. Zurück: Kontodaten, Zahlungsstatus und Fehler.','Vollständig FinSec; Auftragsberechtigung und konsistente Statusverarbeitung sicherstellen.')
flow('F07','C04','C07','Lesen & Speichern','Hin: Datenabfragen und zu speichernde Nutzer-, Verbindungs- und Finanzdaten. Zurück: gespeicherte Daten und Speicherstatus.','Vollständig FinSec; Datenbankzugriffe absichern und auf notwendige Rechte begrenzen.')
for i,target in [('F08','C08'),('F08','C09'),('F08','C10')]:
    flow(i,'C06',target,'Kontoabruf & Zahlungsauftrag','Hin: autorisierter Kontodatenabruf und Zahlungsaufträge. Zurück: Kontostände, vergangene und geplante Transaktionen sowie Zahlungsstatus.','Geteilt: FinSec verantwortet seinen Endpunkt, Autorisierung, geschützten Transport und Antwortprüfung; die Bank ihren Endpunkt und die Transaktionsausführung.')
for i,a,b in [('F11','C08','C09'),('F11','C09','C10')]:
    flow(i,a,b,'Datenaustausch / Transaktionen','Schematischer bidirektionaler Austausch zwischen Banken, etwa zur Abwicklung bankübergreifender Transaktionen.','Außerhalb von FinSec; die beteiligten Banken verantworten diesen Austausch. Die Linien behaupten keine konkrete technische Direktverbindung oder Topologie.')
lines=['digraph FinSec {','graph [rankdir=TB, newrank=true, splines=polyline, bgcolor="white", fontname="DejaVu Sans", fontsize=18, pad=0.35, nodesep=0.65, ranksep=0.8, compound=true, label="FinSec · System Context", labelloc=t];','node [shape=box, style="rounded,filled", fillcolor="#f1f5f9", color="#64748b", fontname="DejaVu Sans", fontsize=12, margin="0.22,0.16", target="_top"];','edge [dir=both, color="#475569", fontname="DejaVu Sans", fontsize=10, arrowsize=0.7, target="_top"];']
for i,name,_,_ in components:
    label=name.replace(' (geplant)','\\n(geplant)')+'\\n'+i
    extra=', shape=cylinder' if i=='C07' else ''
    lines.append(f'{i} [id="{i}", label="{label}", URL="System%20Context.md#{i}", tooltip="{name} – Beschreibung"{extra}];')
lines += ['subgraph cluster_responsibility { label="FinSec-Verantwortung · einschließlich sicherer Verbindungen zu externen Parteien"; style="rounded,filled"; color="#d6a900"; fillcolor="#fff8cc"; penwidth=2; margin=24;', 'client_link [shape=point, width=0.03, label="", color="#d6a900"];', 'subgraph cluster_frontends { label="Frontends"; color="#94a3b8"; fillcolor="#ffffff"; C02; C03; {rank=same; C02; C03;} }', 'subgraph cluster_backend { label="Backend · drei funktionale Bereiche"; color="#94a3b8"; fillcolor="#ffffff"; C04; C05; C06; {rank=same; C05; C06;} }', 'C07;', 'bank_link [shape=point, width=0.03, label="", color="#d6a900"];', '{rank=same; C04; C07;} C07 -> bank_link [style=invis];', '}', '{rank=same; C08; C09; C10;}']
seen_edges=set()
for i,a,b,title,_,_ in flows:
    edge_id=i if i not in seen_edges else f"{i}-{b}"
    seen_edges.add(i)
    attrs=f'id="{edge_id}", label="{i}", URL="System%20Context.md#{i}", tooltip="{i}: {title}"'
    if i in ('F01','F02'):
        # Split external flows so the responsibility boundary includes their internal segment.
        if i=='F01': lines.append('C01 -> client_link [dir=none, color="#94a3b8"];')
        lines.append(f'client_link -> {b} [{attrs}];')
    elif i in ('F08','F09','F10'):
        if i=='F08' and b=='C08': lines.append('C06 -> bank_link [dir=none, color="#475569"];')
        lines.append(f'bank_link -> {b} [{attrs}];')
    else:
        extra=', constraint=false, style=dashed, color="#94a3b8"' if i in ('F11','F12') else ''
        lines.append(f'{a} -> {b} [{attrs}{extra}];')
lines.append('}')
(ROOT/'finsec.dot').write_text('\n'.join(lines)+'\n')
subprocess.run(['dot','-Tcanon','finsec.dot','-o','finsec.formatted.dot'],cwd=ROOT,check=True)
subprocess.run(['dot','-Tsvg','finsec.dot','-o','finsec.svg'],cwd=ROOT,check=True)
svg=(ROOT/'finsec.svg').read_text()
svg=svg[svg.index('<svg'):]
# Inline SVG has internal links; separate SVG opens the same description document.
svg=svg.replace('System%20Context.md#', '#description-')
sections=[]
for i,name,desc,resp in components:
    sections.append(f'<section id="description-{i}"><h3>{i} · {html.escape(name)}</h3><p>{html.escape(desc)}</p><p><strong>Verantwortung:</strong> {html.escape(resp)}</p><a href="#{i}">↑ Zur Komponente im Diagramm</a></section>')
sections.append('<h2>Datenflüsse</h2><p>Durchgezogene Pfeile sind bidirektionale fachliche Datenflüsse; sie legen kein Netzwerkprotokoll fest. F01–F04 gelten jeweils im Funktionsumfang des Frontends.</p>')
for i,a,b,title,desc,resp in dict((f[0], f) for f in flows).values():
    sections.append(f'<section id="description-{i}"><h3>{i} · {a} ↔ {b} · {html.escape(title)}</h3><p>{html.escape(desc)}</p><p><strong>Verantwortung:</strong> {html.escape(resp)}</p><a href="#{i}">↑ Zum Datenfluss im Diagramm</a></section>')
page='''<!doctype html><html lang="de"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>FinSec – System Context</title><style>body{font:16px/1.6 system-ui,sans-serif;color:#172033;max-width:1400px;margin:auto;padding:32px}h1,h2,h3{line-height:1.25}svg{width:100%;height:auto;min-width:850px}.diagram{overflow:auto;border:1px solid #ddd;border-radius:12px}section{padding:20px;margin:18px 0;border:1px solid #dbe2ea;border-radius:10px;scroll-margin-top:20px}:target{outline:3px solid #d6a900}a{color:#1255aa}p{max-width:100ch}svg a:hover polygon,svg a:hover path{stroke:#1255aa;stroke-width:2}</style><h1>FinSec – System Context</h1><p>Planungsstand auf Basis von „Exercise 1: Planning &amp; Analysis V1.0“, Task 1, und den ergänzenden Vorgaben. Komponenten und beschriftete Datenflüsse sind anklickbar; jede Beschreibung enthält einen Rücklink.</p><p><strong>Systemgrenze und Verantwortung:</strong> Der gelbe Rahmen umfasst die FinSec-Komponenten und die FinSec-seitig abzusichernden Kommunikationswege bis zu den externen Endpunkten. Er bedeutet keine Kontrolle über Kundengeräte, Banknetze oder die gesamte Transportinfrastruktur. Die grauen Anschlussstücke führen zu externen Parteien. Gestrichelte Verbindungen zwischen Banken liegen außerhalb der FinSec-Verantwortung.</p><div class="diagram">'''+svg+'</div><h2>Komponenten</h2>'+''.join(sections)+'''<h2>Einordnung und offene Entscheidungen</h2><p>Die drei Backend-Bereiche sind funktionale Verantwortungsbereiche, keine festgelegten Deployment-Stufen oder Microservices. Zugriffe auf die Datenbank sind hier über die Anwendungslogik abstrahiert. Die mobile App ist eingeplant, ihre Plattform und ihr Entwicklungstermin sind offen. Banken sind als eigenständige Parteien modelliert; eine konkrete Bankkooperation oder vollständige Vernetzung wird in der PDF nicht vorgegeben und hier nur schematisch gemäß ergänzender Vorgabe dargestellt.</p><p>Dieses Diagramm bearbeitet Task 1. Die Bewertung zu Task 2 steht in <a href="System%20Context.md#task-2--regulations-standards-and-partners">System Context.md</a>. Das CRA-Selbstbewertungsformular aus Task 3 bleibt separat.</p></html>'''
(ROOT/'System Context.html').write_text(page)
print('Generated finsec.dot, finsec.formatted.dot, finsec.svg and System Context.html')

# Markdown is the primary concise component/flow reference. IDs are shared by
# semantically identical flows; SVG element IDs remain unique per drawn edge.
md = ['# FinSec – System Context', '', '[SVG öffnen](finsec.svg) · [Interaktive Ansicht mit Rücklinks](System%20Context.html)', '', '![FinSec-Systemkontext](finsec.svg)', '', 'Der gelbe Rahmen umfasst FinSec und die von FinSec abzusichernden Teile der Anschlusswege. Kundengeräte und Banken bleiben extern. Die drei Backend-Bereiche sind funktionale Bereiche, keine Deployment-Stufen.', '', '## Komponenten', '', '| ID | Komponente | Kurzbeschreibung | Verantwortung | Diagramm |', '| --- | --- | --- | --- | --- |']
for i, name, desc, resp in components:
    md.append(f'| <a id="{i}"></a>{i} | {name} | {desc} | {resp} | [↩ {i}](finsec.svg#{i}) |')
md += ['', '## Datenflüsse', '', 'Gleiche IDs bezeichnen denselben Datenflusstyp auf mehreren Verbindungen. Im Diagramm stehen nur diese kurzen IDs; die Inhalte sind hier einmalig beschrieben. Die Nutzung und Anfragen gelten jeweils im Funktionsumfang des Frontends.', '', '| ID | Verbindung(en) | Kurzbeschreibung | Verantwortung | Diagramm |', '| --- | --- | --- | --- | --- |']
for i, a, b, title, desc, resp in dict((f[0], f) for f in flows).values():
    connections = ', '.join(f'{f[1]} ↔ {f[2]}' for f in flows if f[0] == i)
    md.append(f'| <a id="{i}"></a>{i} | {connections} | **{title}:** {desc} | {resp} | [↩ {i}](finsec.svg#{i}) |')
md += ['', '## Annahmen', '', '- Die mobile App ist geplant; Plattform und Termin sind offen.', '- Bankübergreifender Austausch ist schematisch dargestellt; die konkrete Topologie ist nicht festgelegt.', '- Datenbankzugriffe sind über die Anwendungslogik abstrahiert.', '- Grundlage: Exercise 1: Planning & Analysis V1.0, Task 1, und ergänzende Diagrammvorgaben.', '', 'Neu erzeugen: `python3 tools/render_context.py` (Graphviz erforderlich).', '']
md += [(ROOT / 'docs' / 'regulations.md').read_text()]
(ROOT / 'System Context.md').write_text('\n'.join(md))
