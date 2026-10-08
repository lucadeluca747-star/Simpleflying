from ursina import *
import math





app = Ursina(title='cuber game', icon='textures/ursina.ico', fullscreen = True, developer_mode = False)

sky = Sky(texture='skybox.jpg', rotation=(0, 0, 0), scale=150)

ground = Entity(
    model='plane',
    scale=150,
    texture='grass', 
    texture_scale=(150, 150),
    collider='box'
)


cube = Entity(
    model='planee.obj',
    texture='plane_roughness.jpg',
    scale=0.3,
    position=(0, 1, 0),
    collider='box'
)


cam = EditorCamera()
cam.look_at(cube)
cam.rotation_x = 15
cam.rotation_y = 180
cam.parent = cube
cam.movement_speed = 0
cam.ignore_input = True
cam.position = (0, 10, 20)

def update():

    if held_keys['a']:
        cube.position += cube.left * 0.1
    if held_keys['d']:
        cube.position += cube.right * 0.1
    if held_keys['w']:
        cube.position -= cube.forward * 1

    if held_keys['s']:
        cube.position += cube.forward * 1

    if held_keys['e']:
        cube.rotation_y += 0.8
        cube.rotation_z -= 0.9
    if held_keys['q']:
        cube.rotation_y -= 0.8
        cube.rotation_z += 0.9
    if held_keys['m']:
        cube.rotation_x += 1
    if held_keys['n']:
        cube.rotation_x -= 1

    if held_keys['f']:
        cube.position = (0, 0, 0.5)
    

    if cube.rotation_z > 0:
        cube.rotation_z -= 0.35
    elif cube.rotation_z < 0:
        cube.rotation_z += 0.35
    else:
        pass
    if cube.rotation_x > 0:
        cube.rotation_x -= 0.15
    elif cube.rotation_x < 0:
        cube.rotation_x += 0.15
    else:
        pass



app.run()