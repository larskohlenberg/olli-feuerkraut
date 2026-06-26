# Integrationsplan: BBQ Brew Crew + Feuerkraut

> **Stand:** 16.06.2026 — Assets der aktuellen Wix-Seite (bbqbrewcrew.com) wurden heruntergeladen.
> **Ziel:** Die Feuerkraut-Landingpage (192.168.177.132:8123) wird zur neuen BBQ Brew Crew Webseite.
> Feuerkraut bleibt als Gewürz-Produktlinie erhalten.

---

## 1. 🖼️ Heruntergeladene Assets

**Archiv:** `~/tmp/bbqbrewcrew-assets/bbqbrewcrew-assets.tar.gz` (45 MB)
**Einzelbilder:** `~/tmp/bbqbrewcrew-assets/images/` (39 Dateien)

### Kategorien

| Kategorie | Dateien | Beispiele |
|-----------|---------|-----------|
| **Logo** | `a43ba9_b11f008fe1c94db29297148b36d02ae4~mv2.png` | BBQ Brew Crew Catering Logo |
| **Hero / Team** | 4x JPG | Chef, Team, Grillfleisch |
| **Blog** | 15x JPG/PNG | Blogbeitrag-Bilder (Raclette, Weihnachten, etc.) |
| **Galerie (Buffet)** | 12x JPG | Buffets, Hochzeit, Meer, Veggie, etc. |
| **Sonstige** | Stock/Wix-Hintergründe | Dekorative Elemente |

> **Hinweis:** Wix liefert die Bilder in Originalqualität. Für die neue Seite sollten sie auf max. 1600px + WebP optimiert werden.

---

## 2. 📋 Branding & Grundstruktur

### Neues Branding
- **Name:** BBQ Brew Crew (bestehende Marke)
- **Feuerkraut:** Wird zur Produktlinie ("Feuerkraut – Gewürze von BBQ Brew Crew")
- **Claim:** "Catering, Promotion und Teambuilding"
- **Marken-Quote:** *"Kein Genuß ist vorübergehend; denn der Eindruck, den er zurücklässt, ist bleibend." — Johann Wolfgang von Goethe*
- **Farbpalette:** Beibehalten (Dark-Theme: Coal, Steel, Copper, Ember, Cream)

### Seiten-Struktur (Single-Page mit Sektionen)

```
/ (index.html)
├── Header / Navigation
│   ├── BBQ Brew Crew Logo + Brandname
│   ├── Nav: Start · Über uns · Leistungen · Feuerkraut · Galerie · Blog · Kontakt
│   └── CTA-Buttons
│
├── Hero
│   ├── BBQ Brew Crew Branding
│   ├── Goethe-Zitat
│   └── CTA: "Buchen / Gewürze kaufen"
│
├── Über uns (neu)
│   ├── Philosophie: "In Taste We Trust"
│   ├── Geschichte (BBQ seit 16. Jahrhundert)
│   └── Team: Horst Waizenegger + Crew
│
├── Leistungen (neu — 3 Säulen)
│   ├── BBQ Catering (deftig-würzig bis elegant-fein)
│   ├── Promotion (Fachkompetenz + Entertainment)
│   └── Grillteam (Meisterschaftskarriere, WM 2022)
│
├── Feuerkraut Gewürze (bestehend, umbenannt)
│   ├── 10 Gewürzmischungen
│   ├── 5er Starter-Flight
│   └── Partner: Kräuterpark Altenau
│
├── Grillevents / Catering (bestehend)
│   ├── Private Runde
│   └── Business Glut
│
├── Buffet & Menü Ideen (neu — Galerie)
│   ├── Genießerbuffet · All American BBQ · Hochzeiten
│   ├── Veggie & Vegan · Griechisches Buffet · Meer …
│   └── Bildergalerie mit Kategorien
│
├── Blog (neu)
│   └── Artikel-Liste (Raclette Deluxe, Weihnachtsmenü, X-Mas VIBES, …)
│
├── Meisterschaften (neu)
│   ├── 8 Jahre Wettkampfkarriere
│   └── BBQ Weltmeisterschaft 2022
│
├── Kontakt (erweitert)
│   ├── Kontaktformular (Name, Email, Telefon, Nachricht)
│   ├── Email: Anfrage@bbqbrewcrew.de
│   └── Telefon: 0151-25273469
│
├── Impressum (neu)
│   ├── Horst Waizenegger
│   ├── Wiesenstrasse 4a, 31167 Bockenem
│   ├── Telefon: 0151-25273469
│   └── Email: Anfrage@bbqbrewcrew.de
│
├── Datenschutz (neu, DSGVO)
│
└── Footer
    ├── Newsletter-Anmeldung
    ├── Social Media (Instagram, YouTube)
    └── Kontakt-Links
```

---

## 3. 🛠️ Technische Umsetzung (Etappen)

### Etappe A — HTML + CSS Grundgerüst
| Schritt | Was | Details |
|:-------:|-----|---------|
| 1 | `index.html` umbauen | `<html lang="de">`, Title "BBQ Brew Crew", Meta-Tags |
| 2 | Navigation erweitern | Alle neuen Sektionen verlinken |
| 3 | Bestehende Sektionen behalten | Hero, Gewürze, Events, "Vom Stand"-Story |
| 4 | Neue Sektionen einfügen | Über uns, Leistungen, Galerie, Blog, Meisterschaften, Kontakt, Impressum |
| 5 | `styles.css` erweitern | Neue Komponenten: Nav-Hamburger, Formular, Galerie, Blog-Karten, Footer |

### Etappe B — Funktionale Erweiterungen
| Schritt | Was | Lösung |
|:-------:|-----|--------|
| 6 | Kontaktformular | Formspree / Web3Forms (kein Backend, rein HTML) |
| 7 | Newsletter | Einfaches Subscribe-Formular (optional) |
| 8 | Blog | Statische HTML-Karten (später CMS optional) |
| 9 | Galerie | CSS-Grid mit Lightbox |
| 10 | Shop | Stripe Payment Links oder Lemon Squeez (vorerst) |

### Etappe C — Bilder optimieren
| Schritt | Was | Details |
|:-------:|-----|---------|
| 11 | JPEGs verkleinern | Max. 1600px (aktuell bis 4032px!) |
| 12 | WebP-Konvertierung | Alle Bilder als WebP + `<picture>`-Fallback |
| 13 | Lazy Loading | `loading="lazy"` auf allen Nicht-Hero-Bildern |
| 14 | Produkt-PNGs optimieren | Aktuell 2-3 MB pro Dose — auf < 500 KB |

### Etappe D — Server & Domain
| Schritt | Was | Details |
|:-------:|-----|---------|
| 15 | Server upgrade | Von Python http.server zu **Caddy** (auto HTTPS) |
| 16 | HTTPS | Let's Encrypt via Caddy (automatisch) |
| 17 | Domain | bbqbrewcrew.com oder Subdomain |
| 18 | Performance | Cache-Control, GZip, Bild-Komprimierung |

---

## 4. 🌶️ Feuerkraut als Produktlinie

Die bestehende Feuerkraut-Sektion bleibt erhalten, nur das Branding ändert sich:

```
Feuerkraut – Gewürze von BBQ Brew Crew
├── 5er Starter-Flight (34,90 €)
├── Feuerprobe      → Allround-Rub (7,90 €)
├── Harzglut         → Wild, Pilze, Kartoffeln
├── Plancha Pfeffer  → Steak, Plancha
├── Pizzaofen Rot    → Pizza, Brot, Dip
├── Rippenruhe       → Ribs, Smoker
├── Burgerbliss      → Burger, Fries
├── Hühnchenheld     → Geflügel, Wings
├── Gartenrauch      → Gemüse, vegan
├── Steakstille      → Steak-Finish
└── Kräuterkante     → Fisch, Quark, Kartoffeln
```

**Änderungen:**
- Feuerkraut bleibt als Markenname der Produktlinie
- Hero-Sektion: "BBQ Brew Crew" statt "Feuerkraut"
- "Feuerkraut – Gewürze aus unserer Grillpraxis" als Sektions-Überschrift
- Preise ergänzen
- Bestellung via Mailto beibehalten oder Shop-Link

---

## 5. 📄 Inhalte aus BBQ Brew Crew (für die Übernahme)

### Über uns
```
"IN TASTE WE TRUST. Wir vertrauen auf den Geschmack."
"Vielleicht nicht immer filigran, aber immer eine Geschmacksexplosion."
"Jahrelange Wettkampf und Kocherfahrungen sind die Grundlage."
"Egal ob Grill-/Kochkurs, BBQ-Catering oder Fine Dining — wir machen alles möglich."
```

### Geschichte
```
"Die Geschichte des BBQ startet im 16. Jahrhundert und der Kolonialisierung
Südamerikas durch die Europäer. Spanische Eroberer beobachteten,
wie Ureinwohner Fleisch über einer Grube auf Reisig brieten."
```

### 3 Leistungsbereiche
1. **BBQ Catering** — Deftig-würzig bis elegant und fein
2. **Promotion** — Fachkompetenz + Entertainment + Verkaufstalent
3. **Grillteam** — 8 Jahre Meisterschaftskarriere, BBQ-WM 2022

### Meisterschaften
- 8 Jahre erfolgreiche Wettkampfkarriere
- Teilnahme an der BBQ Weltmeisterschaft 2022

### Blog-Artikel (Titel)
1. Raclette Deluxe – Fire & Garden Menü (BBQ Brew Crew-Edition)
2. Vorschlag als Weihnachts-BBQ-Menü
3. X-Mas VIBES
4. VOLLGAS statt Kaffeekränzchen

### Kontakt / Impressum
```
Horst Waizenegger
Wiesenstrasse 4a, 31167 Bockenem
Telefon: 0151-25273469
Email: Anfrage@bbqbrewcrew.de
```

---

## 6. 🎯 Prioritäten

| Prio | Was | Aufwand |
|:----:|-----|:-------:|
| 🔴 | Branding + Hero auf BBQ Brew Crew umstellen | 15 Min |
| 🔴 | Navigation erweitern | 15 Min |
| 🔴 | Über uns + Impressum einbauen | 30 Min |
| 🔴 | Kontaktformular + Email | 20 Min |
| 🟡 | Feuerkraut-Gewürze als Produktlinie kennzeichnen | 10 Min |
| 🟡 | Buffet-Galerie | 30 Min |
| 🟡 | Blog-Sektion | 45 Min |
| 🟡 | Meisterschaften | 20 Min |
| 🟢 | Bilder optimieren (WebP, lazy load) | 30 Min |
| 🟢 | Newsletter | 15 Min |
| 🟢 | Server auf Caddy + HTTPS | 60 Min |

**Rot = Muss für MVP | Gelb = Sollte bald | Grün = Kann warten**