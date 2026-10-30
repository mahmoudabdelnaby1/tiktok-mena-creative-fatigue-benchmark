# TikTok Ads MENA Creative Decay & Fatigue Benchmark

> An illustrative creative-fatigue planning worksheet for TikTok Ads. The included figures are synthetic examples, not measured MENA benchmarks.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CURATED_DATASET](https://img.shields.io/badge/Format-CURATED--DATASET-green.svg)](#)
[![Tier: 1](https://img.shields.io/badge/Tier-1-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Provide a planning toolkit with illustrative creative-decay scenarios, a production pipeline planner, and a fatigue-monitoring SOP. The included example values are synthetic and must not be used as regional benchmarks or client forecasts.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `data/benchmarks_by_country.csv`
- `data/benchmarks_by_industry.csv`
- `data/creative_decay_benchmarks.json`
- `data/tiktok_mena_benchmarks.json`
- `docs/methodology-and-sources.md`
- `docs/methodology.md`
- `LICENSE`
- `README.md`
- `SOURCES.md`
- `templates/creative-production-pipeline.md`
- `tests/test_data_integrity.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "media-buying",
  "repository": "tiktok-mena-creative-fatigue-benchmark",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Decay Monitoring:** Track each campaign against its own spend, audience, and creative baseline; the included scenario values are not evidence of a standard MENA fatigue window.
- **Hook Drop-Off Telemetry:** Creative decay manifests first in 2-second and 6-second video view completion rates before impacting CPA.
- **Dialectal Sound Fatigue:** Native Gulf audio trends burn out faster than generic commercial music tracks; rotator tracks sound fatigue separately.

---

## 📚 Primary Documentation & Verifiable References

- [TikTok For Business Creative Center: Trend Discovery](https://ads.tiktok.com/business/creativecenter/) - Platform resource for exploring creative trends; it is not the source of the synthetic values in this repository.
- [TikTok Marketing API: Video Telemetry & Ad Insights](https://ads.tiktok.com/marketing_api/docs/) - Developer reference for video completion rates and frequency metrics.
- [TikTok Ads Academy: Creative Best Practices](https://ads.tiktok.com/business/en/insights) - Official creative guidance for driving lower CPAs across GCC markets.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
