# Copyright (c) Meta Platforms, Inc. and affiliates.

# Definitions of macros and functions facilitating creation of build.mk files
# according to the convention used in ExtendedAndroidTools.
#
# Majority of cross-compiled projects use a build files generation tool like
# autotools or cmake. To build them one needs to first generate a build
# directory and then invoke make or other build system from that directory.
# Some of the projects need to be compiled for Android, some for the host
# platform and some for both. For those reasons build.mk files under projects/*/
# define the following build targets:
# - host build directory
# - host build rule
# - android build directory
# - android build rule
#
# By convention android and host build directories for project "myproject" are
# "$(ANDROID_BUILD_DIR)/myproject" and "$(HOST_BUILD_DIR)/myproject"
# respectively. Corresponding build rules are
# "$(ANDROID_BUILD_DIR)/myproject.done" and "$(HOST_BUILD_DIR)/myproject.done".
# Build rules write built artifacts to $(ANDROID_OUT_DIR) and $(HOST_OUT_DIR)
# and artificial "*.done" files are used only to track successfull runs of the
# compilation step.
#
# project-define macro defined in this file helps set up build targets by
# computing their names and setting up dependencies between them.
#   $(eval $(call project-define,myproject))
# generates the following variables:
# - MYPROJECT_ANDROID: android build target generating myproject.done file
#   after successful compilation of myproject for Android
# - MYPROJECT_ANDROID_BUILD_DIR: build directory to be used by android build
#   rule
# - MYPROJECT_HOST: host build target generating myproject.done file after
#   successful compilation of myproject for the host platform
# - MYPROJECT_HOST_BUILD_DIR: build directory to be used by the host build
#   target
# Additionally the call makes the android/host build rule dependent on the
# corresponding build directory.
#
# Intended usage of project-define is shown below:
#    $(eval $(call project-define,myproject))
#
#    $(MYPROJECT_ANDROID):
#    	cd $(MYPROJECT_ANDROID_BUILD_DIR) && make ...
#    	touch $@
#
#    $(MYPROJECT_ANDROID_BUILD_DIR):
#    	dir $@
#    	cd $@ && $(CMAKE) ...
#    	cd &@ && ./configure ...
#
#    $(MYPROJECT_HOST):
#    	cd $(MYPROJECT_HOST_BUILD_DIR) && make ...
#    	touch $@
#
#    $(MYPROJECT_HOST_BUILD_DIR):
#    	mkdir $@
#    	cd $@ && $(CMAKE) ...
#    	cd &@ && ./configure ...
#
#    projects/myproject/sources:
#    	git clone ...
#
# See project-define and projects/flex/build.mk to see the details and actual
# example of usage.

# Given a project name computes a variable prefix associated with
# the project. For example:
#    $(call project-to-var,bpftrace)_SRC
# resolves to
#    BPFTRACE_SRC
project-to-var = $(shell echo $(1) | tr '[:lower:]' '[:upper:]')

# Resolves to android build target associated with given project.
# For example, when building for arm64:
#     $(call project-android-target,python)
# resolves to
#     build/android/arm64/python.done
project-android-target = $(ANDROID_BUILD_DIR)/$(1).done

# Resolves to host build target associated with given project.
# For example:
#     $(call project-host-target,flex)
# resolces to
#     build/host/flex.done
project-host-target = $(HOST_BUILD_DIR)/$(1).done

# Resolves to android build directory associated with given project.
# For example, when building for x86_64:
#     $(call project-android-build-dir,argp)
# resolves to
#     build/android/x86_64/argp
project-android-build-dir = $(ANDROID_BUILD_DIR)/$(1)

# Resolves to host build directory associated with given project.
# For example:
#     $(call project-host-build-dir,ffi)
# resolves to
#     build/host/ffi
project-host-build-dir = $(HOST_BUILD_DIR)/$(1)

_project-android-deps-var = $(call project-to-var,$(1))_ANDROID_DEPS
_project-host-deps-var = $(call project-to-var,$(1))_HOST_DEPS
_project-sources-var = $(call project-to-var,$(1))_SOURCES

# Resolves to a target generating project's sources, unless appropriate
# PROJECT_SOURCES variable is defined.
project-optional-sources-target = $(call if,\
    $($(call _project-sources-var,$(1))),\
    ,\
    projects/$(1)/sources)

# Resolves to absolute path to project's sources
project-sources = $(call if,\
    $($(call _project-sources-var,$(1))),\
    $(abspath $($(call _project-sources-var,$(1)))),\
    $(abspath projects/$(1)/sources))

# Macro defining project variables and setting up basic dependencies
# between project rules.
#
# The following variables are defined:
# - <PROJECT>_ANDROID variable is assigned the name of project's android target
# - <PROJECT>_ANDROID_BUILD_DIR is assigned the name of project's android build
#   directory
# - <PROJECT>_HOST variable is assigned the name of project's host target
# - <PROJECT>_HOST_BUILD_DIR is assigned the name of project's host build
#   directory
# - <PROJECT>_SRCS is assigned the absolute path of project's sources
#
# The following build dependencies are defined:
# - $(<PROJECT>_ANDROID): $(<PROJECT>_ANDROID_BUILD_DIR)
# - $(<PROJECT>_HOST): $(<PROJECT>_HOST_BUILD_DIR)
#
# If no <PROJECT>_SOURCES is defined then additional dependencies are declared
# - $(<PROJECT>_ANDROID_BUILD_DIR): projects/<project>/sources
# - $(<PROJECT>_HOST_BUILD_DIR): projects/<project>/sources
#
# If <PROJECT>_ANDROID_DEPS is defined it is treated as list of android projects
# added as build dependencies of $(<PROJECT>_ANDROID_BUILD_DIR).
#
# If <PROJECT>_HOST_DEPS is defined it is treated as list of host projects added
# as build dependencies  of $(<PROJECT>_ANDROID_BUILD_DIR) and
# $(<PROJECT>_HOST_BUILD_DIR).
#
# Finally, for convenience a number of phony targets are defined:
# - <project>: $(<PROJECT>_ANDROID)
# - prepare-<project>: $(<PROJECT>_ANDROID_BUILD_DIR)
# - <project>-host: $(<PROJECT>_HOST)
# - prepare-<project>-host: $(<PROJECT>_HOST_BUILD_DIR)
define project-define =
  $(call project-to-var,$(1))_ANDROID := \
      $(call project-android-target,$(1))
  $(call project-to-var,$(1))_ANDROID_BUILD_DIR := \
      $(call project-android-build-dir,$(1))

  $(call project-to-var,$(1))_HOST := \
      $(call project-host-target,$(1))
  $(call project-to-var,$(1))_HOST_BUILD_DIR := \
      $(call project-host-build-dir,$(1))

  $(call project-to-var,$(1))_SRCS := $(call project-sources,$(1))

  .PHONY: $(1) prepare-$(1) $(1)-host prepare-$(1)-host
  $(1): $(call project-android-target,$(1))
  prepare-$(1): $(call project-android-build-dir,$(1)) ; @echo $$<
  $(1)-host: $(call project-host-target,$(1))
  prepare-$(1)-host: $(call project-host-build-dir,$(1)) ; @echo $$<

  $(call project-android-target,$(1)): \
      $(call project-android-build-dir,$(1)) \
      | $(ANDROID_OUT_DIR)

  $(call project-android-build-dir,$(1)): \
      $(call project-optional-sources-target,$(1)) \
      $(foreach dep,\
          $($(call _project-android-deps-var,$(1))),\
          $(call project-android-target,$(dep))) \
      $(foreach dep,\
          $($(call _project-host-deps-var,$(1))),\
          $(call project-host-target,$(dep))) \
      | $(ANDROID_BUILD_DIR)

  $(call project-host-target,$(1)): \
      $(call project-host-build-dir,$(1)) \
      | $(HOST_OUT_DIR)

  $(call project-host-build-dir,$(1)): \
      $(call project-optional-sources-target,$(1)) \
      $(foreach dep,\
          $($(call _project-host-deps-var,$(1))),\
          $(call project-host-target,$(dep))) \
      | $(HOST_BUILD_DIR)

  fetch-sources: projects/$(1)/sources
  remove-sources: remove-$(1)-sources

  .PHONY: remove-$(1)-sources
  remove-$(1)-sources: ; rm -rf projects/$(1)/sources
endef

# Macro defining rules installing a python library/tool via pip
define pip-project =
  $(call project-to-var,$(1))_HOST := \
      $(call project-host-target,$(1))

  $(1)-host: $(call project-host-target,$(1))

  $(call project-host-target,$(1)): \
      $(call project-host-target,python) \
      | $(HOST_BUILD_DIR)
	python3 -m pip install $(if $(2),$(2),$(1))
	touch $$@
endef
