extends CharacterBody2D

var direction: Vector2 = Vector2(1,1)
@export var speed: int = 200


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _physics_process(_delta: float) -> void:
	direction = Input.get_vector("left", "right", "up", "down")
	velocity = direction * speed
	animation()
	move_and_slide()
	
	if Input.is_action_just_released("space"):
		print("to binteo einai 3:23")   
func animation():
	if direction:
		if direction.x != 0 and direction.y == 0: 
			$AnimatedSprite2D.animation = 'left_right'
			$AnimatedSprite2D.flip_h = direction.x > 0
		if direction.y < 0 and direction.x == 0:
			$AnimatedSprite2D.animation = 'up'
		if direction.y > 0 and direction.x == 0:
			$AnimatedSprite2D.animation = 'down'
		if direction.x != 0 and direction.y != 0:
			$AnimatedSprite2D.animation = 'left_right'
			$AnimatedSprite2D.flip_h = direction.x > 0
	else:
		$AnimatedSprite2D.frame = 0

	 # Replace with function body.


func _on_area_2d_body_entered(_body: Node2D) -> void:
	print('victory') 
