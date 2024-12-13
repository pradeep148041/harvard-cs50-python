from twttr import shorten

def main():
    test_upper_lower_cases()

def test_upper_lower_cases():
    assert shorten('twitter') == 'twttr'


if __name__ == "__main__":
    main()
