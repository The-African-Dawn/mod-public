asset_template = '''
entity = {{
    clone = "infantry_2_entity"
    name = "{tag}_infantry_entity"
    pdxmesh = "{tag}_infantry_mesh"

    attach = {{ 	name = "rifle1"	Right_Hand_node = "ak74_right_entity" }}
    attach = {{ 	name = "rifle2"	Left_Hand_node 	= "ak74_left_entity" }}
    attach = {{ 	name = "rifle3"	mid_back_node 	= "ak74_long_idle_entity" }}
    attach = {{ 	name = "rifle4"	Root_node_2 	= "ak74_right_entity" }}

    scale = 1
}}

entity = {{
    clone = "{tag}_infantry_entity"
    name = "{tag}_infantry_2_entity"
    
    attach = {{ 	name = "rifle1"	Right_Hand_node = "m16_no_gp_right_entity" }}
    attach = {{ 	name = "rifle2"	Left_Hand_node 	= "m16_no_gp_left_entity" }}
    attach = {{ 	name = "rifle3"	mid_back_node 	= "m16_no_gp_long_idle_entity" }}
    attach = {{ 	name = "rifle4"	Root_node_2 	= "m16_no_gp_right_entity" }}
}}

entity = {{
    clone = "{tag}_infantry_2_entity"
    name = "{tag}_infantry_3_entity"
    
    attach = {{ 	name = "rifle1"	Right_Hand_node = "qbz95_right_entity" }}
    attach = {{ 	name = "rifle2"	Left_Hand_node 	= "qbz95_left_entity" }}
    attach = {{ 	name = "rifle3"	mid_back_node 	= "qbz95_long_idle_entity" }}
    attach = {{ 	name = "rifle4"	Root_node_2 	= "qbz95_right_entity" }}
}}

entity = {{
    clone = "{tag}_infantry_3_entity"
    name = "{tag}_infantry_4_entity"
    
    attach = {{ 	name = "rifle1"	Right_Hand_node = "famas_right_entity" }}
    attach = {{ 	name = "rifle2"	Left_Hand_node 	= "famas_left_entity" }}
    attach = {{ 	name = "rifle3"	mid_back_node 	= "famas_long_idle_entity" }}
    attach = {{ 	name = "rifle4"	Root_node_2 	= "famas_right_entity" }}
}}
entity = {{
	clone = "{tag}_infantry_3_entity"
	name = "{tag}_infantry_50_entity"
	
	attach = {{ 	name = "rifle1"	Right_Hand_node = "ak12_right_entity" }}
	attach = {{ 	name = "rifle2"	Left_Hand_node 	= "ak12_left_entity" }}
	attach = {{ 	name = "rifle3"	mid_back_node 	= "ak12_long_idle_entity" }}
	attach = {{ 	name = "rifle4"	Root_node_2 	= "ak12_right_entity" }}
}}
entity = {{
	clone = "{tag}_infantry_3_entity"
	name = "{tag}_infantry_6_entity"
	
	attach = {{ 	name = "rifle1"	Right_Hand_node = "qbz191_right_entity" }}
	attach = {{ 	name = "rifle2"	Left_Hand_node 	= "qbz191_left_entity" }}
	attach = {{ 	name = "rifle3"	mid_back_node 	= "qbz191_long_idle_entity" }}
	attach = {{ 	name = "rifle4"	Root_node_2 	= "qbz191_right_entity" }}
}}
entity = {{
	clone = "{tag}_infantry_3_entity"
	name = "{tag}_infantry_20_entity"
	
	attach = {{ 	name = "rifle1"	Right_Hand_node = "xm7_right_entity" }}
	attach = {{ 	name = "rifle2"	Left_Hand_node 	= "xm7_left_entity" }}
	attach = {{ 	name = "rifle3"	mid_back_node 	= "xm7_long_idle_entity" }}
	attach = {{ 	name = "rifle4"	Root_node_2 	= "xm7_right_entity" }}
}}
entity = {{
	clone = "{tag}_infantry_3_entity"
	name = "{tag}_infantry_25_entity"

	attach = {{ 	name = "rifle1"	Right_Hand_node = "m16_right_entity" }}
	attach = {{ 	name = "rifle2"	Left_Hand_node 	= "m16_left_entity" }}
	attach = {{ 	name = "rifle3"	mid_back_node 	= "m16_long_idle_entity" }}
	attach = {{ 	name = "rifle4"	Root_node_2 	= "m16_right_entity" }}

	scale = 1
}}
entity = {{
	clone = "{tag}_infantry_3_entity"
	name = "{tag}_infantry_0_entity"

	attach = {{ 	name = "rifle1"	Right_Hand_node = "kustar_right_entity" }}
	attach = {{ 	name = "rifle2"	Left_Hand_node 	= "kustar_left_entity" }}
	attach = {{ 	name = "rifle3"	mid_back_node 	= "kustar_long_idle_entity" }}
	attach = {{ 	name = "rifle4"	Root_node_2 	= "kustar_right_entity" }}

	scale = 1
}}
entity = {{
    clone = "{tag}_infantry_3_entity"
    name = "{tag}_infantry_40_entity"
    
    attach = {{ 	name = "rifle1"	Right_Hand_node = "hk416_right_entity" }}
    attach = {{ 	name = "rifle2"	Left_Hand_node 	= "hk416_left_entity" }}
    attach = {{ 	name = "rifle3"	mid_back_node 	= "hk416_long_idle_entity" }}
    attach = {{ 	name = "rifle4"	Root_node_2 	= "hk416_right_entity" }}
}}
entity = {{
	name = "{tag}_motorized_entity"
	pdxmesh = "motorized_frame_mesh"
	
	state = {{ name = "idle"				animation = "idle" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "retreat"			animation = "move" 	 				animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "training"			animation = "idle" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "death"			animation = "idle" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "support_attack"	animation = "attack" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "attack"			animation = "attack" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "defend"			animation = "attack" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "move"				animation = "move" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	scale = 1.0
	
	attach = {{ 	name = "vehicle"			vehicle = "generic_motorized_vehicle_entity" }}
	attach = {{ 	name = "infantry"			infantry = "{tag}_infantry_entity" }}
}}
entity = {{
	name = "{tag}_bmp_infantry_entity"
	pdxmesh = "motorized_frame_mesh"
	
	state = {{ name = "idle"				animation = "idle" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "retreat"			animation = "move" 	 				animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "training"			animation = "idle" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "death"			animation = "idle" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "support_attack"	animation = "attack" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "attack"			animation = "attack" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "defend"			animation = "attack" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "move"				animation = "move" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	scale = 1.0
	
	attach = {{ 	name = "vehicle"			vehicle = "bmp1_entity" }}
	attach = {{ 	name = "infantry"			infantry = "{tag}_infantry_entity" }}
}}
entity = {{
	name = "{tag}_btr_entity"
	pdxmesh = "motorized_frame_mesh"
	
	state = {{ name = "idle"				animation = "idle" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "retreat"			animation = "move" 	 				animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "training"			animation = "idle" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "death"			animation = "idle" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "support_attack"	animation = "attack" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "attack"			animation = "attack" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "defend"			animation = "attack" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	state = {{ name = "move"				animation = "move" 					animation_blend_time = 0.3 animation_speed = 1.0 }}
	scale = 1.0
	
	attach = {{ 	name = "vehicle"			vehicle = "btr60_entity" }}
	attach = {{ 	name = "infantry"			infantry = "{tag}_infantry_entity" }}
}}
'''