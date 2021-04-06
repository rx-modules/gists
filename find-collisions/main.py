from pathlib import Path
from beet import DataPack
from itertools import chain

try:
    import rich

    RICH = True
except ModuleNotFoundError:
    RICH = False


stuff = [
    "advancements",
    "functions",
    "loot_tables",
    "predicates",
    "recipes",
    "structures",
    "block_tags",
    "entity_type_tags",
    "fluid_tags",
    "function_tags",
    "item_tags",
    "dimension_types",
    "dimensions",
    "biomes",
    "configured_carvers",
    "configured_features",
    "configured_structure_features",
    "configured_surface_builders",
    "noise_settings",
    "processor_lists",
    "template_pools",
    "item_modifiers",
]


def find_datapack_dirs():
    for path in Path('.').glob('*'):
        if not path.is_dir():
            continue

        if not (path / 'data').exists() or not (path / 'pack.mcmeta').exists():
            continue

        if RICH:
            rich.print('[italic]    dir: [/italic]', end=' ')

        yield path


paths = chain(Path(".").glob("*.zip"), find_datapack_dirs())


def meth():
    cache = {}
    collisions = set()
    for path in paths:
        print("  ", str(path))
        datapack = DataPack()
        datapack.load(path)
        for attr in stuff:
            proxy = getattr(datapack, attr)
            for key in proxy.keys():
                if key.startswith("minecraft") and key in cache:
                    collisions.add(key)
                    cache[key].append((proxy, datapack))
                else:
                    cache[key] = [(proxy, datapack)]
    return cache, collisions


if __name__ == "__main__":
    print('processing:')
    cache, collisions = meth()
    print('\ncollisions:')
    for item in collisions:
        if RICH:
            rich.print(f"  [blue bold]{item}[/blue bold]")
        else:
            print(f"  {item}")
        for p in cache[item]:
            if RICH:
                rich.print(f"    [red bold]{p[1].name}[/red bold]")
            else:
                print(f"    - {p[1].name}")
        print()
