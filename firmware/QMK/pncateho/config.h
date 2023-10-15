// #ifndef CONFIG_H
// #define CONFIG_H


/* USB Device descriptor parameter 
#define VENDOR_ID 0x4541
#define PRODUCT_ID 0x0002
#define DEVICE_VER 0x0002
#define MANUFACTURER Aroum
#define PRODUCT PNCATEHO
#define DESCRIPTION x - key chorded  keyboard
*/

/* key matrix size */
#define MATRIX_ROWS 2
#define MATRIX_COLS 5

/* Set 0 if debouncing isn't needed
#define DEBOUNCING_DELAY 5  */

#define DEBOUNCE 5




#ifdef RGBLIGHT_ENABLE
    #define RGBLED_NUM 10
    #define RGBLIGHT_EFFECT_BREATHING
    #define RGBLIGHT_EFFECT_RAINBOW_MOOD
    #define RGBLIGHT_EFFECT_RAINBOW_SWIRL
    #define RGBLIGHT_EFFECT_SNAKE
    #define RGBLIGHT_EFFECT_KNIGHT
    #define RGBLIGHT_EFFECT_CHRISTMAS
    #define RGBLIGHT_EFFECT_STATIC_GRADIENT
    #define RGBLIGHT_EFFECT_RGB_TEST
    #define RGBLIGHT_EFFECT_ALTERNATING
    #define RGBLIGHT_EFFECT_TWINKLE
    #define RGBLIGHT_LIMIT_VAL 120
    #define RGBLIGHT_HUE_STEP 10
    #define RGBLIGHT_SAT_STEP 17
    #define RGBLIGHT_VAL_STEP 17
    #define RGBLIGHT_LAYERS
    #define RGBLIGHT_MAX_LAYERS 5
    #define RGBLIGHT_LAYERS_OVERRIDE_RGB_OFF
    #define RGBLIGHT_LAYERS
    #define WS2812_DI_PIN B5
#endif

// #endif



/* #define UNUSED_PINS*/
