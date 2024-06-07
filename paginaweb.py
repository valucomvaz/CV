from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Valentina Comini"
PAGE_ICON = ":wave:"
NAME = "Valentina Comini"
DESCRIPTION = """
Estudiante de secundaria
"""
EMAIL = "valucomvaz@gmail.com"
DATOS_DE_CONTACTO = {
    "Teléfono" : "tel://+5491133393801",
    "Lugar de residencia" : "https://maps.app.goo.gl/WAGzxxqGUKNzGpQWA"
}


st.set_page_config(page_title="CV", page_icon="🌷")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Descargar CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(DATOS_DE_CONTACTO))
for index, (platform, link) in enumerate(DATOS_DE_CONTACTO.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Sobre mí")
st.write(
    """
A mis 17 años, estoy a punto de terminar mis estudios
secundarios con orientación en informática. Durante
mi tiempo en la escuela, fui reconocida como escolta
con uno de los mejores promedios de mi clase.
Además, participé en proyectos escolares de diseño
web y programación, lo que me permitió aplicar
conocimientos en algunas situaciones prácticas.
Me motiva mi pasión por aprender y crecer profesionalmente. 
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Habilidades")
st.write(
    """
- 👩‍💻 Programación: Python, SQL, HTML, Kotlin, Paquete Office
- 📊 Data Visualización: Excel, Access
- 📚 Idiomas: Inglés nivel B2
- 🗄️ Trabajo en equipo, responsabilidad, creatividad
"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("Formación académica")
st.write("---")

# --- JOB 1
st.write("📚", "**Instituto Espiritu Santo**")
st.write("2020 - Presente")
st.write(
    """
- ► Colegio secundario con orientación en informática
"""
)

# --- JOB 2
st.write('\n')
st.write("📚", "**Conservatorio Astor Piazzolla**")
st.write("2024 - Presente")
st.write(
    """
- ► Piano, instrumento principal
- ► Teoría y apreciación musical
"""
)

# --- JOB 3
st.write('\n')
st.write("📚", "**Conservatorio Manuel de Falla**")
st.write("2017 - 2020")
st.write(
    """
- ► Piano, instrumento principal
- ► Educación vocal
- ► Expresión corporal
- ► Lenguaje musical
"""
)

# --- JOB 4
st.write('\n')
st.write("📚", "**UTN Facultad Regional Avellaneda**")
st.write("Agosto 2023 - Diciembre 2023")
st.write(
    """
- ► Curso de Ciencia de Datos 1
"""
)

# --- JOB 5
st.write('\n')
st.write("📚", "**Desarrollo con Python**")
st.write("Temporada verano 2024")
st.write(
    """
- ► Curso intensivo de informática
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experiencia laboral")
st.write("---")

# --- JOB 1
st.write("👩‍💻", "**Huerta CoWorking**")
st.write("Atención al cliente")
st.write("Mayo 2024")
st.write(
    """
- ► Primer experiencia de Actividades de
Aproximación (ACAP) al mundo del trabajo.
"""
)

# --- JOB 2
st.write('\n')
st.write("👩‍💻", "**CREA2 Diseño Web Profesional**")
st.write("Junior community manager")
st.write("Temporada invierno 2023")
st.write(
    """
- ► Diseño feed y administración de redes sociales
para cuentas de moda.
"""
)