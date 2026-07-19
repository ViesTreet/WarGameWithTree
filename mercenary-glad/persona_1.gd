extends CharacterBody3D

@export var angle: float
@export var lenght: float
@export var direction = Vector3.FORWARD

# 1. Cambia esto por la ruta real a tu nodo MeshInstance3D del MODELO 3D (el cuerpo)
@onready var cuerpo_mesh: MeshInstance3D = $Armature/Skeleton3D/Cube
@onready var mesh_instance_lineas: MeshInstance3D = $MeshInstance3D # El de las líneas

var objetivo: Node3D
var immediate_mesh: ImmediateMesh
var material_lineas: ORMMaterial3D
var material_cuerpo: BaseMaterial3D # Guardará el material de tu personaje
var angleRad: float

func _ready() -> void:
	angleRad = deg_to_rad(angle)
	
	# Configurar las líneas
	immediate_mesh = mesh_instance_lineas.mesh as ImmediateMesh
	material_lineas = ORMMaterial3D.new()
	material_lineas.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	material_lineas.albedo_color = Color.RED
	
	# 2. OBTENER Y DUPLICAR EL MATERIAL DEL CUERPO
	# Al duplicarlo (.duplicate()), evitamos que todos los personajes se vuelvan verdes a la vez
	if cuerpo_mesh.get_active_material(0):
		material_cuerpo = cuerpo_mesh.get_active_material(0).duplicate()
		cuerpo_mesh.set_surface_override_material(0, material_cuerpo)
	
	objetivo = get_tree().get_first_node_in_group("objetivos") as Node3D

func _physics_process(_delta: float) -> void:
	if objetivo and isInCone():
		# 3. CAMBIAR ALBEDO A VERDE
		if material_cuerpo:
			material_cuerpo.albedo_color = Color.GREEN
	else:
		# 4. VOLVER AL COLOR ORIGINAL (Blanco/Normal)
		if material_cuerpo:
			material_cuerpo.albedo_color = Color.WHITE

func _process(_delta: float) -> void:
	var left_dir = direction.rotated(Vector3.UP, angleRad / 2) * lenght
	var right_dir = direction.rotated(Vector3.UP, -angleRad / 2) * lenght
	
	immediate_mesh.clear_surfaces()
	immediate_mesh.surface_begin(Mesh.PRIMITIVE_LINES, material_lineas)
	
	immediate_mesh.surface_add_vertex(Vector3.ZERO)
	immediate_mesh.surface_add_vertex(left_dir)
	
	immediate_mesh.surface_add_vertex(Vector3.ZERO)
	immediate_mesh.surface_add_vertex(right_dir)
	
	immediate_mesh.surface_end()

func isInCone() -> bool:
	var target_local_pos = to_local(objetivo.global_position)
	var target_dir_flat = Vector3(target_local_pos.x, 0, target_local_pos.z)
	
	if target_dir_flat.length() > lenght:
		return false
		
	var angle_to_target = direction.angle_to(target_dir_flat.normalized())
	return abs(angle_to_target) <= (angleRad / 2)
