bool is_shift_lock_active = false; 
bool other_key_pressed = false;
bool is_alt_tab_active = false; // ADD this near the begining of keymap.c;
uint16_t key_timer = 0;


bool process_record_user(uint16_t keycode, keyrecord_t *record) {


  switch (keycode) {
case A_BASE_JB:
if(record->event.pressed) {
register_code(KC_D);
}
else {
unregister_code(KC_D);
}
 break;
case A_BASE_YH:
if(record->event.pressed) {
register_code(KC_K);
}
else {
unregister_code(KC_K);
}
 break;
case A_BASE_CH:
if(record->event.pressed) {
register_code(KC_R);
}
else {
unregister_code(KC_R);
}
 break;
case A_BASE_YN:
if(record->event.pressed) {
register_code(KC_V);
}
else {
unregister_code(KC_V);
}
 break;
case A_BASE_FB:
if(record->event.pressed) {
register_code(KC_L);
}
else {
unregister_code(KC_L);
}
 break;
case A_BASE_JT:
if(record->event.pressed) {
register_code(KC_G);
}
else {
unregister_code(KC_G);
}
 break;
case A_BASE_NC:
if(record->event.pressed) {
register_code(KC_E);
}
else {
unregister_code(KC_E);
}
 break;
case A_BASE_TF:
if(record->event.pressed) {
register_code(KC_Z);
}
else {
unregister_code(KC_Z);
}
 break;
case A_BASE_NH:
if(record->event.pressed) {
register_code(KC_S);
}
else {
unregister_code(KC_S);
}
 break;
case A_BASE_YC:
if(record->event.pressed) {
register_code(KC_M);
}
else {
unregister_code(KC_M);
}
 break;
case A_BASE_TB:
if(record->event.pressed) {
register_code(KC_U);
}
else {
unregister_code(KC_U);
}
 break;
case A_BASE_JF:
if(record->event.pressed) {
register_code(KC_P);
}
else {
unregister_code(KC_P);
}
 break;
case A_BASE_BY:
if(record->event.pressed) {
register_code(KC_COMM);
}
else {
unregister_code(KC_COMM);
}
 break;
case A_BASE_JH:
if(record->event.pressed) {
register_code(KC_X);
}
else {
unregister_code(KC_X);
}
 break;
case A_BASE_BN:
if(record->event.pressed) {
register_code(KC_Q);
}
else {
unregister_code(KC_Q);
}
 break;
case A_BASE_JC:
if(record->event.pressed) {
register_code(KC_LBRC);
}
else {
unregister_code(KC_LBRC);
}
 break;
case A_BASE_TH:
if(record->event.pressed) {
register_code(KC_SCLN);
}
else {
unregister_code(KC_SCLN);
}
 break;
case A_BASE_FY:
if(record->event.pressed) {
register_code(KC_I);
}
else {
unregister_code(KC_I);
}
 break;
case A_BASE_BC:
if(record->event.pressed) {
register_code(KC_DOT);
}
else {
unregister_code(KC_DOT);
}
 break;
case A_BASE_JN:
if(record->event.pressed) {
register_code(KC_W);
}
else {
unregister_code(KC_W);
}
 break;
case A_BASE_FN:
if(record->event.pressed) {
register_code(KC_O);
}
else {
unregister_code(KC_O);
}
 break;
case A_BASE_TC:
if(record->event.pressed) {
register_code(KC_QUOT);
}
else {
unregister_code(KC_QUOT);
}
 break;
case A_BASE_TY:
if(record->event.pressed) {
register_code(KC_A);
}
else {
unregister_code(KC_A);
}
 break;
case A_BASE_FH:
if(record->event.pressed) {
register_code(KC_RBRC);
}
else {
unregister_code(KC_RBRC);
}
 break;
case A_NAV_FB:
if(record->event.pressed) {
register_code(KC_NO);
}
else {
unregister_code(KC_NO);
}
 break;
case A_SYM_FB:
if(record->event.pressed) {
// register_code(KC_PERC);
SEND_STRING("%");
}
else {
// unregister_code(KC_PERC);
}
 break;
case A_NUM_TF:
if(record->event.pressed) {
register_code(KC_7);
}
else {
unregister_code(KC_7);
}
 break;
case A_SYM_TF:
if(record->event.pressed) {
// register_code(KC_HASH);
SEND_STRING("#");
}
else {
// unregister_code(KC_HASH);
}
 break;
case A_NUM_JT:
if(record->event.pressed) {
register_code(KC_8);
}
else {
unregister_code(KC_8);
}
 break;
case A_NAV_TF:
if(record->event.pressed) {
register_code(KC_TAB);
}
else {
unregister_code(KC_TAB);
}
 break;
case A_NAV_JT:
if(record->event.pressed) {
register_code(KC_NO);
}
else {
unregister_code(KC_NO);
}
 break;
case A_NUM_YN:
if(record->event.pressed) {
register_code(KC_0);
}
else {
unregister_code(KC_0);
}
 break;
case A_NAV_NC:
if(record->event.pressed) {
register_code(KC_CAPS);
}
else {
unregister_code(KC_CAPS);
}
 break;
case A_NAV_YN:
if(record->event.pressed) {
register_code(KC_DEL);
}
else {
unregister_code(KC_DEL);
}
 break;
case A_NUM_NC:
if(record->event.pressed) {
register_code(KC_9);
}
else {
unregister_code(KC_9);
}
 break;
case A_NAV_CH:
if(record->event.pressed) {
register_code(KC_INS);
}
else {
unregister_code(KC_INS);
}
 break;
case A_BASE_SX:
if(record->event.pressed) {
register_code(KC_ENT);
}
else {
unregister_code(KC_ENT);
}
 break;
case A_BASE_JY:
if(record->event.pressed) {
register_code(KC_END);
}
else {
unregister_code(KC_END);
}
 break;
case A_BASE_BH:
if(record->event.pressed) {
register_code(KC_HOME);
}
else {
unregister_code(KC_HOME);
}
 break;
case A_BASE_FC:
if(record->event.pressed) {
SEND_STRING(SS_LCTL(SS_TAP(X_LEFT)));;
}
else {
}
 break;
case A_BASE_TN:
if(record->event.pressed) {
SEND_STRING(SS_LCTL(SS_TAP(X_RIGHT)));;
}
else {
}
 break;
case A_MATH_TF:
if(record->event.pressed) {
register_code(KC_NO);
}
else {
unregister_code(KC_NO);
}
 break;
case A_SYM_NC:
if(record->event.pressed) {
register_code(KC_NO);
}
else {
unregister_code(KC_NO);
}
 break;
case A_MATH_JT:
if(record->event.pressed) {
register_code(KC_NO);
}
else {
unregister_code(KC_NO);
}
 break;
case A_SYM_CH:
if(record->event.pressed) {
register_code(KC_NO);
}
else {
unregister_code(KC_NO);
}
 break;
case A_MATH_YN:
if(record->event.pressed) {
register_code(KC_NO);
}
else {
unregister_code(KC_NO);
}
 break;
case A_MATH_NC:
if(record->event.pressed) {
register_code(KC_NO);
}
else {
unregister_code(KC_NO);
}
 break;
 
  }
  return true;
};

