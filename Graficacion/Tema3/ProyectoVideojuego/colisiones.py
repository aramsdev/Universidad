def rombo_colision(PosObj2X, PosObj2Y, PosObj2Z, Obj2_width, Obj2_height, Obj2_depth
                   ,PosObj1X, PosObj1Y, PosObj1Z, Ob1_height):
    
    Obj2_rombo = (
        (PosObj2X - Obj2_width / 2, PosObj2Y, PosObj2Z),
        (PosObj2X, PosObj2Y, PosObj2Z - Obj2_depth / 2),
        (PosObj2X + Obj2_width / 2, PosObj2Y, PosObj2Z),
        (PosObj2X, PosObj2Y + Obj2_height, PosObj2Z)
    )
    
    Obj1_rombo = (
        (PosObj1X - 0.5, PosObj1Y, PosObj1Z),
        (PosObj1X, PosObj1Y, PosObj1Z - 0.5),
        (PosObj1X + 0.5, PosObj1Y, PosObj1Z),
        (PosObj1X, PosObj1Y + Ob1_height, PosObj1Z)
    )
    
    for p1 in Obj2_rombo:
        for p2 in Obj1_rombo:
            if abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) <= 1.0:
                return True
    return False