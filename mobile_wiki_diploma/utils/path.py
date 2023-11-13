def relative_from_root(path: str):
    import mobile_wiki_diploma
    from pathlib import Path

    return (
        Path(mobile_wiki_diploma.__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )
