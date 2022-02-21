from juliasfinest.lib import try_me

def test_try_me(monkeypatch):
    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr('builtins.input', lambda _: "Fake Meat")

    # go about using input() like you normally would:
    i = input("What are you hungry for? ")

    assert i == "Fake Meat"
