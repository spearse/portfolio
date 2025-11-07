---
layout: default
title: Density Web Platform
permalink: /projects/05-Density-Web-Platform.html
---

# Density Web Platform
## Business Model Transformation - Full-Stack RTO Payment System

**Role:** Full-Stack Engineer
**Duration:** 1 year (RTO system: 2 months intensive development)
**Context:** Same company as Density DAW, supporting web platform team
**Scope:** Complete frontend and backend implementation of RTO payment system
**Technologies:** NestJS, React, TypeScript, PostgreSQL, Chargebee

---

## Overview

While serving as Tech Lead for Density's native DAW application, I also contributed to the company's web platform infrastructure. When the business needed to transform from a subscription model to perpetual licenses and rent-to-own (RTO) payments, I took full ownership of designing and implementing this critical system.

**Key Achievement:** Delivered complete RTO payment system in 2 months with **zero production billing errors**, enabling new business model while maintaining backward compatibility for existing subscribers.

---

## The Business Challenge

After launching with a traditional subscription model, Density needed to pivot to better serve professional DJs who wanted software ownership rather than ongoing subscriptions.

**Requirements:**

**Two Purchase Paths:**
- One-time purchase for $200
- Rent-to-own: $15/month for 14 months

**Backward Compatibility:**
- Existing subscribers could continue their subscriptions
- Provide migration path without forcing changes
- Preserve subscription anniversary dates

**Hardware Bundle Discounts:**
- Discount hardware based on RTO payment progress (e.g., 8/14 payments = X% off hardware)
- Handle promotional discount codes (Black Friday, special events)
- Edge cases: multiple discounts interacting simultaneously

**Financial Correctness:**
- Accurate payment tracking (can't lose money)
- Synchronization with Chargebee billing platform
- State consistency across database and payment provider
- Audit trail for all transactions

---

## Technical Implementation

### Full-Stack Architecture

**Backend (NestJS/TypeScript):**
- RTO state machine tracking 14-month payment lifecycle
- Chargebee webhook integration for payment events
- Database synchronization ensuring consistency
- Complex discount calculation engine
- Subscription lock service preventing race conditions

**Frontend (React/TypeScript):**
- User dashboard showing RTO progress (X of 14 payments)
- Hardware purchase flow with dynamic discount calculation
- Payment method management
- Early buyout option with remaining balance calculation
- Migration path for legacy subscribers

---

### RTO State Machine

Designed a state-based system managing the complete RTO lifecycle:

**States:**
- `rto_active` - User is in active payment plan, has Pro access
- `rto_owned` - User completed all payments, owns software
- `subscription` - Legacy subscription users (backward compatibility)
- `perpetual` - One-time purchase users
- `free` - Free tier users

**State Transitions:**

1. **First RTO Payment:**
   - Grant Pro access immediately
   - Set `rto_active` status
   - Initialize payment counter (1/14)

2. **Monthly Payment:**
   - Update progress counter (2/14, 3/14, etc.)
   - Maintain Pro access
   - Track payment history

3. **14th Payment (Completion):**
   - Convert to `rto_owned` status
   - Cancel subscription in Chargebee
   - Create "free forever" plan (no more charges)
   - Grant perpetual Pro access

4. **Early Buyout:**
   - Calculate remaining balance ((14 - paid) × $15)
   - Process single payment for remainder
   - Immediate conversion to `rto_owned`
   - Cancel subscription

5. **Missed Payment:**
   - Grace period handling
   - Access revocation after grace period
   - Ability to resume with catch-up payment

---

### Complex Discount Calculation Engine

The most technically challenging aspect was the hardware bundle discount logic with multiple variables:

**Discount Factors:**
- **RTO Progress:** 0-14 payments completed
- **User Tier:** Free, Pro, different hardware ownership states
- **Promotional Codes:** Percentage vs fixed amount, expiration dates
- **Bundle Purchase:** Pro + Hardware purchased together
- **Special Events:** Black Friday sales, limited-time offers

**Calculation Logic:**

```typescript
// Simplified pseudocode showing complexity
calculateHardwareDiscount(user) {
  // Base hardware price varies by user tier
  let price = getBasePriceForTier(user.tier);

  // Discount based on RTO contribution
  if (user.licenseType === 'rto_active') {
    const paymentsCompleted = user.rtoInstallmentsPaid;
    const contributionDiscount = calculateProgressDiscount(paymentsCompleted);
    price -= contributionDiscount;
  }

  // Additional promotional discount codes
  if (user.hasDiscountCode) {
    const promoDiscount = validateAndApplyPromoCode(user.discountCode, price);
    price -= promoDiscount;
  }

  // Bundle pricing (Pro + Hardware)
  if (user.purchasingBundle) {
    price -= BUNDLE_DISCOUNT;
  }

  // Ensure price never goes negative, handle edge cases
  return Math.max(price, MINIMUM_HARDWARE_PRICE);
}
```

**Edge Cases Handled:**
- User 8/14 through RTO + Black Friday discount code + bundle purchase
- User completes RTO during hardware checkout process
- Promotional codes with expiration during checkout
- Multiple discount codes (validation and priority)
- Price floor enforcement
- Tax calculation on discounted amounts
- Currency conversion for international users

---

### Chargebee Integration & Webhook Processing

Built robust webhook processing to keep local database synchronized with Chargebee billing platform:

**Events Handled:**

1. **`subscription_created`**
   - Initialize RTO tracking
   - Set up payment schedule
   - Create database records

2. **`payment_succeeded`**
   - Increment payment counter
   - Check for completion (14/14)
   - Trigger ownership conversion if complete
   - Update user dashboard

3. **`subscription_cancelled`**
   - Preserve RTO progress
   - Update access accordingly
   - Handle early vs late cancellation

4. **`subscription_renewed`**
   - Prevent duplicate Pro subscriptions
   - Handle anniversary date logic
   - Update billing cycle

5. **`payment_failed`**
   - Handle grace periods
   - Notification system
   - Retry logic

**Idempotency & Race Conditions:**

Critical challenge: Kubernetes pod restarts were causing webhook processing issues.

**Problem:**
- In-memory caches losing state during pod restart
- Duplicate webhook processing (Chargebee sends multiple times)
- Race conditions during high-traffic periods

**Solution:**
- Implemented subscription lock service using database-backed locks
- Idempotency through database queries instead of memory cache
- Transaction isolation preventing duplicate processing
- Timeout and retry mechanisms
- Comprehensive logging for debugging

---

### Database Schema

Designed schema tracking RTO state and payment history:

```typescript
User {
  id: string
  email: string
  licenseType: 'free' | 'subscription' | 'rto_active' | 'rto_owned' | 'perpetual'
  rtoInstallmentsPaid: number  // 0-14
  chargebeeSubscriptionId: string
  hardwareOwnership: boolean
  discountCodesUsed: string[]
  // ... other fields
}

// Separate tracking table for payment history
RTOPaymentHistory {
  userId: string
  paymentNumber: number  // 1-14
  paymentDate: Date
  amount: number
  chargebeeInvoiceId: string
  transactionId: string
}

// Subscription lock table for idempotency
SubscriptionLock {
  subscriptionId: string
  lockAcquiredAt: Date
  processingPodId: string
}
```

---

### Testing Strategy

Worked extensively with QA team using full environment isolation:

**QA Environments:**
- **QA Frontend** (test.density.com)
- **QA Backend** (staging API)
- **Chargebee Test Site** (sandbox billing with test credit cards)

**Test Scenarios Covered:**

**Happy Paths:**
- 14 successful payments → ownership
- Early buyout at various stages (2/14, 8/14, 13/14)
- Hardware purchase with RTO discount
- Migration from subscription to RTO

**Edge Cases:**
- Payment failures and retry logic
- Hardware discount calculations with various discount combinations
- Backward compatibility for existing subscribers
- Webhook delivery delays and duplicates
- Race conditions (concurrent webhook processing)
- Timezone differences affecting payment dates
- User changing payment method mid-cycle
- Promotional code expiration during checkout

**Result:** **No production billing issues** - All edge cases caught in QA before launch.

---

## Technical Challenges Solved

### 1. Financial Logic Correctness

**Challenge:** When dealing with money, bugs are expensive. Need absolute correctness.

**Problems:**
- Ensuring payment tracking couldn't drift from Chargebee
- Preventing users from getting "free" hardware through discount stacking exploits
- Handling timezone differences in payment date tracking
- Reconciling failed webhook deliveries

**Solution:**
- Comprehensive validation at every step
- Database constraints preventing invalid states
- Extensive logging for audit trails
- Reconciliation jobs comparing Chargebee vs. local database
- Price floor enforcement preventing negative amounts

---

### 2. Backward Compatibility

**Challenge:** Couldn't disrupt existing paying subscribers during migration.

**Requirements:**
- Preserve all existing subscription functionality
- Create migration path for users who wanted to switch
- Handle users mid-billing cycle
- Maintain subscription anniversary dates

**Solution:**
- License type enum supporting both old and new models
- Feature flags for gradual rollout
- Careful webhook handling for legacy subscriptions
- Migration UI with clear explanations
- Dry-run capability for testing migrations

---

### 3. Discount Calculation Edge Cases

**Challenge:** Hardware discount logic with multiple variables created combinatorial explosion of scenarios.

**Variables:**
- RTO progress (0-14 payments)
- User tier (Free, Pro, different hardware ownership states)
- Promotional codes (percentage vs fixed amount)
- Bundle vs individual purchase
- Special event sales (Black Friday)

**Solution:**
- Built discount calculation service with extensive unit tests covering all combinations
- Established minimum price floors
- Clear precedence rules for discount stacking
- Validation preventing invalid combinations
- Admin dashboard for testing discount scenarios

---

### 4. Production Reliability

**Challenge:** Kubernetes pod restarts were causing webhook processing issues.

**Problems:**
- In-memory caches losing state
- Duplicate webhook processing
- Race conditions during high-traffic periods

**Solution:**
- Moved to database-backed subscription locking
- Implemented idempotency through database queries instead of memory
- Added timeout and retry mechanisms
- Transaction isolation for critical operations
- Monitoring and alerting for webhook processing delays

---

## Technologies Used

**Backend:**
- NestJS 9.0 - Node.js framework with dependency injection
- TypeORM - Database ORM with migrations
- PostgreSQL - Primary database
- Passport.js - Authentication strategies
- Chargebee Node SDK - Payment processing integration
- Winston - Structured logging

**Frontend:**
- React 18.2 - UI framework
- Material-UI (MUI) 5.11 - Component library
- Redux + Redux Saga - State management
- Axios - HTTP client
- React Router - Navigation
- Formik + Yup - Form handling and validation

**Infrastructure:**
- Google Cloud Run - Serverless deployment
- Google Cloud Secret Manager - Credential storage
- Docker - Containerization
- GitHub Actions - CI/CD
- Sentry - Error tracking

**Testing:**
- Jest - Unit and integration testing
- React Testing Library - Component testing
- Chargebee Test Environment - Billing sandbox
- Custom test scripts for RTO scenarios
- Postman - API testing

---

## Results & Impact

### Execution

**Timeline:**
- Complete system delivered in **2 months** (design, implement, test, deploy)
- Frontend + Backend + Database + Integration
- Full ownership of entire feature

**Quality:**
- **Zero production billing issues** post-launch
- Seamless migration for existing users
- All edge cases caught in QA before production

**Scale:**
- Handles thousands of users
- Processing payments reliably
- Financial accuracy maintained

---

### Business Value

**New Business Model:**
- Enabled pivot from subscription to ownership without disrupting existing revenue
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

---

### Technical Quality

**Financial Correctness:**
- Maintained across all edge cases
- Reconciliation with Chargebee confirmed accuracy
- Audit trail for all transactions

**Robustness:**
- Proper webhook idempotency
- Race condition prevention
- Graceful error handling

**Testing:**
- Comprehensive test coverage
- QA environment isolated issues pre-production
- No hotfixes needed post-launch

**Maintainability:**
- Clear documentation for future maintenance
- Well-structured codebase
- Easy to extend for new payment models

---

## Key Takeaways

### Full-Stack Versatility

This project demonstrated adaptability, switching from C++ native development (DAW) to TypeScript full-stack work based on company needs. Shows ability to contribute across entire technology stack.

### Financial Systems Expertise

Working with payment processing, subscription management, and complex pricing logic requires:
- Careful architecture and state management
- Extensive testing and validation
- Defensive programming practices
- Audit trails and reconciliation

### Production-Grade Engineering

Proper QA processes, environment isolation, and defensive programming prevented costly production issues when handling real transactions. **Zero billing errors** demonstrates commitment to quality.

### Fast Execution

Delivered business-critical feature in **2 months** while maintaining quality and backward compatibility. Shows ability to execute quickly under pressure while maintaining production standards.

### Business Impact Understanding

Understood business requirements deeply enough to design flexible system supporting current needs and future extensions (e.g., new pricing models, hardware bundles, promotional campaigns).

---

## Career Significance

Density Web Platform demonstrates versatility beyond audio engineering:

- **Full-stack capability:** NestJS backend + React frontend
- **Financial systems:** Payment processing with zero-error requirement
- **Production engineering:** Webhook processing, idempotency, race conditions
- **Business alignment:** Understanding product requirements and translating to technical implementation
- **Fast execution:** 2 months for complete feature with multiple stakeholders

This project complemented native DAW work, showing ability to switch technologies and contribute wherever business needs are greatest.

---

**Related Projects:**
- [Density DAW](02-Density-DAW.html) - Native C++/JUCE application this web platform supports
- [Density Copilot](01-Density-Copilot.html) - AI assistant integrated with both DAW and web platform

**Technologies:**
- NestJS, React, TypeScript, PostgreSQL
- Chargebee payment processing
- Google Cloud Run deployment
- Financial systems and payment processing
