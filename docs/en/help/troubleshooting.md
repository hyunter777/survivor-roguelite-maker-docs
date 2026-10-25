# Troubleshooting

## The Tools menu is missing

Resolve Console compile errors first. Confirm that this package's Editor assembly is imported and dependencies resolved. The root is **Tools/Survivor Roguelite Maker/**. Install the complete package to add the editor windows.

## The game opens but there is no movement

Check Active Input Handling (Input System or Both), keyboard focus, the input component implementing IPlayerInput and the bootstrap's Input reference. Movement is intentionally stopped while the session is paused or a choice/shop phase blocks simulation. Check the Console before changing simulation values.

## Text is blank or the UI reports missing TMP resources

Import TMP Essential Resources, then confirm fonts on your theme/UI prefabs. The package depends on uGUI, which supplies the TMP API in this setup; assign the project resources and fonts. Regenerate UI in your own project folder only when you intend to replace the generated output.

## Entities appear as squares, or everything is silent

Placeholder rendering is the fallback for missing art/prefabs. Map the exact definition ids in ViewCatalogAsset and assign the catalog to the bootstrap. Projectile visuals have separate fields/keys. Empty sound cues are silent; assign clips and check option volumes and sound cooldown/concurrency.

## My new weapon is never offered

Check Content.Weapons, Available, channel policy, tier, character restrictions/bans, tag/family/kind limits, current slots and merge eligibility. Starting Weapons is a separate list. Guarantees select eligible candidates. Validate the whole content registry and inspect Offer Odds under the same character/mode/settings.

## A ranged weapon fires no projectile

Projectile speed must be positive. Check nearest-target range, cooldown, projectile count, source stat bindings and arena bounds. Nearest-target selection happens before the exact range test. Weapon Lab is useful for separating range problems from wave movement.

## My Link/Convert/Limit has no effect

Use a valid target/source key and positive Unit. Check Conversion Fraction for Convert, input/output ranges for Linear, the selected read layer and diagnostics for unknown sources/cycles. A captured limit keeps its original capture. Run Convert at an explicit conversion boundary. Enable extended authoring switches for rule fields where required.

## My trigger does not fire

Check the event/legacy When, Use Trigger Rules, conditions, counter threshold, cooldown, owner/death/neutral/reaction filters and handler registration. Use maintained conditions for temporary stats and event rules for counters and death filters. A run event handler and a combat event handler use different registries. Register controller trigger handlers before Create/StartWave; see [Extending](../extending/index.md).

## I edited an asset during a run and results did not update

Definitions are converted/cached and treated as immutable for that run. Stop and start a fresh run or measurement. Do not mutate shared definition objects to patch one player. Custom integrations that invalidate/rebuild the graph must also re-install graph-local handlers.

## Why can I not save while paused or at a Field level-up?

Save between waves, after the active world completes. Save at an eligible boundary and check CanSave/Save's result. See [Saves](../saves/continue.md) for codecs and stable arena ids.

## A custom effect plays correctly but saving is rejected

Implement IEffectStatePersistence, register the same handler id before restoring and validate its payload. Capture a value payload for each saved application. Restore must return an applied Undo record for the supplied definition and store.

## The same seed gives different results

Compare content/settings versions, actual seed, per-tick input and run choices. A zero session seed chooses a new seed. Custom randomness, unordered processing or a handler-global counter can also break repeatability. Use the same platform and floating-point environment for exact replay comparisons. See [Determinism & Performance](../quality/determinism.md).

## Why do expected DPS, Weapon Lab and live DPS differ?

They use different models/scenarios. Reach, density, target movement/health, measurement length, status/secondary effects and damage attribution matter. Compare identical scenarios and inspect actual hit counts.

## The Playtest panel is missing from a player build

It is intentionally development/editor-only and can also be disabled by SURVIVORS_MAKER_NO_PLAYTEST or DevToolsOptions. The live DPS meter is separately configurable. See [Playtest](../playtesting/panel.md).

## Are multiplayer, a custom art rig or another input device supported automatically?

The shipped flow is single-player. Use ICharacterVisual for custom art rigs and IPlayerInput for new input schemes.

## Custom code and support

Use your own Assets folder/asmdef and register adapters rather than editing package code. Send reproducible steps, Console output, Unity/package versions, seed and a minimal content/settings example to **hyunter@flycat.co.kr**. Exclude private account data and unrelated project files.

## Entry point and reference fields

**Entry point:** Code-only: use the API reference for the named types.

| Field / API | Purpose |
|---|---|
| `Console` | Fix compilation/dependency errors first |
| `Content.Validate` | Validate the connected registry |
| `Seed/settings/input` | Include in a minimal reproduction |

## Figure

![Screenshot slot: validation-issues (capture pending).](../../assets/validation-issues.svg)

Screenshot slot: validation-issues (capture pending).

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [API](../reference/api.md) · [FAQ](faq.md) · [Release Notes](../release-notes.md)
