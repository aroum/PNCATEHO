#include "PNCATEHO.h"

//MAKE SURE THESE ARE INCLUDED
#include "artsey.h"
#include "keymap_combo.h"
#include "artsey.c"

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [_A_BASE] = LAYOUT(A_BASE_B, A_BASE_F, A_BASE_T, A_BASE_J,
                       A_BASE_H, A_BASE_C, A_BASE_N, A_BASE_Y,
                                                     A_BASE_X, A_BASE_S),

    [_A_NUM]  = LAYOUT(A_NUM_B,  A_NUM_F,  A_NUM_T,  A_NUM_J,
                       A_NUM_H,  A_NUM_C,  A_NUM_N,  A_NUM_Y,
                                                     A_NUM_X,  A_NUM_S),

    [_A_NAV]  = LAYOUT(A_NAV_B,  A_NAV_F,  A_NAV_T,  A_NAV_J,
                       A_NAV_H,  A_NAV_C,  A_NAV_N,  A_NAV_Y,
                                                     A_NAV_X,  A_NAV_S),

    [_A_SYM]  = LAYOUT(A_SYM_B,  A_SYM_F,  A_SYM_T,  A_SYM_J,
                       A_SYM_H,  A_SYM_C,  A_SYM_N,  A_SYM_Y,
                                                     A_SYM_X,  A_SYM_S),

    [_A_RGB]  = LAYOUT(A_RGB_B,  A_RGB_F,  A_RGB_T,  A_RGB_J,
                       A_RGB_H,  A_RGB_C,  A_RGB_N,  A_RGB_Y,
                                                     A_RGB_X,  A_RGB_S),

    [_A_MATH] = LAYOUT(A_MATH_B, A_MATH_F, A_MATH_T, A_MATH_J,
                       A_MATH_H, A_MATH_C, A_MATH_N, A_MATH_Y,
                                                     A_MATH_X, A_MATH_S),
};

#ifdef RGBLIGHT_ENABLE
    const rgblight_segment_t PROGMEM capslock_layer[] = RGBLIGHT_LAYER_SEGMENTS(
        {0, 2, HSV_PURPLE});
    const rgblight_segment_t PROGMEM numlock_layer[] = RGBLIGHT_LAYER_SEGMENTS(
        {6, 1, HSV_ORANGE});
    const rgblight_segment_t PROGMEM ctrl_layer[] = RGBLIGHT_LAYER_SEGMENTS(
        {3, 1, HSV_RED});
    const rgblight_segment_t PROGMEM alt_layer[] = RGBLIGHT_LAYER_SEGMENTS(
        {4, 1, HSV_GREEN});
    const rgblight_segment_t PROGMEM gui_layer[] = RGBLIGHT_LAYER_SEGMENTS(
        {5, 1, HSV_CYAN});

    // Now define the array of layers. Later layers take precedence
    const rgblight_segment_t *const PROGMEM my_rgb_layers[] = RGBLIGHT_LAYERS_LIST(
        capslock_layer,
        numlock_layer,
        ctrl_layer,
        alt_layer,
        gui_layer);

    void keyboard_post_init_user(void)
    {
        // Enable the LED layers
        rgblight_layers = my_rgb_layers;
    };

    bool led_update_user(led_t led_state)
    {
        rgblight_set_layer_state(0, led_state.caps_lock);
        rgblight_set_layer_state(1, !led_state.num_lock);
        return true;
    }

    void oneshot_mods_changed_user(uint8_t mods)
    {
        if (mods & MOD_MASK_CTRL)
        {
            rgblight_set_layer_state(2, true);
        }
        if (mods & MOD_MASK_ALT)
        {
            rgblight_set_layer_state(3, true);
        }
        if (mods & MOD_MASK_GUI)
        {
            rgblight_set_layer_state(4, true);
        }
        if (!mods)
        {
            rgblight_set_layer_state(2, false);
            rgblight_set_layer_state(3, false);
            rgblight_set_layer_state(4, false);
        }
    }
#endif