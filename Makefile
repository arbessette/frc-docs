PYTHON ?= .venv/bin/python
SPHINX = "$(PYTHON)" -m sphinx
.PHONY: html check linkcheck preview
html:
	$(SPHINX) -b html -W --keep-going -n source build/html
check:
	$(SPHINX) -b html -E -W --keep-going -n source build/html
linkcheck:
	$(SPHINX) -b linkcheck -W --keep-going source build/linkcheck
preview: html
	"$(PYTHON)" -m http.server 8000 --bind 127.0.0.1 --directory build/html
