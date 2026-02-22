# CMAI-E91: Quantum Cryptography Workshop

**Quantum Key Distribution using the E91 Protocol**

This repository contains materials for teaching the E91 quantum key distribution protocol, including the CHSH Bell inequality test that makes it secure.

---

## Repository Structure

```text
CMAI-E91/
├── slides/                    # Presentation slides (1h30 theory) — coming soon
├── workshops/                 # Hands-on notebooks (1h30 guided)
│   ├── utils/                 # Shared helper code
│   ├── E91_Full_Workshop_en.ipynb   # English Unified Workshop
│   └── E91_Full_Workshop_fr.ipynb   # French Unified Workshop
├── assignment/                # Take-home assignment (Deadline: 24h)
│   ├── assignment_encrypted_messages.txt
│   └── README.md
```

## Quick Links (Google Colab)

Launch the unified workshop notebook directly in Google Colab (no local installation required):

- **E91 Full Workshop:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/workshops/E91_Full_Workshop_en.ipynb) | [Français](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/workshops/E91_Full_Workshop_fr.ipynb)

---

## Prerequisites

- Python 3.9+
- The specific package versions defined in `requirements.txt` are required for reproducibility.

```bash
pip install -r requirements.txt
```

---

## References

- [E91 Original Paper (Ekert, 1991)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.67.661)
- [CHSH Inequality - Wikipedia](https://en.wikipedia.org/wiki/CHSH_inequality)
- [Bell's Theorem - Wikipedia](https://en.wikipedia.org/wiki/Bell%27s_theorem)
- [Qiskit Documentation](https://qiskit.org/documentation/)

---

## Authors
ibrahim Chegrane

---