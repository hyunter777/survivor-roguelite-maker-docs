# Elites, bosses and hordes

Enemy assets expose scaled values with Base, Per Wave and Min. Inspector previews evaluate health/contact damage at waves 1, 5 and 10; verify the actual curve at your target progression. Movement selects chase, keep-distance or one of the wander/offset styles. Special attacks select none, shoot, charge or summon. Summons reference EnemyAsset objects.

Bosses can switch movement/attack definitions by phase. Configure Is Boss, ordered phases and phase thresholds together. Status immunity supports built-in enum values and custom behaviour ids. Burn ticks damage, Slow modifies speed, and Stun prevents movement/attacks/contact; one instance per status behaviour id uses the chosen refresh/stacking rules. Elite modifiers compose with these rules.

A wave contains ordered spawn groups and entries. Configure count/interval/delay, safety and placement settings, Elite Chance/Elite references, and timed Horde events. An arena can supply common groups reused by its waves. Add a boss spawn before enabling End On Boss Death.

Inspect a single wave in Horde Preview before tuning an entire arena in Run Pacing. Capacity/safety limits can make actual spawn counts differ from authored requests.

## Entry point and reference fields

**Entry point:** Assets/Create/Survivor Roguelite Maker/Content/Elite

| Field / API | Purpose |
|---|---|
| `Elite.Modifiers` | Swift, armored, regeneration and other modifiers |
| `IsBoss / Phases` | Phase thresholds/overrides |
| `Hordes` | Timed bursts with enemy/elite references |
| `EndOnBossDeath` | Requires an actual boss encounter |

## Figure

![Screenshot slot: boss-horde-inspector (capture pending).](../../assets/boss-horde-inspector.svg)

Screenshot slot: boss-horde-inspector (capture pending).

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Content](content.md) · [Characters](characters.md) · [Weapons](weapons.md)
