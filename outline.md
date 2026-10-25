# Survivor Roguelite Maker — documentation outline

English is the only published language for the first release. The source is arranged under `docs/en/`; additional locale folders can be enabled without changing the chapter model. This outline is completed before page authoring.

## Page contract

Every guide states its purpose, prerequisites, relevant Unity menu or code-only entry point, a field/API table, a practical workflow, validation checks, related pages and a figure slot. Code examples are complete types or explicitly identified fragments, and complete examples are compile-checked against the package. Screenshots use descriptive filenames, screen-specific captions and an asset manifest. API reference is generated from public symbols/XML documentation, with no implementation source published.

## 1. Introduction

| Page | Sections and coverage | Figure |
|---|---|---|
| `index.md` — Welcome | Product purpose; intended users; choose a learning path; build/test/customize loop; documentation navigation | `game-overview` |
| `introduction/features.md` — Feature overview | Runtime systems; authoring tools; analysis tools; extension points; single-player and platform boundaries | `feature-map` |
| `introduction/requirements.md` — Requirements | Unity target/development version; manifest dependencies; TMP resources; input; pipeline/material assumptions; project setup checks | `project-requirements` |

## 2. Installation and first session

| Page | Sections and coverage | Figure |
|---|---|---|
| `getting-started/installation.md` | Package installation; dependency resolution; input handling; TMP; updating safely; package vs project-owned files | `package-manager` |
| `getting-started/samples.md` | Import the sample once; actual sample display name; generated output and rebuild ownership; Build Demo; scene location; mode selection | `sample-import` |
| `getting-started/demo.md` — Five-minute demo | Install prerequisites; import/build/open; select character/weapon/mode; movement/pause; first wave/choice/shop; success checklist | `demo-menu` |
| `getting-started/first-game.md` — Ten-minute first game | New Game Project wizard; folder/sprites/settings; generated graph; first scene; add a weapon; validate and measure | `new-game-wizard` |

## 3. Core concepts

| Page | Sections and coverage | Figure |
|---|---|---|
| `concepts/architecture.md` | Core/Simulation/Run/Data/Presentation/Balance/Editor responsibilities; definitions vs state; allowed mutation boundaries | `architecture` |
| `concepts/ticks.md` | Fixed step; units; seconds/ticks; order/modules; event lifetime; frame interpolation | `tick-flow` |
| `concepts/definitions.md` | Asset conversion/cache; ids vs references; inventory instances; immutable definitions; updates and cache invalidation | `content-graph` |
| `concepts/run-loop.md` | Arena flow; Field interruptions; progression/settlement; phase/result validation; wave transition and health carry | `run-loop` |

## 4. Authoring guide

| Page | Sections and coverage | Figure |
|---|---|---|
| `authoring/content.md` | Content registry and every connected asset category; creation menus; stable ids; validation and graph completeness | `content-registry` |
| `authoring/characters.md` | Starting weapons/items; effects/triggers; restrictions/preferences; display/localization fields; availability | `character-inspector` |
| `authoring/weapons.md` | Shared weapon fields; ranged/melee/orbit/aura; damage/crit/scaling; targeting; homing; hit effects; custom behaviour id/parameters | `weapon-inspector` |
| `authoring/weapon-tiers.md` | Tier ids/families; NextTier chain; next-tier creation; merge/replacement/full-slot rules; cycle validation | `weapon-tier-chain` |
| `authoring/items-sets.md` | Items vs upgrades; instance/lifetime; max owned; set membership/count/order/highest threshold; capture timing | `item-set-inspector` |
| `authoring/stats-effects.md` | Stat catalog/bindings; Add/Set/list operations; Link/Convert/Limit; source keys/read layers; efficiency; rounding/transforms; expiry and diagnostics | `effect-inspector` |
| `authoring/triggers.md` | Legacy/explicit rules; events/conditions/counters; maintained conditions; filters; reactions/cooldowns; custom handlers and action-specific field rules | `trigger-inspector` |
| `authoring/offers.md` | Channels; tiers/progress/luck; tags/weights; character bans; slots/families; guarantees; banish; authoring switches and eligibility | `offer-settings` |
| `authoring/enemies.md` | Scaled fields; movement kinds; shoot/charge/summon; body/contact damage; status immunities; references and previews | `enemy-inspector` |
| `authoring/elites-bosses-hordes.md` | Elite modifiers; phases and movement/attack overrides; summon references; horde timing/shape; boss ending prerequisites | `boss-horde-inspector` |
| `authoring/waves-arenas.md` | Wave duration/capacity; spawn groups/entries; delays/common groups; elite chances; arena dimensions; schedule vs actual spawns | `wave-editor` |
| `authoring/progression.md` | Unlock targets/conditions; stable target ids; availability; records/profile application; cheated run exclusion | `unlock-settings` |
| `authoring/settings.md` | Run/simulation settings; formulas/bindings; per-mode overrides; timing/limits; validation; versioned balance changes | `game-settings` |

## 5. Maker tools

| Page | Sections and coverage | Figure |
|---|---|---|
| `tools/index.md` | Pick a tool by question; snapshot-based analysis; common Content/Settings inputs; cancellation and stale results | `tools-menu` |
| `tools/content-browser.md` | Graph selection; categories/search; validation messages; linked asset navigation; corrective workflow | `content-browser` |
| `tools/wave-editor.md` | Timeline/schedule editing; expected counts; group/entry controls; Undo; preview links | `wave-editor` |
| `tools/balance-simulator.md` | Bot/seed/runs; run metrics; interpretation and reproducibility; full-run vs fixed-build experiments | `balance-simulator` |
| `tools/run-pacing.md` | Inputs/jobs; threat/power/survival/economy; entered-run denominators; wave editing/re-run; Field wave axis | `run-pacing` |
| `tools/build-lab.md` | Build selection; contribution layers; sets/tags/links; DPS; trial repetitions; comparisons/presets; custom attribution limits | `build-lab` |
| `tools/horde-preview.md` | Record/scrub; frame interval; counts/density; schematic vs game view; repeatability and memory | `horde-preview` |
| `tools/weapon-lab.md` | Weapon/tier/stat sliders; dummy layout; visual preview; measurement/density curve; estimates vs measurements | `weapon-lab` |
| `tools/offer-odds.md` | Channel/mode/progress/luck; seeded paths; guarantee/policy comparison; chance and conditional first-seen; cancellation/denominators | `offer-odds` |
| `tools/content-table.md` | Filtering/sorting; supported fields; multi-edit/Undo; CSV export/import preview; schema/id/conflict validation | `content-table` |
| `tools/wizards-validation.md` | New Game Project/Create Game Scene; templates; UI prefab generation; next-tier tool; validation checklist | `scene-wizard` |

## 6. Presentation

| Page | Sections and coverage | Figure |
|---|---|---|
| `presentation/bootstrap.md` | Scene bootstrap references/lifecycle; missing-part creation; settings/mode/seed; input/camera/session; extension boundary | `bootstrap-inspector` |
| `presentation/catalogs.md` | Definition ids; prefab/sprite/icon fallback; player and projectile entries; pooling/interpolation; character visual adapter | `view-catalog` |
| `presentation/ui-localization.md` | UI prefabs/themes; content text and keys; localized text provider; options/accessibility; custom input focus | `ui-localization` |
| `presentation/feedback-audio.md` | Damage/crit/death/shake; custom event VFX; sound cues/buses/cooldowns/concurrency; music contexts; user options | `feedback-audio` |

## 7. Playtesting

| Page | Sections and coverage | Figure |
|---|---|---|
| `playtesting/panel.md` | F2/setup; every command and phase restrictions; speed/hold/step; cheated-run flag; release stripping | `playtest-panel` |
| `playtesting/metrics.md` | F3 DPS meter; rolling window/weapon attribution; damage share/taken sources; run summary/level timing; interpretation | `run-summary` |

## 8. Saves and options

| Page | Sections and coverage | Figure |
|---|---|---|
| `saves/continue.md` | Between-wave boundary; snapshot contents; stable ids/arena mapping; memory/file adapters; single slot and errors | `save-continue` |
| `saves/options-migrations.md` | Options/profile/run domains; file handling; envelope/payload versions; migrations; custom payload validation; reset behaviour | `options-menu` |

## 9. Extending

| Page | Sections and coverage | Figure |
|---|---|---|
| `extending/index.md` | Adapter selection; assembly references; project-owned code; example installation/compilation; determinism rules | `extension-map` |
| `extending/behaviours.md` | All registries/interfaces; registration/override; empty id compatibility; instance state/parameters; custom weapon example | `behaviour-registry` |
| `extending/modules-events.md` | Six module boundaries; Begin/state; custom event values/lifetime; view/sound registration and read-only consumption | `module-event-flow` |
| `extending/effect-trigger-handlers.md` | Effect Apply/Undo; persistence codec; combat/run trigger registries; authored rules and registration; complete examples | `handler-flow` |
| `extending/bootstrap-systems.md` | Bootstrap extension lifecycle; system replacement; input/text/visual adapters; controller creation boundary; direct host factory | `bootstrap-extension` |
| `extending/save-hooks.md` | Saveable application state; payload versions; migration/storage interfaces; restore validation; no global/random state | `save-hook-flow` |

## 10. Performance and determinism

| Page | Sections and coverage | Figure |
|---|---|---|
| `quality/determinism.md` | Seeds/inputs/content/platform; generator ownership; order; analysis metadata; replay/continue boundaries | `determinism-checklist` |
| `quality/performance.md` | Published benchmark/environment/table; grid vs linear; pool ownership; allocation scopes; profiling recommendations | `performance-table` |

## 11. Recipes

Each recipe has prerequisites, concrete steps, field values/API references, a success check and common failure cases.

| Page | Sections and coverage | Figure |
|---|---|---|
| `recipes/weapon-evolution.md` | Create a tier chain; register tiers; configure merge and eligibility; test at full slots | `weapon-tier-chain` |
| `recipes/boss-wave.md` | Author phases; schedule a boss; end-on-boss-death; horde timing; preview and trial | `boss-horde-inspector` |
| `recipes/status-weapon.md` | Add a slow/burn/stun on-hit entry; probability/stacking/immunity; verify status events | `effect-inspector` |
| `recipes/custom-weapon.md` | Install custom behaviour; author id/parameters; configure bootstrap/analysis; verify damage/events | `behaviour-registry` |
| `recipes/custom-pickup.md` | Implement IPickupBehaviour; register/spawn; accepted/rejected collection; settlement option; custom view id | `custom-pickup` |
| `recipes/localized-ui.md` | Keep ids stable; add text keys/provider; assign bootstrap text; select language/fallback; check UI | `ui-localization` |
| `recipes/field-mode.md` | Mode-specific settings; Field choices/health carry; no shop; full-slot eligibility; same-scene testing | `demo-menu` |
| `recipes/saved-effect.md` | Author Handler id; install codec; save at boundary; restore/Undo; malformed payload rejection | `save-hook-flow` |

## 12. Reference and help

| Page | Sections and coverage | Figure |
|---|---|---|
| `reference/api.md` | Public namespace guide; generated API link at /api/; version/build provenance; source not redistributed | `api-reference` |
| `help/troubleshooting.md` | Setup diagnosis by symptom; missing UI/input/art; offers/effects/triggers; saves; determinism; minimal repro checklist | `validation-issues` |
| `help/faq.md` | Scope/platform/multiplayer; data ownership; custom rigs; estimates vs measurements; development overlays | `faq-checklist` |
| `release-notes.md` | Versioned user-facing changes; compatibility notes; upgrade/identity cautions | `release-notes` |
| `support-license.md` | Support details and reproducible reports; package vs docs licenses; bundled-content notices; privacy boundaries | `support-checklist` |

## Figure and screenshot plan

Use existing product captures when they match the described release UI. Required captures: package/sample import, main menu and gameplay, both wizards, content registry and each major inspector, all maker-tool windows, bootstrap/view/audio catalogs, localization/options, playtest/DPS/result screens, save/continue and validation issues. Required diagrams: architecture, tick/run flow, content identity, registry/module/event flow and save codec flow. Reuse one verified figure on related recipes instead of inventing new UI captures. The implementation manifest is `screenshots-needed.md`; actual images live under `docs/assets/`.

## Delivery checks

- Strict MkDocs build with no warnings, valid links and search/theme/navigation enabled.
- DocFX public API metadata and output at `/api/`, generated by a reproducible local-source script and built in CI without product source.
- Compile complete C# examples against the package; review all menus/fields/defaults against code.
- Publish the documentation-only repository and GitHub Pages through Actions; verify the public root, English guides and API endpoint.
- Keep package cleanup as a separate integration request; no package edits belong to this documentation repository.
