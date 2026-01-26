import streamlit as st
#Estudio de carga combustible
# Datos del área
name_area = st.text_input("Ingrese nombre de área a evaluar: ")
print("--------------------------------------------------------------------------------")
print("Ingrese el número del destino del edificio:")
print("1. Combustibles, lubricantes, aceites minerales y naturales")
print("2. Establecimientos industriales")
print("3. Supermercados y Centros Comerciales")
print("4. Establecimientos de bodegaje")

destino = input("Ingrese el número aquí: ").strip()

try:
    destino = int(destino)  # Convertimos a entero
except ValueError:
    print("Opción incorrecta: debe ingresar un número del 1 al 4.")
else:
    if destino == 1:
        print("El destino de la edificación evaluada es Combustibles, lubricantes, aceites minerales y naturales")
    elif destino == 2:
        print("El destino de la edificación evaluada es Establecimientos industriales")
    elif destino == 3:
        print("El destino de la edificación evaluada es Supermercados y Centros Comerciales")
    elif destino == 4:
        print("El destino de la edificación evaluada es Establecimientos de bodegaje")
    else:
        print("Opción incorrecta: elija un número del 1 al 4.")

print("-" * 80)    
        
cant_pisos = input("Ingrese el número de pisos del edificio evaluado: ")   
print("---------------------------------------------------------------------------------")
# Cálculo de metros cuadrados del área
largo = float(input("Ingrese el largo del área: "))
ancho = float(input("Ingrese el ancho del área: "))
m2 = largo * ancho
print (f"{name_area} posee {m2} metros cuadrados")

print("-" * 80)
print("Listado de materiales y poder calorífico según NCH1916")
print("----------------------")

calor_comb = {"aceite comestible": 46, "aceite de alquitrán": 46, "aceite de colza": 41.9, "aceite de creosota": 37.5, "aceite de hígado": 37.5, "aceite de lino": 37.5,"aceite de nabo silvestre": 41.9, "aceite de oliva": 41.9,"aceite de parafina": 41.9, "aceite de pino": 41.9, "aceite de ricino": 41.9, "aceite de semillas de algodón": 37.5, "aceite de soja": 41.9, "aceite diesel": 46, "aceite pesado de petróleo": 42.7, "acenilacetona": 25.1, "acetaldehído": 25.1, "acetamida": 20.9, "acetanilida": 33.5, "acetato de amilo": 33.5, "acetato de etilo": 25.5, "acetato de metilo": 21.3, "acetato de polivinilo": 20.9, "acetileno": 50.2, "acetileno (gas)": 49.8, "acetofenona": 33.5, "acetona": 30.6, "acetonitrilo": 29.3, "acido acético": 16.8, "acido acrílico": 18, "acido acroleico": 16.8, "acido adípico": 22.3, "acido benzoico": 25.1, "acido butírico n-": 25.1, "acido caprónico": 29.3, "acido cianocético": 16.8, "acido cítrico": 25.1, "acido de canela": 29.3, "acido dietilacético": 29.3, "acido etilbutírico": 29.3, "acido fórmico": 5.9, "acido oleico": 37, "acido oxálico n-": 29.3, "acido tartárico": 6.7, "acroleína": 29.3, "alanina": 16.8, "albúmina vegetal": 25.1, "alcanfor": 37.5, "alcohol alílico": 33.5, "alcohol amílico": 41.9, "alcohol cetílico": 41.9, "alcohol de benzilo": 33.5, "alcohol etílico": 29.7, "alcohol hexadehílico": 41.9, "alcohol isopropílico": 30.2, "alcohol metílico": 22.2, "alcohol n-butílico": 33.6, "alcohol propílico": 30.7, "aldehido de canela": 33.5, "aldehido fórmico": 29.8, "aldehido propílico": 29, "aldol": 25.1, "algodón": 16.8, "almendra": 16.8, "almidón": 16.8, "alquitrán de hulla": 37.2, "anhídrido de ácido acético": 16.8, "anhídrido de ácido benzoico": 29.3, "anhídrido ftálico": 21.4, "anhídrido propiónico": 22.3, "anilina": 37.5, "anisol": 33.5, "antraceno": 41.9, "antracita": 33.5, "antraquinona": 29.3, "arabinosa": 16.8, "asfalto": 40.4, "avellanas": 16.8, "azobenzol": 33.5, "azoxibenzol": 33.5, "azúcar": 16.8, "azúcar de caña": 16.8, "azufre": 8.4, "bambú, caña de": 16.8, "basuras orgánicas secas": 8.4, "benceno": 41.9, "bencilo": 33.5, "bencina": 41.9, "benzacetona": 33.5, "benzaldehído": 33.5, "benzidina": 33.5, "benzil": 33.5, "benzilamina": 37.5, "benzofenona": 33.5, "benzoina": 33.5, "benzol": 41.9, "bromuro de etilo": 7.6, "bromuro de metilo": 7.6, "butano": 46, "butanol": 33.5, "butano (gas)": 49.4, "cacao en polvo": 16.8, "café": 16.8, "cafeína": 20.9, "calcio": 40.2, "carbón briquetas de hulla": 33.5, "carbón coke de hulla": 29.3, "carbón de madera": 29.3, "carbón hulla": 33.5, "carbón lignita": 20.9, "carbón mineral": 25.1, "carburo de alúmina": 16.8, "carburo de aluminio": 16.8, "carne seca (charqui)": 25.1, "cartón": 16.8, "cartones bituminosos": 25.1, "caucho": 41.9, "caucho en planchas": 41.9, "caucho (neumáticos)": 25.1, "celuloide": 16.8, "celulosa": 17.6, "cera de parafina": 41.9, "cera mineral": 41.9, "ceras": 39.6, "cereales": 16.8, "cetanol": 41.9, "chocolate": 25.1, "cicloheptano": 46, "ciclohexano": 46, "ciclohexanol": 33.5, "ciclopentano": 46, "ciclopropano": 50.2, "cloroformo": 3.1, "cloropeno": 44.1, "cloruro de bencilo": 22.7, "cloruro de etilo": 18.9, "cloruro de metilo": 13.4, "cloruro de n-propilo": 23.9, "cloruro de polivinilo": 18.8, "coke": 33.5, "cola, engrudo": 37.5, "colodión": 16.8, "corcho": 16.8, "corcho (en placas)": 16.8, "corteza de roble": 16.8, "cresol": 33.5, "crotonaldehido": 33.5, "cuero": 18.6, "desechos de turba": 16.8, "diamitoléter": 41.9, "dicianuro": 20.9, "diclorobenzol": 16.8, "dietilamina": 41.9, "dietilcarbonato": 20.9, "dietilcetona": 33.5, "dietilester de ácido carbónico": 20.9, "dietilester de ácido malónico": 20.9, "dietileter de ácido oxálico": 20.9, "dietilmalonato": 20.9, "difenil": 41.9, "difenilamina": 37.8, "difeniletano": 41.9, "difenilo": 39.9, "dimetilamina": 18.5, "dimetil glicol": 16.8, "dinitro benceno": 16.8, "dipentano": 46, "estearina": 41.9, "estireno": 41.9, "etano": 50.2, "eter amílico": 41.9, "eter de petróleo": 41.9, "eter etilénico": 33.5, "eter etílico": 33.5, "eter metílico": 30, "etil amina": 34.4, "etil benceno": 41.2, "etileno": 50.2, "etilenglicol": 16.8, "extracto de malta": 12.6, "fenilhidracina": 31.3, "fenol": 33.5, "fenol, resina de": 25.1, "fenolacroleína": 33.5, "fibras de rafia, heno": 16.8, "fibras natulares": 16.8, "fósforo": 25.1, "furano": 25.1, "furfural": 23.5, "gas de alumbrado": 16.8, "gasolina": 47.3, "glicerina": 18, "goma dura": 33.6, "grafito": 31.5, "granos o gajos de uva": 16.8, "grasas": 41.9, "gutapercha": 46, "harina": 16.8, "hemetileno": 46, "heno comprimido": 16.8, "heno libre": 16.8, "heptano": 46, "hexametileno": 46, "hexano": 46, "hidrógeno": 142.3, "hidroquinona": 24.8, "hidróxido de magnesio": 16.8, "hidróxido de sodio": 8.4, "hidruro de aluminio": 20.9, "hidruro de magnesio": 16.8, "isobutano": 45.8, "isopentano": 45.4, "lana comprimida": 20.9, "lana de madera": 16.8, "lana natural": 22.8, "leche en polvo": 16.8, "libros y carpetas": 16.8, "lignito": 24.3, "lino": 16.8, "linóleo": 20.9, "madera de álamo": 16.8, "madera de coníferas": 16.8, "madera de contraplaca": 16.8, "madera de haya (helecho)": 20.9, "madera de hoguera (fuego)": 16.8, "madera de pino seco": 16.8, "madera de roble": 16.8, "madera dura exótica": 16.8, "magnesio": 25.1, "maicena": 16.8, "malta": 16.8, "malta, maíz": 16.8, "mantequilla": 37.8, "metracrilato de metilo": 25.5, "metano (gas)": 55.7, "metanol": 20.9, "metanol (alcohol metílico)": 20.9, "metilamina": 40.3, "metil butil cetona": 34.9, "metil etil cetona": 31.5, "metil propil cetona": 31.5, "monóxido de carbono": 8.4, "monóxido de carbono sulfurado": 8.4, "naftaleno": 39.1, "naftalina en cristales": 40.2, "nitrobenceno": 24.4, "nitrocelulosa": 8.4, "nitroetano": 16.4, "nitrometano": 10.5, "nueces, avellanas": 16.8, "nuez de coco": 20.9, "octano": 46, "oxido de carbono": 9.2, "oxido de etileno": 26.9, "paja natural": 14, "paja de madera": 16.8, "papel": 16.8, "parafina": 46, "pentano": 50.2, "pescado seco": 12.6, "petróleo": 41.9, "piperidina": 37.8, "placa de aglomerado de madera": 16.8, "poliamida":29.3, "policarbonato": 29.3, "poliester": 25.1, "poliestierno": 40.2, "poliestireno en espuma": 41.9, "polietileno": 46.5, "poliformaldehido": 16.8, "poliisobutileno": 46, "poliisopropeno (goma natural sin vulcanizar)": 45.2, "polipropileno": 46, "politetrafluoretileno": 4.2, "poliuretano": 25.1, "polivinilo acetato": 20.9, "polyamida": 29.3, "propano": 50.2, "propileno": 45.8, "resina de cresol": 25.1, "resina de fenol": 25.1, "resina de urea": 12.6, "resina sintética": 41.9, "ron 75%": 20.9, "seda": 20.9, "seda de acetato": 16.8, "sisal": 16.8, "sodio": 4.2, "sulfito de carbonilo": 8.4, "sulfuro de carbono": 12.6, "tabaco": 16.8, "té": 16.8, "tejido de algodón": 16.7, "tetrahidrobenzol": 46, "tolueno": 42.3, "toluol": 41.9, "triacetato": 16.8, "tributilamina": 40.3, "trietilamina": 39.9, "trimetil amina": 37.8, "turba": 25.1, "turba seca y prensada": 16.7, "urea": 8.4, "xilol": 41.9}

#El siguiente código nos arroja el listado de materiales y su calor en mj
for clave, valor in calor_comb.items():
    print(clave, valor)

# Variable acumuladora
suma_total = 0

while True:
    tipomat = input("Ingresa el material a evaluar: ").lower().strip()
    cal_comb = calor_comb.get(tipomat)

    if cal_comb is None:
        print("Error: El material ingresado no existe en la base de datos")
    else:
        cantidad = float(input("Ingresa la cantidad estimada de material (kg): "))
        total_mj = round(cal_comb * cantidad, 3)
        suma_total += total_mj  # acumulamos el total
        print(f"El calor de combustión de {tipomat} es {cal_comb} MJ/kg y el total es {total_mj} MJ")

    print("--------------------------------------------------------------------------------------------------")
    continuar = input("Desea ingresar otro material (1. Sí / 2. No): ").strip()
    if continuar == "2":
        print(f"La suma total de energía de todos los materiales ingresados es: {round(suma_total, 3)} MJ")
        break
print("-" * 80)
#Densidad de carga combustible media
Dcm = suma_total / m2
print(f"La densidad de carga combustible media de {name_area} es {Dcm:.3f}")

#Repetimos el proceso anterior, pero solo considerando la mayor carga de materiales en un área de 4 metros cuadrados
suma_ccpm = 0
print("-" * 80)
print("Cálculo Densidad carga combustible puntual máxima: ")
while True:
    tipomat = input("Ingresa el material a evaluar: ").lower().strip()
    cal_comb = calor_comb.get(tipomat)

    if cal_comb is None:
        print("Error: El material ingresado no existe en la base de datos")
    else:
        cantidad = float(input("Ingresa la cantidad estimada de material (kg): "))
        total_mj = round(cal_comb * cantidad, 3)
        suma_ccpm += total_mj  # acumulamos el total
        print(f"El calor de combustión de {tipomat} es {cal_comb} MJ/kg y el total es {total_mj} MJ")

    print("--------------------------------------------------------------------------------------------------")
    continuar = input("Desea ingresar otro material (1. Sí / 2. No): ").strip()
    if continuar == "2":
        print(f"La suma total de energía de todos los materiales ingresados, considerando 4 metros cuadrados es: {round(suma_ccpm, 3)} MJ")
        break
print("-" * 80)    
#Densidad de carga combustible puntual máxima
Dcpm = round(suma_ccpm / 4, 3)
print(f"La densidad de carga combustible puntual máxima de {name_area} es de {Dcpm} MJ") 

def clasificar_media(valor):
    if valor <= 500:
        return "DC₁"
    elif valor <= 1000:
        return "DC₂"
    elif valor <= 2000:
        return "DC₃"
    elif valor <= 4000:
        return "DC₄"
    elif valor <= 8000:
        return "DC₅"
    elif valor <= 16000:
        return "DC₆"
    else:
        return "DC₇"

def clasificar_puntual(valor):
    if valor <= 3500:
        return "DC₁"
    elif valor <= 6000:
        return "DC₂"
    elif valor <= 10000:
        return "DC₃"
    elif valor <= 16000:
        return "DC₄"
    elif valor <= 24000:
        return "DC₅"
    elif valor <= 32000:
        return "DC₆"
    else:
        return "DC₇"

# Mapa de prioridad (DC₇ es la más restrictiva)
prioridad = {
    "DC₁": 1,
    "DC₂": 2,
    "DC₃": 3,
    "DC₄": 4,
    "DC₅": 5,
    "DC₆": 6,
    "DC₇": 7
}

# Entrada del usuario
media = Dcm
puntual = Dcpm

# Clasificaciones individuales
clas_media = clasificar_media(media)
clas_puntual = clasificar_puntual(puntual)

# Selección de la más restrictiva
mas_restrictiva = clas_media if prioridad[clas_media] > prioridad[clas_puntual] else clas_puntual

# Resultados
print(f"Clasificación por densidad media: {clas_media}")
print(f"Clasificación por densidad puntual: {clas_puntual}")
print(f"Clasificación más restrictiva: {mas_restrictiva}")

# 4. Definición de la Tabla Normativa 
# Formato: [Límite Media (Sobre X), Límite Puntual (Sobre Y), "String de letras por piso"]
# Ordenado de mayor riesgo a menor riesgo.

tabla_normativa = {
    1: [ # Combustibles, lubricantes...
        (8000,  24000, "aaaaa"),
        (4000,  16000, "baaaa"),
        (2000,  10000, "cbaaa"),
        (-1,    -1,    "dcbaa") # Fila base (hasta 2000 / hasta 10000)
    ],
    2: [ # Establecimientos industriales
        (16000, 32000, "aaaaa"),
        (8000,  24000, "baaaa"),
        (4000,  16000, "cbaaa"),
        (2000,  10000, "ccbaa"),
        (1000,  6000,  "dccba"),
        (500,   3500,  "ddccb"),
        (-1,    -1,    "dddcc")
    ],
    3: [ # Supermercados
        (16000, 32000, "baaaa"),
        (8000,  24000, "bbaaa"),
        (4000,  16000, "cbbaa"),
        (2000,  10000, "ccbba"),
        (1000,  6000,  "dccbb"),
        (-1,    -1,    "ddccb")
    ],
    4: [ # Bodegaje
        (16000, 32000, "bbaaa"),
        (8000,  24000, "cbbaa"),
        (4000,  16000, "ccbba"),
        (2000,  10000, "dccbb"),
        (1000,  6000,  "ddccb"),
        (500,   3500,  "dddcc"),
        (-1,    -1,    "ddddc")
    ]
}

# 5. Lógica de Cruce (Determinación de la fila crítica)
if destino in tabla_normativa:
    filas = tabla_normativa[destino]
    
    # Encontramos en qué fila cae la Carga Media
    idx_media = len(filas) - 1 # Por defecto en la última fila
    for i, (lim_m, _, _) in enumerate(filas):
        if Dcm > lim_m:
            idx_media = i
            break
            
    # Encontramos en qué fila cae la Carga Puntual
    idx_puntual = len(filas) - 1 # Por defecto en la última fila
    for i, (_, lim_p, _) in enumerate(filas):
        if Dcpm > lim_p:
            idx_puntual = i
            break
            
    # CRITERIO DEL MAYOR VALOR:
    # Como la tabla está ordenada de mayor a menor riesgo, la fila con índice MENOR 
    # es la más peligrosa (está más arriba en la tabla).
    idx_final = min(idx_media, idx_puntual)
    
    # Selección de fila definitiva
    fila_datos = filas[idx_final]
    letras_pisos = fila_datos[2] # El string de letras, ej: "baaaa"
    
    # 6. Cruce con la cantidad de pisos (Columna)
    # Columna 0 = 1 piso, Columna 4 = 5 o más pisos
    col_idx = col_idx = int(cant_pisos) - 1
    if col_idx < 0: col_idx = 0
    if col_idx > 4: col_idx = 4 # Topeamos en 5 o más
    
    letra_resultado = letras_pisos[col_idx]
    
    # 7. Salida Final
    print("-" * 50)
    print(f"Clasificación según OGUC: CLASE {letra_resultado.upper()}")
    print("-" * 50)
    
else:
    print("Error: El destino seleccionado no tiene tabla normativa asociada.")   
    
# ==============================================================================
# SECCIÓN DE RESISTENCIA AL FUEGO (OGUC - Art. 4.3.3)
# ==============================================================================

print("\n" + "="*80)
print(f"--- REQUISITOS DE RESISTENCIA AL FUEGO (TIPO {letra_resultado.upper()}) ---")

# 1. Definición de Elementos de Construcción (Según tu imagen celeste)
elementos_construccion = {
    1: "Muros cortafuego",
    2: "Muros zona vertical de seguridad y caja de escalera",
    3: "Muros caja ascensores",
    4: "Muros divisorios entre unidades",
    5: "Elementos soportantes verticales",
    6: "Muros no soportantes y tabiques",
    7: "Escaleras",
    8: "Elementos soportantes horizontales",
    9: "Techumbre incluido techo falso"
}

# 2. Definición de la Tabla de Resistencia (Según tu imagen de tabla)
# Las claves son las letras (a, b, c, d) y los valores son listas con los F-ratings
# El orden de la lista corresponde a los elementos del 1 al 9.
tabla_resistencia = {
    'a': ["F-180", "F-120", "F-120", "F-120", "F-120", "F-30", "F-60", "F-120", "F-60"],
    'b': ["F-150", "F-120", "F-90",  "F-90",  "F-90",  "F-15", "F-30", "F-90",  "F-60"],
    'c': ["F-120", "F-90",  "F-60",  "F-60",  "F-60",  "-",    "F-15", "F-60",  "F-30"],
    'd': ["F-120", "F-60",  "F-60",  "F-60",  "F-30",  "-",    "-",    "F-30",  "F-15"]
}

# 3. Lógica de búsqueda y presentación
clave_letra = letra_resultado.lower() # Aseguramos que sea minúscula para buscar en el diccionario

if clave_letra in tabla_resistencia:
    resistencias = tabla_resistencia[clave_letra]
    
    print(f"{'ELEM.':<6} {'DESCRIPCIÓN':<55} {'RESISTENCIA':<10}")
    print("-" * 80)
    
    # Iteramos del 1 al 9 (indices 0 al 8 en la lista)
    for i in range(1, 10):
        nombre_elemento = elementos_construccion[i]
        valor_resistencia = resistencias[i-1] # Ajustamos índice (lista empieza en 0)
        
        # Formato de tabla alineada
        print(f"({i})    {nombre_elemento:<55} {valor_resistencia}")
        
    print("-" * 80)
    print("Nota: Los guiones (-) indican que no se exige resistencia específica.")
else:
    print(f"Error: La clasificación '{letra_resultado}' no existe en la tabla de resistencia.")

print("="*80)    


#Resumen de Resultados
print(f"El área evaluada es {name_area} la cual posee {m2} metros cuadrados")
print(f"La densidad de carga combustible media es de: {Dcm:.3f}")
print(f"La densidad de carga combustible puntual máxima es de: {Dcpm:.3f}")
print(f"La clasificación de acuerdo a NCh 1993 es: {mas_restrictiva}")
print(f"La clasificación de acuerdo a OGUC es: {letra_resultado.upper()}")
print("-" * 80)
print(f"Por lo tanto, la edificación debe tener materiales con la siguiente resistencia al fuego> ")
clave_letra = letra_resultado.lower() # Aseguramos que sea minúscula para buscar en el diccionario

if clave_letra in tabla_resistencia:
    resistencias = tabla_resistencia[clave_letra]
    
    print(f"{'ELEM.':<6} {'DESCRIPCIÓN':<55} {'RESISTENCIA':<10}")
    print("-" * 80)
    
    # Iteramos del 1 al 9 (indices 0 al 8 en la lista)
    for i in range(1, 10):
        nombre_elemento = elementos_construccion[i]
        valor_resistencia = resistencias[i-1] # Ajustamos índice (lista empieza en 0)
        
        # Formato de tabla alineada
        print(f"({i})    {nombre_elemento:<55} {valor_resistencia}")
        
    print("-" * 80)
    print("Nota: Los guiones (-) indican que no se exige resistencia específica.")
else:
    print(f"Error: La clasificación '{letra_resultado}' no existe en la tabla de resistencia.")

import webbrowser
print("\n" + "-"*80)
print("Ahora debes dirigirte al Listado Oficial de Comportamiento al Fuego de Elementos y Componentes de la Construcción para contrastar la RF de los materiales existentes en la edificación con la RF exigida en OGUC")
ver_web = input("¿Desea abrir el Listado Oficial? (si/no): ").lower().strip()

if ver_web == "si":
    # Link real al listado Oficial de Comportamiento al Fuego de Elementos y Componentes de la Construcción
    url = "https://www.minvu.gob.cl/wp-content/uploads/2025/02/Listado-Oficial-de-Comportamiento-al-Fuego-de-Elementos-y-Componentes-de-la-Construccion_-ED17-2025.pdf"
    webbrowser.open(url)

    print("Abriendo navegador...")

