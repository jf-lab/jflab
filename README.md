# Frankland Lab Website Maintenance

## Visit at [www.franklandlab.com](http://www.franklandlab.com)

## Requirements
Options:

- To build locally, please follow all the steps below.
- To only work from Github/Netlify, start at Step 3.

1. macOS, GNU/Linux, Unix (sorry windows...)
2. [Jekyll](https://jekyllrb.com/docs/installation/) Static Pages Generator
    - please follow the instructions carefully to download prerequisites (Ruby, RubyGems, GCC/Make)
    - once you have these working:  
    `gem install jekyll`
3. A [Github Account](https://github.com) (it's free!)
4. Access to the [Github repo](https://github.com/linamnt/franklandlab) and Netlify.com
    - see previous administrator to add you

## Usage

### Adding Publications
In the `_data/` folder, edit the file papers.yml with new publications. All tags required.

### Changing Members
In the `_data/` folder, there are four files, pi.yml, techs.yml, grad_students.yml, and alumni.yml
Edit each as appropriate.
`img_id` must match the name of the member photo in the img/ folder (plus file extension, e.g. `img_id: paul.png`)

### Making a new page

Copy the template.md under pages/ to make your new page.  
If you use `permalink: /title/` tag, the link will be site.com/title/

### Making a new post

Copy the template.md under `_posts/` to make your new post.
Fill in the correct info and you're done, files must be named according to `YYYY-MM-DD-title.md`

_This site was modified from https://github.com/y7kim/agency-jekyll-theme_
