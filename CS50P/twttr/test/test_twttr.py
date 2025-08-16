from twttr import shorten

def test_shorten():
        assert shorten("Jabik") == "Jbk"
        assert shorten("Sthib") == "Sthb"
        assert shorten("MEIN") == "MN"
        assert shorten("Grandma!!!") == "Grndm!!!"
        assert shorten("0") == "0"

