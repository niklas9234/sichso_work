# Architektur und Diagramme

| Ebene | Diagramm | Aufgabe |
| --- | --- | --- |
| Systemkontext | [Übersicht im Projekt-README](../../README.md) | Übung 1. Zeigt die FinSec-Systemgrenze, externe Beteiligte und Datenflüsse. |
| Funktionale Architektur | [Grunddiagramm und Erläuterung](../functional%20architecture.md) | Übung 2. Zeigt die Komponenten innerhalb von FinSec und ihre Schnittstellen. |
| Sicherheitsarchitektur | [Sicherheitsansicht in der Discussion](../../design%20principles%20discussion.md#nachher--sicherheitsarchitektur) | Übung 3. Verfeinert das Grunddiagramm mit Datenbankrechten und EuroTrust-Zugangsmitteln. |
| Vorher/Nachher | [Design Principles Discussion](../../design%20principles%20discussion.md) | Zeigt beide Architekturstände nebeneinander im selben Dokument und begründet die Änderungen. |

Die Sequenzdiagramme zeigen den zeitlichen Ablauf konkreter Anwendungsfälle derselben Architektur. [Konto verknüpfen](../user%20account%20link.md) · [Kontostand abrufen](../user%20balance.md) · [Überweisen](../user%20transfer.md)

## Architekturdiagramme pflegen

`functional.dot` ist die Quelle für das Grunddiagramm, `security.dot` für seine Sicherheitsverfeinerung. Beide verwenden dieselben Komponenten und Schnittstellen. Bei einer Änderung der gemeinsamen Architektur beide DOT-Dateien prüfen. Die Markdown-Dokumente binden dieselben SVG-Dateien ein.

Die SVGs lassen sich im Browser direkt öffnen und mit der Browser-Tastatursteuerung vergrößern. Die Begleittexte beschreiben die wesentlichen Verbindungen und Zugriffsrechte auch ohne Grafik.

Aus dem Repository-Stamm mit Graphviz erzeugen:

```bash
dot -Tsvg docs/architecture/functional.dot -o docs/architecture/functional.svg
dot -Tsvg docs/architecture/security.dot -o docs/architecture/security.svg
```

Für den ursprünglichen Systemkontext liegen [DOT-Quelle](../../finsec.dot), [SVG](../../finsec.svg) und [HTML-Ansicht](../../System%20Context.html) im Repository-Stamm. Eine frühere Ausgestaltung des Systemkontexts liegt im [Archiv](archive/system-context-variant.dot).
