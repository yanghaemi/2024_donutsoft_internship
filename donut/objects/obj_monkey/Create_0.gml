/// @description 여기에 설명 삽입
// 이 에디터에 코드를 작성할 수 있습니다

xx=x
yy= y

spd = 40

image_speed = 0

vspd = 0

drop_sec_cnt = current_second
repeat(current_hour%12){
	var odd_x=irandom(1200)
	var odd_y = irandom(250)
	
	
	instance_create_depth(-100, odd_y, 0, obj_bird)
}

repeat(current_second){
	var odd_x=irandom(1200)
	var odd_y = irandom(200)
	var odd_flower = irandom(2)	
	
	
	if odd_flower =1{
	instance_create_depth(odd_x+20, odd_y+600, 3, obj_flower)
	}
	else{
	instance_create_depth(odd_x+20, odd_y+600, 3, obj_flower2)
	}
}