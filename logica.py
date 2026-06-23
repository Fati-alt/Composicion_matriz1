def composicion(A, B):
    """
    Producto booleano entre dos matrices de relaciones.
    """

    n = len(A)

    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):

            C[i][j] = int(
                any(
                    A[i][k] and B[k][j]
                    for k in range(n)
                )
            )

    return C


def potencia(M, grado):

    n = len(M)

    if grado == 0:

        return [
            [1 if i == j else 0 for j in range(n)]
            for i in range(n)
        ]

    resultado = [fila[:] for fila in M]

    for _ in range(grado - 1):
        resultado = composicion(resultado, M)

    return resultado