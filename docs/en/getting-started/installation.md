# Installation

=== "Purchased package"
    Import the package through your Unity purchase workflow, then wait for dependency resolution and script compilation.

=== "Local UPM package"
    Open Package Manager, choose **Add package from disk**, and select the package's `package.json`.

1. Import/install the purchased package in your Unity 6 project. If using a local UPM copy, add its package.json through Package Manager; keep the package folder intact.
2. Let dependencies resolve and fix Console compile errors before opening maker windows.
3. Enable Input System or Both in Active Input Handling; restart if requested.
4. Import TMP Essential Resources if they are absent.
5. Keep generated content and custom code in your own Assets folder. Back up content and saves before updating the package.

Package code, a sample's authoring source, and a sample's generated assets have different ownership. The builder regenerates its output. Duplicate content into your own game folder for permanent work.

## Entry point and reference fields

**Entry point:** Window > Package Manager

| Field / API | Purpose |
|---|---|
| `package.json` | Package entry point for a local UPM install |
| `Active Input Handling` | Input System or Both |
| `Assets folder` | Project-owned content and custom adapters |

## Figure

![Screenshot slot: package-manager (capture pending).](../../assets/package-manager.svg)

Screenshot slot: package-manager (capture pending).

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Samples](samples.md) · [Five-minute demo](demo.md) · [Ten-minute first game](first-game.md)
