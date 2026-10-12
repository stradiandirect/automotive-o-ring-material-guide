# Automotive O-Ring Material Guide: Buna-N (NBR) vs. FKM (Viton®)

A technical reference for engineers, mechanics, and enthusiasts comparing the two most common elastomers used in automotive sealing applications.

This guide focuses on material properties, compatibility, failure modes, and selection criteria. It is intended as a starting point for engineering decisions — always verify against the specific compound datasheet for your application.

---

## Contents

- [Introduction](#introduction)
- [Buna-N (NBR)](#buna-n-nbr)
- [FKM (Viton®)](#fkm-viton)
- [Comparison Table](#comparison-table)
- [Selection Framework](#selection-framework)
- [Failure Modes](#failure-modes)
- [Data Files](#data-files)
- [References](#references)

---

## Introduction

An O-ring is a simple component with a complex job. In automotive environments it must withstand extreme temperatures, aggressive fluids, and constant mechanical stress. Material selection is not about picking the "best" elastomer — it is about matching the material to the specific demands of the application.

Four factors drive the decision:

1. **Operating temperature** — continuous and peak
2. **Fluid compatibility** — oils, fuels, coolants, additives
3. **Application demands** — pressure, motion (static vs. dynamic), gland geometry
4. **Total cost** — including the cost of premature failure

This guide covers the two workhorses of automotive sealing: **Buna-N (NBR)** and **FKM (Viton®)** .

---

## Buna-N (NBR)

Buna-N, also called Nitrile Rubber or NBR (Acrylonitrile Butadiene Rubber), is the most widely used elastomer for general-purpose automotive sealing.

### Properties

- Excellent resistance to petroleum-based oils, greases, hydraulic fluids, and standard gasoline
- Good low-temperature flexibility
- Superior compression set resistance — resists permanent deformation under load
- Low cost, high availability

### Temperature Range

| Compound | Range |
|---|---|
| Standard NBR | -40°C to +100°C (-40°F to +212°F) |
| High-temp NBR | Up to +120°C (+250°F), short duration |

### Typical Applications

- Engine oil seals and valve cover gaskets
- Transmission seals and pan gaskets
- Fuel lines and fuel pump seals (standard gasoline)
- Power steering seals
- Hydraulic brake system seals (specific formulations)

### Limitations

- Poor ozone and weather resistance — cracks under UV/ozone exposure
- Limited resistance to ketones, esters, strong acids
- Not suitable for continuous service above 100°C

---

## FKM (Viton®)

FKM is a fluoroelastomer family known for exceptional performance in extreme environments.

> **Note on terminology:** FKM is a *family* of materials, not a single compound. Different formulations vary in fluorine content and curing system, which affects chemical and thermal performance. **Viton™** is a trademarked brand of fluoroelastomer owned by Chemours — it is not a generic synonym for all FKM.

### Properties

- Exceptional high-temperature resistance — the primary advantage over NBR
- Superior resistance to modern fuel blends (ethanol, methanol), aromatic hydrocarbons, and many acids
- Excellent ozone, UV, and weathering resistance
- Low compression set under sustained load

### Temperature Range

| Compound | Range |
|---|---|
| Standard FKM | -20°C to +200°C (-4°F to +392°F) |
| Specialty FKM | -40°C to +230°C (-40°F to +446°F) |

### Typical Applications

- High-temperature fuel injection systems
- Oxygen sensors and exhaust system seals
- Turbocharger and supercharger seals
- High-performance transmission seals
- Aerospace and chemical processing seals

### Limitations

- Significantly higher cost than NBR
- Some FKM grades have poor resistance to ketones, esters, and hot hydrofluoric acid
- Standard FKM has poor low-temperature flexibility compared to NBR or silicone

---

## Comparison Table

| Property | Buna-N (NBR) | FKM (Viton®) |
|---|---|---|
| Temperature range | -40°C to +100°C | -20°C to +200°C |
| Petroleum oil resistance | Excellent | Excellent |
| Alcohol-blended fuel resistance | Poor–Fair | Excellent |
| Ozone/weather resistance | Poor | Excellent |
| Compression set resistance | Very good | Excellent |
| Broad chemical resistance | Moderate | Excellent |
| Low-temp flexibility | Good | Fair (standard grades) |
| Relative cost | Low | High |
| Typical use case | Engine/trans seals, standard fuel lines | High-temp fuel, sensors, turbo seals |

A machine-readable version of this data is in [`data/oring-material-properties.csv`](data/oring-material-properties.csv).

---

## Selection Framework

A simple decision path:

1. **Define continuous operating temperature.**
   - ≤ 100°C → Buna-N is a candidate
   - > 100°C → FKM should be the primary consideration

2. **Identify the fluid.**
   - Petroleum oils and standard gasoline → Buna-N
   - Alcohol-blended fuels, aggressive additives, synthetic fluids → FKM
   - Ozone or UV exposure → FKM (required)

3. **Evaluate total cost.**
   - FKM costs more upfront. If NBR fails early from heat or chemical attack, the labor and secondary damage usually exceed the price difference.

4. **Verify the specific compound.**
   - Not all NBR is equal. Not all FKM is equal. Check the datasheet.

A reference implementation of this logic is in [`scripts/material_selector.py`](scripts/material_selector.py).

---

## Failure Modes

| Material | Failure mode | Root cause |
|---|---|---|
| Buna-N | Hardening, cracking, compression set | High-temperature degradation |
| Buna-N | Swelling, softening, dissolution | Aggressive chemicals, ozone |
| FKM | Swelling, softening | Incompatible fluids (ketones, esters) |
| FKM | Cracking, loss of elasticity | Low-temperature embrittlement below rated limit |

---

## Data Files

- [`data/oring-material-properties.csv`](data/oring-material-properties.csv) — comparison data used to build the tables above
- [`scripts/material_selector.py`](scripts/material_selector.py) — reference script implementing the selection framework

---

## References

**Industry standards and material data:**

- Parker Hannifin — [O-Ring Handbook ORD 5700](https://www.parker.com/) — the standard industry reference for O-ring design and material selection
- Apple Rubber — [O-Ring Material Selection Guide](https://www.applerubber.com/) — comprehensive material property charts
- Marco Rubber & Plastics — [Elastomer Selection Guide](https://www.marcorubber.com/) — compound-level compatibility data
- SAE International — [J200 / J1208](https://www.sae.org/) — automotive elastomer specifications
- Chemours — [Viton™ Technical Information](https://www.viton.com/) — official FKM brand documentation

**Practical selection guides:**

- Stradian Direct — [Buna-N or FKM? Picking the Right Automotive O-Ring](https://stradiandirect.com/buna-n-or-fkm-picking-the-right-automotive-o-ring/) — practical walkthrough of the selection decision for automotive applications

---

## Contributing

Corrections and additions welcome. Please open an issue with a source citation for any material property changes.

## License

Content in this repository is provided under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code is provided under MIT.
