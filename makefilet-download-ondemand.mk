# include this makefile snippet for automatic discovery of a:
#   * system-wide 'makefilet' installation (e.g. via the deb package)
#   * project-wide inclusion as a git-submodule (or code copy)
#   * on-demand download (temporarily stored in the local 'build/' directory)

# alternative version: "master" (the tip of the current development branch)
MAKEFILET_DOWNLOAD_VERSION ?= v0.6.6
MAKEFILET_DOWNLOAD_URL ?= https://notabug.org/sumpfralle/makefilet/archive/$(MAKEFILET_DOWNLOAD_VERSION).tar.gz

# first attempt: system-wide installation (e.g. deb package) or submodule of this project?
-include makefilet/main.mk
ifndef DIR_MAKEFILET
# we failed - it is not available globally or as a submodule
# second attempt: include a downloaded makefilet archive
DIR_BUILD ?= build
DIR_MAKEFILET_DOWNLOAD = $(DIR_BUILD)/makefilet
-include $(DIR_MAKEFILET_DOWNLOAD)/main.mk
ifndef DIR_MAKEFILET
# third attempt: download and extract a known release
$(info Downloading 'makefilet' ...)
$(shell mkdir -p "$(DIR_MAKEFILET_DOWNLOAD)" \
	&& wget --no-verbose --output-document - "$(MAKEFILET_DOWNLOAD_URL)" \
	| tar -xz -C "$(DIR_MAKEFILET_DOWNLOAD)" --strip-components=1 -f -)
# last include attempt
-include $(DIR_MAKEFILET_DOWNLOAD)/main.mk
ifndef DIR_MAKEFILET
$(error Failed to initialize 'makefilet'. It seems like it is neither installed system-wide, as a submodule or available via download.)
endif
endif
endif
