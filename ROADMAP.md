# Roadmap

## Phase 1 – abgeschlossen

- HTTP-Health-Service
- Checkmk-kompatibler Local Check
- Ansible-Rolle für reproduzierbare Installation
- automatisierte Unit-Tests
- CI-Workflow

## Phase 2

- Logausgabe als strukturiertes JSON
- zentrale Sammlung in einer lokalen Elastic/OpenSearch-Testumgebung
- Dashboard für Verfügbarkeit und Antwortzeit
- Ansible Molecule oder Container-Test für die Rolle

## Phase 3

- zwei Service-Instanzen hinter einem Reverse Proxy
- dokumentierter Rolling-Update- und Rollback-Ablauf
- Ausfall einer Instanz simulieren
- Wiederherstellungszeit messen

## Phase 4

- Terraform-Lernmodul für eine lokale Testinfrastruktur
- klare Trennung: Terraform stellt Infrastruktur bereit, Ansible konfiguriert Betriebssystem und Anwendung

