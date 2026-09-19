# PHC-0001 — End-to-End Simulated Customer Test

Date: 19 September 2026  
Business: Northshore Fabrication Ltd (fictional)  
Service: Payment Health Check  
Price under test: £199  
Purpose: test the complete first-customer experience before real prospect outreach.

## Test principle

This simulation tests whether the existing service can be sold and fulfilled professionally. It does not count as market validation. Only a real customer payment and real customer evidence count toward the validation gate.

## Fictional customer

Northshore Fabrication Ltd is a 16-person UK B2B fabrication business. It issues approximately 55 invoices per month, mainly on 30-day terms. Typical invoice value is £1,500-£8,000. Some customers require purchase orders and central accounts-payable processing.

Stated problem: invoices are usually paid eventually, but staff spend too much time chasing and some invoices are delayed because of missing purchase-order references, uncertainty over who should receive the invoice, or disputes about whether work was signed off.

## Journey test

### 1. Prospect encounters the offer

Expected experience:
- Understand within seconds that this is a commercial payment-process review.
- See £199 as a fixed one-off price.
- Understand that actual business evidence is reviewed.
- Understand that this is not debt collection, legal advice or accounting/tax advice.
- Be able to see what the final deliverable looks like.

PASS — Current sales page, one-page prospect sheet and sample report support this.

Professional improvement:
- Publish a direct link to the sample report from the sales page once the final public file location is ready.

### 2. Customer decides to buy

Expected experience:
- CTA leads directly to the live £199 Stripe checkout.
- Business/customer identity is collected.
- No discount code or subscription confusion.
- Terms/privacy are available before purchase.

PASS WITH LAUNCH CHECK — Live £199 Stripe link exists and is configured as a one-time purchase.

Required before outreach:
- Confirm HDS naming is consistent in Stripe customer-facing text.
- Confirm website Terms and Privacy links work from the live domain.
- Do not perform a real £199 self-payment merely to test a page.

### 3. Payment succeeds

Simulated event:
Northshore Fabrication pays £199.

Internal action:
- Assign reference PHC-0001.
- Status becomes PAID, then INTAKE OUTSTANDING.
- Send the payment-received/intake email.

PASS — Customer communications pack now defines this step.

Snag:
- Stripe success experience should ultimately point to the intake route or clearly tell the customer what happens next.

### 4. Customer completes intake

Simulated intake:
- Business: Northshore Fabrication Ltd
- 16 employees
- B2B
- VAT registered
- 55 invoices/month
- Typical invoice: £1,500-£8,000
- Standard terms: 30 days
- PO: required by some customers
- Invoice creation: office administrator
- Typical issue delay: same day to 2 working days after completion
- Invoice sending: email, occasionally customer portal
- AP receipt confirmation: inconsistent
- Chasing owner: office administrator, escalated informally to director
- Main problem: PO/reference issues and uncertainty over invoice acceptance
- Time spent chasing: approximately 6 hours/month
- Overdue exposure supplied: fictional £38,400
- Specialist construction mechanisms: no

Files supplied:
- representative invoice;
- standard terms/accepted quotation;
- anonymised aged-debt summary;
- written description of chasing process.

PASS — This is sufficient for an evidence-based review.

### 5. Completeness check

Evidence check identifies:
- invoice received;
- terms received;
- aged debt received;
- chasing process received;
- no clear evidence of a standard completion/sign-off rule.

Decision:
Do not block the entire review solely because completion/sign-off evidence is absent. Record this control as NOT PROVIDED/UNCERTAIN unless the missing item is essential to a material conclusion.

Status:
INTAKE RECEIVED -> READY FOR REVIEW.

PASS — avoids unnecessary customer friction while preserving evidence integrity.

### 6. Review starts

Customer receives:
- review-start confirmation;
- review start date;
- expected delivery date;
- explanation that uncertain evidence will not be guessed.

Internal:
- three-working-day clock begins only now;
- status REVIEWING;
- evidence ledger created.

PASS.

### 7. Evidence analysis

Simulated material findings:

1. CONFIRMED / Critical — PO and AP controls inconsistent.
Evidence: invoice has a PO field; workflow does not consistently establish PO requirement/AP contact before work.
Action: add PO status, billing entity and AP contact to pre-work checkpoint.

2. CONFIRMED / Critical — overdue follow-up is reactive.
Evidence: chasing description lacks a fixed timetable/next-action control.
Action: use named owner, next-action date and standard escalation sequence.

3. CONFIRMED / High — invoice states 30 days but does not show explicit calendar due date.
Action: show payment due date clearly.

4. UNCERTAIN / High — completion evidence is not demonstrated consistently.
Action: define evidence required by job type.
Important: report as uncertainty/evidence gap, not as a proven failure.

PASS — Findings follow Evidence -> Finding -> Impact -> Priority -> Action.

### 8. Scoring

Simulated framework result:
- assessable weight: 70
- earned weighted points: 37.5
- Payment Health Score: 53.57, displayed as 54
- Evidence Confidence: 76.47%, displayed as 76%

PASS — NE/missing evidence is excluded rather than scored as zero.

### 9. Human QA

Required checks:
- correct customer/reference;
- every Critical/High finding tied to evidence;
- no missing evidence converted into a negative fact;
- VAT status known before any VAT-related assessment;
- figures/dates checked;
- contract wording accurately represented;
- recommendations practical;
- no bespoke legal conclusion;
- no debt-recovery promise;
- no cross-customer information;
- 30-day plan matches findings;
- final PDF manually reviewed.

PASS FOR SIMULATION — methodology supports these checks.

### 10. Report delivery

Filename:
PHC-0001_Northshore-Fabrication_Payment-Health-Check.pdf

Delivery email:
Use the report-delivery template. Direct customer first to the executive dashboard and three priority actions.

PASS — polished sample report now demonstrates the intended deliverable.

### 11. Follow-up

Send a short follow-up after the customer has had reasonable time to act.

Measure:
- which recommendations were implemented;
- whether chasing time reduced;
- whether a recurring blocker disappeared;
- whether ownership of overdue invoices became clearer;
- voluntary testimonial/referral only if genuinely earned.

PASS.

## End-to-end result

Overall: PASS WITH PRE-LAUNCH SNAGS.

The service can now be explained, purchased, fulfilled and delivered without requiring a SaaS product, dashboard, CRM or accounting integration.

## Snag list before real outreach

### Launch-critical

1. Verify haydigitalsolutions.co.uk and /payment-health/ are publicly reachable on the custom domain.
2. Verify Terms and Privacy links on the live site.
3. Update remaining customer-facing “Hay Digital” wording in Stripe to “Hay Digital Solutions”.
4. Deploy/test the actual intake mechanism and its file-upload flow.
5. Test upload -> authorised access/download -> deletion/Trash behaviour before collecting real customer documents.
6. Confirm secure case-storage location and 2FA.
7. Complete the ICO fee/self-assessment before accepting real customer personal data where applicable.
8. Run one dummy intake using fictional documents and confirm every file reaches the correct PHC case folder/process.

### Professional but non-blocking

9. Publish the sample report from a stable public link and add it to the sales page.
10. Put the one-page sales sheet in the prospecting pack.
11. Create a simple case manifest for PHC-0001 onward.
12. Keep a deletion due/completed record.

## Stop-building gate

Once launch-critical items 1-8 pass, stop adding features.

Next validation cohort:
- approach 20 genuinely qualified UK B2B prospects;
- £199 remains the real price;
- no free pilot counted as willingness-to-pay;
- no survey response or compliment counted as validation.

Interpretation:
- 0 paid sales plus weak engagement: reconsider/modify the offer;
- 1 paid sale: fulfil it and test a second cohort;
- 2-4 paid sales: meaningful commercial signal;
- 5+ paid sales: prioritise the service and operationalise only the repeated bottlenecks observed in real cases.

The next important evidence is not another simulation. It is a real £199 payment followed by real customer data and a completed report.
