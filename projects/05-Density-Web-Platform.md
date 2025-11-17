---
layout: default
title: Density Web Platform
permalink: /projects/05-Density-Web-Platform.html
---

# Density Web Platform - Business Model Transformation

## Overview

While serving as Tech Lead for Density's native DAW application, I also contributed to the company's web platform infrastructure. When the business needed to transform from a subscription model to perpetual licenses and rent-to-own (RTO) payments, I took full ownership of designing and implementing this critical system.

**Role:** Full-Stack Engineer
**Duration:** 1 year (RTO system: 2 months intensive development)
**Context:** Same company as Density DAW, supporting web platform team
**Scope:** Complete frontend and backend implementation of RTO payment system

## The Business Challenge

After launching with a traditional subscription model, Density needed to pivot to better serve professional DJs who wanted software ownership rather than ongoing subscriptions. The requirements were:

1. **Enable two purchase paths:**
   - One-time purchase for $200
   - Rent-to-own: $15/month for 14 months

2. **Maintain backward compatibility:**
   - Existing subscribers could continue their subscriptions
   - Provide migration path without forcing changes

3. **Hardware bundle discounts:**
   - Discount hardware based on RTO payment progress
   - Handle promotional discount codes
   - Edge cases: multiple discounts interacting

4. **Financial correctness:**
   - Accurate payment tracking (can't lose money)
   - Synchronization with Chargebee billing platform
   - State consistency across database and payment provider

## Technical Implementation

### Architecture

Built a complete full-stack system using:

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

### RTO State Machine

Designed a state-based system managing the complete RTO lifecycle:

**States:**
- `rto_active` - User is in active payment plan, has Pro access
- `rto_owned` - User completed all payments, owns software
- `subscription` - Legacy subscription users (backward compatibility)

**Transitions:**
- First payment → Grant Pro access + `rto_active` status
- Monthly payment → Update progress counter
- 14th payment → Convert to `rto_owned` + cancel subscription + create "free forever" plan
- Early buyout → Calculate remaining balance → Single payment → Immediate ownership
- Missed payment → Handle grace periods and access revocation

### Complex Discount Calculation

The most technically challenging aspect was the hardware bundle discount logic:

```typescript
// Pseudocode showing complexity
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

Edge cases handled:
- User 8/14 through RTO + Black Friday discount code + bundle purchase
- User completes RTO during hardware checkout process
- Promotional codes with expiration during checkout
- Multiple discount codes (validation and priority)
- Price floor enforcement

### Chargebee Integration

Built robust webhook processing to keep local database synchronized with Chargebee:

**Events Handled:**
- `subscription_created` - Initialize RTO tracking
- `payment_succeeded` - Increment payment counter, check for completion
- `subscription_cancelled` - Preserve RTO progress, update access
- `subscription_renewed` - Prevent duplicate Pro subscriptions
- `payment_failed` - Handle grace periods

**Idempotency & Race Conditions:**
- Implemented subscription lock service to prevent concurrent webhook processing
- Addressed production issue where in-memory caching didn't survive pod restarts in Kubernetes
- Migrated to database-backed state management for reliability
- Handled Chargebee's multiple webhook deliveries for same event

### Database Schema

Designed schema tracking RTO state:

```typescript
User {
  id: string
  email: string
  licenseType: 'free' | 'subscription' | 'rto_active' | 'rto_owned' | 'perpetual'
  rtoInstallmentsPaid: number  // 0-14
  chargebeeSubscriptionId: string
  // ... other fields
}

// Separate tracking table for payment history
RTOPaymentHistory {
  userId: string
  paymentNumber: number
  paymentDate: Date
  amount: number
  chargebeeInvoiceId: string
}
```

### Testing Strategy

Worked extensively with QA team using full environment isolation:

**QA Environments:**
- QA Frontend (test.density.com)
- QA Backend (staging API)
- Chargebee Test Site (sandbox billing)

**Test Scenarios:**
- Happy path: 14 successful payments → ownership
- Early buyout at various stages (2/14, 8/14, 13/14)
- Payment failures and retry logic
- Hardware discount calculations with various discount combinations
- Backward compatibility for existing subscribers
- Migration from subscription to RTO
- Webhook delivery delays and duplicates
- Race conditions (concurrent webhook processing)

**No production billing issues** - All edge cases caught in QA before launch.

## Technical Challenges Solved

### 1. Financial Logic Correctness

When dealing with money, bugs are expensive. Key challenges:
- Ensuring payment tracking couldn't drift from Chargebee
- Preventing users from getting "free" hardware through discount stacking exploits
- Handling timezone differences in payment date tracking
- Reconciling failed webhook deliveries

Solution: Built comprehensive validation at every step, database constraints preventing invalid states, and extensive logging for audit trails.

### 2. Backward Compatibility

Couldn't disrupt existing paying subscribers during migration:
- Preserved all existing subscription functionality
- Created migration path for users who wanted to switch
- Handled users mid-billing cycle
- Maintained subscription anniversary dates

Solution: License type enum supporting both old and new models, feature flags for gradual rollout, careful webhook handling for legacy subscriptions.

### 3. Discount Calculation Edge Cases

Hardware discount logic with multiple variables created combinatorial explosion of scenarios:
- RTO progress (0-14 payments)
- User tier (Free, Pro, different hardware ownership states)
- Promotional codes (percentage vs fixed amount)
- Bundle vs individual purchase
- Special event sales (Black Friday)

Solution: Built discount calculation service with extensive unit tests covering all combinations, established minimum price floors, clear precedence rules for discount stacking.

### 4. Production Reliability

Kubernetes pod restarts were causing webhook processing issues:
- In-memory caches losing state
- Duplicate webhook processing
- Race conditions during high-traffic periods

Solution: Moved to database-backed subscription locking, implemented idempotency through database queries instead of memory, added timeout and retry mechanisms.

## Technologies Used

**Backend:**
- NestJS 9.0 - Node.js framework with dependency injection
- TypeORM - Database ORM with PostgreSQL
- Passport.js - Authentication strategies
- Chargebee Node SDK - Payment processing integration

**Frontend:**
- React 18.2 - UI framework
- Material-UI (MUI) 5.11 - Component library
- Redux + Redux Saga - State management
- Axios - HTTP client

**Infrastructure:**
- PostgreSQL - Primary database
- Google Cloud Run - Serverless deployment
- Google Cloud Secret Manager - Credential storage
- Docker - Containerization

**Testing:**
- Jest - Unit and integration testing
- Chargebee Test Environment - Billing sandbox
- Custom test scripts for RTO scenarios

## Results & Impact

**Execution:**
- Complete system delivered in 2 months (design, implement, test, deploy)
- Zero production billing issues post-launch
- Seamless migration for existing users

**Business Value:**
- Enabled new business model without disrupting existing revenue
- Flexible payment options opened market to broader audience
- Hardware bundling increased average transaction value

**Technical Quality:**
- Financial correctness maintained across all edge cases
- Robust webhook processing with proper idempotency
- Comprehensive test coverage catching issues pre-production
- Clear documentation for future maintenance

## Key Takeaways

**Full-Stack Versatility:**
This project demonstrated adaptability, switching from C++ native development (DAW) to TypeScript full-stack work based on company needs.

**Financial Systems Expertise:**
Working with payment processing, subscription management, and complex pricing logic requires careful architecture and extensive testing.

**Production-Grade Engineering:**
Proper QA processes, environment isolation, and defensive programming prevented costly production issues when handling real transactions.

**Fast Execution:**
Delivered business-critical feature in 2 months while maintaining quality and backward compatibility.

---

*This project complemented my work on Density's native DAW application, showcasing the ability to contribute across the entire technology stack as business needs evolved.*
