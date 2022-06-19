def rgb_to_xyz(rgb):
    
    R = rgb[0]
    G = rgb[1]
    B = rgb[2]
    
    var_R = ( R / 255 )
    var_G = ( G / 255 )
    var_B = ( B / 255 )

    if ( var_R > 0.04045 ):
        var_R = ( ( var_R + 0.055 ) / 1.055 ) ** 2.4
    else:
        var_R = var_R / 12.92
    if ( var_G > 0.04045 ):
        var_G = ( ( var_G + 0.055 ) / 1.055 ) ** 2.4
    else:
        var_G = var_G / 12.92
    if ( var_B > 0.04045 ):
        var_B = ( ( var_B + 0.055 ) / 1.055 ) ** 2.4
    else:
        var_B = var_B / 12.92

    var_R = var_R * 100
    var_G = var_G * 100
    var_B = var_B * 100

    X = var_R * 0.4124 + var_G * 0.3576 + var_B * 0.1805
    Y = var_R * 0.2126 + var_G * 0.7152 + var_B * 0.0722
    Z = var_R * 0.0193 + var_G * 0.1192 + var_B * 0.9505

    return (X,Y,Z)

def XYZ_to_CIELAB(XYZ):
    X = XYZ[0]
    Y = XYZ[1]
    Z = XYZ[2]
    
    var_X = X / 95.047
    var_Y = Y / 100.000
    var_Z = Z / 108.883

    if ( var_X > 0.008856 ):
        var_X = var_X ** ( 1/3 )
    else:
        var_X = ( 7.787 * var_X ) + ( 16 / 116 )
    if ( var_Y > 0.008856 ):
        var_Y = var_Y ** ( 1/3 )
    else:
        var_Y = ( 7.787 * var_Y ) + ( 16 / 116 )
    if ( var_Z > 0.008856 ):
        var_Z = var_Z ** ( 1/3 )
    else:
        var_Z = ( 7.787 * var_Z ) + ( 16 / 116 )

    CIE_L = ( 116 * var_Y ) - 16
    CIE_a = 500 * ( var_X - var_Y )
    CIE_b = 200 * ( var_Y - var_Z )
    
    return (CIE_L, CIE_a, CIE_b)
    
def distance(RGB1,RGB2, k_L = 2, K1 = 0.0048, K2 = 0.014, k_c = 1, k_H = 1):
    
    XYZ1 = rgb_to_xyz(RGB1)
    XYZ2 = rgb_to_xyz(RGB2)
    
    CIE1 = XYZ_to_CIELAB(XYZ1)
    CIE2 = XYZ_to_CIELAB(XYZ2)
    
    CIE_L1 = CIE1[0]
    CIE_a1 = CIE1[1]
    CIE_b1 = CIE1[2]
    
    CIE_L2 = CIE2[0]
    CIE_a2 = CIE2[1]
    CIE_b2 = CIE2[2]
    
    delta_L = CIE_L1-CIE_L2
    
    C1 = np.sqrt(CIE_a1**2 + CIE_b1**2)
    C2 = np.sqrt(CIE_a2**2 + CIE_b2**2)
    
    delta_Cab = C1-C2
    
    delta_Hab = np.sqrt( (CIE_a1 - CIE_a2)**2 + (CIE_b1 - CIE_b2)**2 - delta_Cab**2 )
    
    S_L = 1
    S_C = 1 + K1 * C1
    S_H = 1 + K2 * C1
    
    distance = np.sqrt((delta_L/(k_L*S_L))**2 + (delta_Cab/(k_c * S_C))**2 + (delta_Hab/(k_H*S_H))**2)
    
    return distance