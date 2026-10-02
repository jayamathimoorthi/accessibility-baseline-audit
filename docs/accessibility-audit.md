# Accessibility & Architecture Audit

## Audited Website

Public website audited using Google PageSpeed Insights / Lighthouse.

## Findings

### 1. Incorrect ARIA Parent Structure

**Category:** Accessibility

Lighthouse reported:

`[role]s are not contained by their required parent element`

The failing element uses `role="listitem"` without the required parent structure.

**Impact:** Assistive technologies may not interpret the page structure correctly.

**Priority:** High

### 2. Insufficient Color Contrast

**Category:** Accessibility

Lighthouse reported insufficient contrast between foreground and background colors.

Example:

`Avail online Services & Save time`

**Impact:** Low-contrast text can be difficult to read for users with visual impairments.

**Priority:** Medium

### 3. Render-Blocking Resources

**Category:** Performance / Architecture

Lighthouse identified resources that delay initial page rendering.

**Impact:** This can increase the time required for useful page content to appear.

**Priority:** Medium

### 4. Inefficient Cache Lifetimes

**Category:** Performance / Architecture

Lighthouse identified resources with inefficient or missing cache lifetimes.

**Impact:** Resources may need to be downloaded repeatedly, increasing network usage and load time.

**Priority:** Medium

### 5. Browser Errors Logged to Console

**Category:** Reliability / Architecture

Lighthouse reported browser errors in the console.

**Impact:** Console errors may indicate failed requests or JavaScript/runtime problems.

**Priority:** Medium
