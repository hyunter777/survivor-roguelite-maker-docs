# Custom Weapon

## Goal

Install a custom weapon behaviour.

## Procedure

1. Include ExamplePulseWeapon from the behaviour guide.
2. Register example.pulse before waves start, using the bootstrap extension or your own host.
3. Set the WeaponAsset combat Behaviour to example.pulse and author its supported fields.
4. Assign a view entry and optional custom-event feedback.
5. Register equivalent rules in independent analysis hosts, then compare damage/events at a fixed seed.

## Verify

The custom Tick runs once per slot per tick; same-id registration overrides are intentional and case-sensitive.

## Entry point and reference fields

**Entry point:** Use the corresponding Content inspector and Tools/Survivor Roguelite Maker/ tools.

| Field / API | Purpose |
|---|---|
| `Behaviour` | example.pulse |
| `Range / BaseDamage` | Fields read by the example |
| `CooldownTicks` | Example cadence |

## Figure

![Concept diagram.](../../assets/behaviour-registry.svg)

Concept diagram.

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Weapon Evolution](weapon-evolution.md) · [Boss Wave](boss-wave.md) · [Status Weapon](status-weapon.md)
