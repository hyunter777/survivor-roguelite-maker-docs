# Characters

Create a CharacterAsset and add it to Content.Characters. Set a stable Id and readable DisplayName/Description; localize with TextKey rather than changing identity.

StartingWeapons is a menu of allowed starting choices; RunRequest.StartingWeapon selects one. StartingItems is applied once at creation in list order. Effects and triggers come from the character before item effects. MeleeAllowed/RangedAllowed and pool preferences/bans restrict subsequent acquisition.

Enable UseTriggerRules or UsePoolConstraints when relying on their extended fields. Preferred tags supply offer-policy weights. Validate and start a fresh run after changing the definition graph.

## Entry point and reference fields

**Entry point:** Assets/Create/Survivor Roguelite Maker/Content/Character

| Field / API | Purpose |
|---|---|
| `StartingWeapons` | Starting weapon choices |
| `StartingItems` | Ordered initial items |
| `Effects / Triggers` | Character rules |
| `PreferredTags / BannedTags` | Offer policy |
| `UsePoolConstraints` | Opt into authored constraints |

## Figure

![Screenshot slot: character-inspector (capture pending).](../../assets/character-inspector.svg)

Screenshot slot: character-inspector (capture pending).

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Content](content.md) · [Weapons](weapons.md) · [Weapon Tiers](weapon-tiers.md)
