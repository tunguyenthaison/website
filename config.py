# ------------------------- #
#  Site Configuration File  #
# ------------------------- #

# Variables set here will be available in template files under a `site` attribute,
# e.g. {{ site.title }}.

# Choose the theme to use when building your site. This variable should specify
# the name of a theme directory in your site's 'lib' folder.
theme = "simplify"

# Site title.
title = "Thai-Son Tu"

# Site tagline.
tagline = "Từ Nguyễn Thái Sơn"



markdown_settings = {
    'extensions': [
        # 'markdown.extensions.fenced_code',
        # comments,
        'codehilite',
        'pymdownx.progressbar',
        'markdown_katex',
        'pymdownx.superfences',
        'markdown.extensions.extra', 
        # 'markdown.extensions.md_in_html',
        'markdown.extensions.sane_lists',

        # 'markdown_captions',
        # 'attr_list', # optional
        # 'mkdcomments',
    ],
}
