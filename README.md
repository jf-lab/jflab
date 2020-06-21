# JF Lab Website Maintenance

![CI](https://github.com/jf-lab/jflab/workflows/CI/badge.svg) ![Update Lab Members](https://github.com/jf-lab/jflab/workflows/Update%20Lab%20Members/badge.svg)

## Visit at [www.jflab.ca](http://jflab.ca)

## Requirements
Options:

- To build locally, please follow all the steps below.
- To only work from Github/Netlify, start at Step 3.

1. macOS, GNU/Linux, Unix (doesn't work as well on Windows, but might work depending on your set-up)
2. [Jekyll](https://jekyllrb.com/docs/installation/) Static Pages Generator
    - please follow the instructions carefully to download prerequisites (Ruby, RubyGems, GCC/Make)
    - once you have these working:  
    `gem install jekyll`
3. A [Github Account](https://github.com) (it's free!)
4. Access to the [Github repo](https://github.com/linamnt/franklandlab) and Netlify.com
    - see previous administrator to add you
5. Python 3.6+ (if using 3.4/3.5, you need to remove any f-strings)


## Usage

### Adding Publications Manually
- See the examples in `_data/papers.yml` and fill in papers with the appropriate information.
- all fields except link (for pdfs) or alt_link (for online version link) are required
- order from most recent to oldest
- to link a PDF, place the pdf in the _site/pdfs/ folder and link to it
in the `link:` field using the format `pdfs/name-of-pdf.pdf` 

### Adding Publications Automatically via Pubmed Search
- Make sure you have Python 3, then run the following in command line:
`> pip install biopython`
- Edit the `author` and `user_email` variables in the `main()` function of update_papers.py to match your NCBI author search.
- When running the first time, please check to make sure that `_data/recent_pubmed_ids.txt`
is empty (just delete whatever is currently there, as this data belongs to a previous
websites template and won't apply to your website).
- Run the following in command line:
```
> cd website/folder/
> python update_papers.py
> git add _data/*
> git commit -m 'updated publications'
> git push origin master
```

The `main.yml` GA Workflow file also automatically checks for new publications and adds them to the website on `push` to `master`. 

### Changing Members
1. **Edit the lab member info google spreadsheet.** There is a shared google spreadsheet for lab members to update their own information. Please ask the current site administrator for acess. The website will update the repo data on `push` to `master` via GitHub Actions.
2. **Add the member's image file to img/ folder** The image filename must match `img_id` for the member in the spreadsheet (e.g. `img_id: paul.png`). Images should also be square in dimensions to prevent warping. Common image file types accepted (.jpeg, .png).

### Making a new page

Copy the template.md under pages/ to make your new page.  
If you use `permalink: /title/` tag, the link will be site.com/title/

### Making a new post

Copy the template.md under `_posts/` to make your new post.
Fill in the correct info and you're done, files must be named according to `YYYY-MM-DD-title.md`

_This site was modified from https://github.com/y7kim/agency-jekyll-theme_
