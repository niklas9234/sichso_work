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

## Task 2 – Regulations, Standards and Partners

Stand: 11.11.2026. FinSec verarbeitet persönliche Finanzdaten, verbindet Bankkonten und soll Überweisungen ermöglichen. Dafür sind die folgenden Regeln, Standards und Partner wichtig. Die Anforderungen zeigen, was wir bei der Entwicklung berücksichtigen müssen; umgesetzt sind sie damit noch nicht.

Ob FinSec selbst als Kontoinformationsdienst (AISP) oder Zahlungsauslösedienst (PISP) auftritt oder dafür einen zugelassenen Anbieter nutzt, ist noch offen. Davon hängen einige der Pflichten ab.

### Übersicht

| ID | Regel / Standard / Partner | Warum relevant? / Zuständig | Anforderung 1 | Anforderung 2 | Komponenten |
| --- | --- | --- | --- | --- | --- |
| R01 | **DSGVO** [Q1] | Schützt persönliche Daten, also auch unsere Konto- und Nutzerdaten. Zuständig ist die Datenschutzaufsicht, in Deutschland bei privaten Unternehmen meist die Landesbehörde. | **R01.1:** Nur nötige Daten mit passender Rechtsgrundlage verarbeiten und Löschfristen festlegen (Art. 5, 6, 25). | **R01.2:** Daten risikogerecht schützen, z. B. durch Zugriffsschutz, Verschlüsselung und regelmäßige Sicherheitstests (Art. 32). | C02–C07 |
| R02 | **PSD2 / ZAG** [Q2] | Regelt Zahlungsdienste und Kontozugriff. In Deutschland ist dafür insbesondere die BaFin zuständig. Welche Vorgaben gelten, hängt von unserer Rolle ab. | **R02.1:** Vor dem Start klären, ob FinSec eine Registrierung oder Erlaubnis braucht oder über einen zugelassenen Partner arbeitet (u. a. Art. 33). | **R02.2:** Kontodaten und Zahlungsaufträge nur im ausdrücklich beauftragten Umfang verarbeiten; starke Kundenauthentifizierung einbinden, soweit vorgeschrieben (Art. 66, 67, 97). | C02–C04, C06 |
| R03 | **PSD2-Sicherheitsregeln (RTS)** [Q3] | Machen konkrete Vorgaben für sichere Bankverbindungen und starke Kundenauthentifizierung. Relevant für FinSec, Banken und Finanzaufsicht. | **R03.1:** Bei entsprechenden Fernzahlungen die Freigabe an Betrag und Empfänger binden; Änderungen müssen den Authentifizierungscode ungültig machen (Art. 5). | **R03.2:** FinSec gegenüber der Bank mit geeigneten qualifizierten Zertifikaten identifizieren und die Daten verschlüsselt sowie gegen Manipulation geschützt übertragen (Art. 34, 35). | C04, C06; F08 |
| R04 | **Cyber Resilience Act (CRA)** [Q4] | Betrifft sichere Software und den Umgang mit Schwachstellen. Die Übung setzt voraus, dass er für FinSec relevant ist. Zuständig sind die Marktüberwachung und bei vorgesehenen Meldungen auch ENISA. | **R04.1:** Sicherheitsrisiken schon bei der Entwicklung bewerten und sichere Voreinstellungen einplanen (Art. 13, Anhang I Teil I). | **R04.2:** Softwareabhängigkeiten dokumentieren (SBOM), Sicherheitsupdates bereitstellen und Prozesse für Schwachstellen und vorgeschriebene Meldungen festlegen (Art. 14, Anhang I Teil II). | C02–C07 |
| R05 | **DORA** [Q5] | Soll Finanzunternehmen bei IT-Störungen und Angriffen widerstandsfähiger machen. Kann FinSec als Zahlungsinstitut oder Kontoinformationsdienst betreffen; zuständig ist die jeweilige Finanzaufsicht, in Deutschland insbesondere BaFin. | **R05.1:** IT-Risiken, Zuständigkeiten und Wiederherstellung nach Ausfällen planen und regelmäßig testen. | **R05.2:** IT-Vorfälle erkennen, einordnen und bearbeiten; schwerwiegende Vorfälle nach den geltenden Regeln melden. | C02–C07, Betrieb |
| S01 | **OWASP ASVS 5.0.0** [Q6] | Praktischer Sicherheitsstandard für Webanwendungen und APIs. Kein Gesetz, aber eine sinnvolle Prüfliste für unser Entwicklungsteam. | **S01.1:** Datenbankabfragen gegen Injection absichern, z. B. mit parametrisierten Abfragen (V1.2.4). | **S01.2:** Berechtigungen im Backend prüfen, damit Nutzer nicht auf fremde Kontodaten zugreifen können (V8.3.1). | C02, C04–C07 |
| P01 | **Angebundene Banken** [Q2, Q3] | Stellen Kontodaten und Zahlungsfunktionen bereit. Konkrete Banken stehen noch nicht fest; ihre API-Vorgaben müssen wir später ergänzen. | **P01.1:** API-Version, Zertifikate und Antwortformate der jeweiligen Bank prüfen und die Anbindung testen. | **P01.2:** Abgelaufene Berechtigungen und abgelehnte Zahlungen sauber behandeln, ohne unberechtigten Zugriff oder unbeabsichtigte Doppelverarbeitung. | C04, C06, C08–C10 |

Die Bankanforderungen sind bisher aus PSD2/RTS abgeleitet, nicht aus Vorgaben einer bestimmten Bank. Ein zusätzlicher Vertrag mit jeder Bank wird damit nicht als Voraussetzung für den regulierten Kontozugriff angenommen. Für die native App braucht es neben ASVS noch passende mobile Sicherheitsprüfungen.

### CRA, NIS2 und Geltungsbereich

Mit einer „EU Internet Security Guideline“ könnten **CRA** oder **NIS2** gemeint sein. Der CRA betrifft Produkte mit digitalen Elementen; reine eigenständige SaaS-Angebote fallen nicht automatisch darunter. Seine Hauptpflichten gelten grundsätzlich ab **11.12.2027**, die Meldepflichten aus Art. 14 bereits ab **11.09.2026**.

**NIS2** [Q7] betrifft bestimmte Einrichtungen und Sektoren. Ob FinSec darunterfällt, hängt unter anderem von Tätigkeit, Größe und nationaler Umsetzung ab. Bei Überschneidungen mit DORA muss die Abgrenzung geprüft werden (NIS2 Art. 4, DORA Art. 1 Abs. 2). DORA gilt seit **17.01.2025**; mögliche Ausnahmen und vereinfachte Vorgaben hängen vom konkreten Anbieter ab.

### Quellen

- **Q1:** [DSGVO – Verordnung (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj), Art. 5, 6, 25, 32.
- **Q2:** [PSD2 – Richtlinie (EU) 2015/2366](https://eur-lex.europa.eu/eli/dir/2015/2366/oj), Art. 33, 66, 67, 97; in Deutschland insbesondere durch das ZAG umgesetzt.
- **Q3:** [RTS – Delegierte Verordnung (EU) 2018/389](https://eur-lex.europa.eu/eli/reg_del/2018/389/oj), Art. 5, 30, 34, 35; für die Umsetzung die aktuelle konsolidierte Fassung verwenden.
- **Q4:** [CRA – Verordnung (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj), Art. 13, 14, 71 und Anhang I.
- **Q5:** [DORA – Verordnung (EU) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj), Art. 2, 5–19, 24–30.
- **Q6:** [OWASP ASVS 5.0.0](https://github.com/OWASP/ASVS/tree/v5.0.0), [Anforderungskatalog](https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv), V1.2.4 und V8.3.1.
- **Q7:** [NIS2 – Richtlinie (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj), Art. 4, 21, 23.

### Noch offen

OWASP wurde am 11.11.2026 online geprüft. EUR-Lex war durch die Netzwerkfreigabe blockiert; die Rechtsquellen und ihr aktueller Änderungsstand müssen daher vor der Abgabe noch abgeglichen werden. Die Vorlesungsfolien lagen nicht vor. Außerdem müssen wir Anbieterrolle, Sitz und konkrete Bankpartner festlegen. Bis dahin ist die Tabelle eine Vorbewertung. Das CRA-Formular aus Task 3 ist damit noch nicht ausgefüllt.
