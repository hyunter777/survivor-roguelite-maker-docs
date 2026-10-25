# Bootstrap Systems

Place an `ISceneBootstrapExtension` component beside `SurvivorsSceneBootstrap`. Configure Systems runs before the game is configured; Scene Configured runs after the view/UI/catalog wiring. The latter can attach presentation handlers and register effects on the converted content graph before gameplay begins.

```csharp
using SurvivorsMaker.Core;
using SurvivorsMaker.Presentation;
using SurvivorsMaker.Run;
using UnityEngine;

namespace MakerManualExamples
{
    public sealed class ExampleSceneExtension : MonoBehaviour, ISceneBootstrapExtension
    {
        [Min(1)] public int TelemetryTicks = 60;
        public SpriteRenderer PulseMarker;

        public void ConfigureSystems(RunSystems systems)
        {
            systems.Simulation.Behaviours.Weapons.Register("example.pulse", new ExamplePulseWeapon());
            systems.Simulation.Modules.Add(new ExampleTelemetryModule(TelemetryTicks));
        }
        public void SceneConfigured(SurvivorsSceneBootstrap bootstrap)
        {
            var definitions = bootstrap.Content.BuildRunContent();
            if (definitions.EffectHandlers == null) definitions.EffectHandlers = new EffectHandlers();
            definitions.EffectHandlers.Register("example.saved", new ExampleSavedEffect());
            bootstrap.View.RegisterCustomEvent("example.pulse", new ExamplePulseView(PulseMarker));
        }
    }
}
```

```csharp
using SurvivorsMaker.Presentation;
using SurvivorsMaker.Simulation;
using UnityEngine;

namespace MakerManualExamples
{
    public sealed class ExamplePulseView : ICustomEventView
    {
        readonly SpriteRenderer _marker;
        public ExamplePulseView(SpriteRenderer marker) { _marker = marker; }
        public void Show(SimEvent value, SimWorld world, WorldView view)
        {
            if (_marker != null)
                _marker.transform.position = new Vector3(value.Position.X, value.Position.Y, _marker.transform.position.z);
        }
    }
}
```

The marker moves a pre-existing sprite. Use a presentation pool for transient effects. You can also configure custom event effects in Presentation Settings and sound mappings in the sound catalog. `CustomEventRaised` exposes copied event values to listeners. Views must not damage enemies, consume gameplay randomness or mutate the world.

Register systems and views through ISceneBootstrapExtension. For controller trigger registries, use the direct-controller factory before Create/StartWave. Repeat registration for each newly created controller.

Start with `RunSystems.CreateDefault()` and replace one interface implementation on it or its Simulation object. Configure this before creating a run/wave. Keep required systems non-null; the controller checks them. Preserve event, id, pool-return and phase contracts if replacing `ICombat`, `IWeaponSystem`, `IEnemySystem`, `ISpawnSystem` or other core rules. Implement `IWaveView` for additional renderers/telemetry and register with `SurvivorsGame.RegisterView`.

Stat formulas (`IDefenseFormula`, `ILevelCurve`), input (`IPlayerInput`), storage interfaces and text (`ITextProvider`) have narrower adapters when you only need those changes. Configure the behaviour registry in both your scene and your analysis host.

## Entry point and reference fields

**Entry point:** Code-only: use the API reference for the named types.

| Field / API | Purpose |
|---|---|
| `ConfigureSystems` | Before session configuration |
| `SceneConfigured` | After view/UI wiring, before a controller exists |
| `RunController` | Register trigger handlers before its first wave |

## Figure

![Concept diagram.](../../assets/bootstrap-extension.svg)

Concept diagram.

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Index](index.md) · [Behaviours](behaviours.md) · [Modules Events](modules-events.md)
