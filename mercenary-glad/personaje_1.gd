extends CharacterBody3D

@onready var skeleton: Skeleton3D = $Armature/Skeleton3D

const SPEED = 5.0
const JUMP_VELOCITY = 4.5
const BONE_NAME = "Bone.007" 

var bone_id: int
# Guardamos la rotación original de fábrica del hueso
var rotacion_original: Quaternion 
# Aquí guardaremos el ángulo actual al que queremos llegar
var angulo_objetivo: float = 0.0 

func _ready() -> void:
	bone_id = skeleton.find_bone(BONE_NAME)
	# Guardamos la pose inicial del hueso como nuestra base
	rotacion_original = skeleton.get_bone_pose_rotation(bone_id)

func _physics_process(delta: float) -> void:
	# --- Gravedad y Movimiento del personaje (Tu código base) ---
	if not is_on_floor():
		velocity += get_gravity() * delta

	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	var input_dir := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	var direction := (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	if direction:
		velocity.x = direction.x * SPEED
		velocity.z = direction.z * SPEED
		var target_rotation = atan2(-direction.x, -direction.z)
		rotation.y = rotate_toward(rotation.y, target_rotation, delta * 10.0)
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		velocity.z = move_toward(velocity.z, 0, SPEED)

	move_and_slide()
	
	# --- CONTROL DEL ARMA ---
	# Ejemplo: Si presionas "flecha arriba" sube el ángulo, "flecha abajo" lo baja
	if Input.is_action_pressed("ui_up"):
		angulo_objetivo += 10.0 * delta # Sube suavemente el ángulo objetivo
	if Input.is_action_pressed("ui_down"):
		angulo_objetivo -= 10.0 * delta # Baja suavemente el ángulo objetivo
		
	# Limitamos el ángulo para que el brazo no dé una vuelta de 360 grados de terror
	angulo_objetivo = clamp(angulo_objetivo, -0.8, 0.8) 

	# Llamamos a la función de mover el hueso pasando el delta de tiempo
	suavizar_movimiento_hueso(delta)

func suavizar_movimiento_hueso(delta: float) -> void:
	# 1. Obtenemos la rotación que el hueso tiene EN ESTE MOMENTO
	var rotacion_actual = skeleton.get_bone_pose_rotation(bone_id)
	
	# 2. Creamos la rotación "objetivo" partiendo de la original modificada por el ángulo
	# Nota: Cambia Vector3.UP por Vector3.RIGHT o Vector3.FORWARD dependiendo de hacia dónde apunte tu hueso
	var modificacion_rotacion = Quaternion(Vector3.UP, angulo_objetivo)
	var destino_final = rotacion_original * modificacion_rotacion
	
	# 3. ¡LA MAGIA! Interpolamos de la rotación actual a la de destino.
	# El 5.0 es la velocidad de suavizado. Más alto = más rápido. Más bajo = más lento.
	var rotacion_suave = rotacion_actual.slerp(destino_final, 5.0 * delta)
	
	# 4. Aplicamos el resultado
	skeleton.set_bone_pose_rotation(bone_id, rotacion_suave)
