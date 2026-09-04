# MRP II case-study summary

This document summarizes the **fictitious MetalMueble Andino S.A.C. academic case** that provides the business context for the FlexSim model. The original case was developed as group coursework; this repository uses only the key scenario parameters needed to explain the simulation.

## Production requirement

Weekly production requirement: **420 metal school chairs**.

| Production order | Quantity |
| --- | ---: |
| OP-001 | 160 |
| OP-002 | 140 |
| OP-003 | 120 |
| **Total** | **420** |

## Load versus effective capacity

| Work center | Required load | Available capacity | Gap | Utilization |
| --- | ---: | ---: | ---: | ---: |
| Corte | 35.10 h | 68.40 h | +33.30 h | 51.32% |
| Soldadura | 77.85 h | 64.77 h | **-13.08 h** | **120.19%** |
| Ensamble | 51.90 h | 68.40 h | +16.50 h | 75.88% |
| Acabado | 60.60 h | 64.80 h | +4.20 h | 93.52% |

The deterministic MRP II capacity analysis identifies **Soldadura** as the overloaded work center and therefore the principal bottleneck in the base scenario.

## Capacity-adjustment scenario

The academic case evaluates alternatives such as overtime, adding another station, and subcontracting. In the selected overtime scenario, welding capacity increases to **80.96 h**, which brings utilization to approximately **96.16%**.

## Relationship with FlexSim

The Excel / MRP II analysis is deterministic: it compares required hours with planned available capacity. FlexSim adds a dynamic view of the same process by allowing the team to observe:

- work-in-process accumulation;
- queue formation;
- waiting times;
- throughput;
- movement of individual items;
- the operational effect of the welding bottleneck.

The FlexSim package in this repository is therefore a simulation complement to the capacity-planning case rather than a replacement for the MRP II calculations.
