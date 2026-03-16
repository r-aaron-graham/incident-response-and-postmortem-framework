# Incident Response and Postmortem Framework

This repository contains templates and a small script to standardize
incident response and postmortem documentation.  The goal is to
encourage consistent, blameless analysis of incidents and capture
lessons learned to prevent recurrence.

## Contents

- **templates/**: Markdown templates for incident reports and
  postmortems.
- **postmortem_cli.py**: A simple script to generate new postmortem
  files with placeholder sections.

## Usage

Generate a new postmortem:

```bash
python postmortem_cli.py --id INC‑12345 --title "Outage in payment service" --output postmortems/INC‑12345.md
```

Fill out the resulting file with details of the incident, including a
timeline, contributing factors, impact, and corrective actions.

## Conventions

All incident reports and postmortems are stored under `postmortems/`
with filenames prefixed by the incident ID.  Encourage a culture of
blamelessness and focus on systemic improvements rather than
individual fault.