# Review sheet: REMIT checklist v0.3.0

Status **draft** · sources fetched 2026-11-17 · ACER Guidance edition 6.1 (18 December 2024)

Badges: **[LAW]** missing = gap · **[ACER]** missing = "ACER expects" · **[GOOD PRACTICE]** missing = recommendation only.
Tick each check you agree with; write corrections next to anything wrong.

```
obligations: 41 items, 158 checks (good_practice 41, guidance 26, law 91)
adjacent_regimes: 3 items, 5 checks (good_practice 1, law 4)
good_practice: 15 items, 32 checks (good_practice 29, guidance 3)
```

# Part A — REMIT obligations

## Registration

### REMIT-REG-01 · Register with the NRA before trading
*Article 9(1) REMIT, Article 9(4) REMIT* · law · applies to: registered_mp · documents: REG

Register with the NRA of the Member State of establishment or residence, and submit the registration form before the first reportable transaction. A market participant registers with one NRA only.

Checks:
- [ ] `c1` **[LAW]** Names the NRA with which the company is registered.
- [ ] `c2` **[LAW]** Requires registration to be in place before any new legal entity in the group starts reportable trading.
- [ ] `c3` **[GOOD PRACTICE]** Names the role or function responsible for submitting and maintaining the registration.
- [ ] `c4` **[GOOD PRACTICE]** States where the company's ACER code is recorded.

Sources: ACER Guidance 8.7

Reviewer comments:

---

### REMIT-REG-02 · Keep registration data up to date
*Article 9(5) REMIT* · law · applies to: registered_mp · documents: REG, IIP

Report any change to the information in the registration form to the NRA promptly. This includes the place where the company publishes its inside information.

Checks:
- [ ] `c1` **[LAW]** Requires any change to the information in the registration form (e.g. management, ownership, place of publication of inside information) to be communicated to the NRA.
- [ ] `c2` **[LAW]** Requires changes to be notified to the NRA promptly.
- [ ] `c3` **[GOOD PRACTICE]** Lists the internal events that trigger a registration update.
- [ ] `c4` **[GOOD PRACTICE]** Sets an internal time limit (e.g. number of working days) for notifying registration changes.
- [ ] `c5` **[GOOD PRACTICE]** Names the role responsible for submitting registration changes.
- [ ] `c6` **[GOOD PRACTICE]** Specifies a review frequency for registration data (e.g. annual).

Sources: ACER Guidance 8.9, paras. (395)-(396); ACER Guidance 4.2.1, para. (124)

Reviewer comments:

---

### REMIT-REG-03 · Designate an EU representative (third-country participants)
*Article 9(1), second subparagraph, REMIT* · law · applies to: third_country_mp · documents: REG, REGINT

A third-country market participant must appoint, by written mandate, a representative in a Member State where it is active and register with that Member State's NRA. The representative must have the powers and means to deal with NRAs and ACER on its behalf. Its contact details go to the NRA where the representative is established and to ACER.

Checks:
- [ ] `c1` **[LAW]** Identifies the representative and refers to the written mandate.
- [ ] `c2` **[LAW]** States the representative's powers to receive and answer NRA and ACER requests and to give access to information.
- [ ] `c3` **[LAW]** Requires the representative's contact details to be notified to the NRA and to ACER.

Sources: ACER Guidance 8.6, paras. (379)-(381)

> Applies since 2024-11-08.

Reviewer comments:

---

## Reporting

### REMIT-REP-01 · Report transactions and orders through an RRM
*Article 8(1) REMIT, Article 8(4) REMIT IR 2026, Article 3 IR 1348/2014 (until 2027-10-28), Article 3 REMIT IR 2026 (from 2027-10-29)* · law · applies to: registered_mp · documents: TRP

Report records of wholesale energy transactions, including orders to trade, to ACER through a registered reporting mechanism (RRM), directly or through a third party. Reports cover the product, price, quantity, execution date and time, the parties and the beneficiaries. The company reports transactions concluded outside OMPs itself or through a delegate.

Checks:
- [ ] `c1` **[LAW]** Lists the reportable products and venues, or refers to where that list is kept.
- [ ] `c2` **[LAW]** Names the RRM(s) and any third party reporting on the company's behalf.
- [ ] `c3` **[LAW]** Covers orders to trade as well as executed transactions.
- [ ] `c4` **[LAW]** States that transactions concluded outside OMPs, including non-standard contracts, are reported by the company or its delegate.

Sources: ACER TRUM v7.0 (until 2027-10-29); ACER TRUM v8.0 (from 2027-10-29)

Reviewer comments:

---

### REMIT-REP-02 · Meet reporting deadlines
*Article 10 REMIT IR 2026, Article 17 REMIT IR 2026* · law · applies to: registered_mp · documents: TRP

Standard contracts are reported as soon as possible and no later than two working days after the trade, order or lifecycle event. Non-standard contracts are reported no later than ten working days after. Auctions and transportation contracts have their own rules. ACER reads this as: trades on OMPs follow the two-day rule (including off-venue lifecycle events on them), OTC trades the ten-day rule.

Checks:
- [ ] `c1` **[LAW]** States the two-working-day deadline for standard contracts.
- [ ] `c2` **[LAW]** States the ten-working-day deadline for non-standard contracts.
- [ ] `c3` **[LAW]** Applies the deadlines to lifecycle events (amendments, cancellations, terminations).
- [ ] `c4` **[ACER]** Classifies trades on OMPs as standard (T+2) and OTC trades as non-standard (T+10), including off-venue lifecycle events on OMP trades (T+2).

Sources: ACER Open Letter IR 2026, sections 7 and 8

> Article 10(1)-(5) apply since 2026-04-29 to trades, orders and lifecycle events from that date; earlier events keep the IR 1348/2014 timeframes. Article 10(6) (LNG) applies from 2027-10-29 (Article 17(3) IR 2026). Older procedures may still cite 1348/2014 timings.

Reviewer comments:

---

### REMIT-REP-03 · Keep responsibility for delegated reporting
*Article 8(1) REMIT, Article 8(4) REMIT* · law · applies to: registered_mp · documents: TRP

Overall responsibility for reporting stays with the market participant. Its obligation counts as fulfilled once the information has been received from a person or entity listed in Article 8(4)(b)-(f) REMIT (third party, trade reporting system, OMP or other PPAET, trade repository, competent authority).

Checks:
- [ ] `c1` **[LAW]** Identifies which trades are reported by OMPs or third parties and which the company reports itself.
- [ ] `c2` **[LAW]** Requires verification that delegated reports were submitted.
- [ ] `c3` **[LAW]** Requires verification that delegated reports are accurate.
- [ ] `c4` **[ACER]** Describes an escalation step when the RRM or third party cannot report, including informing the NRA and ACER.

Sources: ACER Q&A 2.4.50

Reviewer comments:

---

### REMIT-REP-04 · Report exposures (from 2027)
*Article 8(1) REMIT, Article 6 REMIT IR 2026, Article 17(2) REMIT IR 2026* · law · applies to: exposure_reporter · documents: TRP · **applies from 2027-01-01**

Market participants whose positions reach 600 GWh a year (electricity and natural gas assessed separately, as a sum of absolute monthly values, at the end of each calendar year) report their positions quarterly, by the last day of the month after the quarter, covering the next 18 months. The 2027 assessment uses positions from transactions concluded by 31 December 2026 with delivery in 2027. The first report (reference quarter Q3 2027) is due by 31 October 2027. System operators buying only for system needs report only on ACER's request.

Checks:
- [ ] `c1` **[LAW]** Describes how the exposure-reporting threshold is assessed (separately for electricity and gas).
- [ ] `c2` **[LAW]** Assesses the threshold at the end of each calendar year, on transactions concluded by 31 December.
- [ ] `c3` **[LAW]** States that exposure reports are due quarterly, by the last day of the month after each quarter, starting October 2027.
- [ ] `c4` **[GOOD PRACTICE]** Names the role that performs the threshold assessment.

Sources: ACER Guidance on reporting exposure v1.0, section 2.3

Reviewer comments:

---

### REMIT-REP-05 · Provide fundamental data and disclosed inside information to ACER
*Article 8(5) REMIT, Article 8(6) REMIT, Articles 11-12 REMIT IR 2026* · law · applies to: mp_disclosing · documents: IIP, TRP

Market participants provide ACER and NRAs with information on the capacity and use of their production, storage, consumption, transmission, LNG and hydrogen facilities, including unavailability, and with the inside information they disclose. In practice this goes through the ENTSO transparency platforms and the IIP, which reports disclosed inside information to ACER.

Checks:
- [ ] `c1` **[LAW]** States how fundamental data and disclosed inside information on the company's facilities reach ACER (e.g. via the IIP's reporting).

Sources: ACER MoP on data reporting; ACER Guidance 4.2.1, para. (117)

> Articles 11(4), 12(5) and 12(9) IR 2026 apply from 2028-04-29.

Reviewer comments:

---

### REMIT-REP-06 · Leave OMP reporting to the OMP and give it the data it lacks
*Article 8(1) REMIT IR 2026, Article 8(3) REMIT IR 2026, Article 8(4) REMIT IR 2026, Article 8(5) REMIT IR 2026* · law · applies to: registered_mp · documents: TRP

OMPs report order-book data, trades and lifecycle events for all participants on their platform; market participants must not report that data themselves. From 2027-10-29, participants must give the OMP any information it needs and does not have, at the latest by the Article 10 deadline. Participants can ask the OMP for access to their reported data and validation results.

Checks:
- [ ] `c1` **[LAW]** States that orders and trades on OMPs are reported by the OMP and not reported again by the company.
- [ ] `c2` **[LAW]** Identifies which data the company must give each OMP and by when. _(only if date >= 2027-10-29)_
- [ ] `c3` **[GOOD PRACTICE]** Uses the OMP's reported-data access to reconcile OMP-reported records.

Sources: ACER Open Letter IR 2026, section 11

> Article 8(5) IR 2026 applies from 2027-10-29 (Article 17 IR 2026).

Reviewer comments:

---

### REMIT-REP-07 · Have procedures to verify data quality
*Article 14(1) REMIT IR 2026, Article 14(2) REMIT IR 2026, Article 14(3) REMIT IR 2026* · law · applies to: registered_mp, omp · documents: TRP

Persons required to report are responsible for the completeness, accuracy and timeliness of the data they submit through RRMs and must have procedures to verify this. For data an OMP reports on a participant's behalf, ACER accepts that the participant can hardly verify it. Market participants are also responsible for the completeness, accuracy and timeliness of their IIP disclosures (Article 14(3)), but no procedure duty is attached to that.

Checks:
- [ ] `c1` **[LAW]** Describes a check that the reports the company submits (itself or through its RRM) are complete against the trading system.
- [ ] `c2` **[LAW]** Describes a check that reported fields are accurate.
- [ ] `c3` **[LAW]** Describes a check that reports were submitted within the applicable deadline.
- [ ] `c4` **[ACER]** Describes how rejections or validation errors from the RRM or ACER are corrected and resubmitted.
- [ ] `c5` **[GOOD PRACTICE]** States the frequency of reconciliation against the trading system (e.g. daily).

Sources: ACER Q&A 3.2.44

Reviewer comments:

---

### REMIT-REP-08 · Keep records of transactions reportable only on request
*Article 5(1) REMIT IR 2026, Article 5(3) REMIT IR 2026* · law · applies to: market_participant · documents: TRP

These transactions are reportable only on a reasoned ad-hoc ACER request: intragroup transactions, electricity from units of 10 MW or less and gas from facilities of 20 MW or less, and upstream-pipeline transactions (each unless concluded on an OMP); gas storage not covered by Article 4; market-based redispatch not already reported; voice-broker orders not on screen; gas balancing services not reported under Article 3; and primary capacity allocations with no bids. Their details must be kept for at least five years following conclusion.

Checks:
- [ ] `c1` **[LAW]** Requires records of transactions reportable only on ACER request (e.g. off-OMP intragroup deals) to be kept.
- [ ] `c2` **[LAW]** States a retention period of at least five years following conclusion for these transactions.
- [ ] `c3` **[GOOD PRACTICE]** Identifies which of the company's transactions are reportable only on request.
- [ ] `c4` **[GOOD PRACTICE]** Describes how an ad-hoc ACER request for these transactions would be answered.

Reviewer comments:

---

### REMIT-REP-09a · Report supply to large consumers every six months
*Article 4(2) REMIT IR 2026, Article 4(11) REMIT IR 2026, Article 16(3) REMIT IR 2026, Article 17(3) REMIT IR 2026* · law · applies to: supplier_to_large_consumer · documents: TRP · **applies from 2027-10-29**

Supply or storage of electricity, or supply of gas, to a single consumption unit technically able to consume 600 GWh/year or more is reported every six months, by the last day of the first month of the next semester, unless concluded on an OMP. The supplier must obtain the customer's confirmation of that capability. Outstanding transactions concluded before the obligation applies are backloaded within 90 days. Records are kept for at least five years.

Checks:
- [ ] `c1` **[LAW]** States that supply to consumption units able to consume 600 GWh/year or more is reported every six months, by the last day of the first month of the next semester.
- [ ] `c2` **[LAW]** Requires confirmation from final customers that the consumption unit is technically able to consume 600 GWh/year or more.
- [ ] `c3` **[LAW]** Provides for reporting, within 90 days of the obligation applying, of outstanding transactions concluded before that date.
- [ ] `c4` **[LAW]** States a retention period of at least five years.

Sources: ACER Open Letter IR 2026, section 13

Reviewer comments:

---

### REMIT-REP-09b · Report balancing, capacity-mechanism and gas-storage transactions periodically
*Article 4(1) REMIT IR 2026, Article 4(3)-(7) REMIT IR 2026, Article 4(11) REMIT IR 2026, Article 16(3) REMIT IR 2026, Article 17(4) REMIT IR 2026* · law · applies to: registered_mp · documents: TRP · **applies from 2028-04-29**

Capacity mechanisms are reported annually, by the end of January. Electricity balancing services, whether or not activated, are reported monthly, by the end of the second month after the trade month. Gas storage contracts of 12 months or longer (primary or secondary allocation) and gas-storage derivatives are reported monthly, by the end of the following month. Outstanding transactions are backloaded within 90 days. Records are kept for at least five years.

Checks:
- [ ] `c1` **[LAW]** Identifies which periodic-reporting categories (capacity mechanisms, electricity balancing, gas storage) apply to the company.
- [ ] `c2` **[LAW]** States the reporting frequency and deadline for each applicable category.
- [ ] `c3` **[LAW]** Provides for reporting, within 90 days of the obligation applying, of outstanding transactions concluded before that date.
- [ ] `c4` **[LAW]** States a retention period of at least five years.

Sources: ACER Open Letter IR 2026, section 13

Reviewer comments:

---

### REMIT-REP-10 · Report hydrogen transactions annually
*Article 4(8) REMIT IR 2026, Article 4(9) REMIT IR 2026, Article 4(10) REMIT IR 2026, Article 4(11) REMIT IR 2026, Article 17(4) REMIT IR 2026* · law · applies to: hydrogen_participant · documents: TRP · **applies from 2028-07-01**

Hydrogen supply (EU delivery), transport, storage, derivatives (including CfDs) and balancing transactions are reported once a year, by the last day of January for the previous year, wherever and however concluded. Exempt: physical delivery from a single hydrogen production facility of 50 MW or less; supply or transport in geographically confined hydrogen networks (Article 52 Directive (EU) 2024/1788); and supply to a single consumption unit able to consume less than 600 GWh/year. Participants engaged only in the first two exempt categories need not register. Records are kept for at least five years.

Checks:
- [ ] `c1` **[LAW]** Includes the company's non-exempt hydrogen transactions in annual reporting.
- [ ] `c2` **[LAW]** Sets the annual reporting deadline (last day of January for the previous year).
- [ ] `c3` **[LAW]** States a retention period of at least five years for reportable hydrogen transactions.
- [ ] `c4` **[GOOD PRACTICE]** Documents which Article 4(9) exemption the company relies on, if any.

Sources: ACER Open Letter IR 2026, section 22

Reviewer comments:

---

### REMIT-LNG-01 · Submit LNG market data daily
*Article 7c REMIT, Article 7d REMIT, Article 8(1b) REMIT, Article 7a(2) REMIT, Article 2(23) REMIT, Article 2(25) REMIT* · law · applies to: lng_market_participant · documents: TRP

Anyone engaged in LNG trading specifying or resulting in EU delivery, or where a counterparty regasifies at an EU terminal, wherever established, submits bids, offers and transactions to ACER daily, free of charge, through ACER's reporting channels, as close to real time as possible and before the 18:00 CET price assessment. Prices go in the contract currency and in EUR/MWh, quantities in contract units and in MWh; timestamps and arrival windows in UTC; delivery points with ACER-listed identifiers.

Checks:
- [ ] `c1` **[LAW]** States that LNG bids, offers and transactions are submitted to ACER daily before 18:00 CET.
- [ ] `c2` **[LAW]** Refers to the data fields required by Article 7d REMIT.
- [ ] `c3` **[LAW]** Requires prices in the contract currency and in EUR/MWh (with conversion and exchange rates applied) and quantities in contract units and in MWh.
- [ ] `c4` **[LAW]** Requires timestamps and arrival-window dates in UTC, delivery points using ACER-listed identifiers and, where relevant, the full long-term-contract price formula.
- [ ] `c5` **[GOOD PRACTICE]** Names the role responsible for the daily submission.

Sources: ACER TRUM v8.0, section 5; ACER Guidance 2.4, paras. (55)-(56)

> Applies from 2025-01-01 (Article 3 Regulation (EU) 2024/1106).

Reviewer comments:

---

### REMIT-OMP-01 · OMP order-book reporting, access and records
*Article 8(1a) REMIT, Article 8(1) REMIT IR 2026, Article 8(2) REMIT IR 2026, Article 8(3) REMIT IR 2026, Article 8(11) REMIT IR 2026* · law · applies to: omp · documents: TRP

OMPs report order-book data (matched and unmatched orders, trades, lifecycle events) to ACER on behalf of all participants, and system-generated orders when ACER requests them. On ACER's reasoned request they also give ACER access to the order book within the deadline set. They keep records for at least five years from the transaction day and give each participant, on request, access to its reported data and validation results. Before first reporting they notify ACER for the OMP list and submit reference data, and keep it updated.

Checks:
- [ ] `c1` **[LAW]** States that the OMP reports order-book data on behalf of all participants.
- [ ] `c2` **[LAW]** States a retention period of at least five years from the day of the transaction for reported data.
- [ ] `c3` **[LAW]** Describes how participants can access their reported data and validation results.
- [ ] `c4` **[LAW]** Provides for notification to ACER for the OMP list, submission of reference data before first reporting, and timely updates.
- [ ] `c5` **[LAW]** Describes how a reasoned ACER request for order-book access is met within the deadline set.

Reviewer comments:

---

## Cooperation

### REMIT-COOP-01 · Cooperate with ACER and NRA investigations, inspections and information requests
*Article 13(2) REMIT, Article 13a REMIT, Article 13b REMIT, Article 13g REMIT* · law · applies to: market_participant, any_person · documents: REGINT

NRAs can access documents, demand information, carry out on-site inspections and require existing telephone and data-traffic records under national law. Since REMIT II, ACER can investigate cross-border cases itself, including on-site inspections ordered by ACER decision, without prior announcement where needed; inspecting staff's private premises needs a reasonable suspicion and prior judicial authorisation. Anyone receiving an ACER information request must answer within the time limit and is responsible for the answer being complete, correct and not misleading. Failing to comply with an inspection or information request ordered by ACER decision can lead to daily periodic penalty payments of up to 3% of average daily turnover for up to six months.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Names the function that receives and coordinates NRA or ACER requests and inspections.
- [ ] `c2` **[LAW]** Requires replies to ACER information requests to be complete, correct and not misleading (e.g. through a review before submission).
- [ ] `c3` **[GOOD PRACTICE]** Requires the response deadline in each request to be tracked.
- [ ] `c4` **[GOOD PRACTICE]** Requires existing call recordings, chats and e-mails relevant to the request to be preserved (legal hold) once an inspection or request is received.
- [ ] `c5` **[GOOD PRACTICE]** Gives instructions for an unannounced inspection (check identity and authorisation, call legal/compliance, alter nothing).

Sources: ACER Manual for new market participants 2026, section 6

> Article 13(2) powers are exercised under national law. ACER's own investigatory powers apply since 2024-05-07. Destroying evidence after a request may breach national law; that is outside this checklist.

Reviewer comments:

---

### REMIT-COOP-02 · Answer ACER requests about reported data, including original contracts
*Article 8(9) REMIT IR 2026* · law · applies to: registered_mp, lng_market_participant, omp · documents: TRP, REGINT

ACER may ask market participants, LNG market participants and reporting parties for more information and clarification on reported data, including access to the original contracts. This is a power to request, not a storage duty.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Keeps original contracts (including OTC and non-standard contracts) retrievable so they can be produced if ACER requests them.
- [ ] `c2` **[GOOD PRACTICE]** Names who answers ACER data-quality queries.

Reviewer comments:

---

## Insider Trading

### REMIT-INS-01 · Prevent trading on inside information
*Article 2(1) REMIT, Article 3(1) REMIT, Article 3(2) REMIT, Article 3(5) REMIT* · law · applies to: market_participant, any_person · documents: IIP, MCP

Persons with inside information must not use it to trade, or to cancel or amend existing orders; must not disclose it outside the normal course of their duties; and must not recommend or induce others to trade on it. Where the holder is a company, the prohibition also covers the individuals who take part in its trading decisions. This applies to inside information about other companies' facilities too.

Checks:
- [ ] `c1` **[LAW]** Defines inside information using the REMIT criteria (precise, non-public, relating to wholesale energy products, likely to significantly affect prices).
- [ ] `c2` **[LAW]** Prohibits trading, recommending and disclosure outside the normal course of duties while holding inside information.
- [ ] `c3` **[LAW]** Covers cancelling or amending orders placed before the information was received.
- [ ] `c4` **[LAW]** States that inside information may be shared only on a need-to-know basis in the normal course of duties.
- [ ] `c5` **[LAW]** States that inside information about other companies' facilities must not be traded on, even though the company has no duty to publish it.
- [ ] `c6` **[GOOD PRACTICE]** Gives at least one example of inside information relevant to the company's assets or markets.
- [ ] `c7` **[GOOD PRACTICE]** Requires staff who receive possible inside information to escalate it to a named function.

Sources: ACER Guidance 5.2.1; ACER Guidance 5.2.2; ACER Guidance 2.4, para. (48); ACER Q&A 3.7.12; ACER Q&A 3.7.21

> Information barriers and training are evidence ACER looks for, but not stand-alone legal duties; see REMIT-GP-04 and REMIT-GP-09.

Reviewer comments:

---

### REMIT-INS-02 · Use the unplanned-outage exemption correctly
*Article 3(4)(b) REMIT* · law · applies to: asset_operator_3_4_b · documents: IIP, MCP

Electricity and natural gas producers, gas storage operators and LNG import operators may trade while holding inside information only to cover the immediate physical loss from an unplanned outage, where needed to meet existing contracts or agreed with the TSO for system security. The related transaction information must be reported to ACER and the NRA, and the outage must still be disclosed under Article 4(1).

Checks:
- [ ] `c1` **[LAW]** Limits exemption trades to covering the immediate physical loss from an unplanned outage.
- [ ] `c2` **[LAW]** Requires the exemption trades to be reported to ACER and the NRA.
- [ ] `c3` **[LAW]** Confirms that the outage is still disclosed under Article 4(1).
- [ ] `c4` **[ACER]** Limits exemption trades to within-day losses and to the duration of the causal link with the outage.
- [ ] `c5` **[ACER]** For trades agreed with the TSO, limits them to ancillary services markets under a specific TSO agreement.
- [ ] `c6` **[ACER]** Requires notification of exemption trades as soon as possible via ACER's Notification Platform.
- [ ] `c7` **[ACER]** States that the exemption cannot be used while disclosure is delayed under Article 4(2).

Sources: ACER Guidance 5.5.2, paras. (215)-(221); ACER Guidance 4.4, para. (136)

Reviewer comments:

---

### REMIT-INS-03 · Document reliance on other insider-trading exemptions
*Article 3(3) REMIT, Article 3(4)(a) REMIT, Article 3(4)(c) REMIT* · law · applies to: market_participant, tso · documents: MCP, IIP

The prohibition does not apply to transactions that discharge an obligation which has become due, where that obligation results from an agreement concluded or an order placed before the person possessed the inside information. Nor does it apply to market participants acting under national emergency rules where authorities have intervened and market mechanisms are suspended. TSOs buying electricity, hydrogen or gas for safe and secure system operation are exempt from the trading and recommending prohibitions only.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** States which insider-trading exemptions the company relies on, if any.
- [ ] `c2` **[GOOD PRACTICE]** Requires evidence that the agreement or order behind an exempt transaction was concluded or placed before the inside information was received.

Sources: ACER Guidance 5.5.1; ACER Guidance 5.5.2; ACER Q&A 2.4.56

> The exemptions are defences, not duties; the checks only matter if the company relies on them.

Reviewer comments:

---

### REMIT-INS-04 · Prevent misuse of client order information (front running)
*Article 2(1)(ca) REMIT, Article 3(1) REMIT* · law · applies to: ppat, ppet, trades_for_third_parties · documents: MCP, SUR

Information about a client's pending orders, passed to a firm that trades on the client's behalf, can be inside information for that firm. The firm must not use it to trade for its own account first (front running) or around the client order.

Checks:
- [ ] `c1` **[LAW]** Prohibits using information about clients' pending orders to trade for own account or for others ahead of, or on the basis of, those orders (front running, pre-hedging).
- [ ] `c2` **[GOOD PRACTICE]** Separates client order handling from own-account trading, or monitors for front running.

Sources: ACER Guidance 5.3.2, paras. (195)-(197)

Reviewer comments:

---

## Disclosure

### REMIT-DIS-01 · Disclose inside information through an IIP
*Article 4(1) REMIT* · law · applies to: mp_disclosing · documents: IIP

Publicly disclose inside information about business or facilities that the company, its parent or a related undertaking owns, controls or operates. Since REMIT II this must be done through an Inside Information Platform (IIP). A company website or social media may be used only in addition, with identical content.

Checks:
- [ ] `c1` **[LAW]** Names the IIP(s) used.
- [ ] `c2` **[LAW]** States who discloses inside information on facilities of the parent or related undertakings. _(only if has_group_facilities)_
- [ ] `c3` **[ACER]** States that any other channel (e.g. website) is additional only and must carry identical content.
- [ ] `c4` **[GOOD PRACTICE]** Names who assesses whether information is inside information.
- [ ] `c5` **[GOOD PRACTICE]** Names who publishes on the IIP.

Sources: ACER Guidance 4.2.1, paras. (116)-(123)

Reviewer comments:

---

### REMIT-DIS-02 · Disclose in a timely manner (ACER target - within one hour)
*Article 4(1) REMIT* · law · applies to: mp_disclosing · documents: IIP

Article 4(1) requires effective and timely disclosure (law). ACER expects information not covered by Regulations 2019/943, 715/2009 or 543/2013 to be published as soon as possible and at the latest within one hour, unless other rules specify otherwise, and in every case before the company trades on it or recommends trading (guidance).

Checks:
- [ ] `c1` **[LAW]** Requires inside information to be published without delay.
- [ ] `c2` **[LAW]** Prohibits trading or recommending trading on the information until the UMM is published.
- [ ] `c3` **[ACER]** Sets a target of publication at the latest within one hour.
- [ ] `c4` **[GOOD PRACTICE]** Names an on-call or 24/7 arrangement for publishing inside information outside office hours.
- [ ] `c5` **[ACER]** Requires the publication time to be recorded.

Sources: ACER Guidance 4.3, paras. (133)-(134); ACER MoP, Annex VII, field (5)

Reviewer comments:

---

### REMIT-DIS-03 · Make disclosures complete, correct and in the standard UMM format
*Article 4(1) REMIT* · guidance · applies to: mp_disclosing · documents: IIP

Each Urgent Market Message (UMM) should contain the data fields in Annex VII of the REMIT MoP, be concise and specific, and leave out executive statements and advertising. Forecasts (e.g. outage duration) should be based on all available data, prepared with reasonable effort and updated when new information arrives. ACER treats an incomplete or incorrect disclosure as non-effective, i.e. a breach of Article 4(1).

Checks:
- [ ] `c1` **[ACER]** Refers to the UMM fields in Annex VII of the REMIT MoP or provides a template.
- [ ] `c2` **[ACER]** Requires the UMM to be updated when the expected duration or capacity changes.
- [ ] `c3` **[ACER]** Excludes executive statements and advertising from the message; any disclaimer is avoided or clearly separated.
- [ ] `c4` **[ACER]** Requires the UMM to be checked against the required fields before publication, and names who checks.

Sources: ACER Guidance 4.2.2, paras. (128)-(132); ACER MoP, Annex VII

> The underlying duty (effective disclosure) is Article 4(1) REMIT.

Reviewer comments:

---

### REMIT-DIS-04 · Delay disclosure only under the Article 4(2) conditions
*Article 4(2) REMIT* · law · applies to: mp_disclosing · documents: IIP

Disclosure may exceptionally be delayed to protect legitimate interests, but only if the delay is not likely to mislead the public, confidentiality is ensured and no trading decisions are based on the information. The information and a justification must be sent to ACER and the NRA without delay.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Names who may decide to delay disclosure.
- [ ] `c2` **[LAW]** States the legitimate-interest, not-misleading and confidentiality conditions for delay.
- [ ] `c3` **[LAW]** Prohibits trading decisions based on the delayed information.
- [ ] `c4` **[LAW]** Requires notification of ACER and the NRA without delay when disclosure is delayed, with a written justification.
- [ ] `c5` **[ACER]** Requires disclosure as soon as the legitimate interest ends.
- [ ] `c6` **[GOOD PRACTICE]** Requires the decision to delay to be documented.
- [ ] `c7` **[GOOD PRACTICE]** Uses ACER's standard notification format (unless the NRA requires another).

Sources: ACER Guidance 4.4, paras. (135)-(137)

> Article 4(7) separately allows delay of classified critical-infrastructure information (REMIT-DIS-08).

Reviewer comments:

---

### REMIT-DIS-05 · Handle selective disclosure
*Article 4(3) REMIT* · law · applies to: mp_disclosing · documents: IIP

If the company, or a person employed by or acting for it, passes inside information to someone in the normal course of duties, it must be made public at the same time, unless the recipient has a duty of confidentiality (from law, regulation, articles of association or contract). After an unintentional disclosure, it must be made public as soon as possible.

Checks:
- [ ] `c1` **[LAW]** Requires that inside information shared externally goes only to recipients with a duty of confidentiality, or is published at the same time.
- [ ] `c2` **[LAW]** Requires public disclosure as soon as possible after an unintentional disclosure.
- [ ] `c3` **[GOOD PRACTICE]** Uses NDAs for external recipients who have no confidentiality duty by law.

Reviewer comments:

---

### REMIT-DIS-06 · Have a fallback if the IIP fails
*Article 4(1) REMIT* · guidance · applies to: mp_disclosing · documents: IIP

Companies are not responsible for temporary technical problems of an IIP if they submitted on time. ACER suggests considering a backup solution that meets the same minimum quality requirements, declared in the registration, and switching platforms if problems persist. Until the information is public, the insider trading prohibition still applies.

Checks:
- [ ] `c1` **[ACER]** Describes a backup publication channel that meets the IIP minimum quality requirements, and when to use it.
- [ ] `c2` **[LAW]** States that trading on the information remains prohibited until it is public.

Sources: ACER Guidance 4.2.2, para. (127)

Reviewer comments:

---

### REMIT-DIS-07 · Do not treat transparency-platform publication as timely disclosure
*Article 4(4) REMIT, Article 4(6) REMIT* · law · applies to: mp_disclosing · documents: IIP

Publication under the electricity and gas transparency rules (Regulation 2019/943, Regulation 715/2009 and their network codes) counts as effective but not necessarily timely and public disclosure under Article 4(1). Those rules continue to apply alongside REMIT.

Checks:
- [ ] `c1` **[LAW]** Does not rely on transparency-platform publication alone to meet the Article 4(1) disclosure duty.

Reviewer comments:

---

### REMIT-DIS-08 · Delay for classified critical-infrastructure information
*Article 4(7) REMIT* · law · applies to: mp_disclosing · documents: IIP

Disclosure of sensitive information on the protection of critical infrastructure may be delayed if it is classified in the participant's country.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** If relied on, names who decides that information is classified critical-infrastructure information and how this is documented.

Sources: ACER Guidance 4.5

> A right, not a duty; only relevant if the company relies on it.

Reviewer comments:

---

### REMIT-DIS-09 · Use authorised IIPs and RRMs
*Article 4(1) REMIT, Article 8(1) REMIT, Article 4a REMIT, Article 9a REMIT, Article 40 Delegated Regulation (EU) 2026/255* · law · applies to: registered_mp, mp_disclosing · documents: IIP, TRP · **applies from 2027-10-29**

Under REMIT II, IIPs and RRMs are authorised and supervised by ACER. Most of the authorisation rules in Delegated Regulation 2026/255 apply from 2027-10-29.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Requires checking that the chosen IIP and RRM are authorised by ACER or, during the transition, registered and awaiting ACER's decision.
- [ ] `c2` **[GOOD PRACTICE]** Describes what happens if the IIP or RRM loses its authorisation.

Sources: ACER Open Letter DR 2026, sections 2-4

> Articles 3-8 and 10-39 DR 2026/255, including Annexes I and II, apply from 2027-10-29 (Article 40 DR 2026/255). Already registered RRMs and IIPs may continue until ACER decides on their authorisation (ACER Open Letter DR 2026, sections 3-4).

Reviewer comments:

---

## Market Manipulation

### REMIT-MAN-01 · Prevent trading-based market manipulation
*Article 5 REMIT, Article 2(2)(a) REMIT, Article 2(3) REMIT* · law · applies to: market_participant, any_person · documents: MCP, SUR

Engaging in, or attempting, market manipulation is prohibited. ACER lists the practices it considers relevant, for example wash trades, layering, spoofing, marking the reference period (e.g. the close), capacity withholding and transmission capacity hoarding.

Checks:
- [ ] `c1` **[LAW]** Prohibits market manipulation and attempted market manipulation.
- [ ] `c2` **[ACER]** Names specific prohibited practices (e.g. wash trades, layering, spoofing, marking the close), not only the general prohibition.
- [ ] `c3` **[LAW]** Addresses physical and economic withholding of capacity from the company's assets. _(only if mp_disclosing)_
- [ ] `c4` **[GOOD PRACTICE]** Sets rules for, or monitors, trades between the company's own desks or group entities.
- [ ] `c5` **[GOOD PRACTICE]** Requires staff to report manipulation concerns to compliance.

Sources: ACER Guidance 6.3.2; ACER GN 1/2017 (wash trades); ACER GN 1/2019 (layering and spoofing); ACER GN 1/2018 (transmission capacity hoarding)

Reviewer comments:

---

### REMIT-MAN-02 · Prevent information-based and benchmark manipulation
*Article 2(2)(b) REMIT, Article 2(2)(c) REMIT, Article 2(3)(b) REMIT, Article 5 REMIT* · law · applies to: market_participant, any_person · documents: MCP

Disseminating information through the media, including the internet, or by any other means, that gives or is likely to give false or misleading signals on supply, demand or price is market manipulation where the person knew or ought to have known it was false or misleading; doing so with that intention is attempted manipulation. Transmitting false or misleading input for a benchmark (including price assessments used as benchmarks), where the person knew or ought to have known, or any other behaviour that manipulates a benchmark's calculation, is also market manipulation.

Checks:
- [ ] `c1` **[LAW]** Covers external communications (press, social media, analyst calls) about supply, demand or prices.
- [ ] `c2` **[LAW]** Covers data submitted to price reporting agencies or benchmark administrators.
- [ ] `c3` **[GOOD PRACTICE]** Names who may submit data to price reporters and how its accuracy is checked.

Sources: ACER Guidance 6.2; ACER Guidance 6.2.4; ACER Guidance 6.2.5

Reviewer comments:

---

## Algorithmic Trading

### REMIT-ALG-01 · Systems and risk controls for algorithmic trading
*Article 5a(1) REMIT* · law · applies to: algo_trader · documents: ALG

Have effective systems and risk controls so that algorithmic trading systems are resilient, have enough capacity, work within appropriate thresholds and limits, prevent erroneous orders and do not create a disorderly market. They must comply with REMIT and the rules of connected OMPs. Business continuity arrangements, full testing and monitoring are required.

Checks:
- [ ] `c1` **[LAW]** Defines trading thresholds and limits for algorithms.
- [ ] `c2` **[LAW]** Describes controls that prevent erroneous orders.
- [ ] `c3` **[LAW]** Describes testing before deployment and after changes.
- [ ] `c4` **[LAW]** Describes business continuity arrangements for system failure.
- [ ] `c5` **[LAW]** Names who monitors running algorithms.
- [ ] `c6` **[GOOD PRACTICE]** Specifies limit types (e.g. price, volume, order rate).
- [ ] `c7` **[GOOD PRACTICE]** Provides a means to stop an algorithm immediately (kill switch).

> Article 5a(4) - without prejudice to MiFID II.

Reviewer comments:

---

### REMIT-ALG-02 · Notify algorithmic trading to the NRA and ACER
*Article 5a(2) REMIT* · law · applies to: algo_trader · documents: ALG, REG

Notify the NRA of registration and ACER that the company engages in algorithmic trading. The NRA can ask for strategy descriptions, parameters, limits, controls and testing details.

Checks:
- [ ] `c1` **[LAW]** Requires notification of the NRA and ACER (e.g. via CEREMP) before algorithmic trading starts.
- [ ] `c2` **[LAW]** Keeps strategy descriptions, parameters, limits and controls ready to provide on request.
- [ ] `c3` **[GOOD PRACTICE]** Names the role that maintains the notification.

Sources: ACER Open Letter on algorithmic trading, section 1; ACER Guidance 2.4, para. (52)

Reviewer comments:

---

### REMIT-ALG-03 · Keep algorithmic trading records for five years
*Article 5a(2), third subparagraph, REMIT* · law · applies to: algo_trader · documents: ALG

Keep records on the matters in Article 5a(2) for five years, sufficient for the NRA to monitor compliance.

Checks:
- [ ] `c1` **[LAW]** States a retention period of at least five years.
- [ ] `c2` **[LAW]** Lists the records kept (strategies, parameters, limits, tests, changes).

Reviewer comments:

---

### REMIT-ALG-04 · Direct electronic access providers
*Article 5a(3) REMIT* · law · applies to: dea_provider · documents: ALG

A market participant providing direct electronic access to an OMP must notify the NRA and ACER; on the NRA's request, describe its systems and risk controls and give evidence that they are applied; and keep records for five years. ACER treats DEA providers as PPATs (see REMIT-STR-01 to STR-04).

Checks:
- [ ] `c1` **[LAW]** Requires notification of DEA provision to the NRA and ACER.
- [ ] `c2` **[LAW]** States a retention period of at least five years.
- [ ] `c3` **[GOOD PRACTICE]** Describes the systems and risk controls applied to orders sent by DEA clients and how their application is evidenced.

Sources: ACER Open Letter on algorithmic trading, section 2; ACER Guidance 9.2.1

Reviewer comments:

---

## Suspicious Transactions

### REMIT-STR-01 · Notify suspicious orders and transactions within four weeks
*Article 15(1) REMIT, Article 15(2) REMIT* · law · applies to: ppat, ppet, omp, dea_provider · documents: SUR

Where there is a reasonable suspicion that an order or transaction, on or off an OMP, could breach Article 3, 4 or 5, notify ACER and the NRA without further delay and no later than four weeks after becoming aware of the suspicious event.

Checks:
- [ ] `c1` **[LAW]** States the deadline: without further delay, at the latest four weeks.
- [ ] `c2` **[LAW]** States that the deadline runs from awareness of the suspicious event.
- [ ] `c3` **[LAW]** Covers orders, transactions, cancellations and modifications, on and off venue.
- [ ] `c4` **[LAW]** Covers potential breaches of Articles 3, 4 and 5.

Sources: ACER Guidance 9.3.3; ACER Guidance 9.3.4; ACER Guidance 9.2.1, paras. (416), (418)

> Not a legal obligation for a market participant that is neither a PPAT nor a PPET. ACER treats a market participant providing direct electronic access, or acting as an order book provider, as a PPAT. Any person may voluntarily report suspected market abuse via the STR form on ACER's Notification Platform or to the NRA (ACER Q&A 2.4.6, non-binding). Article 15(2) (PPETs) applies from 2024-11-08.

Reviewer comments:

---

### REMIT-STR-02 · Maintain surveillance arrangements, systems and procedures
*Article 15(3) REMIT* · law · applies to: ppat, ppet, omp, dea_provider · documents: SUR

Establish and maintain effective arrangements, systems and procedures to identify potential breaches, to detect and report suspicious orders and transactions, and to keep surveillance staff free of conflicts of interest and independent. ACER expects this to be proportionate to the size and activity of the firm.

Checks:
- [ ] `c1` **[LAW]** Describes the surveillance system or alerts used to detect potential breaches.
- [ ] `c2` **[ACER]** States that surveillance staff do not report to, and cannot be overruled by, the trading or commercial function.
- [ ] `c3` **[LAW]** Describes how conflicts of interest of surveillance staff are identified and managed.
- [ ] `c4` **[ACER]** Specifies a frequency for reviewing alert calibration and surveillance effectiveness.
- [ ] `c5` **[ACER]** Keeps surveillance procedures and compliance documentation for at least five years.

Sources: ACER Guidance 9.4.1; ACER Guidance 9.4.2; ACER Guidance 9.4.3; ACER Guidance 9.4.3.1; ACER Guidance 9.4.4, para. (495); ACER Guidance 9.4.4.4, para. (516)

> Training for surveillance staff is in REMIT-GP-04.

Reviewer comments:

---

### REMIT-STR-03 · Document the assessment of alerts
*Article 15(3) REMIT* · guidance · applies to: ppat, ppet, omp, dea_provider · documents: SUR

ACER expects a traceable process from alert to decision, with key decision points recorded, substantiated notifications, and the possibility to notify past events that later become suspicious.

Checks:
- [ ] `c1` **[ACER]** Describes how an alert is assessed and who decides whether a suspicion is reasonable.
- [ ] `c2` **[ACER]** Requires each decision and its reasoning to be recorded, including decisions not to notify, and kept for at least five years.
- [ ] `c3` **[ACER]** Covers notification of past events that become suspicious later.
- [ ] `c4` **[ACER]** Requires notifications to state the reasons for the suspicion.
- [ ] `c5` **[ACER]** Requires notifications to be submitted through ACER's Notification Platform.

Sources: ACER Guidance 9.3.3, paras. (453)-(458); ACER Guidance 9.4.2, para. (473); ACER Guidance 9.4.4.4, paras. (512)-(516)

Reviewer comments:

---

### REMIT-STR-04 · Notify the right authorities
*Article 15(4) REMIT* · law · applies to: ppat, ppet, omp, dea_provider · documents: SUR

Notifications go to ACER and to the NRAs of the Member States where the market participant concerned is registered and where the product is delivered.

Checks:
- [ ] `c1` **[LAW]** Requires notification of ACER and of the NRAs where the participant concerned is registered and where the product is delivered.
- [ ] `c2` **[ACER]** Where the product is also a MAR financial instrument, also notifies the competent financial authority. _(only if trades_financial_instruments)_

Sources: ACER Guidance 9.3.2; ACER Guidance 9.3.4

Reviewer comments:

---

# Part B — Adjacent regime (MAR)

## Mar

### MAR-SCOPE-01 · Identify which products are also financial instruments
*Article 1(2) REMIT, Article 2 MAR* · law · applies to: trades_financial_instruments · documents: MCP

REMIT applies without prejudice to MAR. Products that are financial instruments (e.g. cash-settled exchange futures) are also subject to MAR's insider dealing, disclosure and manipulation rules. Physically settled forwards are REMIT-only.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Maps the company's traded products to REMIT-only or REMIT-and-MAR.
- [ ] `c2` **[LAW]** States that MAR rules apply in addition where products are financial instruments.

Sources: ACER Guidance 2.5

Reviewer comments:

---

### MAR-EUA-01 · Emission allowance market participants - disclosure and insider lists
*Article 17(2) MAR, Article 18(8)(a) MAR* · law · applies to: eamp · documents: IIP

An emission allowance market participant above the emission and thermal-input thresholds discloses inside information about its installations and keeps insider lists for that information.

Checks:
- [ ] `c1` **[LAW]** States whether the company is above the Article 17(2) MAR thresholds.
- [ ] `c2` **[LAW]** Requires an insider list for emission-allowance inside information.

Sources: ESMA Q&A on MAR, Q 11.2

Reviewer comments:

---

### MAR-STOR-01 · STORs under MAR for financial instruments
*Article 16 MAR, Article 15(2) REMIT* · law · applies to: mar_ppaet · documents: SUR

PPAETs under MAR report suspicious orders and transactions in financial instruments to their financial competent authority. If they also execute non-financial wholesale energy products, REMIT Article 15(2) adds notification to ACER and the NRA within four weeks.

Checks:
- [ ] `c1` **[LAW]** Distinguishes MAR STORs (to the financial authority) from REMIT notifications (to ACER and the NRA) and their deadlines.

Sources: ACER Guidance 9.2.2

Reviewer comments:

---

# Part C — Good practice (non-binding)

## Governance

### REMIT-GP-01 · Independent, resourced compliance function
applies to: market_participant · documents: CM, MCP

Clear REMIT roles; a compliance function independent of trading, with direct access to senior management and to all relevant information, and enough resources.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Names the REMIT compliance officer or responsible function.
- [ ] `c2` **[GOOD PRACTICE]** States that compliance reports to senior management independently of trading.
- [ ] `c3` **[GOOD PRACTICE]** States that compliance has access to all trading and operational information.

Sources: Nord Pool REMIT Best Practice 3rd ed., sections 2.1.2-2.1.3; ACER Guidance 10.2, para. (521); ACER Manual for new market participants 2026, section 6

Reviewer comments:

---

### REMIT-GP-02 · Documented REMIT risk assessment
applies to: market_participant · documents: CM

Assess likelihood and impact of each REMIT risk and focus controls on the high ones.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Refers to a REMIT risk assessment covering each market-abuse type.
- [ ] `c2` **[GOOD PRACTICE]** States how often the risk assessment is updated.

Sources: Nord Pool REMIT Best Practice 3rd ed., section 2.1.4; ACER Guidance 10.2, para. (521)

Reviewer comments:

---

### REMIT-GP-03 · Annual compliance plan and report to management
applies to: market_participant · documents: CM

A compliance programme built on prevention, detection and response, with a yearly plan and a report to management.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Requires an annual compliance plan.
- [ ] `c2` **[GOOD PRACTICE]** Requires a periodic compliance report to management.

Sources: Nord Pool REMIT Best Practice 3rd ed., section 2.1.5

Reviewer comments:

---

## Training

### REMIT-GP-04 · Role-based REMIT training with records
applies to: market_participant · documents: CM, MCP

Training tailored to traders, plant staff and back office, at onboarding and regularly after, with attendance records.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Defines training audiences by role.
- [ ] `c2` **[GOOD PRACTICE]** States the training frequency, including onboarding.
- [ ] `c3` **[GOOD PRACTICE]** Requires attendance and results to be recorded.

Sources: Nord Pool REMIT Best Practice 3rd ed., section 2.1.6 and Appendix 4; ACER Manual for new market participants 2026, sections 5-6

Reviewer comments:

---

## Governance

### REMIT-GP-05 · Speak-up channel for REMIT concerns
applies to: market_participant · documents: CM, MCP

Low threshold for raising concerns, protection against retaliation, optional anonymous channel.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Describes how staff can raise REMIT concerns, including anonymously.
- [ ] `c2` **[GOOD PRACTICE]** States that people who raise concerns are protected from retaliation.

Sources: Nord Pool REMIT Best Practice 3rd ed., section 2.1.6

Reviewer comments:

---

## Cooperation

### REMIT-GP-06 · Regulator-contact policy and dawn-raid manual
applies to: market_participant · documents: REGINT

Compliance manages regulator contact; a dawn-raid manual tells staff what to do during an inspection.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Names the function that manages contact with NRAs and ACER.
- [ ] `c2` **[GOOD PRACTICE]** Refers to a dawn-raid manual or inspection instructions.

Sources: Nord Pool REMIT Best Practice 3rd ed., section 2.1.6 and Appendix 5

Reviewer comments:

---

## Inside Information

### REMIT-GP-07 · Framework for identifying inside information
applies to: market_participant · documents: IIP

Internal criteria or tested thresholds for assessing inside information, and a map of where it arises and flows.

Checks:
- [ ] `c1` **[ACER]** Sets criteria or thresholds for assessing whether an event is inside information.
- [ ] `c2` **[ACER]** Maps where inside information arises (assets, departments) and where it flows.

Sources: ACER Guidance 3.3, paras. (81)-(83); Nord Pool REMIT Best Practice 3rd ed., sections 3.1 and 3.4

Reviewer comments:

---

### REMIT-GP-08 · Identify insiders and log access to inside information
applies to: market_participant · documents: IIP

A list of insiders or a mechanism to identify them, and a log of who received inside information and when.

Checks:
- [ ] `c1` **[ACER]** Requires a list of persons with access to inside information, or another mechanism to identify them.
- [ ] `c2` **[GOOD PRACTICE]** Requires a log of who received inside information and when, especially during a delayed disclosure.

Sources: ACER Guidance 3.3, para. (82); Nord Pool REMIT Best Practice 3rd ed., section 3.1

Reviewer comments:

---

### REMIT-GP-09 · Information barriers and a documented trade stop
applies to: market_participant · documents: IIP, MCP

Separate traders from people with inside information, and have a documented trade-stop mechanism.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Describes the information barriers between asset operations and trading.
- [ ] `c2` **[GOOD PRACTICE]** Describes a trade-stop mechanism and what is recorded when it is used.

Sources: Nord Pool REMIT Best Practice 3rd ed., sections 3.1.2-3.1.3

Reviewer comments:

---

## Record Keeping

### REMIT-GP-10 · Record trader communications and keep trading records for five years
applies to: market_participant · documents: MCP

Record relevant staff communications and keep transactions, disclosures and trade communications for at least five years. NRAs can demand existing records (Article 13(2) REMIT), so records that exist must be retrievable.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** States which communication channels of traders are recorded (phone, chat, e-mail).
- [ ] `c2` **[GOOD PRACTICE]** States a retention period of at least five years for transactions, disclosures and trade communications.

Sources: ACER Manual for new market participants 2026, section 6; Nord Pool REMIT Best Practice 3rd ed., section 3.1

Reviewer comments:

---

## Market Conduct

### REMIT-GP-11 · Trading mandates and rationale for unusual trades
applies to: market_participant · documents: MCP

Documented trading mandates, recorded reasons for unusual orders, and a list of behaviours to avoid.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Refers to documented trading mandates and limits.
- [ ] `c2` **[GOOD PRACTICE]** Requires traders to record the reason for unusual orders or trades.

Sources: Nord Pool REMIT Best Practice 3rd ed., section 3.2

Reviewer comments:

---

### REMIT-GP-12 · Erroneous-order handling
applies to: market_participant · documents: MCP, IIP

Prevent errors; when one happens, assess it as possible inside information or manipulation risk and investigate.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Requires each erroneous order or trade to be assessed as possible inside information.
- [ ] `c2` **[GOOD PRACTICE]** Describes the incident investigation steps after an erroneous order.

Sources: Nord Pool REMIT Best Practice 3rd ed., section 3.4

Reviewer comments:

---

## Algorithmic Trading

### REMIT-GP-13 · Algorithm governance, including vendor algorithms
applies to: algo_trader · documents: ALG

Design review, separate test environment, documented approval before go-live, kill function, and the same standards for vendor algorithms.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Requires documented approval before an algorithm or a change goes live.
- [ ] `c2` **[GOOD PRACTICE]** Applies the same controls to vendor-supplied algorithms.

Sources: Nord Pool REMIT Best Practice 3rd ed., section 3.3 and Appendix 7

Reviewer comments:

---

## Governance

### REMIT-GP-14 · Compliance involvement in new products and markets
applies to: market_participant · documents: CM, MCP

Compliance signs off before trading a new product or on a new venue.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Requires compliance sign-off before trading a new product or on a new venue.

Sources: Nord Pool REMIT Best Practice 3rd ed., section 2.1.3

Reviewer comments:

---

### REMIT-GP-15 · Monitoring, periodic review and internal audit
applies to: market_participant · documents: SUR, CM

Monitoring of own trading even where Article 15 does not apply, regular review of procedures, internal audit.

Checks:
- [ ] `c1` **[GOOD PRACTICE]** Describes monitoring of the company's own trading by a function independent of the traders.
- [ ] `c2` **[GOOD PRACTICE]** States a review frequency for REMIT procedures and triggers for ad-hoc review.
- [ ] `c3` **[GOOD PRACTICE]** Provides for internal audit of REMIT compliance.

Sources: Nord Pool REMIT Best Practice 3rd ed., section 2.1.7

Reviewer comments:

---
