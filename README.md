# Zero Trust Network Access (ZTNA) — Educational Project

**Prepared by:** Shivraj Jarupla

## Overview
This project demonstrates the basic decision-making logic of a Zero Trust Network Access (ZTNA) approach. Rather than automatically trusting a user because they are inside a network, each request is checked against policy signals.

## Features
- Role-based access to specific resources (least privilege)
- Device-management check
- Multi-factor authentication (MFA) check
- Risk-score evaluation
- Three outcomes: allow, deny, or require additional verification
- Demonstration requests and a final summary

## Requirements
- Python 3.10 or newer recommended
- No third-party libraries required

## Run
From a terminal in this folder:

```bash
python ShivrajJarupla_ZTNA.py
```

On some systems, use `python3` instead of `python`.

## Project structure
- `ShivrajJarupla_ZTNA.py` — simulator source code
- `requirements.txt` — dependency note
- `ShivrajJarupla_ProjectReport.docx` — written report
- `ShivrajJarupla_ZTNA_Presentation.pptx` — presentation

## Important limitation
This is a classroom simulation only. It does not authenticate real users, inspect real devices, or enforce access on a real network. A production ZTNA deployment needs trusted identity services, device posture integrations, policy enforcement components, logging, secure transport, and operational controls.
