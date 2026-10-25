# Ui Localization

GameUiRoot connects menu, HUD, choices, shop, pause/options and results. Generate editable prefabs, assign their references and theme, and retain controller/session actions as the mutation boundary.

Content DisplayName/Description are readable defaults. TextKey and LocalizedTextAsset/ITextProvider supply translations without changing save ids. Assign bootstrap.Text and test missing-key fallback as well as a translated language. User language and accessibility are options, separate from authored theme data.

Route focused text input to the UI and suppress movement in your input adapter while typing. Test navigation and readable contrast in both editor and player.

## Entry point and reference fields

**Entry point:** Tools/Survivor Roguelite Maker/Build UI Prefabs

| Field / API | Purpose |
|---|---|
| `GameUiRoot` | Screen/session binding |
| `UiTheme` | Layout/color/font settings |
| `TextKey` | Stable translation lookup |
| `LocalizedTextAsset` | Bootstrap text provider |
| `OptionsState.Language` | User language selection |

## Figure

![Screenshot slot: ui-localization (capture pending).](../../assets/ui-localization.svg)

Screenshot slot: ui-localization (capture pending).

## Check your result

Validate connected content before starting a new measurement or run. Keep the settings, seed and content version with any result you compare. For code-only adapters, compile against the package version you ship and configure the required authored data before gameplay.

[Documentation home](../index.md) · [Bootstrap](bootstrap.md) · [Catalogs](catalogs.md) · [Feedback Audio](feedback-audio.md)
