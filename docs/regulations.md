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
