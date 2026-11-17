# Week 01 - HTML & CSS tutorial

Static, responsive web site built for the Week 01 tutorial exercises.

## Requirements covered

| Requirement | Where |
|---|---|
| At least two separate pages | `index.html`, `about.html`, `gallery.html` (three pages) |
| Standard layout: header, navigation, multiple columns, footer | `.site-header`, `.site-nav`, `.layout` (2 columns), `.site-footer` (3 columns) |
| Adaptive / responsive, images always viewable | Media queries at 900px and 600px, `img { max-width: 100% }`, fluid gallery grid |
| No JavaScript at all, no templates/frameworks | No `<script>` tags, no Bootstrap or other framework - one hand written CSS file |

## Run it

No build step is required. Either open `index.html` directly in a browser, or serve
the folder:

```bash
python -m http.server 8000
# then browse to http://localhost:8000/
```

## Files

```
Week01-HTML-CSS/
  index.html      home page (two column layout: article + sidebar)
  about.html      second page, same layout
  gallery.html    third page, responsive image grid
  css/style.css   the only stylesheet, fully commented
  images/         photographs used by the site
```

The site was also completed as the W3Schools tutorials on CSS navigation bars,
web site layout and responsive web design were worked through (the nav bar is
built from a `ul` styled with flexbox, the layout uses CSS Grid, and the
breakpoints follow the mobile-first "stack on small screens" pattern).
