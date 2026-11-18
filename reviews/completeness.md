# Completeness and usefulness review: REMIT checklist v0.1

Reviewed file: `reviews/remit-v0.1-under-review.yaml` (version 0.1.0, 22 obligations)
Review date: 2026-11-17
Scope: what is missing, mis-scoped or unusable. Legal accuracy line by line is covered by the other review.

Sources were checked through REMIT MCP and EU MAR MCP (texts fetched 2026-10-30 and 2026-11-10, last checked for changes 2026-11-17), plus the Nord Pool *REMIT Best Practice Report*, 3rd edition (updated 13 April 2026). All source text here is paraphrased.

Source links used throughout:

| Short name | Link |
|---|---|
| REMIT (consolidated) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02011R1227-20250205 |
| IR 2026/256 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R0256 |
| DR 2026/255 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R0255 |
| MAR (consolidated) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0596-20260605 |
| ACER Guidance 6.1 | https://www.acer.europa.eu/sites/default/files/documents/Other%20Documents/6.1st_Edition_ACER_Guidance.pdf |
| ACER Manual for new MPs 2026 | https://www.acer.europa.eu/sites/default/files/REMIT/Guidance%20on%20REMIT%20Application/REMIT-manual-new-market-participants-2026.pdf |
| ACER Q&A (30th ed.) | https://www.acer.europa.eu/sites/default/files/REMIT/Guidance%20on%20REMIT%20Application/Q%26As%20on%20REMIT/REMIT-30th-edition-QAs.pdf |
| Nord Pool Best Practice (3rd ed., 13 Apr 2026) | https://www.nordpoolgroup.com/49c34d/globalassets/download-center/remit/remit-best-practice-report.pdf |

> **Tool issue found while verifying (REMIT MCP).** `get_provision` misreads any citation that starts with "ACER Guidance 6.1, section …": it takes the edition number "6.1" as the section and returns section 6.1 (Introduction to market manipulation). I tried "ACER Guidance 6.1, section 4.4", "…section 2.4, paras. (51)–(59)" and "…section 2.5, paras. (63)–(66)", and all three returned section 6.1. "ACER Guidance 4.4" (no edition) works. The checklist uses the "6.1, section x" form in every `guidance` field, so any automatic source lookup the tool runs will fetch the wrong text. Fix the parser, or store guidance references without the edition number.

---

## 1. Missing binding obligations

Summary of the gaps. The proposed YAML follows.

| # | Gap | Why it matters for a procedure check |
|---|---|---|
| 1 | Cooperation with ACER and NRA investigations: ACER on-site inspections, which can be unannounced (Art 13a REMIT); ACER requests for information, where answers must be complete, correct and not misleading (Art 13b(3)); NRA powers, including asking for existing telephone and data-traffic records (Art 13(2)) | REMIT II gave ACER its own investigatory powers. Most firms have no dawn-raid or regulator-request procedure. |
| 2 | ACER requests for more data and for original contracts behind reported data (Art 8(9) IR 2026) | This is part of the reporting procedure, separate from investigations. |
| 3 | Orders and trades on an OMP are reported by the OMP; market participants must **not** report that data themselves; from 2027-10-29 they must give the OMP any data it lacks (Art 8(1), 8(4), 8(5) IR 2026) | REP-01/03 do not cover the ban on double reporting or the duty to pass data to the OMP. |
| 4 | Data-quality procedures: a person who reports must have procedures to check that its data is complete, accurate and on time (Art 14(2) IR 2026). For IIP disclosures, the responsibility for completeness, accuracy and timeliness sits with the market participant (Art 14(3)). | This is an explicit legal requirement to *have a procedure*, which makes it one of the easiest items for the tool to check. It is not in the list. |
| 5 | Transactions reportable only on ACER's request (intragroup deals off-OMP, small producers ≤10 MW or ≤20 MW for gas, upstream pipelines, voice-broker orders, etc.) and the **5-year record-keeping** for them (Art 5 IR 2026) | Without this, firms that rely on the intragroup exemption fail record keeping without noticing. |
| 6 | Periodic reporting (Art 4 IR 2026): supply to consumption units of 600 GWh/year or more, where the supplier must get a confirmation of capability from the customer; balancing, capacity mechanisms and gas storage; records kept for 5 years. These apply in phases from 2027-10-29 and 2028-04-29. | New in IR 2026. Not covered. |
| 7 | Hydrogen: supply, transport, storage, derivatives and balancing are reportable once a year from 2028-07-01, with exemptions (Art 4(8)–(10) IR 2026). Hydrogen facilities are also in the disclosure duty and in the definition of inside information (Art 4(1), Art 2(1)(b) REMIT). | The checklist never mentions hydrogen. DIS-01 and REP-05 examples cover only power and gas. |
| 8 | LNG market data: daily submission to ACER before 18:00 CET, with fixed data fields, units and timestamps (Art 7c, 7d, 8(1b) REMIT). These apply from 2025-01-01 and cover LNG traders wherever they are established (Art 2(25), 7a(2)). | A whole obligation and addressee type is missing. |
| 9 | OMP obligations: order-book reporting or access (Art 8(1a) REMIT; Art 8(1), 8(3), 8(11) IR 2026), including 5-year records | Relevant if the profile includes broker or exchange entities. Today these are folded into `ppat`. |
| 10 | Information-based and benchmark manipulation (Art 2(2)(b) and (c) REMIT): false or misleading information spread through the media or the internet, and false input to benchmarks | MAN-01 lists only trading-based practices. Firms that send data to price reporters, or post on social media, need this. |
| 11 | Other insider-trading exemptions: obligations that fell due before the inside information was known, TSO system-security purchases, national emergency rules (Art 3(3), 3(4)(a), 3(4)(c)) | A procedure that relies on them should document the conditions. Today only 3(4)(b) is covered. |
| 12 | Client-order information as inside information, and front running (Art 2(1)(ca) and Art 3 REMIT; ACER Guidance 5.3.2) | Applies to PPATs and to any firm trading for others (route-to-market, aggregators). |
| 13 | Delay of disclosure for classified critical-infrastructure information (Art 4(7)); publication under the transparency rules of 2019/943 and 715/2009 counts as effective but not necessarily timely (Art 4(4)) | Procedures that rely on ENTSO-E or ENTSOG transparency publication alone produce a false negative. |
| 14 | Use only *authorised* RRMs and IIPs once the DR 2026/255 regime applies (Art 4a and 9a REMIT; most of DR 2026/255 applies from 2027-10-29) | Vendor due diligence item. |
| 15 | MAR overlap: products that are financial instruments fall under MAR at the same time as REMIT (Art 1(2) REMIT; ACER Guidance 2.5). Emission allowance market participants have their own disclosure duty (Art 17(2) MAR) and **insider lists** (Art 18(8)(a) MAR). MAR STOR duties apply to PPAETs (Art 16 MAR). | REMIT has no insider-list duty, but many energy firms are also EAMPs. Keep these as an `adjacent_regime` block, not as REMIT. |

Not added, on purpose:
- A general REMIT record-keeping duty. There is none. Retention duties exist only in Art 5a(2) and (3) REMIT and Art 4(11), 5(3) and 8(3) IR 2026. ACER's 2026 manual *recommends* keeping transactions, disclosures and transaction communications for at least 5 years, so that item is in the good-practice layer (GP-11).
- Insider lists under REMIT. ACER only recommends "a list of insiders and/or mechanisms" to identify them (Guidance 3.3, para. 82). This is in the good-practice layer (GP-09), with `binding: guidance` noted.
- Penalty provisions (Art 18, 13g). These bind authorities, not procedures.

### 1a. Proposed obligations (paste under `obligations:`)

```yaml
  # ----------------------------------------------------------------- cooperation with authorities
  - id: REMIT-COOP-01
    area: cooperation
    title: Cooperate with ACER and NRA investigations, inspections and information requests
    legal_basis: ["Article 13(2) REMIT", "Article 13a REMIT", "Article 13b REMIT", "Article 9(1)(b)-(c) REMIT"]
    binding: law
    applies_to: [market_participant, third_country_mp, ppat, ppet, lng_market_participant, omp]
    status: in_force
    requirement: >-
      NRAs can access documents, demand information, inspect premises and require
      existing telephone and data-traffic records. Since REMIT II, ACER can also run
      its own investigations in cross-border cases. ACER's on-site inspections can be
      unannounced and can extend to staff's private premises with court authorisation.
      Persons must submit to inspections ordered by ACER decision. Answers to ACER
      information requests must be complete, correct and not misleading, within the
      deadline set. Refusal can lead to periodic penalty payments.
    procedure_should_cover:
      - Names the function that receives and coordinates NRA or ACER requests and inspections
      - States that replies to information requests are reviewed for completeness and correctness before submission
      - Tracks the response deadline set in each request
      - Gives instructions for an unannounced inspection (check identity and written authorisation, call legal/compliance, do not delete or alter records)
      - States that existing call recordings and chat or e-mail logs must be preserved when an inspection or request is received
    guidance: ["ACER Manual for new market participants 2026, section 6"]
    related_behaviours: [obstruction_of_investigation]
    notes: Article 13(2) powers are exercised under national law. ACER powers apply from 2024-05-07 (REMIT II).

  - id: REMIT-COOP-02
    area: reporting
    title: Answer ACER requests about reported data, including original contracts
    legal_basis: ["Article 8(9) REMIT IR 2026"]
    binding: law
    applies_to: [market_participant, lng_market_participant]
    status: in_force
    requirement: >-
      ACER may ask market participants, including LNG market participants, and
      reporting parties for more information and clarifications on reported data. This
      can include access to the original contracts.
    procedure_should_cover:
      - States that original contracts (including non-standard and OTC contracts) are stored so they can be produced on request
      - Names who answers ACER data-quality queries
    guidance: []
    related_behaviours: [data_reporting_failure]

  # ----------------------------------------------------------------- reporting (additions)
  - id: REMIT-REP-06
    area: reporting
    title: Leave OMP reporting to the OMP and give it the data it lacks
    legal_basis: ["Article 8(1) REMIT IR 2026", "Article 8(4) REMIT IR 2026", "Article 8(5) REMIT IR 2026", "Article 8(3) REMIT IR 2026"]
    binding: law
    applies_to: [market_participant]
    status: in_force
    requirement: >-
      OMPs report order-book data for all participants on their platform. Market
      participants must not report that data themselves. They report off-OMP
      transactions and exposures. From 2027-10-29 they must give the OMP any
      information it needs and does not have, at the latest by the reporting deadline.
      A participant may ask the OMP for continuous access to its reported data and the
      validation results.
    procedure_should_cover:
      - States that trades and orders on OMPs are reported by the OMP and not reported again by the company
      - Identifies which data the company must provide to each OMP and by when (from 2027-10-29)
      - Uses the OMP's reported-data access to reconcile OMP-reported records
    guidance: ["ACER Open Letter IR 2026, section 11"]
    related_behaviours: [data_reporting_failure]
    notes: Article 8(5) IR 2026 applies from 2027-10-29 (Article 17 IR 2026).

  - id: REMIT-REP-07
    area: reporting
    title: Have procedures to verify data quality
    legal_basis: ["Article 14(1) REMIT IR 2026", "Article 14(2) REMIT IR 2026", "Article 14(3) REMIT IR 2026"]
    binding: law
    applies_to: [market_participant, mp_disclosing]
    status: in_force
    requirement: >-
      Persons who report are responsible for the completeness, accuracy and timeliness
      of their data and must have procedures to verify this for data sent through RRMs.
      Market participants are responsible for the completeness, accuracy and
      timeliness of their IIP disclosures. Failures caused by a third party or an IIP
      are that party's responsibility.
    procedure_should_cover:
      - Describes a check of completeness of submitted reports against the trading system
      - Describes a check of accuracy of reported fields
      - Describes a check of timeliness against the applicable deadline
      - Describes how ACER/RRM rejections or validation errors are corrected and resubmitted
    guidance: []
    related_behaviours: [data_reporting_failure]

  - id: REMIT-REP-08
    area: reporting
    title: Keep records of transactions reportable only on request
    legal_basis: ["Article 5(1) REMIT IR 2026", "Article 5(3) REMIT IR 2026"]
    binding: law
    applies_to: [market_participant]
    status: in_force
    requirement: >-
      Some transactions are reportable only on a reasoned ACER request. Examples are
      off-OMP intragroup deals, output of small units (10 MW power, 20 MW gas),
      upstream pipelines, certain gas storage, market-based redispatch, voice-broker
      orders not on screen and gas balancing services. The participant must keep their
      details for at least five years.
    procedure_should_cover:
      - Lists which of the company's transactions fall under on-request reporting (e.g. intragroup)
      - States a retention period of at least five years for these transactions
      - Describes how an ad-hoc ACER request would be answered
    guidance: []
    related_behaviours: [data_reporting_failure]

  - id: REMIT-REP-09
    area: reporting
    title: Report periodic transactions
    legal_basis: ["Article 4(1)-(7) REMIT IR 2026", "Article 4(11) REMIT IR 2026"]
    binding: law
    applies_to: [market_participant, supplier_to_large_consumer]
    status: upcoming
    applies_from: 2027-10-29
    requirement: >-
      Some transactions are reported periodically rather than within days. Supply to a
      single consumption unit able to consume at least 600 GWh/year is reported every
      six months, and the supplier must get the customer's confirmation of that
      capability. Electricity balancing services are reported monthly, capacity
      mechanisms yearly and longer-term gas storage contracts and storage derivatives
      monthly. Records are kept for at least five years.
    procedure_should_cover:
      - Identifies which periodic categories apply to the company
      - States the reporting frequency and deadline for each applicable category
      - Requires written confirmation of consumption capability from customers at or above 600 GWh/year (suppliers)
      - States a retention period of at least five years
    guidance: ["ACER Open Letter IR 2026, section 13"]
    related_behaviours: [data_reporting_failure]
    notes: Article 4(2) applies from 2027-10-29; Article 4(1) and 4(3)-(7) from 2028-04-29 (Article 17 IR 2026).

  - id: REMIT-REP-10
    area: reporting
    title: Report hydrogen transactions annually
    legal_basis: ["Article 4(8) REMIT IR 2026", "Article 4(9) REMIT IR 2026", "Article 4(10) REMIT IR 2026", "Article 7(3) REMIT IR 2026"]
    binding: law
    applies_to: [hydrogen_participant]
    status: upcoming
    applies_from: 2028-07-01
    requirement: >-
      Hydrogen supply, transport, storage, derivatives (including CfDs) and balancing
      transactions in the Union are reported once a year, by the end of January of the
      following year. Exempt are output of units of 50 MW or less, geographically
      confined networks and supply to units below 600 GWh/year. Participants that only
      do exempt small-production or confined-network deals do not need to register.
    procedure_should_cover:
      - States whether the company trades hydrogen products and which exemption, if any, it relies on
      - Sets the annual reporting deadline (end of January for the previous year)
    guidance: []
    related_behaviours: [data_reporting_failure]

  # ----------------------------------------------------------------- LNG
  - id: REMIT-LNG-01
    area: lng_reporting
    title: Submit LNG market data daily
    legal_basis: ["Article 7c REMIT", "Article 7d REMIT", "Article 8(1b) REMIT", "Article 7a(2) REMIT", "Article 2(23)-(25) REMIT"]
    binding: law
    applies_to: [lng_market_participant]
    status: in_force
    requirement: >-
      Anyone engaged in LNG trading with EU delivery or EU regasification, wherever
      established, submits bids, offers and transactions to ACER every day, free of
      charge, as close to real time as possible and before the 18:00 CET price
      assessment. Required fields, units (EUR/MWh and MWh as well as contract units)
      and UTC timestamps are prescribed. Market participant obligations and
      prohibitions under REMIT apply to LNG market participants.
    procedure_should_cover:
      - States that LNG bids, offers and transactions are submitted daily before 18:00 CET
      - Lists the data fields required by Article 7d (incl. arrival window, delivery point, timestamps)
      - Requires prices in EUR/MWh and quantities in MWh in addition to contract units, with conversion rates
      - Names the reporting channel and the owner of the daily submission
    guidance: ["ACER TRUM v8.0, section 5", "ACER Guidance 6.1, section 2.4, paras. (55)-(56)"]
    related_behaviours: [data_reporting_failure]
    notes: Applies from 2025-01-01 (Article 3 Regulation (EU) 2024/1106).

  # ----------------------------------------------------------------- OMP (if profiled)
  - id: REMIT-OMP-01
    area: reporting
    title: OMP order-book reporting and records
    legal_basis: ["Article 8(1a) REMIT", "Article 8(1) REMIT IR 2026", "Article 8(3) REMIT IR 2026", "Article 8(11) REMIT IR 2026"]
    binding: law
    applies_to: [omp]
    status: in_force
    requirement: >-
      OMPs report order-book data (matched and unmatched orders, trades, lifecycle
      events) for all participants, or give ACER order-book access on request. They
      keep records for at least five years, give participants access to their reported
      data, and notify ACER to be included in the OMP list.
    procedure_should_cover:
      - States that the OMP reports order-book data on behalf of all participants
      - Describes how ACER order-book access requests are met within the deadline set
      - States a retention period of at least five years
      - Describes how participants can access their reported data and validation results
    guidance: []
    related_behaviours: [data_reporting_failure]

  # ----------------------------------------------------------------- insider trading (additions)
  - id: REMIT-INS-03
    area: insider_trading
    title: Document reliance on other insider-trading exemptions
    legal_basis: ["Article 3(3) REMIT", "Article 3(4)(a) REMIT", "Article 3(4)(c) REMIT"]
    binding: law
    applies_to: [market_participant, tso]
    status: in_force
    requirement: >-
      The prohibition does not apply to transactions that fulfil an obligation which
      fell due before the inside information was held, or to participants acting under
      national emergency rules. TSOs buying electricity, hydrogen or gas for safe
      system operation are exempt from the trading and recommending prohibitions.
    procedure_should_cover:
      - States which exemptions the company relies on, if any
      - Requires documentation that a pre-existing obligation or order existed before the inside information was received
    guidance: ["ACER Guidance 5.5.2", "ACER Q&A, Q 2.4.56"]
    related_behaviours: [insider_trading]

  - id: REMIT-INS-04
    area: insider_trading
    title: Prevent misuse of client order information (front running)
    legal_basis: ["Article 2(1)(ca) REMIT", "Article 3(1) REMIT"]
    binding: law
    applies_to: [ppat, ppet, trades_for_third_parties]
    status: in_force
    requirement: >-
      Information about a client's pending orders, passed to a service provider trading
      on the client's behalf, can be inside information for that provider. The provider
      must not use it to trade on its own account first (front running,
      pre-positioning) or to capture a spread through extra trades (double printing).
    procedure_should_cover:
      - Prohibits own-account trading ahead of or against client orders
      - Separates client order handling from own-account trading or monitors for front running
    guidance: ["ACER Guidance 5.3.2"]
    related_behaviours: [insider_trading, front_running]

  # ----------------------------------------------------------------- disclosure (additions)
  - id: REMIT-DIS-07
    area: disclosure
    title: Do not treat transparency-platform publication as timely disclosure
    legal_basis: ["Article 4(4) REMIT", "Article 4(6) REMIT"]
    binding: law
    applies_to: [mp_disclosing]
    status: in_force
    requirement: >-
      Publishing under the electricity and gas transparency rules (Regulation
      2019/943, Regulation 715/2009 and their network codes) is effective disclosure but
      not necessarily timely and public disclosure under Article 4(1). Those sector
      rules continue to apply alongside REMIT.
    procedure_should_cover:
      - States that publication on a transparency platform does not by itself meet the Article 4(1) timing requirement
    guidance: []
    related_behaviours: [failure_to_publish_inside_information]

  - id: REMIT-DIS-08
    area: disclosure
    title: Delay for classified critical-infrastructure information
    legal_basis: ["Article 4(7) REMIT"]
    binding: law
    applies_to: [mp_disclosing]
    status: in_force
    requirement: >-
      Disclosure of sensitive information on the protection of critical infrastructure
      may be delayed if it is classified in the participant's country.
    procedure_should_cover:
      - If relied on, names who decides that information is classified critical-infrastructure information and how this is documented
    guidance: ["ACER Guidance 4.5"]
    related_behaviours: [failure_to_publish_inside_information]

  - id: REMIT-DIS-09
    area: disclosure
    title: Use authorised IIPs and RRMs
    legal_basis: ["Article 4(1) REMIT", "Article 4a REMIT", "Article 8(1) REMIT", "Article 9a REMIT", "Delegated Regulation (EU) 2026/255"]
    binding: law
    applies_to: [market_participant, mp_disclosing]
    status: upcoming
    applies_from: 2027-10-29
    requirement: >-
      Inside information must be disclosed through IIPs, and data reported through RRMs.
      Under REMIT II both are authorised by ACER. The authorisation rules in Delegated
      Regulation 2026/255 apply mostly from 2027-10-29.
    procedure_should_cover:
      - Requires checking that the chosen IIP and RRM are authorised by ACER (or registered under the transitional regime)
      - Describes what happens if the IIP or RRM loses its authorisation
    guidance: ["ACER Open Letter DR 2026"]
    related_behaviours: [data_reporting_failure, failure_to_publish_inside_information]
    notes: Check the exact transitional date against Article 40 DR 2026/255 before publishing.

  # ----------------------------------------------------------------- manipulation (addition)
  - id: REMIT-MAN-02
    area: market_manipulation
    title: Prevent information-based and benchmark manipulation
    legal_basis: ["Article 2(2)(b) REMIT", "Article 2(2)(c) REMIT", "Article 2(3)(b) REMIT", "Article 5 REMIT"]
    binding: law
    applies_to: [any_person, market_participant]
    status: in_force
    requirement: >-
      Spreading false or misleading information through the media, including the
      internet, is market manipulation. So is giving false input to a benchmark or
      manipulating its calculation, where the person knew or ought to have known.
    procedure_should_cover:
      - Covers external communications (press, social media, analyst calls) about supply, demand or prices
      - Covers data submitted to price reporting agencies or benchmark administrators, including who may submit and how accuracy is checked
    guidance: ["ACER Guidance 6.2", "Nord Pool REMIT Best Practice 3rd ed., section 3.2"]
    related_behaviours: [dissemination_false_information, benchmark_manipulation]
```

### 1b. Adjacent regime: MAR (separate block, not REMIT)

Keep these out of `obligations:` so the REMIT gap score stays clean. Show them only when the profile has `eamp`, `mar_ppaet`, or "trades financial instruments" set to true.

```yaml
adjacent_regimes:
  - id: MAR-SCOPE-01
    framework: MAR
    title: Identify which products are also financial instruments
    legal_basis: ["Article 1(2) REMIT", "Article 2 MAR"]
    binding: law
    applies_to: [market_participant]
    requirement: >-
      REMIT applies without prejudice to MAR. Products that are financial instruments
      (e.g. cash-settled exchange futures) fall under MAR's insider dealing, disclosure
      and manipulation rules as well as REMIT's. Physically settled forwards and
      REMIT-carve-out OTF products are REMIT-only.
    procedure_should_cover:
      - Maps the company's traded products to REMIT-only or REMIT-and-MAR
      - States that MAR rules apply in addition where products are financial instruments
    guidance: ["ACER Guidance 2.5"]

  - id: MAR-EUA-01
    framework: MAR
    title: Emission allowance market participants - disclosure and insider lists
    legal_basis: ["Article 17(2) MAR", "Article 18(8)(a) MAR"]
    binding: law
    applies_to: [eamp]
    requirement: >-
      An emission allowance market participant above the emission and thermal-input
      thresholds discloses inside information on its installations' capacity and
      unavailability. It keeps insider lists for that information under Article 18
      paragraphs 1 to 5.
    procedure_should_cover:
      - States whether the company is above the Article 17(2) thresholds
      - Requires an insider list for emission-allowance inside information
    guidance: ["ESMA Q&A on MAR, Q 11.2"]

  - id: MAR-STOR-01
    framework: MAR
    title: STORs under MAR for financial instruments
    legal_basis: ["Article 16 MAR", "Article 15(2) REMIT"]
    binding: law
    applies_to: [mar_ppaet]
    requirement: >-
      PPAETs under MAR report suspicious orders and transactions in financial
      instruments to their competent financial authority. If they also execute
      non-financial wholesale energy products, REMIT Article 15(2) adds notification to
      ACER and the NRA within four weeks.
    procedure_should_cover:
      - Distinguishes MAR STORs (to the financial authority) from REMIT notifications (to ACER and NRA) and their deadlines
    guidance: ["ACER Guidance 9.2.2"]
```

---

## 2. Addressee model

Problems with the current list:

1. **`market_participant` is defined too narrowly.** It is tied to "reportable under Article 8(1)", which is the registration test in Art 9(1). Article 2(7) REMIT defines a market participant as anyone, including TSOs, DSOs, storage and LNG system operators, who enters into transactions or places orders on a wholesale energy market. Disclosure and the prohibitions apply on that wider basis.
2. **`mp_with_inside_info` mixes two tests.** Every market participant can *hold* inside information, for example about a competitor's plant. The *disclosure* duty only covers business or facilities that the participant, or its parent or related undertaking, owns, controls or is operationally responsible for (Art 4(1); ACER Guidance 2.4, paras. (47)–(48)). As written, the tool will tell a pure trading house to publish UMMs. Replace it with `mp_disclosing`.
3. **`ppat` merges OMPs and brokers**, and **`ppet` is incomplete.** ACER reads "execution" as including own-account trading. A PPET has Article 15 obligations only if it is a MAR Article 16 PPAET that also executes non-financial wholesale energy products (ACER Guidance 9.2.2, paras. (424)–(426)).
4. **Missing:** LNG market participants (any domicile), system operators (TSO, DSO, SSO, LSO, hydrogen network operator), large final customers (600 GWh or more), suppliers to them, hydrogen traders, entities below thresholds that need not register, firms subject to exposure reporting, emission allowance market participants, and firms trading for third parties.

Proposed replacement:

```yaml
addressees:
  market_participant: Any person, including TSOs, DSOs, SSOs and LNG system operators, that enters into transactions or places orders on one or more EU wholesale energy markets (Art 2(7) REMIT)
  registered_mp: Market participant entering into transactions reportable under Art 8(1), and therefore required to register (Art 9(1))
  third_country_mp: Registered market participant established or resident outside the EU (Art 9(1), second subparagraph)
  mp_disclosing: Market participant that, alone or through its parent or related undertaking, owns, controls or is operationally responsible for business or facilities (production, storage, consumption, transmission, LNG, hydrogen) to which inside information relates (Art 4(1))
  lng_market_participant: Any person, wherever established, engaged in LNG trading with EU delivery or EU regasification (Art 2(23), 2(25), 7a(2), 7c)
  hydrogen_participant: Market participant trading hydrogen supply, transport, storage, derivatives or balancing products in the EU (Art 2(4) REMIT; Art 4(8) IR 2026)
  tso: Transmission system operator acting as a market participant (special exemptions Art 3(3), 4(5))
  system_operator: DSO, storage system operator, LNG system operator or hydrogen network operator (Art 2(7), 2(11a)-(11c) REMIT; ACER Guidance 2.4)
  large_final_customer: Final customer with consumption capacity of 600 GWh/year or more, so its supply contracts are wholesale energy products (Art 2(4) last subparagraph, 2(5))
  supplier_to_large_consumer: Supplier to a consumption unit able to consume 600 GWh/year or more (Art 4(2) IR 2026)
  below_registration_threshold: Participant only doing small-production (power 10 MW or less, gas 20 MW or less, hydrogen 50 MW or less), upstream-pipeline or confined-hydrogen-network deals, so not required to register (Art 5(2), 4(10) IR 2026)
  exposure_reporter: Market participant above the exposure-reporting threshold (Art 6 IR 2026)
  algo_trader: Market participant engaging in algorithmic trading as defined in Art 2(18)
  dea_provider: Market participant allowing another person to use its trading code for direct electronic access to an OMP (Art 2(19), 5a(3))
  omp: Organised marketplace - energy exchange, energy broker platform, capacity platform (Art 2(20))
  ppat: Person professionally arranging transactions (reception and transmission of orders, e.g. broker), including OMPs (Art 2(8a), 15(1))
  ppet: Person professionally executing transactions that is a PPAET under Art 16 MAR and also executes non-financial wholesale energy products; execution includes own-account trading (Art 15(2); ACER Guidance 9.2.2)
  trades_for_third_parties: Firm that trades on behalf of others (route-to-market, aggregator, asset optimiser) and therefore receives client order information (Art 2(1)(ca))
  eamp: Emission allowance market participant under MAR (adjacent regime)
  mar_ppaet: Person professionally arranging or executing transactions in financial instruments under Art 16 MAR (adjacent regime)
  any_person: Any natural or legal person, including employees and traders
```

Suggested profile questions. Each answer sets flags, and checks whose `applies_to` does not match are skipped instead of reported as gaps.

```yaml
profile_questions:
  - {id: q_trades,        text: "Do you enter into transactions or place orders on EU wholesale power, gas, hydrogen or LNG markets?", sets: [market_participant]}
  - {id: q_reportable,    text: "Are any of those transactions reportable (i.e. not only small-unit / upstream / confined-network deals)?", sets: [registered_mp], else_sets: [below_registration_threshold]}
  - {id: q_third_country, text: "Is the company established outside the EU?", sets: [third_country_mp]}
  - {id: q_assets,        text: "Do you, your parent or a related undertaking own, control or operate production, storage, consumption, transmission, LNG or hydrogen facilities?", sets: [mp_disclosing]}
  - {id: q_lng,           text: "Do you trade LNG with EU delivery or EU regasification?", sets: [lng_market_participant]}
  - {id: q_h2,            text: "Do you trade hydrogen products?", sets: [hydrogen_participant]}
  - {id: q_operator,      text: "Are you a TSO, DSO, storage, LNG or hydrogen network operator?", sets: [tso | system_operator]}
  - {id: q_large_cons,    text: "Are you, or do you supply, a consumer of 600 GWh/year or more?", sets: [large_final_customer | supplier_to_large_consumer]}
  - {id: q_exposure,      text: "Are you above the exposure-reporting threshold for the coming year?", sets: [exposure_reporter]}
  - {id: q_algo,          text: "Do you use algorithmic trading, or provide DEA to an OMP?", sets: [algo_trader | dea_provider]}
  - {id: q_intermediary,  text: "Do you operate an OMP, act as broker, or execute orders for clients?", sets: [omp | ppat | trades_for_third_parties]}
  - {id: q_mar,           text: "Are you a MAR PPAET (e.g. investment firm) or an emission allowance market participant, or do you trade energy financial instruments?", sets: [mar_ppaet | eamp]}
```

---

## 3. Check quality: vague or false-positive-prone items

Rules applied. Each item makes one claim. It is phrased so that a passage either satisfies it or does not. It does not require something the law does not require, unless `binding` marks it as guidance. A further suggestion: give each check an `id` such as `REMIT-DIS-04.c2`, so that the tool's findings and user feedback stay stable across versions.

| Obligation / item (current) | Problem | Rewrite |
|---|---|---|
| REG-01 "Names the NRA … and its ACER code" | Two facts in one item. The ACER code is often in a register, not in the procedure, so this fires a false positive. | (a) "Names the NRA with which the company is registered." (b) "States where the company's ACER code is recorded." |
| REG-01 "Assigns an owner for the registration" | "Owner" is ambiguous (a person, a role, a team). | "Names the role or function responsible for submitting and maintaining the registration." |
| REG-02 "Sets a prompt timeline and an owner" | Two items, and "prompt" cannot be tested. | (a) "Sets a time limit for notifying registration changes to the NRA." (b) "Names the role responsible for submitting registration changes." |
| REG-02 "Requires periodic review of registration data" | Not required by Art 9(5). The trigger is any change. | Mark `binding: good_practice`, or rewrite as "Specifies a review frequency for registration data (e.g. annual)". |
| REG-03 (all) | Should only run if `third_country_mp`. | Add the `applies_to` gate. No text change. |
| REP-01 "Lists the reportable products and venues" | Usually in an annex or system, so a false positive. | "Lists the reportable products and venues, or refers to where that list is kept." |
| REP-01 "Covers OTC and non-standard contracts, not only exchange trades" | Combined with REP-06, it should also say OMP trades are *not* self-reported. | "States that transactions concluded outside OMPs, including non-standard contracts, are reported by the company or its delegate." |
| REP-02 "Has a daily or regular reconciliation that detects late or missing reports" | "Regular" is vague. Overlaps with Art 14(2) IR 2026. | Move to REP-07 as "Requires reconciliation of submitted reports against the trading system at a stated frequency." |
| REP-03 "Covers what happens when the RRM or third party fails" | Open-ended. | "Describes an escalation step when the RRM or third party cannot report, including informing ACER and/or the NRA." (ACER Q&A 2.4.50) |
| REP-03 "Requires checks that delegated reports were actually submitted and are correct" | Two checks. | (a) "Requires verification that delegated reports were submitted." (b) "Requires verification that delegated reports are accurate." |
| REP-04 "Explains how the 600 GWh threshold is assessed and by whom" | Two items. The assessment date is missing. | (a) "Describes the method for assessing the exposure-reporting threshold." (b) "Names the role that performs the threshold assessment." (c) "Assesses the threshold on transactions concluded by 31 December of the previous year." |
| REP-04 "Sets quarterly report deadlines from October 2027" | Fine, but make it precise. | "States that exposure reports are due quarterly, by the last day of the month after each quarter, starting October 2027." |
| REP-05 (single item) | Fine. Gate it to `mp_disclosing`. Add hydrogen. | "States how fundamental data and disclosed inside information on its power, gas, hydrogen or LNG facilities reach ACER (e.g. via the IIP)." |
| INS-01 "Defines inside information and gives energy-specific examples" | Two checks. | (a) "Defines inside information using the four REMIT criteria." (b) "Gives at least one example relevant to the company's assets or markets." |
| INS-01 "Describes how access to inside information is restricted (information barriers, need-to-know)" | Information barriers are good practice, not law. A firm with a need-to-know rule but no barriers would be flagged. | "States that inside information may only be shared on a need-to-know basis in the normal course of duties." (law, Art 3(1)(b)). Move barriers to GP-10. |
| INS-01 "Describes how staff are trained and what they must do when they receive inside information" | Two items. Training is good practice. | (a) "Requires staff who receive possible inside information to escalate it to a named function." (b) Move training to GP-05. |
| INS-01 (missing) | Inside information about *third-party* facilities. | Add: "States that inside information about other companies' facilities must not be traded on, even though the company has no duty to publish it." (ACER Guidance 2.4, para. (48); Q&A 3.7.12) |
| DIS-01 "Covers facilities of the parent and related undertakings" | Fires a false positive for standalone entities. | Make it conditional: "If the company has a parent or related undertakings with facilities, states who discloses for them." |
| DIS-01 "Describes who decides whether information is inside information and who publishes" | Two items. | (a) "Names who assesses whether information is inside information." (b) "Names who publishes on the IIP." |
| DIS-02 "Covers outages and events outside office hours" | "Covers" is vague. | "Names an on-call or 24/7 arrangement for publishing inside information outside office hours." |
| DIS-03 "Includes a check of completeness and correctness before publication" | "Includes a check" is vague. | "Requires the UMM to be checked against the required fields before publication, and names who checks." |
| DIS-04 "Lists the three conditions … and the no-trading rule" | Four elements in one item. | (a) "States the legitimate-interest, not-misleading and confidentiality conditions for delay." (b) "Prohibits trading decisions based on the delayed information." |
| DIS-04 "…with justification, using ACER's standard format" | Two items. | (a) "Requires notification of ACER and the NRA without delay when disclosure is delayed." (b) "Requires a written justification to be sent with that notification." |
| DIS-05 "Requires confidentiality obligations (NDAs) for external recipients" | **False positive.** A duty of confidentiality can arise from law, the articles of association or a contract (Art 4(3)). An NDA is one option, not a requirement. The simultaneous-disclosure rule is missing. | (a) "Requires that inside information shared externally in the normal course of duties goes only to recipients with a duty of confidentiality, or is published at the same time." (b) "Requires public disclosure as soon as possible after an unintentional disclosure." |
| MAN-01 "Describes the prohibited practices relevant to the company's markets, with examples" | "Relevant" cannot be tested. | "Names specific prohibited practices (for example wash trades, layering/spoofing, marking the close, capacity withholding), not only the general prohibition." |
| MAN-01 "Covers capacity withholding where the company owns … assets" | Conditional on the profile. | Gate on `mp_disclosing`: "Addresses physical and economic withholding of capacity from the company's assets." |
| MAN-01 "Covers internal trades between desks or group companies (wash trade risk)" | OK, but "covers" is vague. | "Sets rules for, or monitors, trades between the company's own desks or group entities." |
| ALG-01 "Describes ongoing monitoring of algorithm behaviour" | Vague. | "Names who monitors running algorithms and states that monitoring happens during trading hours." |
| ALG-01 "Describes controls against erroneous orders (including a kill switch)" | A kill switch is not named in Art 5a. | (a) "Describes controls that prevent erroneous orders." (b) "Provides a means to stop an algorithm immediately (kill switch)." Mark (b) as guidance / good practice (Nord Pool 3.3). |
| ALG-02 "Records that the notification was made and who maintains it" | Procedures describe processes, not facts. | (a) "Requires notification of the NRA and ACER (e.g. via CEREMP) before algorithmic trading starts." (b) "Names the role that maintains the notification." (CEREMP route: ACER Guidance 2.4, para. (52)) |
| ALG-04 "Describes controls over DEA clients" | Vague. | "Describes the systems and risk controls applied to orders sent by DEA clients, and how their application is evidenced." |
| STR-02 "Guarantees the independence of surveillance staff…" | "Guarantees" cannot be tested. Two items. | (a) "States that surveillance staff do not report to the trading function." (b) "Describes how conflicts of interest of surveillance staff are identified and managed." |
| STR-02 "Describes training for staff on REMIT compliance" | Not in Art 15(3). It duplicates the training item. | Move to GP-05. |
| STR-02 "Describes periodic review of the effectiveness of surveillance" | Guidance-level. | Keep, but mark it guidance-backed. Rewrite: "Specifies a frequency for reviewing alert calibration and surveillance effectiveness." |
| STR-03 "Explains how notifications are written and submitted via ACER's Notification Platform" | Two items. | (a) "Requires notifications to be submitted through ACER's notification platform." (b) "Requires notifications to state the reasons for suspicion." |
| STR-04 (single item) | Make it explicit. | "Requires notification of ACER and of the NRAs where the participant concerned is registered and where the product is delivered." |
| STR-01–04 for non-PPAT market participants | Will fire for every trading company. | The `applies_to` gate is enough. In the report, also note that voluntary notification and internal surveillance remain good practice. |

---

## 4. Good-practice layer (non-binding)

Add `good_practice` to the `binding` enum, and report these separately as "recommendations", never as "gaps". The Nord Pool report presents itself as guidance, not legal advice. ACER Guidance 6.1 is non-binding.

```yaml
good_practice:
  - id: REMIT-GP-01
    area: governance
    title: Independent, resourced compliance function with management backing
    binding: good_practice
    applies_to: [market_participant]
    practice: >-
      Clear REMIT roles. A compliance function independent of trading, with direct
      access to senior management and to all relevant information, and enough
      resources. Visible management support. Remuneration that does not reward risky
      trading.
    procedure_should_cover:
      - Names the REMIT compliance officer or responsible function
      - States that compliance reports to senior management independently of trading
      - States that compliance has access to all trading and operational information
    sources: ["Nord Pool REMIT Best Practice 3rd ed., sections 2.1.2-2.1.3", "ACER Guidance 10.2, para. (521) (compliance organisation)", "ACER Manual for new market participants 2026, section 6"]

  - id: REMIT-GP-02
    area: governance
    title: Documented REMIT risk assessment
    binding: good_practice
    applies_to: [market_participant]
    practice: >-
      Assess likelihood and impact of each REMIT risk (insider trading, manipulation
      types, reporting, disclosure), grade them, and focus controls on high risks.
    procedure_should_cover:
      - Refers to a REMIT risk assessment covering each market-abuse type
      - States how often the risk assessment is updated
    sources: ["Nord Pool REMIT Best Practice 3rd ed., section 2.1.4", "ACER Guidance 10.2, para. (521) (compliance risks)"]

  - id: REMIT-GP-03
    area: governance
    title: Annual compliance plan and report to management
    binding: good_practice
    applies_to: [market_participant]
    practice: A compliance programme built on prevention, detection and response, with a yearly plan and a year-end report to management.
    procedure_should_cover:
      - Requires an annual compliance plan
      - Requires a periodic compliance report to management
    sources: ["Nord Pool REMIT Best Practice 3rd ed., section 2.1.5", "ACER Guidance 10.2, para. (521) (reporting processes)"]

  - id: REMIT-GP-04
    area: training
    title: Role-based REMIT training with records
    binding: good_practice
    applies_to: [market_participant]
    practice: >-
      Training tailored to risk groups (traders, plant/control-room staff, back
      office). It is given at onboarding, refreshed regularly, and repeated after
      incidents or rule changes, with assessments and attendance records. Mandatory
      market-manipulation training for traders.
    procedure_should_cover:
      - Defines training audiences by role
      - States the training frequency, including onboarding
      - Requires attendance and results to be recorded
    sources: ["Nord Pool REMIT Best Practice 3rd ed., section 2.1.6, Appendix 4, section 3.4.11", "ACER Manual for new market participants 2026, sections 5-6"]

  - id: REMIT-GP-05
    area: governance
    title: Speak-up channel for REMIT concerns
    binding: good_practice
    applies_to: [market_participant]
    practice: Low threshold for raising concerns, protection against retaliation, an optional anonymous channel, and statistics reported to management.
    procedure_should_cover:
      - Describes how staff can raise REMIT concerns, including anonymously
      - States that people who raise concerns are protected from retaliation
    sources: ["Nord Pool REMIT Best Practice 3rd ed., section 2.1.6"]

  - id: REMIT-GP-06
    area: cooperation
    title: Regulator-contact policy and dawn-raid manual
    binding: good_practice
    applies_to: [market_participant]
    practice: >-
      Compliance manages contact with regulators. A dawn-raid manual instructs
      reception and the responsible person: check IDs and legal basis, call counsel,
      protect privileged documents, delete nothing, and review the record before
      signing. Supports REMIT-COOP-01.
    procedure_should_cover:
      - Names the function that manages contact with NRAs and ACER
      - Refers to a dawn-raid manual or inspection instructions
    sources: ["Nord Pool REMIT Best Practice 3rd ed., section 2.1.6 and Appendix 5", "ACER Manual for new market participants 2026, section 6"]

  - id: REMIT-GP-07
    area: inside_information
    title: Framework for identifying inside information, with tested thresholds
    binding: guidance
    applies_to: [market_participant]
    practice: >-
      Internal rules to assess whether facts are inside information (e.g. tested
      capacity or MW thresholds), mapped information flows, and handling rules that
      fit the company's structure and trading.
    procedure_should_cover:
      - Sets criteria or thresholds for assessing whether an event is inside information
      - Maps where inside information arises (assets, departments) and where it flows
    sources: ["ACER Guidance 3.3, paras. (81)-(83)", "Nord Pool REMIT Best Practice 3rd ed., sections 3.1 and 3.4"]

  - id: REMIT-GP-08
    area: inside_information
    title: Identify insiders and log access to inside information
    binding: guidance
    applies_to: [market_participant]
    practice: >-
      A list of insiders or a mechanism to identify them. A log of who received inside
      information and when, kept especially while disclosure is delayed.
    procedure_should_cover:
      - Requires a list of persons with access to inside information, or another mechanism to identify them
      - Requires a log of who received inside information and when during a delayed disclosure
    sources: ["ACER Guidance 3.3, para. (82)", "Nord Pool REMIT Best Practice 3rd ed., section 3.1 (pp. 47, 52)"]

  - id: REMIT-GP-09
    area: inside_information
    title: Information barriers and a documented trade stop
    binding: good_practice
    applies_to: [market_participant]
    practice: >-
      Separate traders from people with inside information (physical separation,
      access controls with logging). A documented trade-stop mechanism (alarm,
      notification or system block) for when a trader holds inside information or a
      barrier fails, recording start, end, trigger and products.
    procedure_should_cover:
      - Describes the information barriers between asset operations and trading
      - Describes a trade-stop mechanism and what is recorded when it is used
    sources: ["Nord Pool REMIT Best Practice 3rd ed., sections 3.1.2-3.1.3 (pp. 43-48)", "ACER Manual for new market participants 2026, section 6"]

  - id: REMIT-GP-10
    area: record_keeping
    title: Record trader communications and keep trading records for five years
    binding: good_practice
    applies_to: [market_participant]
    practice: >-
      Record telephone calls of relevant staff such as traders. Keep transactions,
      disclosures and transaction communications for at least five years. NRAs can
      demand existing call and data-traffic records (Art 13(2)(d) REMIT), so records
      that exist must be retrievable.
    procedure_should_cover:
      - States which communication channels of traders are recorded (phone, chat, e-mail)
      - States a retention period of at least five years for transactions, disclosures and trade communications
    sources: ["ACER Manual for new market participants 2026, section 6", "Nord Pool REMIT Best Practice 3rd ed., section 3.1 (p. 47)"]

  - id: REMIT-GP-11
    area: market_conduct
    title: Trading mandates and rationale for unusual trades
    binding: good_practice
    applies_to: [market_participant]
    practice: >-
      Document trading mandates and deviations from them. Record the reason for
      unusual orders or trades. Keep a list of behaviours to avoid. Control media
      communication and the accuracy of benchmark inputs.
    procedure_should_cover:
      - Refers to documented trading mandates and limits
      - Requires traders to record the reason for unusual orders or trades
    sources: ["Nord Pool REMIT Best Practice 3rd ed., section 3.2 (pp. 56-59)"]

  - id: REMIT-GP-12
    area: market_conduct
    title: Erroneous-order handling
    binding: good_practice
    applies_to: [market_participant]
    practice: >-
      Prevent errors (pre-trade limits, fewer manual steps). When an error happens,
      assess whether it is inside information, using tested thresholds, or a
      manipulation risk. Publish through the IIP with a template if needed, and
      investigate the incident.
    procedure_should_cover:
      - Requires each erroneous order or trade to be assessed as possible inside information
      - Describes the incident investigation steps after an erroneous order
    sources: ["Nord Pool REMIT Best Practice 3rd ed., section 3.4"]

  - id: REMIT-GP-13
    area: algorithmic_trading
    title: Algorithm governance, including vendor algorithms
    binding: good_practice
    applies_to: [algo_trader]
    practice: >-
      Formal design review, testing in a separate environment, documented approval
      before go-live, kill and suspend functions, real-time monitoring, and the same
      standards applied to third-party vendor algorithms.
    procedure_should_cover:
      - Requires documented approval before an algorithm or a change goes live
      - Applies the same controls to vendor-supplied algorithms
    sources: ["Nord Pool REMIT Best Practice 3rd ed., section 3.3 (incl. 3.3.9) and Appendix 7"]

  - id: REMIT-GP-14
    area: governance
    title: Compliance involvement in new products and markets
    binding: good_practice
    applies_to: [market_participant]
    practice: Compliance is involved in organisational changes and new product or market decisions before trading starts (registration, reporting and surveillance coverage).
    procedure_should_cover:
      - Requires compliance sign-off before trading a new product or on a new venue
    sources: ["Nord Pool REMIT Best Practice 3rd ed., section 2.1.3 (pp. 13-14)"]

  - id: REMIT-GP-15
    area: governance
    title: Monitoring, periodic review and internal audit
    binding: good_practice
    applies_to: [market_participant]
    practice: >-
      A three-lines-of-defence model. Trade monitoring even where Art 15 does not
      apply. Staff told that they may be monitored. The risk assessment and plan are
      reviewed regularly and after rule changes or incidents. Internal audit of the
      compliance function.
    procedure_should_cover:
      - Describes monitoring of the company's own trading by a function independent of the traders
      - States a review frequency for REMIT procedures and triggers for ad-hoc review
      - Provides for internal audit of REMIT compliance
    sources: ["Nord Pool REMIT Best Practice 3rd ed., section 2.1.7", "ACER Guidance 10.2, para. (521) (monitoring improvements)"]
```

**Left out on purpose:** *personal account dealing*. Neither the Nord Pool report (I checked the full text in three parts) nor the ACER documents in REMIT MCP give a REMIT-specific source for it. Add it only once a source is found, for example MiFID rules for investment firms, which I did not verify here.

---

## 5. Procedure mapping

Document types: **IIP** = inside information policy, **MCP** = market conduct policy, **TRP** = transaction reporting procedure, **SUR** = surveillance & STOR procedure, **REG** = registration procedure, **ALG** = algo trading policy. Two more types are proposed: **REGINT** (regulatory interaction / investigation procedure) and **CM** (umbrella REMIT compliance manual). Many firms, especially small ones, have one manual. ACER's 2026 manual recommends a single internal REMIT compliance manual. If the user uploads a CM, run **all** checks against it.

```yaml
procedure_mapping:
  # obligation id: [primary document, secondary documents...]
  REMIT-REG-01:  [REG]
  REMIT-REG-02:  [REG, IIP]        # IIP change -> registration update
  REMIT-REG-03:  [REG, REGINT]
  REMIT-REP-01:  [TRP]
  REMIT-REP-02:  [TRP]
  REMIT-REP-03:  [TRP]
  REMIT-REP-04:  [TRP]
  REMIT-REP-05:  [IIP, TRP]
  REMIT-REP-06:  [TRP]
  REMIT-REP-07:  [TRP, IIP]        # Art 14(3) part belongs to IIP
  REMIT-REP-08:  [TRP]
  REMIT-REP-09:  [TRP]
  REMIT-REP-10:  [TRP]
  REMIT-LNG-01:  [TRP]
  REMIT-OMP-01:  [TRP]
  REMIT-COOP-01: [REGINT, MCP]
  REMIT-COOP-02: [TRP, REGINT]
  REMIT-INS-01:  [IIP, MCP]
  REMIT-INS-02:  [IIP, MCP]
  REMIT-INS-03:  [MCP, IIP]
  REMIT-INS-04:  [MCP, SUR]
  REMIT-DIS-01:  [IIP]
  REMIT-DIS-02:  [IIP]
  REMIT-DIS-03:  [IIP]
  REMIT-DIS-04:  [IIP]
  REMIT-DIS-05:  [IIP]
  REMIT-DIS-06:  [IIP]
  REMIT-DIS-07:  [IIP]
  REMIT-DIS-08:  [IIP]
  REMIT-DIS-09:  [IIP, TRP]
  REMIT-MAN-01:  [MCP, SUR]
  REMIT-MAN-02:  [MCP]
  REMIT-ALG-01:  [ALG]
  REMIT-ALG-02:  [ALG, REG]
  REMIT-ALG-03:  [ALG]
  REMIT-ALG-04:  [ALG]
  REMIT-STR-01:  [SUR]
  REMIT-STR-02:  [SUR]
  REMIT-STR-03:  [SUR]
  REMIT-STR-04:  [SUR]
  MAR-SCOPE-01:  [MCP]
  MAR-EUA-01:    [IIP]
  MAR-STOR-01:   [SUR]
  REMIT-GP-01:   [CM, MCP]
  REMIT-GP-02:   [CM]
  REMIT-GP-03:   [CM]
  REMIT-GP-04:   [CM, MCP]
  REMIT-GP-05:   [CM, MCP]
  REMIT-GP-06:   [REGINT]
  REMIT-GP-07:   [IIP]
  REMIT-GP-08:   [IIP]
  REMIT-GP-09:   [IIP, MCP]
  REMIT-GP-10:   [MCP]
  REMIT-GP-11:   [MCP]
  REMIT-GP-12:   [MCP, IIP]
  REMIT-GP-13:   [ALG]
  REMIT-GP-14:   [CM, MCP]
  REMIT-GP-15:   [SUR, CM]
document_rules:
  - If the uploaded document is a combined REMIT manual (CM), run all applicable checks.
  - Run primary-document checks as gaps. When a check comes from a secondary document, report it as "may be covered elsewhere" rather than as a gap.
  - Ask the user to tag the document type at upload. Keyword-based auto-detection is a fallback only.
```

---

## Notes for the checklist author

- `REP-02` and the new reporting items depend on the IR 2026 phasing: deadlines from 2026-04-29, Art 4(2) and 8(5) from 2027-10-29, the rest of Art 4 from 2028-04-29, hydrogen from 2028-07-01. Every `status: upcoming` item should get an `applies_from` date, and the tool should check it against today's date.
- `meta.framework` should mention IR 2026/256 and DR 2026/255, plus MAR as an adjacent regime.
- The `binding` enum needs `good_practice`. Keep `guidance` for ACER statements and `good_practice` for industry sources, so users can see the difference.
