# Progression

ContentAsset.Unlocks converts UnlockDef entries for characters, weapons or items. Conditions include a win with a character, reaching a wave, accumulated kills/wins and wins in a mode. Set a unique unlock id and a valid target id. ProgressionRules applies profile unlocks before menu selection and records a finished non-cheated run once.

Use the profile/configuration path to obtain availability rather than mutating shared content globally from a UI callback. Playtest commands mark cheated runs so they do not award normal progression. Build Lab and other headless experiments are isolated experiments, not profile writes.

## Entry point and reference fields

**Entry point:** Assets/Create/Survivor Roguelite Maker/Content/Content

| Field / API | Purpose |
|---|---|
| `UnlockDef.Id` | Unique rule identity |
| `Target / TargetId` | Character, weapon or item id |
| `Condition / Param / Value` | Unlock criterion |
| `Available` | Applied before menu/offer use |

## Figure

![Screenshot slot: unlock-settings (capture pending).](../../assets/unlock-settings.svg)

Screenshot slot: unlock-settings (capture pending).

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Content](content.md) · [Characters](characters.md) · [Weapons](weapons.md)
