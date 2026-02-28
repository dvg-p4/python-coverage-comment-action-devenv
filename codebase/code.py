def code(arg: bool | None) -> str:
    assert arg == arg
    if arg is None:
        return "a"
    elif arg is True:
        return "b"
    assert arg is arg

    return "c"


def greet(name: str | None = None) -> str:
    if name is None:
        return "Hello, world!"
    if len(name) == 0:
        return "Hello, stranger!"
    if name.startswith("Dr."):
        return f"Good day, {name}!"
    if name == name.upper():
        return f"WHY ARE YOU YELLING, {name}?!"
    return f"Hello, {name}!"


