# Compliance Lens report — Nordwind Energy Trading GmbH

Checklist v0.3.0 · assessed as of 2026-11-18 · model claude-sonnet-5-5 via Claude Code

Automated first-pass review. It reads only the documents supplied and is not legal advice; a lawyer should confirm each finding.

## inside-information-policy.docx

42 checks · **4 conflicts** · **4 gaps** · 6 weak points · 7 ACER expectations · 6 recommendations · 15 covered

### Conflicts with REMIT

- **REMIT-INS-01.c5** States that inside information about other companies' facilities must not be traded on, even though the company has no duty to publish it. · §1.3  
  The policy excludes a sister company's plant from its scope. It does not say that inside information about other companies' facilities must not be traded on.  
  > Kraftwerk Elbufer is owned by our sister company Nordwind Erzeugung GmbH and is therefore outside the scope of this policy.  
  _Prevent trading on inside information — Article 2(1) REMIT, Article 3(1) REMIT, Article 3(2) REMIT, Article 3(5) REMIT_
- **REMIT-DIS-01.c2** States who discloses inside information on facilities of the parent or related undertakings. · §1.3  
  The policy limits disclosure to facilities owned by Nordwind Trading and excludes sister-company plants. It does not say who discloses for parent or related undertakings.  
  > Only information about facilities owned by Nordwind Trading itself needs to be published under this policy.  
  _Disclose inside information through an IIP — Article 4(1) REMIT_
- **REMIT-DIS-02.c1** Requires inside information to be published without delay. · §4.2  
  A 24-hour window is not 'without delay' and conflicts with the requirement of timely, as-soon-as-possible disclosure.  
  > Publication takes place within 24 hours of the information becoming known to Nordwind Trading.  
  _Disclose in a timely manner (ACER target - within one hour) — Article 4(1) REMIT_
- **REMIT-DIS-07.c1** Does not rely on transparency-platform publication alone to meet the Article 4(1) disclosure duty. · §4.5  
  The policy relies on transparency-platform publication alone to meet the REMIT disclosure duty. That conflicts with Article 4(1), under which such publication is not necessarily timely disclosure.  
  > Where an outage is also published on the ENTSO-E Transparency Platform, this satisfies our obligation under REMIT and no separate Urgent Market Message is needed.  
  _Do not treat transparency-platform publication as timely disclosure — Article 4(4) REMIT, Article 4(6) REMIT_

### Gaps (required by law, missing)

- **REMIT-INS-01.c3** Covers cancelling or amending orders placed before the information was received. · §3.1  
  The ban covers only acquiring and disposing. Cancelling or amending existing orders is not mentioned.  
  > must not acquire or dispose of wholesale energy products to which the information relates  
  _Prevent trading on inside information — Article 2(1) REMIT, Article 3(1) REMIT, Article 3(2) REMIT, Article 3(5) REMIT_
- **REMIT-DIS-04.c3** Prohibits trading decisions based on the delayed information.  
  The delay section does not prohibit trading decisions based on the delayed information.  
  _Delay disclosure only under the Article 4(2) conditions — Article 4(2) REMIT_
- **REMIT-DIS-04.c4** Requires notification of ACER and the NRA without delay when disclosure is delayed, with a written justification. · §5.2  
  Internal documentation only. There is no requirement to notify ACER and the NRA without delay.  
  > Compliance documents each decision to delay publication, including the reasons.  
  _Delay disclosure only under the Article 4(2) conditions — Article 4(2) REMIT_
- **REMIT-DIS-05.c2** Requires public disclosure as soon as possible after an unintentional disclosure.  
  No rule on publishing as soon as possible after an unintentional disclosure.  
  _Handle selective disclosure — Article 4(3) REMIT_

### Weak points (required by law, only partly covered)

- **REMIT-REP-05.c1** States how fundamental data and disclosed inside information on the company's facilities reach ACER (e.g. via the IIP's reporting). · §4.6  
  States that messages reach ACER via the EEX platform. Nothing covers fundamental data on facilities, and the route is described only for disclosed inside information. The ENTSO-E point in P22 wrongly treats it as a substitute.  
  > The EEX Transparency Platform forwards our published Urgent Market Messages to ACER.  
  _Provide fundamental data and disclosed inside information to ACER — Article 8(5) REMIT, Article 8(6) REMIT, Articles 11-12 REMIT IR 2026_
- **REMIT-DIS-01.c1** Names the IIP(s) used. · §4.1  
  The company website is the primary channel. EEX is optional ('where possible'), and the document does not designate an IIP as the required route.  
  > published on our company website www.nordwind-trading.example and, where possible, also on the EEX Transparency Platform.  
  _Disclose inside information through an IIP — Article 4(1) REMIT_
- **REMIT-DIS-02.c2** Prohibits trading or recommending trading on the information until the UMM is published. · §3.1  
  The general insider-trading ban exists, but it is not tied to the period before the UMM is published. It does not state that trading or recommending is barred until publication.  
  > must not acquire or dispose of wholesale energy products to which the information relates  
  _Disclose in a timely manner (ACER target - within one hour) — Article 4(1) REMIT_
- **REMIT-DIS-04.c2** States the legitimate-interest, not-misleading and confidentiality conditions for delay. · §5.1  
  Only a broad commercial-harm test is given. The not-misleading and confidentiality conditions are absent, and commercial harm is wider than the legitimate-interest condition.  
  > if publication would harm Nordwind Trading's commercial interests  
  _Delay disclosure only under the Article 4(2) conditions — Article 4(2) REMIT_
- **REMIT-DIS-05.c1** Requires that inside information shared externally goes only to recipients with a duty of confidentiality, or is published at the same time. · §3.6  
  Requires an NDA for advisers and banks. It does not cover all external recipients, nor the alternative of simultaneous publication.  
  > Inside information may be shared with external advisers and banks only after they have signed a non-disclosure agreement.  
  _Handle selective disclosure — Article 4(3) REMIT_
- **REMIT-DIS-06.c2** States that trading on the information remains prohibited until it is public. · §3.1  
  The trading ban applies to those possessing inside information, but the document does not state that it continues until publication, including during IIP failure.  
  > must not acquire or dispose of wholesale energy products to which the information relates  
  _Have a fallback if the IIP fails — Article 4(1) REMIT_

### ACER expects

- **REMIT-DIS-01.c3** States that any other channel (e.g. website) is additional only and must carry identical content. · §4.1  
  The website is treated as the primary channel and the IIP as optional, which reverses the rule. There is no identical-content requirement.  
  > published on our company website ... and, where possible, also on the EEX Transparency Platform.  
  _Disclose inside information through an IIP — Article 4(1) REMIT_
- **REMIT-DIS-02.c3** Sets a target of publication at the latest within one hour. · §4.2  
  The target is 24 hours, far longer than ACER's one-hour expectation.  
  > Publication takes place within 24 hours of the information becoming known to Nordwind Trading.  
  _Disclose in a timely manner (ACER target - within one hour) — Article 4(1) REMIT_
- **REMIT-DIS-02.c5** Requires the publication time to be recorded.  
  The document does not require the publication time to be recorded. Only the template has a publication date/time field.  
  _Disclose in a timely manner (ACER target - within one hour) — Article 4(1) REMIT_
- **REMIT-DIS-03.c3** Excludes executive statements and advertising from the message; any disclaimer is avoided or clearly separated.  
  Nothing excludes executive statements or advertising from the message, and nothing addresses disclaimers.  
  _Make disclosures complete, correct and in the standard UMM format — Article 4(1) REMIT_
- **REMIT-DIS-04.c5** Requires disclosure as soon as the legitimate interest ends.  
  No requirement to publish as soon as the legitimate interest ends.  
  _Delay disclosure only under the Article 4(2) conditions — Article 4(2) REMIT_
- **REMIT-GP-07.c2** Maps where inside information arises (assets, departments) and where it flows. · §3.4, §3.5  
  There is no map of where inside information arises or flows. The document only mentions plants and a separate operations building.  
  > Compliance keeps a list of all persons who have access to inside information about the plants marketed by Nordwind Trading.  
  _Framework for identifying inside information — non-binding_
- **REMIT-DIS-06.c1** Describes a backup publication channel that meets the IIP minimum quality requirements, and when to use it. · §4.1  
  Website and EEX are mentioned as channels, but no backup channel for IIP failure, minimum quality requirements or switching trigger is described.  
  > published on our company website www.nordwind-trading.example and, where possible, also on the EEX Transparency Platform  
  _Have a fallback if the IIP fails — Article 4(1) REMIT_

### Recommendations (good practice)

- **REMIT-DIS-01.c5** Names who publishes on the IIP. · §4.1  
  Names the channels but not a person, role or team responsible for publishing. It also treats the website as primary and the IIP as optional, which is not a statement of who publishes.  
  > Inside information is published on our company website www.nordwind-trading.example and, where possible, also on the EEX Transparency Platform.  
  _Disclose inside information through an IIP — Article 4(1) REMIT_
- **REMIT-DIS-02.c4** Names an on-call or 24/7 arrangement for publishing inside information outside office hours.  
  No on-call or 24/7 arrangement for publishing outside office hours is mentioned.  
  _Disclose in a timely manner (ACER target - within one hour) — Article 4(1) REMIT_
- **REMIT-DIS-04.c7** Uses ACER's standard notification format (unless the NRA requires another).  
  No mention of ACER's standard notification format.  
  _Delay disclosure only under the Article 4(2) conditions — Article 4(2) REMIT_
- **REMIT-DIS-08.c1** If relied on, names who decides that information is classified critical-infrastructure information and how this is documented. · §5.1  
  The delay provisions do not rely on the critical-infrastructure delay, so the check does not apply. Silence on it is not a defect.  
  > The Head of Trading may decide to delay publication of inside information if publication would harm Nordwind Trading's commercial interests.  
  _Delay for classified critical-infrastructure information — Article 4(7) REMIT_
- **REMIT-GP-09.c2** Describes a trade-stop mechanism and what is recorded when it is used. · §3.1  
  There is a personal trading prohibition, but no trade-stop mechanism or recording of its use.  
  > must not acquire or dispose of wholesale energy products to which the information relates  
  _Information barriers and a documented trade stop — non-binding_
- **REMIT-GP-08.c2** Requires a log of who received inside information and when, especially during a delayed disclosure. · §3.4  
  A list of persons with access exists, but there is no log of who received information and when, and none for delayed disclosure.  
  > Compliance keeps a list of all persons who have access to inside information  
  _Identify insiders and log access to inside information — non-binding_

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
- REMIT-DIS-03.c4 §4.3 Requires the UMM to be checked against the required fields before publication, and names who checks.
- REMIT-DIS-04.c1 §5.1 Names who may decide to delay disclosure.
- REMIT-DIS-04.c6 §5.2 Requires the decision to delay to be documented.
- REMIT-DIS-05.c3 §3.6 Uses NDAs for external recipients who have no confidentiality duty by law.
- REMIT-GP-07.c1 §2.2 Sets criteria or thresholds for assessing whether an event is inside information.
- REMIT-GP-08.c1 §3.4 Requires a list of persons with access to inside information, or another mechanism to identify them.
- REMIT-GP-09.c1 §3.5 Describes the information barriers between asset operations and trading.

</details>

## market-conduct-policy.docx

32 checks · **1 conflicts** · **5 gaps** · 5 weak points · 0 ACER expectations · 12 recommendations · 9 covered

### Conflicts with REMIT

- **REMIT-ALG-03.c1** States a retention period of at least five years. · §4.6  
  Algorithm documentation is retained for three years, shorter than the five years REMIT requires. The five-year period in P14 covers only recordings, chats and tickets.  
  > Documentation of algorithms, including strategy descriptions, parameters and test results, is kept for three years.  
  _Keep algorithmic trading records for five years — Article 5a(2), third subparagraph, REMIT_

### Gaps (required by law, missing)

- **REMIT-MAN-01.c3** Addresses physical and economic withholding of capacity from the company's assets.  
  Physical and economic withholding of capacity is not addressed.  
  _Prevent trading-based market manipulation — Article 5 REMIT, Article 2(2)(a) REMIT, Article 2(3) REMIT_
- **REMIT-MAN-02.c2** Covers data submitted to price reporting agencies or benchmark administrators.  
  Data submitted to price reporting agencies or benchmark administrators is not addressed.  
  _Prevent information-based and benchmark manipulation — Article 2(2)(b) REMIT, Article 2(2)(c) REMIT, Article 2(3)(b) REMIT, Article 5 REMIT_
- **REMIT-ALG-01.c4** Describes business continuity arrangements for system failure.  
  No business continuity or system failure arrangements are described; only a kill switch and automatic rejection exist, which are not continuity arrangements.  
  _Systems and risk controls for algorithmic trading — Article 5a(1) REMIT_
- **REMIT-ALG-02.c1** Requires notification of the NRA and ACER (e.g. via CEREMP) before algorithmic trading starts.  
  The policy does not require notifying the NRA or ACER about algorithmic trading.  
  _Notify algorithmic trading to the NRA and ACER — Article 5a(2) REMIT_
- **MAR-SCOPE-01.c2** States that MAR rules apply in addition where products are financial instruments.  
  MAR is not mentioned, and there is no statement that it applies in addition for financial instruments.  
  _Identify which products are also financial instruments — Article 1(2) REMIT, Article 2 MAR_

### Weak points (required by law, only partly covered)

- **REMIT-MAN-01.c1** Prohibits market manipulation and attempted market manipulation. · §2.1  
  Manipulation is prohibited, including orders giving false signals. Attempted manipulation is reflected only partly, through 'orders without intention to execute'. It is not expressly prohibited as an attempt.  
  > Market manipulation is strictly prohibited.  
  _Prevent trading-based market manipulation — Article 5 REMIT, Article 2(2)(a) REMIT, Article 2(3) REMIT_
- **REMIT-MAN-02.c1** Covers external communications (press, social media, analyst calls) about supply, demand or prices. · §2.3  
  The policy restricts press and social media communications to Communications. It does not expressly prohibit false or misleading information on supply, demand or price, or cover analyst calls, but it addresses the channel.  
  > Only the Communications department may speak to the press or publish statements about market conditions. Traders must not comment on market rumours on social media.  
  _Prevent information-based and benchmark manipulation — Article 2(2)(b) REMIT, Article 2(2)(c) REMIT, Article 2(3)(b) REMIT, Article 5 REMIT_
- **REMIT-ALG-01.c3** Describes testing before deployment and after changes. · §4.4  
  Pre-deployment testing is described, but testing after changes to existing algorithms is not addressed.  
  > New algorithms are tested in the EPEX simulation environment before go-live and require the written approval of the Head of Trading.  
  _Systems and risk controls for algorithmic trading — Article 5a(1) REMIT_
- **REMIT-ALG-02.c2** Keeps strategy descriptions, parameters, limits and controls ready to provide on request. · §4.6  
  Strategy descriptions, parameters and tests are kept, but nothing says they are ready to provide to the NRA on request, and limits and controls are not listed.  
  > Documentation of algorithms, including strategy descriptions, parameters and test results, is kept for three years.  
  _Notify algorithmic trading to the NRA and ACER — Article 5a(2) REMIT_
- **REMIT-ALG-03.c2** Lists the records kept (strategies, parameters, limits, tests, changes). · §4.6  
  Strategies, parameters and test results are listed. Limits and changes to algorithms are not mentioned, so the list is incomplete.  
  > including strategy descriptions, parameters and test results  
  _Keep algorithmic trading records for five years — Article 5a(2), third subparagraph, REMIT_

### Recommendations (good practice)

- **REMIT-MAN-01.c4** Sets rules for, or monitors, trades between the company's own desks or group entities. · §2.4  
  Intragroup trades are expressly allowed without any monitoring or conditions. This permits wash-trade-like activity, which conflicts with the requirement to control such trades.  
  > Trades between Nordwind group companies on EPEX SPOT are allowed to balance positions within the group.  
  _Prevent trading-based market manipulation — Article 5 REMIT, Article 2(2)(a) REMIT, Article 2(3) REMIT_
- **REMIT-INS-03.c1** States which insider-trading exemptions the company relies on, if any.  
  The document does not state any insider-trading exemptions relied on.  
  _Document reliance on other insider-trading exemptions — Article 3(3) REMIT, Article 3(4)(a) REMIT, Article 3(4)(c) REMIT_
- **REMIT-INS-03.c2** Requires evidence that the agreement or order behind an exempt transaction was concluded or placed before the inside information was received.  
  No requirement for evidence that an agreement or order predates receipt of inside information.  
  _Document reliance on other insider-trading exemptions — Article 3(3) REMIT, Article 3(4)(a) REMIT, Article 3(4)(c) REMIT_
- **REMIT-MAN-02.c3** Names who may submit data to price reporters and how its accuracy is checked.  
  No rule on who may submit data to price reporters or how its accuracy is checked.  
  _Prevent information-based and benchmark manipulation — Article 2(2)(b) REMIT, Article 2(2)(c) REMIT, Article 2(3)(b) REMIT, Article 5 REMIT_
- **REMIT-ALG-02.c3** Names the role that maintains the notification.  
  No notification exists and no role is named to maintain it.  
  _Notify algorithmic trading to the NRA and ACER — Article 5a(2) REMIT_
- **MAR-SCOPE-01.c1** Maps the company's traded products to REMIT-only or REMIT-and-MAR.  
  The policy does not map traded products to REMIT-only or REMIT-and-MAR.  
  _Identify which products are also financial instruments — Article 1(2) REMIT, Article 2 MAR_
- **REMIT-GP-11.c2** Requires traders to record the reason for unusual orders or trades.  
  The policy has no requirement for traders to record the reason for unusual orders or trades.  
  _Trading mandates and rationale for unusual trades — non-binding_
- **REMIT-GP-12.c1** Requires each erroneous order or trade to be assessed as possible inside information.  
  Nothing requires erroneous orders or trades to be assessed as possible inside information.  
  _Erroneous-order handling — non-binding_
- **REMIT-GP-12.c2** Describes the incident investigation steps after an erroneous order. · §4.3  
  Only automatic rejection of limit-breaching orders is described. There are no investigation steps after an erroneous order.  
  > Orders that breach a pre-trade limit are rejected automatically.  
  _Erroneous-order handling — non-binding_
- **REMIT-GP-13.c2** Applies the same controls to vendor-supplied algorithms.  
  The policy does not mention vendor-supplied algorithms or apply the same controls to them.  
  _Algorithm governance, including vendor algorithms — non-binding_
- **REMIT-GP-10.c2** States a retention period of at least five years for transactions, disclosures and trade communications. · §3.2  
  Five years is stated for recordings, chat logs and trade tickets (transactions). Disclosures, such as inside information publications, are not mentioned, so coverage is incomplete.  
  > Recordings, chat logs and trade tickets are kept for five years.  
  _Record trader communications and keep trading records for five years — non-binding_
- **REMIT-GP-13.c1** Requires documented approval before an algorithm or a change goes live. · §4.4  
  Written approval is required before go-live for new algorithms. Changes to existing algorithms are not mentioned, so the requirement is only partly met.  
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
- REMIT-GP-09.c2 (partial) Describes a trade-stop mechanism and what is recorded when it is used.
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
- REMIT-GP-11.c1 §3.1 Refers to documented trading mandates and limits.

</details>

## transaction-reporting-procedure.docx

35 checks · **6 conflicts** · **4 gaps** · 1 weak points · 2 ACER expectations · 6 recommendations · 16 covered

### Conflicts with REMIT

- **REMIT-REG-02.c2** Requires changes to be notified to the NRA promptly. · §1.3  
  Changes are batched to an annual January review, which is not prompt notification as Article 9(5) requires.  
  > reported to the Bundesnetzagentur at the annual review of registration data in January  
  _Keep registration data up to date — Article 9(5) REMIT_
- **REMIT-REP-01.c3** Covers orders to trade as well as executed transactions. · §2.2  
  Orders to trade are expressly excluded, although REMIT requires them to be reported.  
  > Only executed transactions are reported. Orders that are not executed are not reportable.  
  _Report transactions and orders through an RRM — Article 8(1) REMIT, Article 8(4) REMIT IR 2026, Article 3 IR 1348/2014 (until 2027-10-28), Article 3 REMIT IR 2026 (from 2027-10-29)_
- **REMIT-REP-02.c2** States the ten-working-day deadline for non-standard contracts. · §3.2  
  One month is longer than the ten working days allowed.  
  > Non-standard contracts are reported within one month of their conclusion.  
  _Meet reporting deadlines — Article 10 REMIT IR 2026, Article 17 REMIT IR 2026_
- **REMIT-REP-06.c1** States that orders and trades on OMPs are reported by the OMP and not reported again by the company. · §2.4, §4.1  
  The document says exchanges report to ACER, but it also has the company report all exchange trades again. That is double reporting, which the requirement prohibits.  
  > Nordwind Trading additionally reports all trades executed on EEX and EPEX SPOT through TradeLink RRM.  
  _Leave OMP reporting to the OMP and give it the data it lacks — Article 8(1) REMIT IR 2026, Article 8(3) REMIT IR 2026, Article 8(4) REMIT IR 2026, Article 8(5) REMIT IR 2026_
- **REMIT-REP-08.c1** Requires records of transactions reportable only on ACER request (e.g. off-OMP intragroup deals) to be kept. · §2.5  
  The document says intragroup trades are not recorded. This conflicts with the duty to keep records of transactions reportable on request.  
  > Intragroup trades between Nordwind companies concluded outside an organised market place are not REMIT-relevant and are not recorded for REMIT purposes.  
  _Keep records of transactions reportable only on request — Article 5(1) REMIT IR 2026, Article 5(3) REMIT IR 2026_
- **REMIT-REP-08.c2** States a retention period of at least five years following conclusion for these transactions. · §2.5  
  No five-year retention period is stated. The document says intragroup trades are not recorded at all.  
  > are not REMIT-relevant and are not recorded for REMIT purposes.  
  _Keep records of transactions reportable only on request — Article 5(1) REMIT IR 2026, Article 5(3) REMIT IR 2026_

### Gaps (required by law, missing)

- **REMIT-REG-01.c2** Requires registration to be in place before any new legal entity in the group starts reportable trading.  
  No requirement that a new group legal entity be registered before starting reportable trading.  
  _Register with the NRA before trading — Article 9(1) REMIT, Article 9(4) REMIT_
- **REMIT-REP-02.c3** Applies the deadlines to lifecycle events (amendments, cancellations, terminations).  
  The deadlines are not applied to lifecycle events such as amendments, cancellations or terminations.  
  _Meet reporting deadlines — Article 10 REMIT IR 2026, Article 17 REMIT IR 2026_
- **REMIT-REP-07.c2** Describes a check that reported fields are accurate. · §4.2, §4.3  
  The reconciliation only ensures all trades were reported. No check of field accuracy is described. Validation errors are fixed, but that does not verify accuracy.  
  > Rejected reports and validation errors received from TradeLink RRM are corrected and resubmitted on the same working day.  
  _Have procedures to verify data quality — Article 14(1) REMIT IR 2026, Article 14(2) REMIT IR 2026, Article 14(3) REMIT IR 2026_
- **REMIT-REP-07.c3** Describes a check that reports were submitted within the applicable deadline. · §3.1, §3.2  
  Deadlines are stated, but no check that reports were submitted on time is described.  
  > Standard contracts are reported by the end of the next working day (T+1).  
  _Have procedures to verify data quality — Article 14(1) REMIT IR 2026, Article 14(2) REMIT IR 2026, Article 14(3) REMIT IR 2026_

### Weak points (required by law, only partly covered)

- **REMIT-REP-03.c3** Requires verification that delegated reports are accurate. · §4.1  
  Back Office checks receipt of exchange confirmations and reconciles RRM reports against the blotter. This is some verification of delegated reporting, but accuracy of delegated reports is not verified; receipt only.  
  > Back Office checks every morning that the exchanges' reporting confirmations have been received.  
  _Keep responsibility for delegated reporting — Article 8(1) REMIT, Article 8(4) REMIT_

### ACER expects

- **REMIT-REP-03.c4** Describes an escalation step when the RRM or third party cannot report, including informing the NRA and ACER.  
  No escalation step if the RRM or a third party cannot report, and no informing of the NRA or ACER.  
  _Keep responsibility for delegated reporting — Article 8(1) REMIT, Article 8(4) REMIT_
- **REMIT-REP-02.c4** Classifies trades on OMPs as standard (T+2) and OTC trades as non-standard (T+10), including off-venue lifecycle events on OMP trades (T+2). · §3.1, §3.2  
  The document does not classify OMP trades as standard and OTC trades as non-standard, and does not cover off-venue lifecycle events. It sets a one-month deadline for non-standard contracts.  
  > Standard contracts are reported by the end of the next working day (T+1).  
  _Meet reporting deadlines — Article 10 REMIT IR 2026, Article 17 REMIT IR 2026_

### Recommendations (good practice)

- **REMIT-REG-02.c3** Lists the internal events that trigger a registration update.  
  No internal events triggering a registration update are listed.  
  _Keep registration data up to date — Article 9(5) REMIT_
- **REMIT-REG-02.c4** Sets an internal time limit (e.g. number of working days) for notifying registration changes. · §1.3  
  Only an annual review date is given, not a time limit for notifying changes, so no working-day limit is set.  
  > at the annual review of registration data in January  
  _Keep registration data up to date — Article 9(5) REMIT_
- **REMIT-REP-08.c4** Describes how an ad-hoc ACER request for these transactions would be answered.  
  The document does not describe how an ad-hoc ACER request for these transactions would be answered.  
  _Keep records of transactions reportable only on request — Article 5(1) REMIT IR 2026, Article 5(3) REMIT IR 2026_
- **REMIT-COOP-02.c2** Names who answers ACER data-quality queries.  
  The document does not name who answers ACER data-quality queries.  
  _Answer ACER requests about reported data, including original contracts — Article 8(9) REMIT IR 2026_
- **REMIT-REP-06.c3** Uses the OMP's reported-data access to reconcile OMP-reported records. · §4.1  
  Back Office checks that exchange confirmations arrive each morning. It does not reconcile OMP-reported records using the OMP's access to reported data, so this is only partial.  
  > Back Office checks every morning that the exchanges' reporting confirmations have been received.  
  _Leave OMP reporting to the OMP and give it the data it lacks — Article 8(1) REMIT IR 2026, Article 8(3) REMIT IR 2026, Article 8(4) REMIT IR 2026, Article 8(5) REMIT IR 2026_
- **REMIT-REP-08.c3** Identifies which of the company's transactions are reportable only on request. · §2.5  
  The document identifies intragroup trades but treats them as not relevant, not as reportable on request. It does not identify the other categories.  
  > Intragroup trades between Nordwind companies concluded outside an organised market place are not REMIT-relevant  
  _Keep records of transactions reportable only on request — Article 5(1) REMIT IR 2026, Article 5(3) REMIT IR 2026_

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
- REMIT-REG-02.c1 §1.3 Requires any change to the information in the registration form (e.g. management, ownership, place of publication of inside information) to be communicated to the NRA.
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
