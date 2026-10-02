# Accessibility Baseline Audit

## Overview

This project documents a baseline accessibility and technical audit of a public website using Google Lighthouse / PageSpeed Insights.

The purpose is to identify accessibility and technical issues, document evidence, and provide recommendations for improvement.

## Audit Tools

- Google PageSpeed Insights
- Lighthouse
- Chrome DevTools
- Keyboard accessibility checks

## Findings

### 1. Incorrect ARIA Parent Structure

Lighthouse reported:

`[role]s are not contained by their required parent element`

The issue involves an element using `role="listitem"` without the required parent structure.

### 2. Insufficient Color Contrast

Lighthouse reported insufficient contrast between foreground and background colors.

Example:

`Avail online Services & Save time`

### 3. Render-Blocking Resources

Some CSS and JavaScript resources can delay the initial rendering of the page.

### 4. Inefficient Cache Lifetimes

Some resources have inefficient or missing cache lifetimes, which can cause repeated downloads.

### 5. Browser Errors

Lighthouse reported browser errors in the console that require further investigation.

## Repository Structure

```text
accessibility-baseline-audit/
├── client/
│   └── index.html
├── server/
│   └── app.py
├── docs/
│   ├── accessibility-audit.md
│   └── evidence/
├── tests/
│   ├── test_accessibility.py
│   └── README.md
├── README.md
├── requirements.txt
└── .gitignore
