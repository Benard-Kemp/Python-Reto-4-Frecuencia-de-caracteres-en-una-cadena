def frecuencia_caracteres(texto: str | None) -> dict:
    """
    Cuenta la frecuencia de cada carácter en una cadena.

    Reglas:
    - None -> {}
    - No str -> TypeError
    - str -> diccionario {caracter: frecuencia}
    """
    if texto is None:
        return {}

    if not isinstance(texto, str):
        raise TypeError("El parámetro 'texto' debe ser una cadena (str) o None.")

    frecuencias = {}

    for caracter in texto:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1

    return frecuencias
