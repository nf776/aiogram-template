from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader


def get_fluent_localization() -> FluentLocalization:
    locales_dir = Path(__file__).parent.joinpath("locales")
    l10n_loader = FluentResourceLoader(str(locales_dir) + "/{locale}")
    return FluentLocalization(
        ["ru"],
        [
            "strings.ftl", 
            "sender.ftl"
        ], 
        l10n_loader
    )
