from ursina import*
from ursina.prefabs.first_person_controller  import FirstPersonController

app = Ursina()
Sky()
Player = FirstPersonController()

boxes = []
for n in range(30):
    for k in range(30):
        box = Button(
            parent= scene,
            model= "cube",
            origin_y= 0.5,
            texture= "white_cube",
            color= color.blue,
            highlight_color= color.lime,
            position= (k,0,n)
        )
        boxes.append(box)
def input(key):
    for box in boxes:
        if box.hovered:
            if key== 'left mouse down':
                newBox = Button(
                    parent= scene,
                    model= "cube",
                    origin_y= 0.5,
                    texture= "white_cube",
                    color= color.red,
                    hightlight_color= color.lime,
                    position= box.position + mouse.normal
                )
                boxes.append(newBox)
            if key== 'right mouse down':
                boxes.remove(box)
                destroy(box)
app.run()