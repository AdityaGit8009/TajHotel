# TajHotel

A five-page hotel website design with destinations, hotels, experiences and offers. It runs as a static site with the bundled Bootstrap stylesheet and JavaScript.

## Preview locally

From the repository root, run `python -m http.server 8000` and open [the home page](http://localhost:8000/).

| Section | Source |
| --- | --- |
| Home | [index.html](index.html) |
| Hotels | [hotels.html](hotels.html) |
| Destinations | [destination.html](destination.html) |
| Experiences | [experiences.html](experiences.html) |
| Offers and promotions | [offers.html](offers.html) |

Shared presentation lives in [style.css](style.css). Available photos and brand assets are served from the repository root. Pages disclose unavailable property photos and use local artwork for the home hero. The newsletter and booking controls are static design elements.

Run `python tests/test_assets.py` after editing a page or moving an asset. GitHub runs this check on pushes and pull requests.
