// Copyright (c) Meta Platforms, Inc. and affiliates.

#ifndef ARGP_WRAPPER_H
#define ARGP_WRAPPER_H

#ifndef ARGP_EI
#  define ARGP_EI inline
#endif

// since ece81a73b64483a68f5157420836d84beb3a1680 argp.h as distributed with
// gnulib requires _GL_INLINE_HEADER_BEGIN macro to be defined.
#ifndef _GL_INLINE_HEADER_BEGIN
#  define _GL_INLINE_HEADER_BEGIN
#  define _GL_INLINE_HEADER_END
#endif

#ifndef _GL_ATTRIBUTE_FORMAT
#  define _GL_ATTRIBUTE_FORMAT(spec) __attribute__ ((__format__ spec))
#endif

#ifndef _GL_ATTRIBUTE_SPEC_PRINTF_SYSTEM
#  define _GL_ATTRIBUTE_SPEC_PRINTF_SYSTEM __printf__
#endif

#include "argp-real.h"
#endif
