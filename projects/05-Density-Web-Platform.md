---
layout: default
title: Density Web Platform
permalink: /projects/05-Density-Web-Platform.html
---

# Density Web Platform
## Business Model Transformation - Full-Stack RTO Payment System

**Role:** Full-Stack Engineer
**Duration:** 1 year (RTO system: 2 months intensive)
**Context:** Supporting web platform alongside DAW tech lead role
**Technologies:** NestJS, React, TypeScript, PostgreSQL, Chargebee

---

<div class="highlight-box">

### 🎯 Key Achievements

- **Zero production billing errors** delivering complete RTO payment system in 2 months
- **Enabled business model pivot** from subscription to perpetual licenses with rent-to-own option
- **Complex discount engine** handling RTO progress, promotional codes, bundle pricing, and edge cases
- **Full-stack ownership** of frontend, backend, database, and payment integration
- **Solved production race conditions** with database-backed subscription locking
- **Backward compatibility** preserving existing subscriptions during business model transition

</div>

<div class="metrics-box">
  <div class="metric">
    <span class="metric-value">0</span>
    <span class="metric-label">Billing<br>Errors</span>
  </div>
  <div class="metric">
    <span class="metric-value">2 Months</span>
    <span class="metric-label">Complete<br>System Built</span>
  </div>
  <div class="metric">
    <span class="metric-value">14</span>
    <span class="metric-label">Payment<br>Lifecycle</span>
  </div>
  <div class="metric">
    <span class="metric-value">100%</span>
    <span class="metric-label">Backward<br>Compatible</span>
  </div>
</div>

## Overview

While serving as Tech Lead for Density's native DAW, I contributed to the company's web platform infrastructure. When the business needed to pivot from subscription to perpetual licenses with rent-to-own (RTO) payments, I took full ownership of designing and implementing this critical system.

**Key Achievement:** Delivered complete RTO payment system in 2 months with **zero production billing errors**, enabling new business model while maintaining backward compatibility.

---

## The Business Challenge

<div class="two-col">
  <div class="col-box">
    <h4>💰 New Purchase Model</h4>
    <ul>
      <li><strong>One-time purchase:</strong> $200 upfront</li>
      <li><strong>Rent-to-own:</strong> $15/month for 14 months</li>
      <li>Pro access from first RTO payment</li>
      <li>Early buyout option available</li>
    </ul>
  </div>
  <div class="col-box">
    <h4>⚖️ Backward Compatibility</h4>
    <ul>
      <li>Existing subscribers continue subscriptions</li>
      <li>Migration path without forcing changes</li>
      <li>Preserve subscription anniversary dates</li>
      <li>Support both models simultaneously</li>
    </ul>
  </div>
  <div class="col-box">
    <h4>🎁 Hardware Bundle Discounts</h4>
    <ul>
      <li>Discount hardware based on RTO progress</li>
      <li>Promotional discount codes (Black Friday, etc.)</li>
      <li>Edge cases: multiple discounts interacting</li>
      <li>Bundle pricing (Pro + Hardware together)</li>
    </ul>
  </div>
  <div class="col-box">
    <h4>✅ Financial Correctness</h4>
    <ul>
      <li>Accurate payment tracking (can't lose money)</li>
      <li>Synchronization with Chargebee platform</li>
      <li>State consistency across systems</li>
      <li>Audit trail for all transactions</li>
    </ul>
  </div>
</div>

---

## Technical Implementation

### RTO State Machine

<div class="highlight-box">

Designed state-based system managing complete RTO lifecycle:

**States:**
- `rto_active` - In payment plan, has Pro access
- `rto_owned` - Completed all payments, owns software
- `subscription` - Legacy subscription users
- `perpetual` - One-time purchase users

**Key Transitions:**
1. **First RTO Payment:** Grant Pro access immediately, initialize counter (1/14)
2. **Monthly Payment:** Update progress counter (2/14, 3/14, etc.)
3. **14th Payment (Completion):** Convert to `rto_owned`, cancel subscription, grant perpetual access
4. **Early Buyout:** Calculate remaining balance, process payment, immediate ownership
5. **Missed Payment:** Grace period handling, access revocation, catch-up payment option

</div>

---

### Complex Discount Calculation Engine

The most technically challenging aspect—handling multiple discount factors:

<div class="two-col">
  <div class="col-box">
    <h4>Discount Factors</h4>
    <ul>
      <li><strong>RTO Progress:</strong> 0-14 payments completed</li>
      <li><strong>User Tier:</strong> Free, Pro, hardware states</li>
      <li><strong>Promotional Codes:</strong> Percentage vs fixed</li>
      <li><strong>Bundle Purchase:</strong> Pro + Hardware together</li>
      <li><strong>Special Events:</strong> Black Friday, limited-time</li>
    </ul>
  </div>
  <div class="col-box">
    <h4>Edge Cases Handled</h4>
    <ul>
      <li>User 8/14 through RTO + Black Friday code + bundle</li>
      <li>User completes RTO during checkout</li>
      <li>Promo codes expiring mid-checkout</li>
      <li>Multiple discount code validation</li>
      <li>Price floor enforcement</li>
      <li>Tax calculation on discounted amounts</li>
    </ul>
  </div>
</div>

---

### Chargebee Integration & Webhook Processing

<div class="highlight-box">

Built robust webhook processing keeping local database synchronized with Chargebee:

**Events Handled:**
- `subscription_created` - Initialize RTO tracking and payment schedule
- `payment_succeeded` - Increment counter, check for completion (14/14)
- `subscription_cancelled` - Preserve RTO progress, update access
- `payment_failed` - Handle grace periods and retry logic

**Idempotency Challenge:** Kubernetes pod restarts causing webhook processing issues

**Solution:** Database-backed subscription locking, idempotency through database queries (not memory cache), transaction isolation, timeout/retry mechanisms

</div>

---

### Database Schema

Designed schema tracking RTO state and payment history:

```typescript
User {
  licenseType: 'free' | 'subscription' | 'rto_active' | 'rto_owned' | 'perpetual'
  rtoInstallmentsPaid: number  // 0-14
  chargebeeSubscriptionId: string
  hardwareOwnership: boolean
  discountCodesUsed: string[]
}

RTOPaymentHistory {
  userId: string
  paymentNumber: number  // 1-14
  paymentDate: Date
  amount: number
  chargebeeInvoiceId: string
}

SubscriptionLock {
  subscriptionId: string
  lockAcquiredAt: Date
  processingPodId: string
}
```

---

## Testing Strategy

<div class="highlight-box">

Worked extensively with QA team using full environment isolation:

**QA Environments:**
- QA Frontend (test.density.com)
- QA Backend (staging API)
- Chargebee Test Site (sandbox billing with test credit cards)

**Test Scenarios:** 14 successful payments, early buyouts at various stages, payment failures, hardware discount combinations, backward compatibility, race conditions, timezone differences

**Result:** **No production billing issues** - All edge cases caught in QA before launch

</div>

---

## Key Technical Challenges Solved

<div class="two-col">
  <div class="col-box">
    <h4>Financial Logic Correctness</h4>
    <p><strong>Problem:</strong> Bugs are expensive with money. Need absolute correctness.</p>
    <p><strong>Solution:</strong> Comprehensive validation, database constraints, extensive logging, reconciliation jobs, price floor enforcement.</p>
  </div>
  <div class="col-box">
    <h4>Backward Compatibility</h4>
    <p><strong>Problem:</strong> Can't disrupt existing paying subscribers during migration.</p>
    <p><strong>Solution:</strong> License type enum supporting both models, feature flags, careful webhook handling, migration UI with explanations.</p>
  </div>
  <div class="col-box">
    <h4>Discount Edge Cases</h4>
    <p><strong>Problem:</strong> Multiple discount variables created combinatorial explosion of scenarios.</p>
    <p><strong>Solution:</strong> Discount calculation service with extensive unit tests, minimum price floors, clear precedence rules, validation.</p>
  </div>
  <div class="col-box">
    <h4>Production Reliability</h4>
    <p><strong>Problem:</strong> Kubernetes pod restarts causing webhook processing issues.</p>
    <p><strong>Solution:</strong> Database-backed subscription locking, idempotency through queries not memory, transaction isolation, monitoring.</p>
  </div>
</div>

---

## Results & Impact

<div class="metrics-box">
  <div class="metric">
    <span class="metric-value">2 Months</span>
    <span class="metric-label">Complete<br>Delivery</span>
  </div>
  <div class="metric">
    <span class="metric-value">0</span>
    <span class="metric-label">Billing<br>Errors</span>
  </div>
  <div class="metric">
    <span class="metric-value">1000s</span>
    <span class="metric-label">Users<br>Supported</span>
  </div>
  <div class="metric">
    <span class="metric-value">✓</span>
    <span class="metric-label">Seamless<br>Migration</span>
  </div>
</div>

### Business Value

<div class="highlight-box">

**New Business Model:**
- Enabled pivot from subscription to ownership without disrupting revenue
- Flexible payment options opened market to broader audience
- Reduced barrier to entry with $15/month option

**Revenue Optimization:**
- Hardware bundling increased average transaction value
- RTO discount incentivized hardware purchases
- Promotional codes drove sales during special events

**Customer Satisfaction:**
- Professional DJs preferred ownership model
- Early buyout option provided flexibility
- Clear progress tracking in user dashboard

</div>

---

## Technologies Used

**Backend:** NestJS 9.0, TypeORM, PostgreSQL, Passport.js, Chargebee Node SDK, Winston

**Frontend:** React 18.2, Material-UI (MUI) 5.11, Redux + Redux Saga, Axios, React Router, Formik + Yup

**Infrastructure:** Google Cloud Run, Google Cloud Secret Manager, Docker, GitHub Actions, Sentry

**Testing:** Jest, React Testing Library, Chargebee Test Environment, Postman

---

## Key Takeaways

<div class="highlight-box">

**Full-Stack Versatility:** Switched from C++ native development (DAW) to TypeScript full-stack work based on company needs. Shows adaptability across entire technology stack.

**Financial Systems Expertise:** Payment processing requires careful architecture, extensive testing, defensive programming, audit trails, and reconciliation.

**Production-Grade Engineering:** Proper QA processes and defensive programming prevented costly production issues. **Zero billing errors** demonstrates commitment to quality.

**Fast Execution:** Delivered business-critical feature in 2 months while maintaining quality and backward compatibility.

**Business Impact Understanding:** Designed flexible system supporting current needs and future extensions (new pricing models, hardware bundles, promotional campaigns).

</div>

---

## Career Significance

Density Web Platform demonstrates versatility beyond audio engineering:

- **Full-stack capability** across NestJS backend and React frontend
- **Financial systems** with zero-error requirement
- **Production engineering** solving webhook processing, idempotency, race conditions
- **Business alignment** translating product requirements to technical implementation
- **Fast execution** delivering complete feature in 2 months

This project complemented native DAW work, showing ability to switch technologies and contribute wherever business needs are greatest.

---

**Related Projects:**
- [Density DAW](02-Density-DAW.html) - Native C++/JUCE application this web platform supports
- [Density Copilot](01-Density-Copilot.html) - AI assistant integrated with both DAW and web platform
