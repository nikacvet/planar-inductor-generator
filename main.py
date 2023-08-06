from generator import Coordinates
import cadquery as cq

# init
n = 3
w = 2
s = 1
d_out = 50
# copy of d_out
d_tmp = d_out
metal_height = 2
height = 10

# get coordinates
cords = Coordinates()
# first layer
outline = Coordinates.create_coordinates(n,w,s,d_out,d_tmp)
# second layer
outline2 = [(x,((-1)*y) + d_tmp,-height) for x,y in outline]
# third layer
outline3 = [(x,y + d_tmp,-height*2) for x,y in Coordinates.rotate(outline,n,0,0,-90)]
# fourth layer
outline4 = [(((-1)*x + d_tmp),y + d_tmp,-height*(3)) for x,y in Coordinates.rotate(outline,n,0,0,-90)]
# fifth layer
outline5 = [((x + d_tmp),y + d_tmp,-height*(4)) for x,y in Coordinates.rotate(outline,n,0,0,-180)]
# sixth layer
#TODO IMPLEMENT

# via locations
end_outline3 = outline3[len(outline3) // 2]
start_outline4 = outline4[0]

# generate
result = (
    cq.Workplane()
    .polyline(outline) # first frame
    .close()
    .extrude(metal_height)
    .faces('<Z') # get end of outline face
    .moveTo(Coordinates.x_down + w / 2,Coordinates.y_down + w / 2) # move to vias start point
    .rect(w,w) # draw vias
    .extrude(-height) # extrude vias
    .faces('<Z') # get vias's Z face
    .polyline(outline2) # second frame starting from vias face
    .close()
    .extrude(2)
    .faces("<Z") # get face of frame
    .workplane()
    .moveTo(outline2[-1][0] + w / 2,-outline2[-1][1] + w / 2) # vias
    .rect(w,w)
    .extrude(height)
    .faces('>Z') # get vias face
    .workplane()
    .polyline(outline3) # frame 3
    .close()
    .extrude(-metal_height)
    .faces("<Z")
    .workplane()
    .moveTo(end_outline3[0] + w / 2,-end_outline3[1] - w / 2) # vias
    .rect(w,w)
    .extrude(height)
    .faces('>Z')
    .workplane()
    .polyline(outline4)
    .close()
    .extrude(-metal_height)
    .faces('<Z') # vias 4
    .workplane()
    .moveTo(outline4[-1][0] - w / 2,-outline4[-1][1] + w / 2)
    .rect(w,w)
    .extrude(height)
    .faces('>Z')
    .workplane()
    .polyline(outline5)
    .close()
    .extrude(-metal_height)
    )

# export
cq.exporters.export(result, 'object1.step')

