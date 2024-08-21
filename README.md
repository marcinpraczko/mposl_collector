# MPOSL Collector

Over the years, I have written and worked on various solutions, snippets, and pieces of code.
These have been scattered across numerous local folders, making them difficult to find and manage.
This repository serves as a central place to consolidate and share all these valuable resources.
By organizing them here, I hope to make them more accessible and useful, both for myself and for others who might benefit from them.


## Structure

- `apps` - Folder with some applications / tools (some of them are conifgure as docker images)
- `snippets` - Place with snippets (hardcoded, Emacs - YASnippet, vscode and PyCharm)
- `quick-start` - This folder is having simple commands to allow quicker work with collector project

## Apps (Tools)

### Apps/Sphinx-doc

This aims to have docker image with Sphinx-doc tool and all helpful configuration.

There is `Makefile` in `apps/sphinx-doc` which so far builds proper docker images and uploading them
to local instance of minikube.

-  To see all options please run

```bash
cd apps/sphinx-doc
make
```

- To build images locally

```bash
cd apps/sphinx-doc
make build-docker-images
```

- For more documentation please see: `apps/sphinx-doc/README.rst`
