# FinSec – System Context

[SVG öffnen](finsec.svg) · [Interaktive Ansicht mit Rücklinks](System%20Context.html)

![FinSec-Systemkontext](finsec.svg)

Der gelbe Rahmen umfasst FinSec und die von FinSec abzusichernden Teile der Anschlusswege. Kundengeräte und Banken bleiben extern. Die drei Backend-Bereiche sind funktionale Bereiche, keine Deployment-Stufen.

## Komponenten

| ID | Komponente | Kurzbeschreibung | Verantwortung | Diagramm |
| --- | --- | --- | --- | --- |
| <a id="C01"></a>C01 | Kund:innen | Nutzen FinSec zur Verwaltung ihrer verbundenen Bankkonten. | Extern: Geräte und eigenes Verhalten liegen außerhalb von FinSec; FinSec verantwortet sichere Authentisierung, Sitzungen und Datenübertragung. | [↩ C01](finsec.svg#C01) |
| <a id="C02"></a>C02 | Web-Frontend | Bietet die browserbasierte Oberfläche mit eingeschränktem Funktionsumfang. | FinSec verantwortet die Webanwendung und ihre sichere Kommunikation; der genaue Funktionsumfang ist noch offen. | [↩ C02](finsec.svg#C02) |
| <a id="C03"></a>C03 | Mobile App (geplant) | Bietet auf dem persönlichen Mobilgerät den vollen geplanten Funktionsumfang. | FinSec verantwortet App-Code, lokale Datenverarbeitung und Kommunikation; Betriebssystem und Gerät liegen außerhalb seiner Kontrolle. Plattform und Realisierungstermin sind offen. | [↩ C03](finsec.svg#C03) |
| <a id="C04"></a>C04 | Anwendungslogik | Steuert Anwendungsfälle einschließlich Nutzer- und Zugriffsverwaltung. | FinSec verantwortet Autorisierung, Sitzungsprüfung, fachliche Regeln und die sichere Koordination der Backend-Bereiche. | [↩ C04](finsec.svg#C04) |
| <a id="C05"></a>C05 | Finanzdatenverarbeitung | Klassifiziert, aggregiert und analysiert Finanzdaten für Auswertungen und Sparhinweise. | FinSec verantwortet korrekte und zweckgebundene Verarbeitung sowie den Schutz der verarbeiteten Daten. | [↩ C05](finsec.svg#C05) |
| <a id="C06"></a>C06 | Bankanbindung | Ruft autorisierte Kontodaten autonom ab und leitet Zahlungsaufträge an Banken weiter. | FinSec verantwortet Einwilligungs- und Berechtigungsprüfung, geschützte Zugangsmittel sowie sichere API-Aufrufe und Antwortverarbeitung. | [↩ C06](finsec.svg#C06) |
| <a id="C07"></a>C07 | Datenbank | Speichert Nutzer-, Verbindungs- und Finanzdaten für FinSec. | FinSec verantwortet Zugriffsschutz, Datenminimierung, Aufbewahrung, Löschung und die Absicherung von Speicherung und Sicherungen. | [↩ C07](finsec.svg#C07) |
| <a id="C08"></a>C08 | Bank 1 | Stellt Kontodaten und Zahlungsdienste einer angebundenen EU-Bank bereit. | Extern: Die Bank verantwortet ihre Systeme und die Ausführung von Zahlungen; FinSec verantwortet seine Integrationsseite. | [↩ C08](finsec.svg#C08) |
| <a id="C09"></a>C09 | Bank 2 | Stellt Kontodaten und Zahlungsdienste einer weiteren angebundenen EU-Bank bereit. | Extern: Verantwortung wie C08; die Bank bleibt eine eigenständige externe Partei. | [↩ C09](finsec.svg#C09) |
| <a id="C10"></a>C10 | Bank n | Steht stellvertretend für weitere angebundene EU-Banken. | Extern: Verantwortung wie C08; n bezeichnet die Erweiterbarkeit und keine konkrete Bank. | [↩ C10](finsec.svg#C10) |

## Datenflüsse

Gleiche IDs bezeichnen denselben Datenflusstyp auf mehreren Verbindungen. Im Diagramm stehen nur diese kurzen IDs; die Inhalte sind hier einmalig beschrieben. Die Nutzung und Anfragen gelten jeweils im Funktionsumfang des Frontends.

| ID | Verbindung(en) | Kurzbeschreibung | Verantwortung | Diagramm |
| --- | --- | --- | --- | --- |
| <a id="F01"></a>F01 | C01 ↔ C02 | **Nutzung & Rückmeldungen:** Hin: Anmeldedaten, Kontoverknüpfung, Abfragen und – soweit unterstützt – Überweisungsdaten. Zurück: Kontoinformationen, Auswertungen und Auftragsstatus. | FinSec verantwortet geschützte Übertragung, sichere Endpunkte und Eingabeprüfung; Kundengeräte bleiben extern. | [↩ F01](finsec.svg#F01) |
| <a id="F02"></a>F02 | C01 ↔ C03 | **Nutzung & Rückmeldungen:** Hin: Anmeldedaten, Kontoverknüpfung, Abfragen und – soweit unterstützt – Überweisungsdaten. Zurück: Kontoinformationen, Auswertungen und Auftragsstatus. | FinSec verantwortet geschützte Übertragung, sichere Endpunkte und Eingabeprüfung; Kundengeräte bleiben extern. | [↩ F02](finsec.svg#F02) |
| <a id="F03"></a>F03 | C02 ↔ C04 | **Anfragen & Ergebnisse:** Hin: Anmeldeanfrage, Sitzungsnachweis, Datenabfragen und unterstützte Überweisungsaufträge. Zurück: Anmeldeergebnis, Finanzdaten, Auswertungen und Auftragsstatus. | Vollständig FinSec: Authentisierung, Autorisierung, Vertraulichkeit und Integrität der Kommunikation. | [↩ F03](finsec.svg#F03) |
| <a id="F04"></a>F04 | C03 ↔ C04 | **Anfragen & Ergebnisse:** Hin: Anmeldeanfrage, Sitzungsnachweis, Datenabfragen und unterstützte Überweisungsaufträge. Zurück: Anmeldeergebnis, Finanzdaten, Auswertungen und Auftragsstatus. | Vollständig FinSec: Authentisierung, Autorisierung, Vertraulichkeit und Integrität der Kommunikation. | [↩ F04](finsec.svg#F04) |
| <a id="F05"></a>F05 | C04 ↔ C05 | **Analyseauftrag & Auswertung:** Hin: Analyseauftrag und zulässige Finanzdaten. Zurück: Klassifikation, Aggregate, Auswertungen und Sparhinweise. | Vollständig FinSec; Zugriff und Zweckbindung müssen auch zwischen internen Bereichen gelten. | [↩ F05](finsec.svg#F05) |
| <a id="F06"></a>F06 | C04 ↔ C06 | **Bankauftrag & Ergebnis:** Hin: autorisierte Kontoabrufe und Zahlungsaufträge. Zurück: Kontodaten, Zahlungsstatus und Fehler. | Vollständig FinSec; Auftragsberechtigung und konsistente Statusverarbeitung sicherstellen. | [↩ F06](finsec.svg#F06) |
| <a id="F07"></a>F07 | C04 ↔ C07 | **Lesen & Speichern:** Hin: Datenabfragen und zu speichernde Nutzer-, Verbindungs- und Finanzdaten. Zurück: gespeicherte Daten und Speicherstatus. | Vollständig FinSec; Datenbankzugriffe absichern und auf notwendige Rechte begrenzen. | [↩ F07](finsec.svg#F07) |
| <a id="F08"></a>F08 | C06 ↔ C08, C06 ↔ C09, C06 ↔ C10 | **Kontoabruf & Zahlungsauftrag:** Hin: autorisierter Kontodatenabruf und Zahlungsaufträge. Zurück: Kontostände, vergangene und geplante Transaktionen sowie Zahlungsstatus. | Geteilt: FinSec verantwortet seinen Endpunkt, Autorisierung, geschützten Transport und Antwortprüfung; die Bank ihren Endpunkt und die Transaktionsausführung. | [↩ F08](finsec.svg#F08) |
| <a id="F11"></a>F11 | C08 ↔ C09, C09 ↔ C10 | **Datenaustausch / Transaktionen:** Schematischer bidirektionaler Austausch zwischen Banken, etwa zur Abwicklung bankübergreifender Transaktionen. | Außerhalb von FinSec; die beteiligten Banken verantworten diesen Austausch. Die Linien behaupten keine konkrete technische Direktverbindung oder Topologie. | [↩ F11](finsec.svg#F11) |

## Annahmen

- Die mobile App ist geplant; Plattform und Termin sind offen.
- Bankübergreifender Austausch ist schematisch dargestellt; die konkrete Topologie ist nicht festgelegt.
- Datenbankzugriffe sind über die Anwendungslogik abstrahiert.
- Grundlage: Exercise 1: Planning & Analysis V1.0, Task 1, und ergänzende Diagrammvorgaben.

Neu erzeugen: `python3 tools/render_context.py` (Graphviz erforderlich).
