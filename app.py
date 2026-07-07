import streamlit as st
from pathlib import Path

# ===============================
# CONFIGURACIÓN
# ===============================

PASSWORD = st.secrets["PASSWORD"]

st.set_page_config(
    page_title="Acceso protegido",
    page_icon="🔒",
    layout="centered"
)

# ===============================
# ESTILOS
# ===============================

st.markdown("""
<style>

.stApp{
    background:#000000;
}

.main > div{
    max-width:650px;
}

.card{
    background:#181818;
    padding:40px;
    border-radius:24px;
    box-shadow:0 0 35px rgba(255,255,255,.05);
    text-align:center;
}

h1,h2,h3,p,label{
    color:white !important;
}

.stTextInput label{
    color:white !important;
}

.stTextInput input{
    background:#2a2a2a;
    color:white;
    border:1px solid #444;
    border-radius:12px;
}

.stButton>button{
    width:100%;
    background:white;
    color:black;
    border:none;
    border-radius:12px;
    padding:12px;
    font-size:17px;
    font-weight:600;
    transition:.2s;
}

.stButton>button:hover{
    background:#d9d9d9;
}

img{
    border-radius:18px;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# TARJETA
# ===============================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown(
    "<h1 style='font-size:60px;'>🔒</h1>",
    unsafe_allow_html=True
)

# Mostrar la imagen solo si existe
image_path = Path("foto.jpg")

if image_path.exists():
    st.image(str(image_path), use_container_width=True)

st.markdown(
    "<h2 style='text-align:center;'>Acceso protegido</h2>",
    unsafe_allow_html=True
)

st.write("Introduce la contraseña para desbloquear la descarga.")

password = st.text_input(
    "Contraseña",
    type="password"
)

if st.button("Desbloquear"):

    if password == PASSWORD:

        st.success("Acceso concedido ✅")

        zip_path = Path("archivo.zip")

        if zip_path.exists():

            with open(zip_path, "rb") as file:

                st.download_button(
                    label="📦 Descargar ZIP",
                    data=file,
                    file_name="archivo.zip",
                    mime="application/zip"
                )

        else:

            st.error("No se encontró el archivo ZIP.")

    else:

        st.error("❌ Contraseña incorrecta")

st.markdown("</div>", unsafe_allow_html=True)
