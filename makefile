PY_BIN ?= python

build_dir = build/

default_target: all

profile?=""

.PHONY: build build-example with-output clean all
with-output:
	mkdir -p $(build_dir)

clean:
	rm -rf $(build_dir)

build-example: with-output
	$(PY_BIN) build.py example.json $(profile) assets/ $(build_dir)

build: with-output
	$(PY_BIN) build.py links.json $(profile) assets/ $(build_dir)

all: build
