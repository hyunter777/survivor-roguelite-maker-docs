# Survivor Roguelite Maker documentation

[Read the manual](https://hyunter777.github.io/survivor-roguelite-maker-docs/) · [Public API](https://hyunter777.github.io/survivor-roguelite-maker-docs/api/)

English user guides, recipes, product captures and public API reference for Survivor Roguelite Maker.

## Build

Use Python 3.12, .NET 8 and DocFX 2.81.0.

```sh
python -m pip install --user -r requirements.txt
dotnet tool install --global docfx --version 2.81.0
python scripts/build.py
```

Preview the manual with `python -m mkdocs serve`. The combined build writes the manual to `site/` and the API reference to `site/api/`. GitHub Actions builds and deploys the same artifact.

## Refresh public API metadata

Use an installed package, Unity managed reference assemblies and an imported project's UI/TMP/Input System assemblies. Pass their local folders explicitly:

```sh
python scripts/generate_api.py --package-root <package-folder> --unity-managed <editor-managed-folder> --script-assemblies <project-script-assemblies>
python scripts/check_examples.py --unity-managed <editor-managed-folder>
python scripts/build.py
```

Commit the sanitized `api-metadata/` output and the guide changes. Assembly binaries and local build projects stay in the ignored `.build/` folder. The public Actions build reads committed metadata.

## Add a language

English pages live in `docs/en/`. Add translated folders such as `docs/ko/`, `docs/ja/` or `docs/zh/`, then add their locale entries to the i18n plugin in `mkdocs.yml`. English is the default root locale. Translate navigation through locale-specific nav translations.

## Contribute

Follow `outline.md` and `screenshots-needed.md`. Use direct instructions and factual present-tense sentences. Keep menu paths, field names and examples aligned with the package. Send documentation corrections through issues or pull requests.

Documentation copyright © FlyCat. The purchased package carries its own distribution license. Example snippets are available for use with the product in your projects. Support: hyunter@flycat.co.kr.
