# Custom Pickup

Create a registered pickup that heals the primary player using its authored pickup value. This example consumes the pickup even when health is already full; change that acceptance policy deliberately if your design differs.

```csharp
using System;
using SurvivorsMaker.Simulation;
namespace MakerManualExamples
{
    public sealed class ExampleRepairPickup : IPickupBehaviour
    {
        public void Collect(SimWorld world, PlayerState player, Pickup pickup)
        {
            if (!ReferenceEquals(player, world.Player)) return;
            var healed = world.Combat.HealPlayer(world, Math.Max(0, pickup.Value));
            world.Emit(SimEventKind.HealCollected, pickup.Position, targetId: pickup.Id, amount: healed);
            pickup.Collected = true;
        }
    }
    public static class ExamplePickupRegistration
    {
        public static void Register(SimSystems systems) => systems.Behaviours.Pickups.Register("example.repair", new ExampleRepairPickup());
        public static Pickup Spawn(SimWorld world, Vec2 position, int amount) => world.SpawnPickup("example.repair", position, amount);
    }
}
```

Register before spawning; invalid ids are rejected before list/id mutation. Collection is accepted only when Collected becomes true. A rejected pickup remains available for a later collection attempt. Supply a matching custom pickup view entry and test it in range.

Implement IPickupSettlementBehaviour.Settle to collect custom pickups at wave end. Settlement uses the normal wallet/effect boundary. Do not return/remove a pickup from unrelated code while the pickup system owns collection.

## Entry point and reference fields

**Entry point:** Code-only: use the API reference for the named types.

| Field / API | Purpose |
|---|---|
| `IPickupBehaviour.Collect` | Collection callback |
| `Collected` | Acceptance flag |
| `IPickupSettlementBehaviour` | Optional leftover settlement |
| `SpawnPickup` | Registered id, fresh world id |

## Figure

![Screenshot slot: custom-pickup (capture pending).](../../assets/custom-pickup.svg)

Screenshot slot: custom-pickup (capture pending).

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Weapon Evolution](weapon-evolution.md) · [Boss Wave](boss-wave.md) · [Status Weapon](status-weapon.md)
