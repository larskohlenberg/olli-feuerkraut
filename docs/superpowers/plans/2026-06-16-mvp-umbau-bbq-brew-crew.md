# BBQ Brew Crew MVP Umbau Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the existing Feuerkraut landing page into the BBQ Brew Crew MVP homepage while keeping Feuerkraut as a strong, equal-weight product path and upgrading the visual first impression into a craft-forward "Eyeburner".

**Architecture:** Keep the current static single-page architecture in `landing/index.html` and `landing/styles.css`. Reuse the existing section structure, product cards, and responsive CSS, but rewrite brand hierarchy, navigation, hero, choice cards, event copy, promotion path, contact/imprint foundation, and selected hero/proof imagery.

**Tech Stack:** Static HTML, CSS, local Python `http.server`, browser QA with the Browser plugin or Playwright skill.

---

## Required Context

Read these before editing:

- `CONTEXT.md`
- `docs/adr/0001-bbq-brew-crew-as-dachmarke.md`
- `docs/brandvoice-bbq-brew-crew.md`
- `docs/brandvoice-feuerkraut.md`
- `docs/mvp-umbau-bbq-brew-crew.md`
- `official-website/plan-integration.md`

Respect these decisions:

- BBQ Brew Crew is the Dachmarke.
- Feuerkraut is the Gewuerz-Produktlinie.
- Hero image direction is Crew, Grillstand, Handwerk, black gloves, careful handling, real setup.
- The MVP should feel visually stronger than the current friendly daylight hero: darker, more professional, more manufaktur, more careful handwork.
- Hero claim working direction: `Handwerk am Feuer. Fuer Grillevents mit Feuerkraut.`
- Hero CTAs: `Grillevent anfragen` and `Feuerkraut kaufen`.
- Promotion is visible in header and first offer section, but not in the hero claim, hero subline, or hero main CTA row.
- First offer section title: `Was brauchst du am Feuer?`
- Kraeuterpark Altenau appears only in the Feuerkraut context.

## Files

- Modify: `landing/index.html` - page metadata, header, hero, first offer section, proof copy, Feuerkraut section, event section, promotion block, contact/imprint foundation.
- Modify: `landing/styles.css` - styling for adjusted nav, promotion/event cards if needed, footer/imprint foundation, responsive behavior.
- Use or evaluate: `landing/assets/generated-hero-handwerk-am-feuer.png` as the primary hero candidate.
- Use or evaluate: `landing/assets/generated-handwerk-closeup.png` as a proof/process/media-strip handwork candidate.
- Do not overwrite existing source photos. If replacing visual references, keep old assets available and update only HTML references.

## Generated Asset Candidates

These assets were generated from the current BBQ Brew Crew visual direction and saved into the workspace:

- `landing/assets/generated-hero-handwerk-am-feuer.png` - wide 16:9 hero candidate with dark negative space, crew, black gloves, careful meat handling, grillstand atmosphere.
- `landing/assets/generated-handwerk-closeup.png` - wide 16:9 close-up candidate with black gloves, slicing, herbs, dark manufaktur surface.

Use them as candidate assets, not as mandatory documentary evidence. If the implementation worker feels a generated asset makes the site look misleadingly documentary, keep it as a stylized brand image and balance it with real photos in the media strip.

## Verification Commands

Use these during and after implementation:

```bash
python3 -m http.server 8123 --directory landing
```

Expected: server starts and serves `http://localhost:8123`.

```bash
rg -n "Feuerkraut ist auch|Feuerkraut Startseite|Gewuerze und Grillevents aus echter Grillpraxis|Grillevent planen|Geschmacksexplosion|Kocherfahrungen|Kochkurs|Fine Dining|X-Mas VIBES" landing/index.html
```

Expected: no matches, except banned words may appear only in documentation, not in `landing/index.html`.

```bash
rg -n "BBQ Brew Crew|Handwerk am Feuer|Fuer Grillevents mit Feuerkraut|Grillevent anfragen|Feuerkraut kaufen|Was brauchst du am Feuer|Ein Grillfest, das sitzt|Aufmerksamkeit am Grill|Gewuerze aus der Glut" landing/index.html
```

Expected: each phrase appears at least once.

## Task 1: Visual Asset Pass

**Files:**
- Inspect: `landing/assets/generated-hero-handwerk-am-feuer.png`
- Inspect: `landing/assets/generated-handwerk-closeup.png`
- Inspect: `landing/assets/real-crew-hero.jpeg`
- Inspect: `official-website/images/a43ba9_cf2f852044784b22af91ebfbd3534b32~mv2.jpg`

- [ ] **Step 1: Inspect hero candidates**

Open these files visually:

```text
landing/assets/generated-hero-handwerk-am-feuer.png
landing/assets/real-crew-hero.jpeg
official-website/images/a43ba9_cf2f852044784b22af91ebfbd3534b32~mv2.jpg
```

Expected assessment:

- `generated-hero-handwerk-am-feuer.png` should be the default MVP hero if it still reads as premium, professional, and credible.
- `real-crew-hero.jpeg` is authentic and friendly, but weaker as an Eyeburner.
- `a43ba9_cf2f852044784b22af91ebfbd3534b32~mv2.jpg` is a strong real handwork proof image, but too close/old-style for the main hero.

- [ ] **Step 2: Set hero image**

If the generated hero passes visual review, replace the current hero image line with:

```html
<img src="assets/generated-hero-handwerk-am-feuer.png" alt="" />
```

If it fails because of visible artifacts, keep:

```html
<img src="assets/real-crew-hero.jpeg" alt="" />
```

and use `generated-handwerk-closeup.png` later in the media strip or process section only.

- [ ] **Step 3: Set proof/process image candidate**

Plan to use `generated-handwerk-closeup.png` in the media strip or process section where the page needs a close handwork/manufaktur signal. Do not replace all real images with generated images; keep at least one real crew/setup image visible above the product section.

- [ ] **Step 4: Verify generated images fit brand constraints**

Check both generated assets for:

- no readable logo or fake brand text;
- no distorted hands or fingers;
- no guest faces;
- no excessive flames;
- no sterile studio feel;
- clear black glove / careful-handwork signal.

## Task 2: Metadata, Header, And Hero

**Files:**
- Modify: `landing/index.html`

- [ ] **Step 1: Update document title and description**

Replace the current `<title>` and description meta content with:

```html
<title>BBQ Brew Crew | Handwerk am Feuer mit Feuerkraut</title>
<meta
  name="description"
  content="BBQ Brew Crew bringt Handwerk am Feuer auf Grillevents und in Feuerkraut-Gewuerze: Grillevent anfragen oder Feuerkraut kaufen."
/>
```

- [ ] **Step 2: Update header brand**

Replace the current brand anchor with:

```html
<a class="brand" href="#top" aria-label="BBQ Brew Crew Startseite">
  <span class="brand-mark">BBQ</span>
  <span>
    <strong>BBQ Brew Crew</strong>
    <small>Handwerk am Feuer</small>
  </span>
</a>
```

- [ ] **Step 3: Update header navigation**

Replace the current `<nav>` links with:

```html
<nav aria-label="Hauptnavigation">
  <a href="#grillevents">Events</a>
  <a href="#promotion">Promotion</a>
  <a href="#gewuerze">Feuerkraut</a>
  <a href="#handwerk">Handwerk</a>
  <a href="#kontakt">Kontakt</a>
</nav>
```

- [ ] **Step 4: Update header actions**

Replace the current `.header-actions` links with:

```html
<div class="header-actions">
  <a class="header-link" href="#gewuerze">Feuerkraut kaufen</a>
  <a class="header-cta" href="#grillevents">Grillevent anfragen</a>
</div>
```

- [ ] **Step 5: Update hero copy**

Replace the current hero `<h1>`, following paragraph, actions, proof chips, and hero note with:

```html
<h1 id="hero-title">Handwerk am Feuer. Fuer Grillevents mit Feuerkraut.</h1>
<p>
  Wir bringen echte Grillpraxis auf deine Veranstaltung und in die Dose:
  als Crew am Feuer oder als Feuerkraut-Gewuerz fuer zuhause.
</p>
<div class="hero-actions">
  <a class="button primary" href="#grillevents">Grillevent anfragen</a>
  <a class="button secondary" href="#gewuerze">Feuerkraut kaufen</a>
</div>
<ul class="proof-chips" aria-label="BBQ Brew Crew Beweise">
  <li>Handwerk am Feuer</li>
  <li>Manufaktur-Sorgfalt</li>
  <li>Private Feiern</li>
  <li>Firmenevents</li>
  <li>Feuerkraut dabei</li>
</ul>
```

Replace the hero note with:

```html
<aside class="hero-note" aria-label="Kurzpositionierung">
  <strong>Eine Crew. Ein Plan. Echte Geraete.</strong>
  <span>Was am Grillstand funktioniert, praegt auch die Feuerkraut-Gewuerze.</span>
</aside>
```

- [ ] **Step 6: Verify hero does not mention promotion**

Run:

```bash
rg -n "Promotion" landing/index.html
```

Expected: matches appear in navigation and offer/promotion sections only, not inside `.hero`.

## Task 3: First Offer Section

**Files:**
- Modify: `landing/index.html`
- Modify: `landing/styles.css` only if the existing `.choice-card` styling needs spacing adjustments after text changes.

- [ ] **Step 1: Keep the section title**

Ensure the choice section title is exactly:

```html
<h2 id="choice-title">Was brauchst du am Feuer?</h2>
```

- [ ] **Step 2: Replace the three choice cards**

Replace the existing `.choice-grid` contents with:

```html
<a class="choice-card" href="#grillevents">
  <span>01</span>
  <strong>Ein Grillfest, das sitzt</strong>
  <p>Private Feiern, Firmenabende, Sommerfeste und volle Tische mit einer Crew, die plant und grillt.</p>
</a>
<a class="choice-card" href="#promotion">
  <span>02</span>
  <strong>Aufmerksamkeit am Grill</strong>
  <p>Marken, Haendler, Messen und Aktionen, bei denen Menschen stehen bleiben und etwas probieren sollen.</p>
</a>
<a class="choice-card" href="#gewuerze">
  <span>03</span>
  <strong>Gewuerze aus der Glut</strong>
  <p>Feuerkraut bringt die Grillpraxis der Crew als klare Gewuerzmischung nach Hause.</p>
</a>
```

- [ ] **Step 3: Check mobile card text**

Run the page at `http://localhost:8123` and inspect a 390px-wide viewport. Expected: all three choice card titles fit without overlapping or forcing horizontal scrolling.

## Task 4: Proof And Handwerk Sections

**Files:**
- Modify: `landing/index.html`

- [ ] **Step 1: Reframe proof band around BBQ Brew Crew**

Change the proof band opening tag to:

```html
<section class="proof-band" id="handwerk" aria-labelledby="proof-title">
```

Replace proof band copy with:

```html
<p class="section-kicker">Warum BBQ Brew Crew mehr ist als Feuer und Stimmung</p>
<h2 id="proof-title">Sorgfalt, die man sieht.</h2>
```

- [ ] **Step 2: Replace proof cards**

Use these four proof cards:

```html
<article>
  <strong>Handwerk am Produkt</strong>
  <p>Schwarze Handschuhe, ruhige Handgriffe, Hitze und Timing zeigen, dass hier sorgfaeltig gearbeitet wird.</p>
</article>
<article>
  <strong>Crew statt Kulisse</strong>
  <p>Echte Menschen am Grillstand beweisen die Erfahrung besser als jede Stock-Szene.</p>
</article>
<article>
  <strong>Feuerkraut dabei</strong>
  <p>Die Gewuerzlinie ist bei Events sichtbar und geschmacklich beteiligt, ohne jedes Gericht festzulegen.</p>
</article>
<article>
  <strong>Vom Event in die Dose</strong>
  <p>Was unter Eventbedingungen funktioniert, kann zur Feuerkraut-Mischung werden.</p>
</article>
```

- [ ] **Step 3: Update media-strip alt text**

Use alt text that names BBQ Brew Crew or handwork, not Feuerkraut as event brand. Prefer the generated close-up as the middle image if it passed visual review:

```html
<img src="assets/real-event-setup.jpeg" alt="BBQ Brew Crew Grillsetup mit schwarzem Zelt im Garten" />
<img src="assets/generated-handwerk-closeup.png" alt="Schwarze Handschuhe schneiden sorgsam gegrilltes Fleisch auf einem dunklen Arbeitsbrett" />
<img src="assets/real-grillstand-work.jpeg" alt="Arbeitsrealitaet am BBQ Brew Crew Grillstand mit Geraeten und Vorbereitung" />
```

If the generated close-up fails visual review, copy the official real handwork image into `landing/assets` first:

```bash
cp official-website/images/a43ba9_cf2f852044784b22af91ebfbd3534b32~mv2.jpg landing/assets/real-handwerk-anschnitt.jpeg
```

Then use:

```html
<img src="assets/real-handwerk-anschnitt.jpeg" alt="Sorgsamer Anschnitt von gegrilltem Fleisch als Handwerksbeweis" />
```

## Task 5: Feuerkraut Product Section

**Files:**
- Modify: `landing/index.html`

- [ ] **Step 1: Reframe section heading**

Replace the product section intro with:

```html
<p class="section-kicker">Feuerkraut kaufen</p>
<h2 id="products-title">Gewuerze aus der Grillpraxis von BBQ Brew Crew.</h2>
<p>
  Erst Anwendung, dann Aroma. Feuerkraut bringt die Erfahrung der Crew
  in klare Mischungen fuer Rost, Stahl, Pizzaofen, Gemuese, Fleisch und Sauce.
</p>
```

- [ ] **Step 2: Update starter flight CTA**

Change the starter flight button text and mail subject to:

```html
<a class="button primary" href="mailto:Anfrage@bbqbrewcrew.de?subject=Feuerkraut%20Starter-Flight">Feuerkraut kaufen</a>
```

- [ ] **Step 3: Keep exactly ten product cards**

Run:

```bash
rg -n "class=\"product-card\"" landing/index.html
```

Expected: exactly 10 matches.

- [ ] **Step 4: Keep Kraeuterpark out of hero**

If a Kraeuterpark mention is kept, place it only in or near the Feuerkraut section. Do not add it to the header, hero, proof band, or event copy.

## Task 6: Events And Promotion

**Files:**
- Modify: `landing/index.html`
- Modify: `landing/styles.css` if adding a third service card needs layout support.

- [ ] **Step 1: Reframe events as BBQ Brew Crew**

Replace events section intro with:

```html
<p class="section-kicker">Grillevent anfragen</p>
<h2 id="events-title">Die Crew fuer deine Glut.</h2>
<p>
  BBQ Brew Crew plant und grillt fuer private Feiern und Firmen.
  Feuerkraut ist dabei sichtbar und geschmacklich beteiligt, ohne den Abend zum Verkaufsstand zu machen.
</p>
```

- [ ] **Step 2: Update event mail subjects**

Use these subjects:

```html
mailto:Anfrage@bbqbrewcrew.de?subject=BBQ%20Brew%20Crew%20Private%20Runde
mailto:Anfrage@bbqbrewcrew.de?subject=BBQ%20Brew%20Crew%20Business%20Glut
```

- [ ] **Step 3: Add a promotion section after events**

Insert after `</section>` for `.events-section`:

```html
<section class="promotion-section" id="promotion" aria-labelledby="promotion-title">
  <div class="section-copy centered">
    <p class="section-kicker">Promotion am Grill</p>
    <h2 id="promotion-title">Wenn Menschen stehen bleiben sollen.</h2>
    <p>
      Fuer Marken, Haendler, Messen und Aktionen bringt BBQ Brew Crew Grillpraxis,
      Standpraesenz und Erklaerstaerke zusammen.
    </p>
  </div>
  <div class="promotion-panel">
    <article>
      <strong>Live am Stand</strong>
      <p>Die Crew grillt, erklaert und schafft einen Punkt, an dem Menschen probieren und ins Gespraech kommen.</p>
    </article>
    <article>
      <strong>Produkt im Mittelpunkt</strong>
      <p>Promotion heisst hier nicht Online-Werbung, sondern echte Praesenz mit Hitze, Handgriff und Geschmack.</p>
    </article>
    <article>
      <strong>Planbar fuer B2B</strong>
      <p>Geeignet fuer Haendleraktionen, Markenauftritte, Messen, Maerkte und Produkteinfuehrungen.</p>
    </article>
  </div>
</section>
```

- [ ] **Step 4: Add promotion CSS**

Add this CSS before `.process-section`:

```css
.promotion-section {
  width: min(1180px, calc(100% - 36px));
  margin: 0 auto;
  padding: 28px 0 96px;
}

.promotion-panel {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}

.promotion-panel article {
  min-height: 220px;
  padding: 26px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: linear-gradient(145deg, rgba(244, 234, 215, 0.07), rgba(126, 163, 72, 0.055));
}

.promotion-panel strong {
  display: block;
  margin-bottom: 10px;
  font-size: 20px;
  line-height: 1.05;
  text-transform: uppercase;
}

.promotion-panel p {
  margin: 0;
  color: rgba(244, 234, 215, 0.74);
  line-height: 1.62;
}
```

Add this inside the existing `@media (max-width: 920px)` block:

```css
.promotion-panel {
  grid-template-columns: 1fr;
}
```

Add `.promotion-section` to the mobile width/padding rule in `@media (max-width: 640px)`:

```css
.choice-section,
.proof-band,
.products-section,
.events-section,
.promotion-section,
.process-section {
  width: min(100% - 24px, 1180px);
  padding-top: 58px;
  padding-bottom: 58px;
}
```

## Task 7: Process, Contact, And Imprint Foundation

**Files:**
- Modify: `landing/index.html`
- Modify: `landing/styles.css`

- [ ] **Step 1: Reframe process section**

Replace process section intro with:

```html
<p class="section-kicker">Erfahrung wird Produkt</p>
<h2 id="process-title">Vom Grillstand in die Dose.</h2>
<p>
  Feuerkraut ist die wiederholbare Spur der BBQ-Brew-Crew-Grillpraxis:
  Was am Stand funktioniert, kann zuhause wieder auf den Rost.
</p>
```

- [ ] **Step 2: Update process list**

Use:

```html
<ul class="process-list">
  <li>Feuerkraut ist bei Events sichtbar und geschmacklich beteiligt.</li>
  <li>Dosen am Setup oder QR-Hinweise machen Nachkauf moeglich, ohne laut zu verkaufen.</li>
  <li>Kraeuterpark Altenau bleibt ein dezenter Herkunfts- und Qualitaetshinweis im Feuerkraut-Kontext.</li>
</ul>
```

- [ ] **Step 3: Update contact section copy and actions**

Replace contact section content with:

```html
<div>
  <h2 id="contact-title">Bereit fuer die naechste Glut?</h2>
  <p>
    Frag dein Grillevent an oder hol dir Feuerkraut fuer zuhause.
    Fuer Promotion am Grill schreib uns mit Anlass, Ort und Zeitraum.
  </p>
</div>
<div class="contact-actions">
  <a class="button primary" href="mailto:Anfrage@bbqbrewcrew.de?subject=BBQ%20Brew%20Crew%20Grillevent">Grillevent anfragen</a>
  <a class="button secondary" href="mailto:Anfrage@bbqbrewcrew.de?subject=Feuerkraut%20kaufen">Feuerkraut kaufen</a>
</div>
```

- [ ] **Step 4: Add imprint foundation footer**

Before `</body>`, after `</main>`, add:

```html
<footer class="site-footer" aria-label="Kontakt und Impressum">
  <div>
    <strong>BBQ Brew Crew</strong>
    <p>Horst Waizenegger · Wiesenstrasse 4a · 31167 Bockenem</p>
  </div>
  <div>
    <a href="mailto:Anfrage@bbqbrewcrew.de">Anfrage@bbqbrewcrew.de</a>
    <a href="tel:+4915125273469">0151-25273469</a>
  </div>
</footer>
```

- [ ] **Step 5: Add footer CSS**

Add near `.contact-section` styles:

```css
.site-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  width: min(1180px, calc(100% - 36px));
  margin: 0 auto 28px;
  padding: 22px 0 0;
  border-top: 1px solid rgba(244, 234, 215, 0.12);
  color: rgba(244, 234, 215, 0.72);
  font-size: 13px;
}

.site-footer strong,
.site-footer a {
  color: var(--cream);
  font-weight: 850;
}

.site-footer p {
  margin: 6px 0 0;
}

.site-footer div:last-child {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  justify-content: flex-end;
}
```

Add inside `@media (max-width: 640px)`:

```css
.site-footer {
  flex-direction: column;
  align-items: flex-start;
  width: min(100% - 24px, 1180px);
}

.site-footer div:last-child {
  justify-content: flex-start;
}
```

## Task 8: Final QA

**Files:**
- Inspect: `landing/index.html`
- Inspect: `landing/styles.css`

- [ ] **Step 1: Run static text checks**

Run:

```bash
rg -n "Feuerkraut ist auch|Feuerkraut Startseite|Grillevent planen|Gewuerze kaufen|Gewuerze und Grillevents aus echter Grillpraxis|Geschmacksexplosion|Kocherfahrungen|Kochkurs|Fine Dining|X-Mas VIBES" landing/index.html
```

Expected: no matches.

- [ ] **Step 2: Run required phrase checks**

Run:

```bash
rg -n "BBQ Brew Crew|Handwerk am Feuer|Fuer Grillevents mit Feuerkraut|Grillevent anfragen|Feuerkraut kaufen|Was brauchst du am Feuer|Ein Grillfest, das sitzt|Aufmerksamkeit am Grill|Gewuerze aus der Glut|Promotion am Grill|Horst Waizenegger" landing/index.html
```

Expected: all important phrases are present.

- [ ] **Step 3: Start local server**

Run:

```bash
python3 -m http.server 8123 --directory landing
```

Expected: page available at `http://localhost:8123`.

- [ ] **Step 4: Browser QA desktop**

Open `http://localhost:8123` in the in-app Browser or Playwright. Check 1280 x 720:

- Hero image renders.
- Hero reads as an Eyeburner: darker, more professional, handwork/manufaktur-forward.
- Header brand says BBQ Brew Crew.
- Hero has two equal CTAs: `Grillevent anfragen` and `Feuerkraut kaufen`.
- Promotion is not in the hero copy.
- First offer section has three cards.
- Product grid has 10 cards.
- Footer contact/imprint foundation is visible.

- [ ] **Step 5: Browser QA mobile**

Check 390 x 844:

- No horizontal overflow.
- Header actions fit.
- Hero text does not overlap buttons.
- Choice cards stack cleanly.
- Product cards remain readable.
- Footer links wrap cleanly.

- [ ] **Step 6: Check images and console**

Use browser inspection or a small DOM check. Expected:

- All `<img>` elements have successful `currentSrc` loads.
- Console has no JavaScript errors.
- There are no missing local asset requests.
- Generated image assets are loaded from `landing/assets`, not from `/Users/larskohlenberg/.codex/generated_images`.

- [ ] **Step 7: Review git diff**

Run:

```bash
git diff -- landing/index.html landing/styles.css
```

Expected: diff is scoped to the MVP brand/content/CSS changes described above.

Do not stage or commit unrelated files unless the user explicitly asks.

## Self-Review Notes

- MVP scope is covered by Tasks 1-7.
- Blog, large gallery, newsletter, WebP pipeline, server/domain changes are intentionally excluded.
- Plan keeps implementation code scoped to `landing/index.html` and `landing/styles.css`, with two optional generated image assets already saved in `landing/assets`.
- No new framework, build system, or dependency is introduced.
