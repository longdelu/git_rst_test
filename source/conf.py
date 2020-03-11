# -*- coding: utf-8 -*-
#
# bulid+reStructuredText+Sphinx+env documentation build configuration file, created by
# sphinx-quickstart on Sat Nov 23 16:53:44 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.imgmath', 
              'sphinx.ext.todo', 
              'sphinx.ext.autosectionlabel', 
              'sphinx.ext.autosummary', 
              'sphinx.ext.autodoc',
              'recommonmark']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Numbered figure
numfig = True

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:

from recommonmark.parser import CommonMarkParser
source_parsers = {'.md': CommonMarkParser,}

source_suffix = ['.rst', '.md']
#source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'reStructuredText+Sphinx'
copyright = u'2019, Guanrong'
author = u'Guanrong'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.1.0'
# The full version, including alpha/beta/rc tags.
release = u'0.1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = u'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = u'bulid+reStructuredText+Sphinx+env'


# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'xelatex'
latex_logo   = ''
# latex_show_pagerefs = True
latex_show_urls = 'footnote'

latex_docclass = {
    'howto':'ctexart',
    'manual':'ctexrep'
}

latex_elements = {

    'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',

    'preamble': u'''
    
\\addto\\captionsenglish{\\renewcommand{\\contentsname}{{目\\hspace{1em}录}}}
\\addto\\captionsenglish{\\renewcommand{\\chaptername}{章节}}
\\usepackage{indentfirst}
\\usepackage{xcolor}
\\usepackage{geometry}
\\usepackage{xwatermark}
\\usepackage{xunicode,xltxtra}
\\geometry{left=31.7mm,right=31.7mm,includehead,includefoot,top=5mm,headheight=16mm,headsep=7mm,bottom=16.5mm}
\\setlength{\\parindent}{2em}
\\XeTeXlinebreaklocale "zh" 
\\XeTeXlinebreakskip = 0pt plus 1pt
\\setmainfont{Times New Roman}
''', 

'sphinxsetup': u'''verbatimwithframe=false,
%VerbatimColor={named}{Gainsboro}, %TitleColor={named}{Black},
VerbatimColor={RGB}{230,230,230},
hintBorderColor={named}{LightCoral}, attentionBgColor={named}{LightPink},
attentionborder=3pt, attentionBorderColor={named}{Crimson},
noteBorderColor={named}{Olive}, noteborder=2pt,
cautionBorderColor={named}{Cyan}, cautionBgColor={named}{LightCyan},
cautionborder=3pt
''',
    
    'hyperref': '''
% Include hyperref last.
\\usepackage[bookmarksnumbered=true]{hyperref}
% Fix anchor placement for figures with captions.
\usepackage{hypcap}% it must be loaded after hyperref.
% Set up styles of URL: it should be placed after hyperref.
\urlstyle{same}
''',
    'fncychap':'\\usepackage[Bjornstrup]{fncychap}',
    
    # 'releasename':u'版本',
    
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10.5pt,openright',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    # 图片对齐风格由'htbp'改成'H',即不使用float alignment
    'figure_align': 'H',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, u'bulid+reStructuredText+Sphinx+env.tex', u'bulid+reStructuredText+Sphinx+env',
     u'Guanrong', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'bulid+reStructuredText+Sphinx+env', u'bulid+reStructuredText+Sphinx+env',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'bulid+reStructuredText+Sphinx+env', u'bulid+reStructuredText+Sphinx+env',
     author, 'bulid+reStructuredText+Sphinx+env', 'One line description of project.',
     'Miscellaneous'),
]






