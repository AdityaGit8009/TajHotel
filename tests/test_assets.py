"""Validate every local browser resource on a case-sensitive checkout."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ["index.html", "hotels.html", "experiences.html", "destination.html", "offers.html"]

class Resources(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("src", "href", "poster") and value:
                url = urlsplit(value.strip())
                if url.path and not (url.scheme or url.netloc):
                    self.targets.append(unquote(url.path))

class HotelSite(unittest.TestCase):
    def test_all_relative_targets_exist_at_their_exact_case(self):
        names = {p.name for p in ROOT.iterdir() if p.is_file()}
        for name in PAGES:
            with self.subTest(page=name):
                parser = Resources()
                parser.feed((ROOT / name).read_text(encoding="utf-8-sig"))
                for target in parser.targets:
                    self.assertIn(target.removeprefix("./"), names, target)

if __name__ == "__main__":
    unittest.main()
