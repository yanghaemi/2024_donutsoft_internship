/// @description 여기에 설명 삽입
// 이 에디터에 코드를 작성할 수 있습니다

var odd_x=irandom(1200)
var odd_y = irandom(200)
var odd_flower = irandom(2)

drop_sec_cnt ++
sprite_index = spr_monkey_act

if odd_flower =1{
instance_create_depth(odd_x+20, odd_y+600, 3, obj_flower)
}
else{
instance_create_depth(odd_x+20, odd_y+600, 3, obj_flower2)
}

if drop_sec_cnt % 60 =0{
	instance_destroy(obj_flower)
	instance_destroy(obj_flower2)
}


if drop_sec_cnt % 21600 =0{
	if odd_flower{
	instance_create_depth(-100, odd_y, 0, obj_bird)
	}
	else {
	instance_create_depth(room_width+5, odd_y, 0, obj_bird)
	}
	instance_create_depth(0,506,0,obj_drop_stone)
}


