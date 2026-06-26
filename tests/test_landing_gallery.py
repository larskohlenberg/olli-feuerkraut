from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
LANDING = ROOT / "landing"
INDEX = LANDING / "index.html"


class LandingGalleryTest(unittest.TestCase):
    def setUp(self):
        self.html = INDEX.read_text(encoding="utf-8")

    def test_tailwind_gallery_section_is_present(self):
        self.assertIn("https://cdn.tailwindcss.com", self.html)
        self.assertIn('id="eindruecke"', self.html)
        self.assertIn("Echte Eindruecke", self.html)
        self.assertIn('data-gallery-layout="balanced-grid"', self.html)
        self.assertIn("lg:grid-cols-3", self.html)
        self.assertNotIn("lg:col-span-7", self.html)
        self.assertNotIn("lg:col-span-5", self.html)

    def test_gallery_assets_exist_and_are_referenced(self):
        expected_assets = [
            "assets/gallery-crew-am-stand.jpeg",
            "assets/gallery-event-tisch.jpeg",
            "assets/gallery-garten-setup.jpeg",
            "assets/gallery-promotion-stand.jpeg",
            "assets/gallery-grillkaese-closeup.jpeg",
            "assets/gallery-salate-event.jpeg",
        ]

        for asset in expected_assets:
            with self.subTest(asset=asset):
                self.assertIn(asset, self.html)
                self.assertTrue((LANDING / asset).is_file())

    def test_gallery_uses_six_equal_desktop_cards(self):
        self.assertEqual(self.html.count("data-gallery-card"), 6)
        self.assertEqual(self.html.count("lg:h-[360px]"), 6)


if __name__ == "__main__":
    unittest.main()
