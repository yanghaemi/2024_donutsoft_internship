/// @description 여기에 설명 삽입
// 이 에디터에 코드를 작성할 수 있습니다

draw_set_color(c_black)
global.new_font = font_add("EF_jejudoldam(윈도우용_TTF).ttf", 40, true, false,32,12644)
draw_set_font(global.new_font);

draw_text(400, 50, "현재 시간: ")
draw_text(680, 50, current_hour)
draw_text(780, 50, current_minute)
draw_text(880, 50, current_second)
