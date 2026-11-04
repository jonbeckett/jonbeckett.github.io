# jonbeckett.com

This repository contains the source for [jonbeckett.com](https://jonbeckett.com), a personal site about flight simulation and aviation. It is built with Jekyll, uses the Minimal Mistakes remote theme, and is configured for GitHub Pages with the custom domain recorded in `CNAME`.

## Site content

- `index.html` defines the homepage, including links to Jonathan's channels and sponsor information.
- `_pages/` contains the About, Contact, Disclaimer, Posts, Categories, and Tags pages.
- `_posts/` contains dated Markdown blog posts.
- `_data/navigation.yml` defines the main navigation.
- `_includes/` contains custom template includes.
- `assets/` contains the site's stylesheet and images.
- `docs/` contains technical notes about the site's setup and maintenance.

The repository also includes Copilot and Cline guidance in `.github/`, `.cline/`, and `.clinerules/`. `batch_generate_aircraft.py` is a separate legacy helper and is not part of the Jekyll build.

## Run locally

Install Ruby and Bundler, then install the project dependencies and start the Jekyll development server:

```sh
bundle install
bundle exec jekyll serve
```

Open <http://localhost:4000> to preview the site. To generate the site without starting a server, run:

```sh
bundle exec jekyll build
```

The generated site is written to `_site/`; it is build output, not source content.
