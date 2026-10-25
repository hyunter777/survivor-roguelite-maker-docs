# Save Hooks

Set Effect.Handler to your registered id. A handler must return an `AppliedEffect` containing itself and enough state to undo the actual contribution. Do not mutate shared Effect definitions. Implement IEffectStatePersistence for saveable applications.

This additive example is intentionally small so its capture/restore/undo contract is visible:

```csharp
using System;
using System.Globalization;
using SurvivorsMaker.Core;
using SurvivorsMaker.Simulation;

namespace MakerManualExamples
{
    public sealed class ExampleSavedEffect : IEffectStatePersistence
    {
        AppliedEffect Add(Effect effect, EffectStore store, int value)
        {
            store.Values[effect.Target] = store.Get(effect.Target) + value;
            store.Touch();
            return new AppliedEffect(effect, true, handler: this, state: value);
        }
        public AppliedEffect Apply(Effect effect, EffectStore store) => Add(effect, store, effect.Amount);
        public void Undo(AppliedEffect applied, EffectStore store)
        {
            store.Values[applied.Effect.Target] = store.Get(applied.Effect.Target) - (int)applied.State;
            store.Touch();
        }
        public string Capture(AppliedEffect applied) => ((int)applied.State).ToString(CultureInfo.InvariantCulture);
        public AppliedEffect Restore(Effect effect, EffectStore store, string payload)
        {
            if (!int.TryParse(payload, NumberStyles.Integer, CultureInfo.InvariantCulture, out var value))
                throw new ArgumentException("Invalid example effect payload.");
            return Add(effect, store, value);
        }
    }
}
```

Validate handler ranges, payload versions and arithmetic. Restore must apply the saved contribution to the supplied Store and return an Undo record for the supplied Effect. Capture/Restore must not use time, randomness or mutable handler-global state. Call Store.Touch after writes. Read handler contributions in the Store residual returned by StatBuild.Explain.

SaveEnvelope records a Domain and SchemaVersion; its payload also has a Version. These are different version layers. `SaveMigrationRegistry.CreateDefault(legacyArenaIds)` includes the supported legacy-to-current paths. A future schema is not rewritten as the current one. Register explicit ISaveMigration steps when extending your own transport/schema, and validate the resulting payload before swapping the active run.

Custom effect handlers need IEffectStatePersistence. Capture returns a detached value payload; Restore reapplies it to a supplied store and returns an Undo record. Implement the codec before saving an application. See the complete [effect handler example](index.md).

## Entry point and reference fields

**Entry point:** Code-only: use the API reference for the named types.

| Field / API | Purpose |
|---|---|
| `Capture` | Detached payload value |
| `Restore` | Apply saved contribution and return Undo record |
| `Store.Touch` | Invalidate values after deliberate writes |
| `ArgumentException` | Reject malformed payload |

## Figure

![Concept diagram.](../../assets/save-hook-flow.svg)

Concept diagram.

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Index](index.md) · [Behaviours](behaviours.md) · [Modules Events](modules-events.md)
