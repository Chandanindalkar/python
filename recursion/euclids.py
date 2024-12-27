# base case: if (length % breadth) == 0
# recursive case: euclids(new_length, breadth)

def euclids(x, y, area=None):
    length = x if x > y else y
    breadth = y if y < x else x
    if area is None:
        area = x*y
        
    if (length % breadth) == 0:
        print('Biggest Square would be of size:', breadth, 'x', breadth)
        total_boxes = (area//(breadth*breadth))
        print('The plot can be divided into', total_boxes, 'biggest squares')
    else:
        biggest_boxes = length // breadth
        x = length - (biggest_boxes * breadth)
        euclids(x,breadth, area)

euclids(1680, 640)