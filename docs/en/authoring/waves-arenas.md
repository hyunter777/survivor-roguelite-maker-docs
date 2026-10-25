# Waves Arenas

Enemy assets expose scaled values with Base, Per Wave and Min. Inspector previews evaluate health/contact damage at waves 1, 5 and 10; verify the actual curve at your target progression. Movement selects chase, keep-distance or one of the wander/offset styles. Special attacks select none, shoot, charge or summon. Summons reference EnemyAsset objects, not copied embedded enemy definitions.

Bosses can switch movement/attack definitions by phase. Configure Is Boss, ordered phases and phase thresholds together. Status immunity supports built-in enum values and custom behaviour ids. Burn ticks damage, Slow modifies speed, and Stun prevents movement/attacks/contact; one instance per status behaviour id uses the chosen refresh/stacking rules. Elite modifiers compose with these rules.

A wave contains ordered spawn groups and entries. Configure count/interval/delay, safety and placement settings, Elite Chance/Elite references, and timed Horde events. An arena can supply common groups reused by its waves. End On Boss Death requires the boss encounter to occur; do not use it as a substitute for authoring a boss spawn.

Inspect a single wave in Horde Preview before tuning an entire arena in Run Pacing. Capacity/safety limits can make actual spawn counts differ from authored requests.

## Entry point and reference fields

**Entry point:** Tools/Survivor Roguelite Maker/Wave Editor

| Field / API | Purpose |
|---|---|
| `DurationSeconds / MaxAlive` | Wave duration/capacity |
| `Groups / Entries` | Ordered schedule |
| `EliteChance / Elite` | Per-entry elite selection |
| `Arena.Width / Height` | World dimensions |
| `CommonGroups` | Reusable arena schedule groups |

## Figure

![Screenshot slot: wave-editor (capture pending).](../../assets/wave-editor.svg)

Screenshot slot: wave-editor (capture pending).

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Content](content.md) · [Characters](characters.md) · [Weapons](weapons.md)
