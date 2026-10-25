# Field Mode

## Goal

Use Field mode in one scene.

## Procedure

1. Assign Content and an optional separate FieldSettings on the bootstrap.
2. Enable the mode selector or set Mode to Field.
3. Configure FieldWeaponChance, choice tiers and current weapon capacity.
4. Set FieldCarryHealth according to the intended wave transition.
5. Play through a mid-wave level-up and a wave boundary.

## Verify

The current wave pauses for choices and resumes; no Arena shop is inserted.

## Entry point and reference fields

**Entry point:** Use the corresponding Content inspector and Tools/Survivor Roguelite Maker/ tools.

| Field / API | Purpose |
|---|---|
| `Mode` | Field |
| `FieldCarryHealth` | Transition health |
| `FieldWeaponChance` | Weapon/upgrade category weight |

## Figure

![Product capture.](../../assets/demo-menu.png)

Product capture.

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Weapon Evolution](weapon-evolution.md) · [Boss Wave](boss-wave.md) · [Status Weapon](status-weapon.md)
