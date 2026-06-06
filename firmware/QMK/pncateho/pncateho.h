#ifndef PNCATEHO_H
#define PNCATEHO_H

#include "quantum.h"

#define LAYOUT( \
	K00, K01, K02, K03, K04,\
        K10, K11, K12, K13, K14 \
) { \
	{ K00, K01, K02, K03, K04 }, \
	{ K10, K11, K12, K13, K14 }  \
}

#endif