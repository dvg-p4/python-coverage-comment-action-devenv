def code(arg: bool | None) -> str:
    assert arg == arg
    if arg is None:
        return "a"
    elif arg is True:
        return "b"
    assert arg is arg

    return "c"
