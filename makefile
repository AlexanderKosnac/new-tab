build_dir = build/

default_target: all

with-output:
	mkdir -p $(build_dir)

clean:
	rm -rf $(build_dir)

build-example: with-output
	python build.py example.json assets/ $(build_dir)

all: build-example
