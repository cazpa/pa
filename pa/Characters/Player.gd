extends KinematicBody2D

const speed = 70

var moveDir = Vector2(0,0)
var spriteDir = "down"

func _physics_process(delta):
	controls_loop()
	movement_loop()
	spriteDir_loop()
	
	if moveDir != Vector2(0, 0):
		anim_switch("walk")
	else:
		anim_switch("idle")
	
func controls_loop():
	var left = Input.is_action_pressed("ui_left")
	var right = Input.is_action_pressed("ui_right")
	var up = Input.is_action_pressed("ui_up")
	var down = Input.is_action_pressed("ui_down")
	var fudown = Input.is_action_pressed("ui_page_up")
	
	moveDir.x = -int(left) + int(right) # Fix priority-issue when pressing multiple keys
	moveDir.y = -int(up) + int(down)
	
func movement_loop():
	var motion = moveDir.normalized() * speed
	move_and_slide(motion, Vector2(0,0))

func spriteDir_loop():
	match moveDir:
		Vector2(-1, 0):
			spriteDir = "left"
		Vector2(1, 0):
			spriteDir = "right"
		Vector2(0, -1):
			spriteDir = "up"
		Vector2(0, 1):
			spriteDir = "down"
			
func anim_switch(animation):
	var newAnim = str(animation, spriteDir) # str(walk, up); str(run, left)
	if $Anim.current_animation != newAnim:
		$Anim.play(newAnim)
	if (Input.is_action_pressed("ui_page_up")):
         $Anim.play("fuforward")
	elif (Input.is_action_pressed("ui_page_down")):
		$Anim.play("fuleft")