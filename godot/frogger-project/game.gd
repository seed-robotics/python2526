extends Node2D
var score: int

var car_scene: PackedScene = preload('res://scenes/car.tscn')

func _ready() -> void:
	pass # Replace with function body.

func _process(delta: float) -> void:
	pass

func _on_car_timer_timeout() -> void:
	var car = car_scene.instantiate() as Area2D
	var pos_marker = $CarStartPositions.get_children().pick_random() as Marker2D
	car.position = pos_marker.position
	$Oblects.add_child(car)
	car.connect("body_entered", _go_to_title)

func _go_to_title(_test):
	call_deferred("scene_change")

func _on_timer_timeout() -> void:
	score += 1
	$CanvasLayer/Label.text = str(score)

func _on_area_2d_body_entered(_body: Node2D) -> void:
	call_deferred("scene_change")
	if score < Global.score:
		Global.score = score

func scene_change():
	get_tree().change_scene_to_file("res://scenes/title.tscn")
