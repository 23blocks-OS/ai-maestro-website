---
name: AI Maestro company preview
description: Near-white preview at /business/. The public homepage is a separate system and is not governed by these tokens.
colors:
  ink: "#171717"
  ink-soft: "#3a3a3a"
  muted: "#4d4d4d"
  canvas: "#ffffff"
  fill: "#f6f6f6"
  fill-strong: "#efefef"
  line: "#e6e6e6"
  inverse: "#ffffff"
typography:
  display:
    fontFamily: "Figtree, Segoe UI, sans-serif"
    fontSize: "clamp(2.15rem, 1.15rem + 2.6vw, 3.55rem)"
    fontWeight: 680
    lineHeight: 1.08
    letterSpacing: "-0.03em"
  body:
    fontFamily: "Figtree, Segoe UI, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 450
    lineHeight: 1.6
    letterSpacing: "0em"
  mono:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "0.9em"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
rounded:
  sm: "6px"
  md: "8px"
  lg: "12px"
spacing:
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "48px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.inverse}"
    rounded: "{rounded.sm}"
    padding: "9px 16px"
  button-primary-hover:
    backgroundColor: "#2a2a2a"
    textColor: "{colors.inverse}"
    rounded: "{rounded.sm}"
    padding: "9px 16px"
  button-secondary:
    backgroundColor: "{colors.fill}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "9px 16px"
---

## Overview

This file records the `/business/` preview only. `index.html` and the shared header keep their existing look. Do not restyle the public site from these tokens.

The preview is a light, quiet marketing page. Figtree does both headings and body. The constellation mark is the only chromatic element. Product screenshots sit in a gray stage so the first screen shows the actual decision UI.

## Colors

White canvas, charcoal text, gray fills and hairlines. No rust, red, beige, or tan. Links are charcoal with an underline, not a second brand color.

## Typography

One sans, self-hosted. Display is heavy and tight. Body is 17px. The install command is the only monospace, and it uses the system face. Headlines use `text-wrap: balance`. There is no eyebrow above a heading.

## Layout

A single column, 68rem, with the same left edge for the header, the headline, and the screenshot stage. Space above a heading is larger than the space under it. The first viewport holds the headline, two actions, and the demo screenshot.

## Elevation & Depth

No drop shadows. Separation is a 1px line or a gray fill.

## Shapes

Buttons are 6px. The screenshot stage and the brief are 12px. The product image inside the stage is 8px.

## Components

Primary action is near-black. Secondary action is a gray fill. The header is solid white and sticky. Focus is a 2px charcoal outline.

## Do's and Don'ts

Do show a real Northwind Labs screenshot and say it is a scripted demo. Do keep available and planned offers distinct. Do not invent customers, metrics, or a signup. Do not copy Notion’s interface. Do not apply this system to the public homepage.
