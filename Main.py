from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from PIL import Image, ImageDraw

app = Ursina()
window.borderless = False

def create_block_texture():
    size = 64
    image = Image.new('RGB', (size, size), color=(160, 160, 160))  
    draw = ImageDraw.Draw(image)
    
    border = 6
    draw.rectangle([0, 0, size-1, size-1], outline=(30, 30, 30), width=border) #black  
    
    path = 'block_texture.png'
    image.save(path)
    return load_texture(path)

block_texture = create_block_texture()


# MAZE 




blocks = {}

# Floor
ground = Entity(model='plane', texture='white_cube', color=color.rgb(0, 50, 0), scale=(55, 1, 40), position=(27, -1, 20), collider='box')

# Walls
for z in range(len(maze)):
    for x in range(len(maze[z])):
        if maze[z][x] == 1:
            e = Entity(
                model='cube',
                texture=block_texture,
                position=(x, 0, z),
                scale=(1, 5, 1),
                collider='box'
            )

            blocks[(x, 0, z)] = e

# Player
player = FirstPersonController(position=(0, 1, 1), speed=20, mouse_sensitivity=Vec2(100))

# Exit
exit_zone = Entity(
    model='cube',
    color=color.red,
    position=(51, 1, 30),  
    scale=Vec3(0.8, 0.8, 0.8),
    collider='box'
)

# Win text
win_text = Text('', origin=(0, 0), scale=2, color=color.azure)

# Update fuction
def update():
    if distance(player.position, exit_zone.position) < 1:
        win_text.text = 'YOU WIN!'
    if held_keys['escape']:
        application.quit()

app.run()
