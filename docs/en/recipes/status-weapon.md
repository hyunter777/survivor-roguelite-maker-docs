# Status Weapon

## Goal

Add status on hit.

## Procedure

1. Start with a working weapon and append an ApplyStatus entry to OnHit.
2. Select a built-in status or registered Behaviour id.
3. Set Chance, DurationSeconds, TickSeconds/Magnitude and stacking limits.
4. Check the target enemy immunity lists and elite modifiers.
5. Compare hit and status events, including stacked burn damage timing.

## Verify

An immune target must remain unaffected; a valid application emits StatusApplied with the behaviour id.

## Entry point and reference fields

**Entry point:** Use the corresponding Content inspector and Tools/Survivor Roguelite Maker/ tools.

| Field / API | Purpose |
|---|---|
| `OnHit` | Ordered proc list |
| `Stacking / MaxStacks` | Refresh/stack policy |
| `StatusImmunityIds` | Custom-id immunity |

## Figure

![Screenshot slot: effect-inspector (capture pending).](../../assets/effect-inspector.svg)

Screenshot slot: effect-inspector (capture pending).

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Weapon Evolution](weapon-evolution.md) · [Boss Wave](boss-wave.md) · [Custom Weapon](custom-weapon.md)
