// Copyright 2024 Mayoroffk
// SPDX-License-Identifier: GPL-2.0-or-later

#include "pncateho.h"

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┐
     * │ B │ F │ T │ J │
     * ├───┼───┼───┼───┤
     * │ H │ C │ N │ Y │
     * └───────────┼───┼───┐
     *             │Bsp│Spc│
     *             └───┴───┘
     */
    [0] = LAYOUT(
        KC_B,  KC_F,  KC_T,  KC_J,
        KC_H,  KC_C,  KC_N,  KC_Y,
                             KC_BSPC,  KC_SPC
    )
};
