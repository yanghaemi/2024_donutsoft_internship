/// @description 여기에 설명 삽입
// 이 에디터에 코드를 작성할 수 있습니다



if flag =0{
flag = 1

instance_create_depth(0,0,3, obj_bg_space)
obj_monkey.spd = 40/9.8
}
else{
	flag =0
	instance_destroy(obj_bg_space)
	instance_destroy(obj_drop_stone)
	obj_monkey.spd = 40
}

