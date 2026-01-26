import streamlit as st
import pandas as pd
from fpdf import FPDF
import tempfile
import os

# Configuración de la página
st.set_page_config(page_title="Estudio de Carga Combustible", layout="wide")

st.title("🔥 Estudio de Carga Combustible")
st.markdown("Cálculo según NCh1916, NCh1993 y OGUC.")

# --- DICCIONARIOS DE DATOS ---
calor_comb = {
    "aceite comestible": 46, "aceite de alquitrán": 46, "aceite diesel": 46, "aceite pesado de petróleo": 42.7,
    "acetileno": 50.2, "acetona": 30.6, "acido acético": 16.8, "alcohol etílico": 29.7, 
    "alcohol metílico": 22.2, "algodón": 16.8, "asfalto": 40.4, "azúcar": 16.8, 
    "bencina": 41.9, "butano": 46, "cartón": 16.8, "caucho (neumáticos)": 25.1, 
    "celulosa": 17.6, "gasolina": 47.3, "glicerina": 18, "grasas": 41.9, 
    "harina": 16.8, "leche en polvo": 16.8, "libros y carpetas": 16.8, 
    "madera de pino seco": 16.8, "madera de roble": 16.8, "papel": 16.8, 
    "parafina": 46, "petróleo": 41.9, "plástico (polietileno)": 46.5, 
    "poliestireno": 40.2, "polivinilo acetato": 20.9, "propano": 50.2, 
    "ropa / textiles": 16.8, "tabaco": 16.8
}

elementos_construccion = {
    1: "Muros cortafuego", 2: "Muros zona vertical de seguridad y caja de escalera",
    3: "Muros caja ascensores", 4: "Muros divisorios entre unidades",
    5: "Elementos soportantes verticales", 6: "Muros no soportantes y tabiques",
    7: "Escaleras", 8: "Elementos soportantes horizontales",
    9: "Techumbre incluido techo falso"
}

tabla_resistencia = {
    'a': ["F-180", "F-120", "F-120", "F-120", "F-120", "F-30", "F-60", "F-120", "F-60"],
    'b': ["F-150", "F-120", "F-90",  "F-90",  "F-90",  "F-15", "F-30", "F-90",  "F-60"],
    'c': ["F-120", "F-90",  "F-60",  "F-60",  "F-60",  "-",    "F-15", "F-60",  "F-30"],
    'd': ["F-120", "F-60",  "F-60",  "F-60",  "F-30",  "-",    "-",    "F-30",  "F-15"]
}

# --- FUNCIONES AUXILIARES ---
def clean_text(text):
    return str(text).encode('latin-1', 'replace').decode('latin-1')

def crear_pdf(area, m2, dcm, dcpm, clas_nch, clas_oguc, resistencias, imagen_upload):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Título
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, clean_text(f"Informe de Carga Combustible: {area}"), ln=True, align='C')
    pdf.ln(5)
    
    # --- INSERTAR IMAGEN ---
    if imagen_upload is not None:
        try:
            # Aseguramos leer el archivo desde el inicio
            imagen_upload.seek(0) 
            
            # Guardamos la imagen temporalmente
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
                tmp_file.write(imagen_upload.read())
                tmp_path = tmp_file.name

            # Agregamos la imagen centrada (ancho 100mm)
            # x=55 centra aproximadamente en A4 (210mm ancho) -> (210-100)/2 = 55
            pdf.image(tmp_path, x=55, w=100)
            pdf.ln(5)
            
            # Borramos el archivo temporal
            os.remove(tmp_path)
        except Exception as e:
            pdf.set_font("Arial", 'I', 10)
            pdf.cell(0, 10, clean_text(f"No se pudo cargar la imagen: {e}"), ln=True)

    # Datos Generales
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, clean_text("1. Resumen de Resultados"), ln=True)
    pdf.set_font("Arial", size=11)
    
    pdf.cell(0, 8, clean_text(f"Área Total Evaluada: {m2} m2"), ln=True)
    pdf.cell(0, 8, clean_text(f"Densidad de Carga Media (Dcm): {dcm:.2f} MJ/m2"), ln=True)
    pdf.cell(0, 8, clean_text(f"Densidad de Carga Puntual (Dcpm): {dcpm:.2f} MJ/m2"), ln=True)
    pdf.cell(0, 8, clean_text(f"Clasificación NCh 1993: {clas_nch}"), ln=True)
    pdf.ln(5)
    
    # Clasificación OGUC
    pdf.set_font("Arial", 'B', 14)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(0, 10, clean_text(f"Clasificación OGUC: CLASE {clas_oguc}"), ln=True, fill=True, align='C')
    pdf.ln(10)
    
    # Tabla de Resistencia
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, clean_text("2. Exigencias de Resistencia al Fuego"), ln=True)
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(10, 8, "#", 1)
    pdf.cell(140, 8, clean_text("Elemento de Construcción"), 1)
    pdf.cell(30, 8, "Resistencia", 1, ln=True)
    
    pdf.set_font("Arial", size=10)
    if resistencias:
        for i in range(1, 10):
            nombre = elementos_construccion[i]
            valor = resistencias[i-1]
            pdf.cell(10, 8, str(i), 1)
            pdf.cell(140, 8, clean_text(nombre), 1)
            pdf.cell(30, 8, clean_text(valor), 1, ln=True)
    else:
        pdf.cell(0, 8, clean_text("No se encontraron datos de resistencia."), 1, ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'I', 8)
    pdf.cell(0, 10, clean_text("Informe generado automáticamente por la aplicación de Carga Combustible."), ln=True, align='C')
    
    # --- CORRECCIÓN FINAL ---
    # fpdf2 devuelve bytearray con dest='S', lo convertimos a bytes y listo.
    return bytes(pdf.output(dest='S'))

# --- 1. INGRESO DE DATOS ---
with st.container():
    st.header("1. Datos del Edificio")
    col1, col2 = st.columns(2)
    
    with col1:
        name_area = st.text_input("Nombre del área a evaluar:")
        
        opciones_destino = {
            1: "Combustibles, lubricantes, aceites minerales y naturales",
            2: "Establecimientos industriales",
            3: "Supermercados y Centros Comerciales",
            4: "Establecimientos de bodegaje"
        }
        
        destino = st.selectbox(
            "Destino del edificio:", 
            options=list(opciones_destino.keys()), 
            format_func=lambda x: f"{x}. {opciones_destino[x]}"
        )
        
        cant_pisos = st.number_input("Número de pisos:", min_value=1, step=1)

    with col2:
        largo = st.number_input("Largo (m):", min_value=0.1)
        ancho = st.number_input("Ancho (m):", min_value=0.1)
        m2 = largo * ancho
        st.info(f"📏 Área Total: **{m2:.2f} m²**")
        
        # --- UPLOAD DE IMAGEN ---
        st.markdown("**Imagen del Edificio / Plano (Opcional):**")
        imagen_archivo = st.file_uploader("Subir imagen (JPG/PNG)", type=["png", "jpg", "jpeg"])

# --- 2. GESTIÓN DE MATERIALES (SESSION STATE) ---
if 'materiales_general' not in st.session_state:
    st.session_state.materiales_general = []
if 'materiales_puntual' not in st.session_state:
    st.session_state.materiales_puntual = []

def agregar_material(tipo_lista, material, cantidad):
    calor = calor_comb[material]
    total = calor * cantidad
    st.session_state[tipo_lista].append({
        "Material": material,
        "MJ/kg": calor,
        "Cantidad (kg)": cantidad,
        "Total MJ": total
    })

# --- INTERFAZ DE CARGA ---
st.markdown("---")
st.header("2. Inventario de Materiales")

tab1, tab2 = st.tabs(["Carga General (Promedio)", "Carga Puntual (Máxima en 4m²)"])

# TAB 1: CARGA GENERAL
with tab1:
    col_mat1, col_mat2, col_mat3 = st.columns([3, 2, 1])
    with col_mat1:
        sel_mat_gen = st.selectbox("Seleccionar Material (General):", sorted(calor_comb.keys()), key="sel_gen")
    with col_mat2:
        cant_gen = st.number_input("Cantidad (kg):", min_value=0.0, step=0.1, key="cant_gen")
    with col_mat3:
        st.write("")
        st.write("")
        if st.button("Agregar a General"):
            if cant_gen > 0:
                agregar_material('materiales_general', sel_mat_gen, cant_gen)
                st.success("Agregado")

    if st.session_state.materiales_general:
        df_gen = pd.DataFrame(st.session_state.materiales_general)
        st.dataframe(df_gen, use_container_width=True)
        suma_total_gen = df_gen["Total MJ"].sum()
        if st.button("Limpiar lista General"):
            st.session_state.materiales_general = []
            st.rerun()
    else:
        st.info("No hay materiales agregados.")
        suma_total_gen = 0

# TAB 2: CARGA PUNTUAL
with tab2:
    st.markdown("Ingrese los materiales presentes en los **4 m²** de mayor concentración.")
    col_p1, col_p2, col_p3 = st.columns([3, 2, 1])
    with col_p1:
        sel_mat_pun = st.selectbox("Seleccionar Material (Puntual):", sorted(calor_comb.keys()), key="sel_pun")
    with col_p2:
        cant_pun = st.number_input("Cantidad (kg):", min_value=0.0, step=0.1, key="cant_pun")
    with col_p3:
        st.write("")
        st.write("")
        if st.button("Agregar a Puntual"):
            if cant_pun > 0:
                agregar_material('materiales_puntual', sel_mat_pun, cant_pun)
                st.success("Agregado")

    if st.session_state.materiales_puntual:
        df_pun = pd.DataFrame(st.session_state.materiales_puntual)
        st.dataframe(df_pun, use_container_width=True)
        suma_total_pun = df_pun["Total MJ"].sum()
        if st.button("Limpiar lista Puntual"):
            st.session_state.materiales_puntual = []
            st.rerun()
    else:
        st.info("No hay materiales para cálculo puntual.")
        suma_total_pun = 0


# --- 3. CÁLCULOS Y RESULTADOS ---
st.markdown("---")
st.header("3. Resultados del Análisis")

# Inicializamos variables
Dcm = 0
Dcpm = 0
clas_media = "N/A"
clas_puntual = "N/A"
mas_restrictiva = "N/A"
letra_resultado = "N/A"
resistencias_finales = []

if m2 > 0:
    Dcm = suma_total_gen / m2
    Dcpm = suma_total_pun / 4

    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric(label="Densidad de Carga Media (Dcm)", value=f"{Dcm:.2f} MJ/m²")
    with col_res2:
        st.metric(label="Densidad Puntual Máxima (Dcpm)", value=f"{Dcpm:.2f} MJ/m²")

    # Clasificación NCh
    def clasificar_media(valor):
        if valor <= 500: return "DC1"
        elif valor <= 1000: return "DC2"
        elif valor <= 2000: return "DC3"
        elif valor <= 4000: return "DC4"
        elif valor <= 8000: return "DC5"
        elif valor <= 16000: return "DC6"
        else: return "DC7"

    def clasificar_puntual(valor):
        if valor <= 3500: return "DC1"
        elif valor <= 6000: return "DC2"
        elif valor <= 10000: return "DC3"
        elif valor <= 16000: return "DC4"
        elif valor <= 24000: return "DC5"
        elif valor <= 32000: return "DC6"
        else: return "DC7"

    clas_media = clasificar_media(Dcm)
    clas_puntual = clasificar_puntual(Dcpm)

    prioridad = {"DC1": 1, "DC2": 2, "DC3": 3, "DC4": 4, "DC5": 5, "DC6": 6, "DC7": 7}
    try:
        if prioridad[clas_media] > prioridad[clas_puntual]:
            mas_restrictiva = clas_media
        else:
            mas_restrictiva = clas_puntual
    except:
        mas_restrictiva = "Error"

    st.subheader(f"Clasificación NCh 1993: **{mas_restrictiva}**")
    
    # Clasificación OGUC
    tabla_normativa = {
        1: [(8000, 24000, "aaaaa"), (4000, 16000, "baaaa"), (2000, 10000, "cbaaa"), (-1, -1, "dcbaa")],
        2: [(16000, 32000, "aaaaa"), (8000, 24000, "baaaa"), (4000, 16000, "cbaaa"), (2000, 10000, "ccbaa"), (1000, 6000, "dccba"), (500, 3500, "ddccb"), (-1, -1, "dddcc")],
        3: [(16000, 32000, "baaaa"), (8000, 24000, "bbaaa"), (4000, 16000, "cbbaa"), (2000, 10000, "ccbba"), (1000, 6000, "dccbb"), (-1, -1, "ddccb")],
        4: [(16000, 32000, "bbaaa"), (8000, 24000, "cbbaa"), (4000, 16000, "ccbba"), (2000, 10000, "dccbb"), (1000, 6000, "ddccb"), (500, 3500, "dddcc"), (-1, -1, "ddddc")]
    }

    filas = tabla_normativa.get(destino, [])
    
    idx_media = len(filas) - 1
    for i, (lim_m, _, _) in enumerate(filas):
        if Dcm > lim_m:
            idx_media = i
            break
            
    idx_puntual = len(filas) - 1
    for i, (_, lim_p, _) in enumerate(filas):
        if Dcpm > lim_p:
            idx_puntual = i
            break
            
    idx_final = min(idx_media, idx_puntual)
    if filas:
        letra_resultado = filas[idx_final][2][min(max(int(cant_pisos) - 1, 0), 4)].upper()
    else:
        letra_resultado = "N/A"

    st.success(f"## Clasificación OGUC: CLASE {letra_resultado}")

    # Tabla Resistencia
    st.markdown("### Requisitos de Resistencia al Fuego")
    clave_letra = letra_resultado.lower()
    if clave_letra in tabla_resistencia:
        resistencias_finales = tabla_resistencia[clave_letra]
        datos_tabla = []
        for i in range(1, 10):
            datos_tabla.append({
                "Elemento": elementos_construccion[i],
                "Resistencia Exigida": resistencias_finales[i-1]
            })
        st.table(pd.DataFrame(datos_tabla))
    
    # --- BOTÓN DE DESCARGA PDF ---
    st.markdown("---")
    if letra_resultado != "N/A":
        # Llamamos a la función crear_pdf pasando también la imagen (si existe)
        pdf_bytes = crear_pdf(
            name_area, m2, Dcm, Dcpm, mas_restrictiva, letra_resultado, resistencias_finales, 
            imagen_archivo # <--- Aquí pasamos la imagen subida
        )
        
        st.download_button(
            label="📄 Descargar Informe en PDF",
            data=pdf_bytes,
            file_name=f"Informe_{name_area}.pdf",
            mime="application/pdf"
        )

# Link externo
st.markdown("---")
url = "https://www.minvu.gob.cl/wp-content/uploads/2025/02/Listado-Oficial-de-Comportamiento-al-Fuego-de-Elementos-y-Componentes-de-la-Construccion_-ED17-2025.pdf"
st.link_button("Abrir Listado Oficial MINVU (PDF)", url)

