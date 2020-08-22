include makefilet-download-ondemand.mk

DIR_PYDIST = $(DIR_BUILD)/pydist

.PHONY: default-target
default-target: build

.PHONY: build
build: $(DIR_PYDIST)

.PHONY: distribute-pypi
distribute-pypi: clean $(DIR_PYDIST)
	@if ! which twine >/dev/null 2>&1 || [ "$$(printf "1.11.0\n$$(twine --version | head -1 | cut -d" " -f3)" | sort -V | head -1)" != "1.11.0" ]; then \
		echo "you need twine >v1.11.0" >&2; \
		exit 1; \
	fi
	twine upload $(DIR_PYDIST)/*

$(DIR_PYDIST):
	python3 setup.py sdist --dist-dir "$(DIR_PYDIST)"
