# E91 Quantum Key Distribution Workshop

**Duration:** 1h30 (slides) + 1h30 (hands-on)  
**Level:** Beginner

---

## Overview

This workshop introduces **Quantum Key Distribution (QKD)** using the **E91 protocol**, which leverages quantum entanglement for secure communication.

You'll learn:
- How quantum entanglement works
- The CHSH Bell inequality test
- How to detect eavesdroppers using quantum mechanics
- Building a complete QKD system

---

## Notebooks

Complete the appropriate notebook for your language:

### [E91_Full_Workshop_en.ipynb](E91_Full_Workshop_en.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/workshops/E91_Full_Workshop_en.ipynb)
**English Version**

### [E91_Full_Workshop_fr.ipynb](E91_Full_Workshop_fr.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algolab-quantique/CMAI-E91-Students/blob/main/workshops/E91_Full_Workshop_fr.ipynb)
**Version Française**

These notebooks combine the entire curriculum into a single flow:
1. **Understanding Entanglement (CHSH)** - Learn measurement bases and test quantum correlations against classical limits.
2. **Key Distribution (E91)** - Build a complete QKD system and detect eavesdropping attempts.
3. **Coding Challenge** - Take-home assignment to test your understanding using a different Bell state.

~3 hours total

---

## Requirements

We use specific versions of these libraries to guarantee the encrypted messages can be correctly decrypted by your random number generators.

```bash
pip install -r ../requirements.txt
```

---

## Files

```
workshops/
├── 01_CHSH_Bell_Inequality.ipynb    ← Start here!
├── 02_E91_Protocol.ipynb            ← Continue here
├── encrypted_messages.txt           ← Messages to decrypt
└── utils/
    └── encryption_algorithms.py     ← Encryption helpers
```

---

## Tips

1. **Run cells in order** - Later cells depend on earlier ones
2. **Read the markdown** - Explanations help you understand the physics
3. **Check your answers** - Each exercise has a test cell
4. **Ask questions** - Quantum mechanics is tricky!

---

## Key Concepts

| Concept | Classical | Quantum (E91) |
|---------|-----------|---------------|
| Key generation | Computational algorithms | Entangled photons |
| Security basis | Mathematical difficulty | Laws of physics |
| Eavesdrop detection | None inherent | CHSH violation changes |
| CHSH value | |S| ≤ 2 | |S| ≈ 2.83 |

---

## After the Workshop

Complete the [assignment](../assignment/) to test your understanding!

