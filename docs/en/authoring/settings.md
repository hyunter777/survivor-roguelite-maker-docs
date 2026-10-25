# Settings

GameSettingsAsset exposes Run and Simulation plus serializable defense/level-curve settings. Content.Settings supplies defaults; the bootstrap can assign separate ArenaSettings and FieldSettings. Do not accidentally measure one settings asset and play another.

Run covers shop prices, offers, choices, inventory policies, income settlement, conversions and save arena ids. Simulation covers fixed frequency, stat bindings, combat/player/spawn rules and weapon timing. Expose new values as settings or definition fields.

Authoring seconds and simulation ticks are not interchangeable. Use the inspector's unit display and SimSettings.Ticks in code. Stat ids come from the selected catalog/bindings. Validate finite ranges and remeasure after changing a formula or cap.

## Entry point and reference fields

**Entry point:** Assets/Create/Survivor Roguelite Maker/Game Settings

| Field / API | Purpose |
|---|---|
| `Run` | RunSettings |
| `Simulation` | SimSettings with formulas connected |
| `Defense / LevelCurve` | Configured built-in formula instances |
| `ArenaSettings / FieldSettings` | Optional per-mode overrides |
| `SaveArenaIds` | Stable ids in content order |

## Figure

![Screenshot slot: game-settings (capture pending).](../../assets/game-settings.svg)

Screenshot slot: game-settings (capture pending).

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Content](content.md) · [Characters](characters.md) · [Weapons](weapons.md)
