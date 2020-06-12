#ifndef LIBINTL_H
#define LIBINTL_H

// libintl.h is included in a lot of sources in efutils, but provided
// functionalities are not really necessary. Because of that we follow
// the AOSP example and provide a fake header turning some functions into
// nops with macros

#define gettext(x)      (x)
#define dgettext(x,y)   (y)

#endif
