/// @description 여기에 설명 삽입
// 이 에디터에 코드를 작성할 수 있습니다




if 7 <=current_hour <= 16 {
	sprite_index=spr_sky
}
else if 16 < current_hour <= 21{
	sprite_index=spr_sky3
}
else if 21 < current_hour <24 or 0<= current_hour < 7{
	sprite_index=spr_sky3
}
else{
	sprite_index=spr_sky2
}