import math

def distance(p1, p2):
    return math.dist(p1, p2)

def vector(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def is_perpendicular(v1, v2):
    return dot_product(v1, v2) == 0

def is_parallel(v1, v2):
    return v1[0]*v2[1] == v1[1]*v2[0]

def classify_quadrilateral(A, B, C, D):
    # Vektorlar
    AB = vector(A, B)
    BC = vector(B, C)
    CD = vector(C, D)
    DA = vector(D, A)

    # Tomon uzunliklari
    AB_len = distance(A, B)
    BC_len = distance(B, C)
    CD_len = distance(C, D)
    DA_len = distance(D, A)

    # Diagonallar
    AC = distance(A, C)
    BD = distance(B, D)

    # To‘g‘ri burchaklar tekshiruvi
    right_angles = (
        is_perpendicular(AB, BC) and
        is_perpendicular(BC, CD) and
        is_perpendicular(CD, DA) and
        is_perpendicular(DA, AB)
    )

    # Parallel tomonlar tekshiruvi
    parallel1 = is_parallel(AB, CD)
    parallel2 = is_parallel(BC, DA)

    if parallel1 and parallel2:
        if right_angles:
            return "To‘g‘ri burchakli to‘rtburchak"
        elif AB_len == BC_len == CD_len == DA_len:
            return "Romb"
        else:
            return "Parallelogram"
    elif parallel1 or parallel2:
        return "Trapetsiya"
    else:
        return "To‘rtburchak yasash mumkin emas"

# --- FOYDALANUVCHI KIRITADI ---
try:
    x1, y1 = map(float, input("A nuqta (x1 y1): ").split())
    x2, y2 = map(float, input("B nuqta (x2 y2): ").split())
    x3, y3 = map(float, input("C nuqta (x3 y3): ").split())
    x4, y4 = map(float, input("D nuqta (x4 y4): ").split())

    A = (x1, y1)
    B = (x2, y2)
    C = (x3, y3)
    D = (x4, y4)

    result = classify_quadrilateral(A, B, C, D)
    print("Natija:", result)

except Exception as e:
    print("Xatolik:", e)
