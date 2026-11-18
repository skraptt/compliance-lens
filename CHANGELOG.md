# Changelog: REMIT obligation checklist

## 0.3.0 (2026-11-17)

A third review checked the 16 items added in v0.2 and the four open judgement calls (`reviews/legal-accuracy-v0.2-new-items.md`). Every date, threshold and deadline matched the primary text. The fixes:

### False gaps removed (checks marked `law` that the law does not require)
- COOP-01.c4: preserving records once a request arrives (legal hold) → good_practice
- COOP-02.c1: storing original contracts (Art 8(9) IR is a power to request, not a storage duty) → good_practice
- REP-07.c4: rejection-handling procedure → guidance (ACER Q&A 3.2.44)
- REP-09 confirmation: "written" dropped (Art 4(2) IR prescribes no form)

### Judgement calls decided
- STR-02.c2 (surveillance reporting line) → guidance (ACER Guidance 9.4.3.1). The legal duty of independence stays in c3.
- REG-02 split: "communicate any change" and "promptly" stay law; the trigger-event list and an internal day limit become good_practice.
- COOP-01.c4 → good_practice (see above).

### Corrections
- **REP-09 split into REP-09a and REP-09b.** REP-09a covers large-consumer supply (Art 4(2) IR) from 2027-10-29. REP-09b covers balancing, capacity mechanisms and gas storage (Art 4(1), (3)-(7)) from 2028-04-29. Before the split, the tool would have reported gaps for duties not yet in force. The 90-day backloading duty (Art 16(3) IR) is added to both.
- **COOP-01:** periodic penalties apply only when someone fails to comply with an ACER decision (Art 13g: up to 3% of average daily turnover, up to 6 months). Inspecting private premises needs a reasonable suspicion and judicial authorisation. Art 13g is added; addressees now include `any_person`.
- **INS-03:** Art 3(4)(a) is restated. The obligation must result from an agreement or order made before the person had the inside information; it need not have fallen due before.
- **OMP-01:** reporting is mandatory, and order-book access on request comes on top. The Art 8(11) notification and reference-data check is added.
- **LNG-01:** checks for the contract currency, UTC timestamps, ACER delivery-point identifiers and the price formula are added; the scope wording is aligned with Art 2(23).
- **REP-07:** addressees changed to `registered_mp` and `omp`. **REP-08:** the missing category Art 5(1)(i) is added. **REP-10:** five-year retention is added; the exemption wording is made precise.
- **INS-04.c1:** tied to the use of client-order information (front running, pre-hedging).
- **MAN-02:** the knowledge standard now also covers spreading false information; ACER Guidance 6.2.4 and 6.2.5 are added.
- **DIS-09:** the legal basis is now Art 4(1) and 8(1) REMIT. Transitional rules cite Open Letter DR sections 3-4; RRMs and IIPs already registered may continue until ACER decides.
- **REG-03:** guidance reference corrected to ACER Guidance 8.6, paras. (379)-(381), confirmed against the source.

### Counts
REMIT obligations: 41 items, 158 checks (91 law, 26 ACER, 41 good practice). MAR adjacent regime: 3 items. Good practice: 15 items.

### Still open
- The REMIT MCP parser bug (see 0.2.0, open item 1).
- Personal account dealing: still no REMIT source.
- A final human read of the in-force law checks in DIS-01–05, INS-01/02 and MAN-01/02 before `status: reviewed`.

## 0.2.0 (2026-11-17)

Two independent reviews of v0.1 were applied: a legal-accuracy review (`reviews/legal-accuracy.md`) and a completeness review (`reviews/completeness.md`). Both checked their claims against the REMIT and MAR MCP servers.

### Structure
- Each check now has an id (`REMIT-DIS-04.c3`) and its own `basis`: `law`, `guidance` (ACER expectation) or `good_practice`. The tool reports only missing **law** checks as gaps, so the false gaps found in v0.1 (kill switch, NDAs, disclaimers, information barriers, training, periodic reviews) can no longer occur.
- Checks can be conditional (`when: has_group_facilities`, `when: "date >= 2027-10-29"`).
- Each item names the procedure documents it belongs in (`documents: [IIP, MCP]`), and document rules have been added for combined manuals.
- New sections: `adjacent_regimes` (MAR, scored separately) and `good_practice` (15 items, reported as recommendations only).
- New addressee model and 15 profile questions. `mp_with_inside_info` is replaced by `mp_disclosing`, because the disclosure duty only covers the company's own or group facilities.
- Guidance references are written as "ACER Guidance 4.4", so the REMIT MCP resolves them correctly (see open item 1).

### Corrections to v0.1
- **STR-01 to STR-04:** ACER treats DEA providers and order book providers as PPATs, so `dea_provider` and `omp` are now in scope. The note on voluntary notification now cites ACER Q&A 2.4.6 and is marked non-binding.
- **DIS-05:** limited to the market participant and its staff (not `any_person`). The confidentiality duty may come from law, regulation, articles of association or contract, so NDAs are good practice. After an unintentional leak the test is "as soon as possible", not "immediate".
- **INS-02:** the addressees are now the exact Article 3(4)(b) group. ACER's limits (within-day losses, TSO ancillary services, Notification Platform) are added as guidance checks. The "no combination with Art 4(2)" check is marked as ACER's reading.
- **REP-02:** the LNG deadline in Art 10(6) applies only from 2027-10-29. Events before 2026-04-29 keep the old timeframes. ACER's reading (on-OMP trades = T+2, OTC trades = T+10) is added as a guidance check.
- **REP-03 and the new REP-06:** OMP trades must not be reported again by the company. From 2027-10-29 the company must give the OMP any data it lacks. Discharging entities are limited to Art 8(4)(b)-(f).
- **REP-04:** the 600 GWh test is on positions, assessed separately for electricity and gas. Exact reporting deadlines are now given.
- **DIS-02, DIS-03, DIS-04, DIS-06, ALG-01, ALG-04, INS-01, MAN-01, REG-01, REG-02:** wording that went beyond the law has been marked as guidance or good practice.
- **REG-03:** applies since 2024-11-08; the guidance reference is added.

### New obligations (16)
COOP-01 (investigations and inspections), COOP-02 (ACER data requests and original contracts), REP-06 (OMP reporting), REP-07 (data-quality procedures, Art 14 IR 2026), REP-08 (on-request transactions, 5-year records), REP-09 (periodic reporting, from 2027-10-29), REP-10 (hydrogen, from 2028-07-01), LNG-01 (daily LNG data), OMP-01, INS-03 (other exemptions), INS-04 (front running), DIS-07 (transparency platforms ≠ timely disclosure), DIS-08 (critical infrastructure), DIS-09 (authorised IIPs and RRMs, from 2027-10-29; date verified against Art 40 DR 2026/255), MAN-02 (information-based and benchmark manipulation).

### Counts
- REMIT obligations: 40 items, 146 checks (87 law, 24 ACER, 35 good practice).
- MAR adjacent regime: 3 items.
- Good practice: 15 items.

### Open items for the reviewer
1. **Bug in the REMIT MCP:** `get_provision("ACER Guidance 6.1, section 4.4")` returns section 6.1 because the edition number is read as the section. "ACER Guidance 4.4" works. Fix the parser in remit-mcp.
2. **Judgement calls on `basis`** that need a lawyer's eye: STR-02.c2 ("surveillance staff do not report to trading" marked as law), REG-02.c1–c2, COOP-01.c4 (preserving records marked as law).
3. **Left out on purpose:**
   - Personal account dealing: no REMIT-specific source was found.
   - The `large_final_customer` and `below_registration_threshold` addressees: no obligation uses them yet.
4. **Spot checks:** the two references behind the critical STR-01 change were re-checked and confirmed: ACER Guidance 9.2.1, paras. (416) and (418), which list DEA and order book providers as PPATs, and Q&A 2.4.6, the public STR channel. The other paragraph numbers the reviewers added, such as ACER Guidance 9.4.4.4 paras. (512)-(516), have not been re-checked by hand. Spot-check them before setting `status: reviewed`.
