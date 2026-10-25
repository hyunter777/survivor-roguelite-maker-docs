"""Use direct, present-tense wording in the public API reference."""
import re

REPLACEMENTS = {
    'which cannot reference UnityEngine': 'with engine-independent arithmetic',
    'living enemies that may be within': 'living enemy candidates near',
    'the asset is created and should be assigned': 'create the asset and assign it',
    'Built-in events may set it for detail': 'Built-in events use it for detail',
    'Returns how many matched in total (may exceed what was written).': 'Returns the total match count, including matches beyond the output capacity.',
    'Custom/store contributions are an unattributed net residual:\narbitrary handler state cannot safely be replayed to discover per-provider amounts.': 'Custom/store contributions use the net Store residual.',
    'Extra enemies a projectile may hit after the first.': 'Extra enemies a projectile hits after the first.',
    'Results are candidates (they may lie a little outside the radius;\ncallers keep their exact tests)': 'Results include candidates outside the radius; apply exact distance and shape tests. Candidates appear',
    'A type may expose a static Default/Instance property or a public parameterless constructor.': 'Use a type with a static Default/Instance property or a public parameterless constructor.',
    'How often this guarantee may reserve slots': 'How often this guarantee reserves slots',
    'this group may appear in': 'for this group',
    'Capacity may grow during play.': 'Capacity grows during play as needed.',
    'overrides should retain this invalidation.': 'Retain this invalidation in overrides.',
    'May also be driven by a host.': 'A host can also drive this component.',
    "Melee targets may be this much farther than the weapon's reach.": "Additional distance allowed for melee targets beyond the weapon's reach.",
    'Null when the run is in a phase that cannot be saved (a wave is running, or it ended).': 'Returns a snapshot between waves; returns null during an active wave or after the run ends.',
    '(may be null)': '(optional)',
    'one that cannot be read at all': 'an unreadable file',
    'weapons that cannot currently fit': 'weapons beyond the active slot capacity',
    'Optional prefab; may carry an': 'Optional prefab with an optional',
    'Plain description. May be empty.': 'Optional plain description.',
    'so obsolete requests cannot flood the worker pool.': 'to keep obsolete requests out of the worker pool.',
    'Problems an author should fix': 'Authoring errors',
    'A run whose arena cannot be mapped stays in the backup only.': 'The backup preserves runs with an unmapped arena.',
    '0 = off (enemies may stack).': '0 = off, allowing enemies to stack.',
    'Reset by default so unknown growth counters cannot pay historical thresholds again.': 'Resets unknown growth counters by default and starts threshold tracking from zero.',
    'Rules for an effect the built-in methods cannot express': 'Rules for a custom effect',
    'Scope in which a guarantee may be consumed': 'Scope in which a guarantee is consumed',
    'wind-up may start only when': 'wind-up starts when',
    '(custom statuses; built-ins may be listed here too)': '(accepts custom and built-in status ids)',
    'only the listed channels may offer it.': 'only the listed channels offer it.',
    'both may be null.': 'both parameters are optional.',
    'Either may be empty.': 'Both descriptions are optional.',
    'True when the panel may run here': 'True when the panel runs here',
    'Offsets may be signed.': 'Offsets accept positive and negative values.',
    'Death cannot be overridden.': 'Death takes precedence.',
    'Voices of this cue that may play at once.': 'Maximum simultaneous voices for this cue.',
    'Weapons the player may pick one of at run start.': 'Weapon choices at run start.',
    'What kind of music should play.': 'Music context.',
    'Null = cannot merge.': 'Null disables merging.',
    'Reads optional public result metadata without requiring a Shared contract change.\n            Missing metadata stays unavailable; probabilities and private/default analysis settings are not substitutes.': 'Reads public analysis metadata and reports the fields supplied by each result.',
}


def polish(text):
    # Show tooltip field declarations; their runtime UI text belongs to the product UI.
    if re.match(r'(?:public const string \w+Tooltip|Public Const \w+Tooltip As String) =', text):
        return text.split(' =', 1)[0]
    for original, replacement in REPLACEMENTS.items():
        text = text.replace(original, replacement)
    return text
