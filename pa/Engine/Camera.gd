extends Camera2D

func _process(delta):
	var pos = get_node("../Player").global_position - Vector2(0, 16)
	var x = floor(pos.x / 1920) * 1920 
	var y = floor(pos.y / 1184) * 1184 # 1200-16 for adjusting the hood