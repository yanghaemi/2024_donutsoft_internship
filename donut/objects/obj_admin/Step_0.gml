/// @description 여기에 설명 삽입
// 이 에디터에 코드를 작성할 수 있습니다

var odd = irandom(1300)


if(obj_mode_change_btn.flag = 0){
	if delay = 0 {
		instance_create_depth(odd, -100, 1, obj_drop)
		delay = 60
		//room_speed
	}

	if delay > 0{
		delay --
	}
}

if(obj_mode_change_btn.flag = 1){
	if delay = 0 {
		instance_create_depth(odd, -100, 0, obj_drop_stone)
		delay = 80
		//room_speed
	}

	if delay > 0{
		delay --
	}
}







