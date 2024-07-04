/// @description 여기에 설명 삽입
// 이 에디터에 코드를 작성할 수 있습니다

draw_set_color(c_black)
//global.new_font = font_add("EF_jejudoldam(윈도우용_TTF).ttf", 40, true, false,32,12644)
//draw_set_font(global.new_font);

//draw_text_transformed(400, 50, obj_monkey.drop_sec_cnt,2,2,0)
draw_text_transformed(550, 50, current_hour,2,2,0)
draw_text_transformed(650, 50, current_minute,2,2,0)
draw_text_transformed(750, 50, current_second,2,2,0)
