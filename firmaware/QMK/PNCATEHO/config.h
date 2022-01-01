#ifndef CONFIG_H
#define CONFIG_H

#include "config_common.h"

/* USB Device descriptor parameter */
#define VENDOR_ID 0x4541
#define PRODUCT_ID 0x0002
#define DEVICE_VER 0x0002
#define MANUFACTURER Aroum
#define PRODUCT PNCATEHO
#define DESCRIPTION x - key chorded  keyboard

/* key matrix size */
#define MATRIX_ROWS 2
#define MATRIX_COLS 5

/* Set 0 if debouncing isn't needed */
#define DEBOUNCING_DELAY 5

/* prevent stuck modifiers */
#define PREVENT_STUCK_MODIFIERS

/* ws2812 RGB LED */
#define RGB_DI_PIN B5

#ifdef RGBLIGHT_ENABLE
    #define RGBLED_NUM 10 // Number of LEDs
    #define DRIVER_LED_TOTAL RGBLED_NUM
    #define RGBLIGHT_SLEEP
    #define RGBLIGHT_LIMIT_VAL 180
    #define RGBLIGHT_HUE_STEP 5
    #define RGBLIGHT_SAT_STEP 10
    #define RGBLIGHT_VAL_STEP 60
    #define RGBLIGHT_EFFECT_STATIC_LIGHT
    #define RGBLIGHT_EFFECT_TWINKLE
    #define RGBLIGHT_LAYERS
    #define RGBLIGHT_MAX_LAYERS 5
    #define RGBLIGHT_LAYERS_OVERRIDE_RGB_OFF
    #define RGBLIGHT_LAYERS
#endif
#endif

#define DIRECT_PINS                                  \
    {                                                \
        {F7, F6, F5, F4, B6}, { B2, B3, B1, E6, B4 } \
    }
#define UNUSED_PINS
