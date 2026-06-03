extends Node2D

var car_scene: PackedScene = preload('res://scenes/car.tscn')
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_car_timer_timeout() -> void:
	var car = car_scene.instantiate() as Area2D
	var pos_marker = $CarStartPositions.get_children().pick_random() as Marker2D
	car.position = pos_marker.position
	$Oblects.add_child(car)
	car.connect("body_entered", _go_to_title)

func _go_to_title(_test):
	print('player lost')
	
