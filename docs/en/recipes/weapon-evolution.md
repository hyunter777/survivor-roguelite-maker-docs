# Weapon Evolution

## Goal

Build a tier-chain weapon.

## Procedure

1. Create a first-tier WeaponAsset and give it a unique id and Family.
2. Use the next-tier tool to create/link successive tiers; review proposed price and scaling.
3. Register the chain in Content.Weapons and choose starting roots on the character.
4. Configure WeaponSlots and MergeOnFullSlots for your acquisition design.
5. Test two equal copies, a next-tier replacement and terminal-tier/full-slot rejection.

## Verify

The resulting acquisition must either succeed by the documented rules or be absent from offers; it must not trap a choice window.

## Entry point and reference fields

**Entry point:** Use the corresponding Content inspector and Tools/Survivor Roguelite Maker/ tools.

| Field / API | Purpose |
|---|---|
| `NextTier` | Successor definition |
| `Family` | Consistent grouping |
| `MergeOnFullSlots` | Full-capacity policy |

## Figure

![Screenshot slot: weapon-tier-chain (capture pending).](../../assets/weapon-tier-chain.svg)

Screenshot slot: weapon-tier-chain (capture pending).

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Boss Wave](boss-wave.md) · [Status Weapon](status-weapon.md) · [Custom Weapon](custom-weapon.md)
