# Stats Effects

For Add/Set/Link/Limit/Convert, Target is a stat id. The inspector offers the selected content's stat catalog; a valid id outside that catalog remains editable. List operations use free-form entry ids with a List key. A nonempty Handler selects a registered custom effect implementation.

| Method | Meaning |
|---|---|
| Add | Add Amount within the selected permanent/temporary fold |
| Set | Replace the preceding scalar fold in that layer |
| Tally | Accumulate a keyed value in a named list |
| Append | Append a key/value entry; duplicates are retained |
| AppendUnique | Keep an id while at least one provider remains |
| Link | Read Source, divide by Unit, multiply by Amount, then transform/round/clamp output |
| Convert | Explicitly consume a source budget and create output at a boundary |
| Limit | Set a fixed, captured or following minimum/maximum |

Evaluated methods require valid explicit values. In particular, Unit must be positive; Convert also needs a valid Conversion Fraction. With Linear enabled, the input interval starts at Input Min + Buffer and maps to the output interval, with optional inversion. Whole Bundles truncates the number of complete units; other rounding modes apply their specified output rounding.

For internal stat sources, Read Layer selects Permanent, With Temporary or Final. External Source uses a case-sensitive adapter key instead. Common run keys include `currency`, `items`, `weapons`, `free_weapon_slots`, `item:<id>`, `weapon_family:<family>`, `weapon_kind:<enum name>` and `set:<id>`. Unique/duplicate and tier queries also exist on `RunStatSource`. Combat adds its own sources through `SimStatSource`; use the supported key list in that adapter when adding a new dependency.

Do not treat a Build Lab provider label such as `character:<id>` or `grant:<id>` as an external source query. Provider identity and a Link's Input Source are separate fields.

Lifetime Waves expires relative to acquisition/start wave; zero disables wave expiry. Lifetime Ticks advances only during combat. Wave-scoped timed effects restart for a new wave, while Run-scoped ones retain remaining ticks. Temporary controls the evaluation layer; lifetime controls removal. A captured limit keeps its saved capture, even if its source later changes.

## Entry point and reference fields

**Entry point:** Assets/Create/Survivor Roguelite Maker/Stat Catalog

| Field / API | Purpose |
|---|---|
| `Target` | Stat id or list-entry id |
| `Source / ExternalSource` | Stat dependency or external key |
| `ReadLayer` | Permanent / WithTemporary / Final |
| `Unit / Rounding` | Bundle size and output rules |
| `LimitMode` | Fixed / Captured / Following |
| `LifetimeWaves / LifetimeTicks` | Expiry boundaries |

## Figure

![Screenshot slot: effect-inspector (capture pending).](../../assets/effect-inspector.svg)

Screenshot slot: effect-inspector (capture pending).

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Content](content.md) · [Characters](characters.md) · [Weapons](weapons.md)
