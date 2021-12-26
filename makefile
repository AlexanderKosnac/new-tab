SHELL := /bin/bash
PY_BIN ?= python

build_dir = build/

default_target: all

profile?=""

check-python-version:
	@$(PY_BIN) scripts/check-version.py \
	    "$(shell $(PY_BIN) --version 2>&1 | cut -d " " -f 2)" \
	    "3" \
	    "4" \
	    "Using $(PY_BIN) but only Python of version 3 is supported. Use \`make PY_BIN=<python_version>\` to specify the python version."

with-output:
	mkdir -p $(build_dir)

clean:
	rm -rf $(build_dir)

build-example: with-output check-python-version
	$(PY_BIN) build.py example.json $(profile) assets/ $(build_dir)

build: with-output check-python-version
	$(PY_BIN) build.py links.json $(profile) assets/ $(build_dir)

all: build
