# Documentation

## Semantics and conventions for docstrings

Becomes the \_\_doc\_\_ attribute

[PEP 257](https://www.python.org/dev/peps/pep-0257/) for recomendations

## Installing Sphinx

```
$ pip install sphinx
$ pip install recommonmark //for markup use
```

Allow [markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html) support

## Setup

Create **doc** folder and in that folder run

`$ sphinx-quickstart`

Answer each question asked. Be sure to say yes to the autodoc extension, as we will use this later.

Allow Google and Numpy Docstrings

```
extensions = ['sphinx.ext.napoleon']
```

## Themes

Choose a [Theme](https://sphinx-themes.org/) or install one

`pip install sphinx_rtd_theme`

`html_theme = 'sphinx_rtd_theme'`

## Create documentation

Modify the index.rst. You can add references to MD files.

### Build the APIs from the docstrings

Point to the directory with the modules

```
import os
import sys
sys.path.insert(0, os.path.abspath('..\\..\\'))
```

Add the extensions for docstrings and md files

```
extensions = ['recommonmark',
              'sphinx.ext.autodoc',
              'sphinx.ext.viewcode'
              ]
```


`$ sphinx-apidoc -f -o docs/source modelproj/`

Then build the main html (you can use)

`$ sphinx-build doc/source doc/build`

or

`$ make html`

## Final Details

### Editing

You can include md files and links to classes using rst

```
:class:`Player`
:class:`gamedemo.Player`
```

### Tip

You can do everything with just one command

`sphinx-apidoc --full -o docs/source modpro/`

## Publishing

**TODO** [GitHub Pages](https://pages.github.com/)

## Links

[sphinx-for-python-documentation](https://gisellezeno.com/tutorials/sphinx-for-python-documentation.html)

[Documenting your project with Sphinx](https://pythonhosted.org/an_example_pypi_project/sphinx.html)
