def greeting(name):
    print(f"Hello {name}")


def kids(*args):
    print(min(args))


def kw(**kwargs):
    print(kwargs["name"])


def def_par(name="Max"):
    print(name)


person1 = {"Max": 22}
