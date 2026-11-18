# Compliance Lens report — Nordwind Energy Trading GmbH

Checklist v0.3.0 · assessed as of 2026-11-18 · model Claude (blind stand-in, not API)

Automated first-pass review. It reads only the documents supplied and is not legal advice; a lawyer should confirm each finding.

## inside-information-policy.docx

42 checks · **5 conflicts** · **4 gaps** · 4 weak points · 8 ACER expectations · 6 recommendations · 15 covered

### Conflicts with REMIT

- **REMIT-INS-01.c5** States that inside information about other companies' facilities must not be traded on, even though the company has no duty to publish it. · §1.3  
  Excludes a group company's plant from the whole policy, including the trading prohibition; REMIT prohibits trading on inside information about any facility, including other companies' facilities.  
  > Kraftwerk Elbufer is owned by our sister company Nordwind Erzeugung GmbH and is therefore outside the scope of this policy.  
  _Prevent trading on inside information — Article 2(1) REMIT, Article 3(1) REMIT, Article 3(2) REMIT, Article 3(5) REMIT_
- **REMIT-DIS-01.c1** Names the IIP(s) used. · §4.1  
  Names EEX Transparency Platform but makes IIP publication optional ('where possible') with the website as primary channel; REMIT II requires disclosure through an IIP.  
  > Inside information is published on our company website www.nordwind-trading.example and, where possible, also on the EEX Transparency Platform.  
  _Disclose inside information through an IIP — Article 4(1) REMIT_
- **REMIT-DIS-01.c2** States who discloses inside information on facilities of the parent or related undertakings. · §1.3  
  Article 4(1) covers facilities owned, controlled or operated by the parent or related undertakings; the policy excludes the sister company's Kraftwerk Elbufer and does not assign disclosure responsibility.  
  > Only information about facilities owned by Nordwind Trading itself needs to be published under this policy.  
  _Disclose inside information through an IIP — Article 4(1) REMIT_
- **REMIT-DIS-02.c1** Requires inside information to be published without delay. · §4.2  
  A 24-hour window is inconsistent with disclosure in a timely manner / without delay under Article 4(1).  
  > Publication takes place within 24 hours of the information becoming known to Nordwind Trading.  
  _Disclose in a timely manner (ACER target - within one hour) — Article 4(1) REMIT_
- **REMIT-DIS-07.c1** Does not rely on transparency-platform publication alone to meet the Article 4(1) disclosure duty. · §4.5  
  Relies on ENTSO-E publication alone; under Article 4(4) such publication is effective but not necessarily timely and public disclosure under Article 4(1).  
  > Where an outage is also published on the ENTSO-E Transparency Platform, this satisfies our obligation under REMIT and no separate Urgent Market Message is needed.  
  _Do not treat transparency-platform publication as timely disclosure — Article 4(4) REMIT, Article 4(6) REMIT_

### Gaps (required by law, missing)

- **REMIT-INS-01.c3** Covers cancelling or amending orders placed before the information was received.  
  The prohibition covers acquiring or disposing only; cancelling or amending orders placed before receipt of inside information is not addressed.  
  _Prevent trading on inside information — Article 2(1) REMIT, Article 3(1) REMIT, Article 3(2) REMIT, Article 3(5) REMIT_
- **REMIT-DIS-04.c3** Prohibits trading decisions based on the delayed information.  
  No prohibition on trading decisions based on information whose disclosure is delayed.  
  _Delay disclosure only under the Article 4(2) conditions — Article 4(2) REMIT_
- **REMIT-DIS-04.c4** Requires notification of ACER and the NRA without delay when disclosure is delayed, with a written justification.  
  No notification of ACER and the NRA with justification; only internal documentation is required.  
  _Delay disclosure only under the Article 4(2) conditions — Article 4(2) REMIT_
- **REMIT-DIS-05.c2** Requires public disclosure as soon as possible after an unintentional disclosure.  
  No requirement to publish as soon as possible after an unintentional disclosure.  
  _Handle selective disclosure — Article 4(3) REMIT_

### Weak points (required by law, only partly covered)

- **REMIT-REP-05.c1** States how fundamental data and disclosed inside information on the company's facilities reach ACER (e.g. via the IIP's reporting). · §4.6  
  Explains how published UMMs reach ACER, but says nothing on fundamental capacity/unavailability data, and publication on the IIP is only 'where possible', so ACER may not receive all disclosures.  
  > The EEX Transparency Platform forwards our published Urgent Market Messages to ACER.  
  _Provide fundamental data and disclosed inside information to ACER — Article 8(5) REMIT, Article 8(6) REMIT, Articles 11-12 REMIT IR 2026_
- **REMIT-DIS-02.c2** Prohibits trading or recommending trading on the information until the UMM is published. · §3.1  
  General prohibition on trading while holding inside information implies no trading before publication, but there is no explicit rule tying trading to UMM publication.  
  > Employees who possess inside information must not acquire or dispose of wholesale energy products to which the information relates  
  _Disclose in a timely manner (ACER target - within one hour) — Article 4(1) REMIT_
- **REMIT-DIS-04.c2** States the legitimate-interest, not-misleading and confidentiality conditions for delay. · §5.1  
  Only a broad commercial-interest ground; the not-misleading and confidentiality conditions of Article 4(2) are absent.  
  > The Head of Trading may decide to delay publication of inside information if publication would harm Nordwind Trading's commercial interests.  
  _Delay disclosure only under the Article 4(2) conditions — Article 4(2) REMIT_
- **REMIT-DIS-06.c2** States that trading on the information remains prohibited until it is public. · §3.1  
  General insider-trading prohibition applies, but the policy does not state that it continues until publication, e.g. during an IIP outage.  
  > Employees who possess inside information must not acquire or dispose of wholesale energy products to which the information relates  
  _Have a fallback if the IIP fails — Article 4(1) REMIT_

### ACER expects

- **REMIT-DIS-01.c3** States that any other channel (e.g. website) is additional only and must carry identical content. · §4.1  
  The website is the primary channel and the IIP secondary; ACER expects the website to be additional only, with identical content. No identical-content requirement.  
  > Inside information is published on our company website www.nordwind-trading.example and, where possible, also on the EEX Transparency Platform.  
  _Disclose inside information through an IIP — Article 4(1) REMIT_
- **REMIT-DIS-02.c3** Sets a target of publication at the latest within one hour. · §4.2  
  Sets a 24-hour deadline, far beyond ACER's expectation of publication at the latest within one hour.  
  > Publication takes place within 24 hours of the information becoming known to Nordwind Trading.  
  _Disclose in a timely manner (ACER target - within one hour) — Article 4(1) REMIT_
- **REMIT-DIS-03.c3** Excludes executive statements and advertising from the message; any disclaimer is avoided or clearly separated.  
  Nothing excludes executive statements, advertising or disclaimers from UMMs.  
  _Make disclosures complete, correct and in the standard UMM format — Article 4(1) REMIT_
- **REMIT-DIS-04.c5** Requires disclosure as soon as the legitimate interest ends.  
  No requirement to disclose once the legitimate interest ends.  
  _Delay disclosure only under the Article 4(2) conditions — Article 4(2) REMIT_
- **REMIT-DIS-06.c1** Describes a backup publication channel that meets the IIP minimum quality requirements, and when to use it.  
  No backup publication channel or IIP-failure procedure is described.  
  _Have a fallback if the IIP fails — Article 4(1) REMIT_
- **REMIT-GP-07.c2** Maps where inside information arises (assets, departments) and where it flows.  
  No map of where inside information arises (assets, departments) or how it flows.  
  _Framework for identifying inside information — non-binding_
- **REMIT-DIS-02.c5** Requires the publication time to be recorded. · §P31  
  The UMM template contains a publication date/time field, but the policy does not require the publication time to be recorded internally.  
  > publication date/time  
  _Disclose in a timely manner (ACER target - within one hour) — Article 4(1) REMIT_
- **REMIT-DIS-03.c4** Requires the UMM to be checked against the required fields before publication, and names who checks. · §4.3  
  A four-eyes check by Market Operations is required, but it is not stated that the check is against the required Annex VII fields.  
  > Each message is checked by a second person from the Market Operations team before publication.  
  _Make disclosures complete, correct and in the standard UMM format — Article 4(1) REMIT_

### Recommendations (good practice)

- **REMIT-DIS-02.c4** Names an on-call or 24/7 arrangement for publishing inside information outside office hours.  
  No on-call or 24/7 publication arrangement outside office hours.  
  _Disclose in a timely manner (ACER target - within one hour) — Article 4(1) REMIT_
- **REMIT-DIS-04.c7** Uses ACER's standard notification format (unless the NRA requires another).  
  No reference to ACER's standard delay-notification format.  
  _Delay disclosure only under the Article 4(2) conditions — Article 4(2) REMIT_
- **REMIT-DIS-08.c1** If relied on, names who decides that information is classified critical-infrastructure information and how this is documented.  
  Delay for classified critical-infrastructure information is not addressed.  
  _Delay for classified critical-infrastructure information — Article 4(7) REMIT_
- **REMIT-GP-08.c2** Requires a log of who received inside information and when, especially during a delayed disclosure.  
  No log of who received inside information and when, including during delayed disclosure.  
  _Identify insiders and log access to inside information — non-binding_
- **REMIT-GP-09.c2** Describes a trade-stop mechanism and what is recorded when it is used.  
  No trade-stop mechanism or record of its use is described.  
  _Information barriers and a documented trade stop — non-binding_
- **REMIT-DIS-01.c5** Names who publishes on the IIP. · §4.3  
  Implies Market Operations prepares and publishes UMMs, but does not expressly name who publishes on the IIP.  
  > Each message is checked by a second person from the Market Operations team before publication.  
  _Disclose inside information through an IIP — Article 4(1) REMIT_

### May be covered in another document

- REMIT-REG-02.c1 (missing) Requires any change to the information in the registration form (e.g. management, ownership, place of publication of inside information) to be communicated to the NRA.
- REMIT-REG-02.c2 (missing) Requires changes to be notified to the NRA promptly.
- REMIT-REG-02.c3 (missing) Lists the internal events that trigger a registration update.
- REMIT-REG-02.c4 (missing) Sets an internal time limit (e.g. number of working days) for notifying registration changes.
- REMIT-REG-02.c5 (missing) Names the role responsible for submitting registration changes.
- REMIT-REG-02.c6 (missing) Specifies a review frequency for registration data (e.g. annual).
- REMIT-INS-03.c1 (missing) States which insider-trading exemptions the company relies on, if any.
- REMIT-INS-03.c2 (missing) Requires evidence that the agreement or order behind an exempt transaction was concluded or placed before the inside information was received.
- REMIT-GP-12.c1 (missing) Requires each erroneous order or trade to be assessed as possible inside information.
- REMIT-GP-12.c2 (missing) Describes the incident investigation steps after an erroneous order.

### Not yet in force

- REMIT-DIS-09 Use authorised IIPs and RRMs — applies from 2027-10-29

<details><summary>Covered</summary>

- REMIT-INS-01.c1 §2.1 Defines inside information using the REMIT criteria (precise, non-public, relating to wholesale energy products, likely to significantly affect prices).
- REMIT-INS-01.c2 §3.1, §3.2 Prohibits trading, recommending and disclosure outside the normal course of duties while holding inside information.
- REMIT-INS-01.c4 §3.2 States that inside information may be shared only on a need-to-know basis in the normal course of duties.
- REMIT-INS-01.c6 §2.2 Gives at least one example of inside information relevant to the company's assets or markets.
- REMIT-INS-01.c7 §3.3 Requires staff who receive possible inside information to escalate it to a named function.
- REMIT-DIS-01.c4 §2.2 Names who assesses whether information is inside information.
- REMIT-DIS-03.c1 §4.3, §P31 Refers to the UMM fields in Annex VII of the REMIT MoP or provides a template.
- REMIT-DIS-03.c2 §4.4 Requires the UMM to be updated when the expected duration or capacity changes.
- REMIT-DIS-04.c1 §5.1 Names who may decide to delay disclosure.
- REMIT-DIS-04.c6 §5.2 Requires the decision to delay to be documented.
- REMIT-DIS-05.c1 §3.6 Requires that inside information shared externally goes only to recipients with a duty of confidentiality, or is published at the same time.
- REMIT-DIS-05.c3 §3.6 Uses NDAs for external recipients who have no confidentiality duty by law.
- REMIT-GP-07.c1 §2.2 Sets criteria or thresholds for assessing whether an event is inside information.
- REMIT-GP-08.c1 §3.4 Requires a list of persons with access to inside information, or another mechanism to identify them.
- REMIT-GP-09.c1 §3.5 Describes the information barriers between asset operations and trading.

</details>

## market-conduct-policy.docx

32 checks · **1 conflicts** · **5 gaps** · 5 weak points · 0 ACER expectations · 11 recommendations · 10 covered

### Conflicts with REMIT

- **REMIT-ALG-03.c1** States a retention period of at least five years. · §4.6  
  Three-year retention is shorter than the five years required by Article 5a(2) REMIT.  
  > Documentation of algorithms, including strategy descriptions, parameters and test results, is kept for three years.  
  _Keep algorithmic trading records for five years — Article 5a(2), third subparagraph, REMIT_

### Gaps (required by law, missing)

- **REMIT-MAN-01.c3** Addresses physical and economic withholding of capacity from the company's assets.  
  Physical and economic capacity withholding are not addressed.  
  _Prevent trading-based market manipulation — Article 5 REMIT, Article 2(2)(a) REMIT, Article 2(3) REMIT_
- **REMIT-MAN-02.c2** Covers data submitted to price reporting agencies or benchmark administrators.  
  Data submitted to price reporting agencies or benchmark administrators is not addressed.  
  _Prevent information-based and benchmark manipulation — Article 2(2)(b) REMIT, Article 2(2)(c) REMIT, Article 2(3)(b) REMIT, Article 5 REMIT_
- **REMIT-ALG-01.c4** Describes business continuity arrangements for system failure.  
  No business continuity arrangements for algorithmic system failure.  
  _Systems and risk controls for algorithmic trading — Article 5a(1) REMIT_
- **REMIT-ALG-02.c1** Requires notification of the NRA and ACER (e.g. via CEREMP) before algorithmic trading starts.  
  No notification of algorithmic trading to the NRA and ACER.  
  _Notify algorithmic trading to the NRA and ACER — Article 5a(2) REMIT_
- **MAR-SCOPE-01.c2** States that MAR rules apply in addition where products are financial instruments.  
  No statement that MAR applies to products that are financial instruments.  
  _Identify which products are also financial instruments — Article 1(2) REMIT, Article 2 MAR_

### Weak points (required by law, only partly covered)

- **REMIT-MAN-01.c1** Prohibits market manipulation and attempted market manipulation. · §2.1  
  Market manipulation is prohibited, but attempted market manipulation is not mentioned.  
  > Market manipulation is strictly prohibited.  
  _Prevent trading-based market manipulation — Article 5 REMIT, Article 2(2)(a) REMIT, Article 2(3) REMIT_
- **REMIT-MAN-02.c1** Covers external communications (press, social media, analyst calls) about supply, demand or prices. · §2.3  
  Restricts who communicates externally, but does not prohibit disseminating false or misleading information on supply, demand or prices, nor cover analyst calls.  
  > Only the Communications department may speak to the press or publish statements about market conditions. Traders must not comment on market rumours on social media.  
  _Prevent information-based and benchmark manipulation — Article 2(2)(b) REMIT, Article 2(2)(c) REMIT, Article 2(3)(b) REMIT, Article 5 REMIT_
- **REMIT-ALG-01.c3** Describes testing before deployment and after changes. · §4.4  
  Testing before deployment is required, but not testing after changes to existing algorithms.  
  > New algorithms are tested in the EPEX simulation environment before go-live  
  _Systems and risk controls for algorithmic trading — Article 5a(1) REMIT_
- **REMIT-ALG-02.c2** Keeps strategy descriptions, parameters, limits and controls ready to provide on request. · §4.6  
  Strategy descriptions, parameters and test results are kept, but limits and controls are not listed and nothing addresses providing them on request.  
  > Documentation of algorithms, including strategy descriptions, parameters and test results, is kept for three years.  
  _Notify algorithmic trading to the NRA and ACER — Article 5a(2) REMIT_
- **REMIT-ALG-03.c2** Lists the records kept (strategies, parameters, limits, tests, changes). · §4.6  
  Strategies, parameters and tests are listed; limits and changes are not.  
  > Documentation of algorithms, including strategy descriptions, parameters and test results  
  _Keep algorithmic trading records for five years — Article 5a(2), third subparagraph, REMIT_

### Recommendations (good practice)

- **REMIT-MAN-01.c4** Sets rules for, or monitors, trades between the company's own desks or group entities. · §2.4  
  Permits intra-group trades on the exchange without controls or monitoring; such trades without change in beneficial interest risk being wash trades, a practice ACER treats as manipulation.  
  > Trades between Nordwind group companies on EPEX SPOT are allowed to balance positions within the group.  
  _Prevent trading-based market manipulation — Article 5 REMIT, Article 2(2)(a) REMIT, Article 2(3) REMIT_
- **REMIT-INS-03.c1** States which insider-trading exemptions the company relies on, if any.  
  No insider-trading exemptions are stated.  
  _Document reliance on other insider-trading exemptions — Article 3(3) REMIT, Article 3(4)(a) REMIT, Article 3(4)(c) REMIT_
- **REMIT-INS-03.c2** Requires evidence that the agreement or order behind an exempt transaction was concluded or placed before the inside information was received.  
  No evidence requirement for exempt transactions.  
  _Document reliance on other insider-trading exemptions — Article 3(3) REMIT, Article 3(4)(a) REMIT, Article 3(4)(c) REMIT_
- **REMIT-MAN-02.c3** Names who may submit data to price reporters and how its accuracy is checked.  
  No rule on who submits data to price reporters or how accuracy is checked.  
  _Prevent information-based and benchmark manipulation — Article 2(2)(b) REMIT, Article 2(2)(c) REMIT, Article 2(3)(b) REMIT, Article 5 REMIT_
- **REMIT-ALG-02.c3** Names the role that maintains the notification.  
  No role is named to maintain the algorithmic-trading notification.  
  _Notify algorithmic trading to the NRA and ACER — Article 5a(2) REMIT_
- **MAR-SCOPE-01.c1** Maps the company's traded products to REMIT-only or REMIT-and-MAR.  
  Traded products are not mapped to REMIT-only or REMIT-and-MAR.  
  _Identify which products are also financial instruments — Article 1(2) REMIT, Article 2 MAR_
- **REMIT-GP-11.c2** Requires traders to record the reason for unusual orders or trades.  
  No requirement to record reasons for unusual orders or trades.  
  _Trading mandates and rationale for unusual trades — non-binding_
- **REMIT-GP-12.c1** Requires each erroneous order or trade to be assessed as possible inside information.  
  Erroneous orders are not assessed as possible inside information.  
  _Erroneous-order handling — non-binding_
- **REMIT-GP-12.c2** Describes the incident investigation steps after an erroneous order.  
  No incident investigation steps after erroneous orders.  
  _Erroneous-order handling — non-binding_
- **REMIT-GP-13.c2** Applies the same controls to vendor-supplied algorithms.  
  Vendor-supplied algorithms are not addressed.  
  _Algorithm governance, including vendor algorithms — non-binding_
- **REMIT-GP-13.c1** Requires documented approval before an algorithm or a change goes live. · §4.4  
  Written approval before go-live for new algorithms, but changes to existing algorithms are not covered.  
  > New algorithms are tested in the EPEX simulation environment before go-live and require the written approval of the Head of Trading.  
  _Algorithm governance, including vendor algorithms — non-binding_

### May be covered in another document

- REMIT-INS-01.c1 (missing) Defines inside information using the REMIT criteria (precise, non-public, relating to wholesale energy products, likely to significantly affect prices).
- REMIT-INS-01.c2 (missing) Prohibits trading, recommending and disclosure outside the normal course of duties while holding inside information.
- REMIT-INS-01.c3 (missing) Covers cancelling or amending orders placed before the information was received.
- REMIT-INS-01.c4 (missing) States that inside information may be shared only on a need-to-know basis in the normal course of duties.
- REMIT-INS-01.c5 (missing) States that inside information about other companies' facilities must not be traded on, even though the company has no duty to publish it.
- REMIT-INS-01.c6 (missing) Gives at least one example of inside information relevant to the company's assets or markets.
- REMIT-INS-01.c7 (missing) Requires staff who receive possible inside information to escalate it to a named function.
- REMIT-GP-01.c1 (partial) Names the REMIT compliance officer or responsible function.
- REMIT-GP-01.c2 (missing) States that compliance reports to senior management independently of trading.
- REMIT-GP-01.c3 (missing) States that compliance has access to all trading and operational information.
- REMIT-GP-04.c1 (missing) Defines training audiences by role.
- REMIT-GP-04.c2 (missing) States the training frequency, including onboarding.
- REMIT-GP-04.c3 (missing) Requires attendance and results to be recorded.
- REMIT-GP-09.c1 (missing) Describes the information barriers between asset operations and trading.
- REMIT-GP-09.c2 (missing) Describes a trade-stop mechanism and what is recorded when it is used.
- REMIT-GP-14.c1 (missing) Requires compliance sign-off before trading a new product or on a new venue.

<details><summary>Covered</summary>

- REMIT-MAN-01.c2 §2.2 Names specific prohibited practices (e.g. wash trades, layering, spoofing, marking the close), not only the general prohibition.
- REMIT-MAN-01.c5 §2.5 Requires staff to report manipulation concerns to compliance.
- REMIT-ALG-01.c1 §4.2 Defines trading thresholds and limits for algorithms.
- REMIT-ALG-01.c2 §4.2, §4.3 Describes controls that prevent erroneous orders.
- REMIT-ALG-01.c5 §4.5 Names who monitors running algorithms.
- REMIT-ALG-01.c6 §4.2 Specifies limit types (e.g. price, volume, order rate).
- REMIT-ALG-01.c7 §4.3 Provides a means to stop an algorithm immediately (kill switch).
- REMIT-GP-10.c1 §3.2 States which communication channels of traders are recorded (phone, chat, e-mail).
- REMIT-GP-10.c2 §3.2 States a retention period of at least five years for transactions, disclosures and trade communications.
- REMIT-GP-11.c1 §3.1 Refers to documented trading mandates and limits.

</details>

## transaction-reporting-procedure.docx

35 checks · **6 conflicts** · **5 gaps** · 1 weak points · 2 ACER expectations · 6 recommendations · 15 covered

### Conflicts with REMIT

- **REMIT-REG-02.c2** Requires changes to be notified to the NRA promptly. · §1.3  
  Batching changes to an annual January review can delay notification up to a year; Article 9(5) requires prompt notification.  
  > Changes to registration data are reported to the Bundesnetzagentur at the annual review of registration data in January.  
  _Keep registration data up to date — Article 9(5) REMIT_
- **REMIT-REP-01.c3** Covers orders to trade as well as executed transactions. · §2.2  
  REMIT requires reporting of orders to trade as well as transactions; excluding non-executed orders conflicts with Article 8(1).  
  > Only executed transactions are reported. Orders that are not executed are not reportable.  
  _Report transactions and orders through an RRM — Article 8(1) REMIT, Article 8(4) REMIT IR 2026, Article 3 IR 1348/2014 (until 2027-10-28), Article 3 REMIT IR 2026 (from 2027-10-29)_
- **REMIT-REP-02.c2** States the ten-working-day deadline for non-standard contracts. · §3.2  
  One month exceeds the ten-working-day deadline for non-standard contracts.  
  > Non-standard contracts are reported within one month of their conclusion.  
  _Meet reporting deadlines — Article 10 REMIT IR 2026, Article 17 REMIT IR 2026_
- **REMIT-REP-06.c1** States that orders and trades on OMPs are reported by the OMP and not reported again by the company. · §2.4  
  Market participants must not report OMP data themselves; the company duplicates exchange reporting.  
  > To be on the safe side, Nordwind Trading additionally reports all trades executed on EEX and EPEX SPOT through TradeLink RRM.  
  _Leave OMP reporting to the OMP and give it the data it lacks — Article 8(1) REMIT IR 2026, Article 8(3) REMIT IR 2026, Article 8(4) REMIT IR 2026, Article 8(5) REMIT IR 2026_
- **REMIT-REP-08.c1** Requires records of transactions reportable only on ACER request (e.g. off-OMP intragroup deals) to be kept. · §2.5  
  Off-OMP intragroup trades are reportable on ACER request and their details must be kept; the procedure declares them irrelevant and keeps no records.  
  > Intragroup trades between Nordwind companies concluded outside an organised market place are not REMIT-relevant and are not recorded for REMIT purposes.  
  _Keep records of transactions reportable only on request — Article 5(1) REMIT IR 2026, Article 5(3) REMIT IR 2026_
- **REMIT-REP-08.c2** States a retention period of at least five years following conclusion for these transactions. · §2.5  
  No records are kept, conflicting with the five-year retention requirement following conclusion.  
  > are not REMIT-relevant and are not recorded for REMIT purposes.  
  _Keep records of transactions reportable only on request — Article 5(1) REMIT IR 2026, Article 5(3) REMIT IR 2026_

### Gaps (required by law, missing)

- **REMIT-REG-01.c2** Requires registration to be in place before any new legal entity in the group starts reportable trading.  
  No requirement that new group entities register before starting reportable trading.  
  _Register with the NRA before trading — Article 9(1) REMIT, Article 9(4) REMIT_
- **REMIT-REP-02.c3** Applies the deadlines to lifecycle events (amendments, cancellations, terminations).  
  Deadlines are not applied to lifecycle events (amendments, cancellations, terminations).  
  _Meet reporting deadlines — Article 10 REMIT IR 2026, Article 17 REMIT IR 2026_
- **REMIT-REP-03.c3** Requires verification that delegated reports are accurate.  
  Only receipt of exchange confirmations is checked; accuracy of delegated reports is not verified.  
  _Keep responsibility for delegated reporting — Article 8(1) REMIT, Article 8(4) REMIT_
- **REMIT-REP-07.c2** Describes a check that reported fields are accurate.  
  No check that reported fields are accurate; reconciliation targets completeness only.  
  _Have procedures to verify data quality — Article 14(1) REMIT IR 2026, Article 14(2) REMIT IR 2026, Article 14(3) REMIT IR 2026_
- **REMIT-REP-07.c3** Describes a check that reports were submitted within the applicable deadline.  
  No check that reports were submitted within the applicable deadline.  
  _Have procedures to verify data quality — Article 14(1) REMIT IR 2026, Article 14(2) REMIT IR 2026, Article 14(3) REMIT IR 2026_

### Weak points (required by law, only partly covered)

- **REMIT-REG-02.c1** Requires any change to the information in the registration form (e.g. management, ownership, place of publication of inside information) to be communicated to the NRA. · §1.3  
  Changes are reported to the NRA, but only annually rather than as they occur; specific items like place of publication of inside information are not mentioned.  
  > Changes to registration data are reported to the Bundesnetzagentur at the annual review of registration data in January.  
  _Keep registration data up to date — Article 9(5) REMIT_

### ACER expects

- **REMIT-REP-03.c4** Describes an escalation step when the RRM or third party cannot report, including informing the NRA and ACER.  
  No escalation, including informing NRA and ACER, when the RRM or third party cannot report.  
  _Keep responsibility for delegated reporting — Article 8(1) REMIT, Article 8(4) REMIT_
- **REMIT-REP-02.c4** Classifies trades on OMPs as standard (T+2) and OTC trades as non-standard (T+10), including off-venue lifecycle events on OMP trades (T+2). · §3.1, §3.2  
  Distinguishes standard and non-standard contracts, but does not classify OMP vs OTC trades or address off-venue lifecycle events on OMP trades.  
  > Standard contracts are reported by the end of the next working day (T+1).  
  _Meet reporting deadlines — Article 10 REMIT IR 2026, Article 17 REMIT IR 2026_

### Recommendations (good practice)

- **REMIT-REG-02.c4** Sets an internal time limit (e.g. number of working days) for notifying registration changes. · §1.3  
  Instead of a short internal time limit, changes wait for the annual review, inconsistent with prompt notification.  
  > Changes to registration data are reported to the Bundesnetzagentur at the annual review of registration data in January.  
  _Keep registration data up to date — Article 9(5) REMIT_
- **REMIT-REP-08.c3** Identifies which of the company's transactions are reportable only on request. · §2.5  
  Identifies off-OMP intragroup trades but wrongly classifies them as not REMIT-relevant rather than reportable on request.  
  > Intragroup trades between Nordwind companies concluded outside an organised market place are not REMIT-relevant  
  _Keep records of transactions reportable only on request — Article 5(1) REMIT IR 2026, Article 5(3) REMIT IR 2026_
- **REMIT-REG-02.c3** Lists the internal events that trigger a registration update.  
  No internal trigger events for registration updates are listed.  
  _Keep registration data up to date — Article 9(5) REMIT_
- **REMIT-REP-08.c4** Describes how an ad-hoc ACER request for these transactions would be answered.  
  No process for answering ad-hoc ACER requests for these transactions.  
  _Keep records of transactions reportable only on request — Article 5(1) REMIT IR 2026, Article 5(3) REMIT IR 2026_
- **REMIT-COOP-02.c2** Names who answers ACER data-quality queries.  
  No one is named to answer ACER data-quality queries.  
  _Answer ACER requests about reported data, including original contracts — Article 8(9) REMIT IR 2026_
- **REMIT-REP-06.c3** Uses the OMP's reported-data access to reconcile OMP-reported records. · §4.1  
  Exchange confirmations are checked for receipt, but OMP reported-data access is not used to reconcile records.  
  > Back Office checks every morning that the exchanges' reporting confirmations have been received.  
  _Leave OMP reporting to the OMP and give it the data it lacks — Article 8(1) REMIT IR 2026, Article 8(3) REMIT IR 2026, Article 8(4) REMIT IR 2026, Article 8(5) REMIT IR 2026_

### May be covered in another document

- REMIT-REP-05.c1 (missing) States how fundamental data and disclosed inside information on the company's facilities reach ACER (e.g. via the IIP's reporting).
- REMIT-ALG-02.c1 (missing) Requires notification of the NRA and ACER (e.g. via CEREMP) before algorithmic trading starts.
- REMIT-ALG-02.c2 (missing) Keeps strategy descriptions, parameters, limits and controls ready to provide on request.
- REMIT-ALG-02.c3 (missing) Names the role that maintains the notification.

### Not yet in force

- REMIT-DIS-09 Use authorised IIPs and RRMs — applies from 2027-10-29
- REMIT-REP-04 Report exposures (from 2027) — applies from 2027-01-01
- REMIT-REP-06 Leave OMP reporting to the OMP and give it the data it lacks — applies from 2027-10-29
- REMIT-REP-09b Report balancing, capacity-mechanism and gas-storage transactions periodically — applies from 2028-04-29

<details><summary>Covered</summary>

- REMIT-REG-01.c1 §1.1 Names the NRA with which the company is registered.
- REMIT-REG-01.c3 §1.2 Names the role or function responsible for submitting and maintaining the registration.
- REMIT-REG-01.c4 §1.1 States where the company's ACER code is recorded.
- REMIT-REG-02.c5 §1.2 Names the role responsible for submitting registration changes.
- REMIT-REG-02.c6 §1.3 Specifies a review frequency for registration data (e.g. annual).
- REMIT-REP-01.c1 §2.1 Lists the reportable products and venues, or refers to where that list is kept.
- REMIT-REP-01.c2 §2.3, §4.1 Names the RRM(s) and any third party reporting on the company's behalf.
- REMIT-REP-01.c4 §2.3 States that transactions concluded outside OMPs, including non-standard contracts, are reported by the company or its delegate.
- REMIT-REP-02.c1 §3.1 States the two-working-day deadline for standard contracts.
- REMIT-REP-03.c1 §2.3, §4.1 Identifies which trades are reported by OMPs or third parties and which the company reports itself.
- REMIT-REP-03.c2 §4.1 Requires verification that delegated reports were submitted.
- REMIT-REP-07.c1 §4.2 Describes a check that the reports the company submits (itself or through its RRM) are complete against the trading system.
- REMIT-REP-07.c4 §4.3 Describes how rejections or validation errors from the RRM or ACER are corrected and resubmitted.
- REMIT-REP-07.c5 §4.2 States the frequency of reconciliation against the trading system (e.g. daily).
- REMIT-COOP-02.c1 §5.1 Keeps original contracts (including OTC and non-standard contracts) retrievable so they can be produced if ACER requests them.

</details>
