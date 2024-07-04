/// @description 여기에 설명 삽입
// 이 에디터에 코드를 작성할 수 있습니다





if (instance_number(obj_bird) % 13 != 0){
	move_towards_point(target_x, target_y, 10);
	if(point_distance(x, y, target_x, target_y) < 5) {
    // 속도를 0으로 설정하여 이동을 멈춤
    speed = 0;
	}
}else {
	move_towards_point(room_width+100, room_height-150, 7)
	instance_destroy(obj_bird)
}