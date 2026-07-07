import streamlit as st
from pathlib import Path

# =====================================
# CONFIGURACIÓN
# =====================================

PASSWORD = st.secrets["PASSWORD"]

st.set_page_config(
    page_title="Acceso protegido",
    page_icon="🔒",
    layout="centered"
)

# =====================================
# ESTILOS
# =====================================

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
    box-shadow:0 0 35px rgba(255,255,255,.08);
    text-align:center;
}

h1,h2,p{
    color:white !important;
}

.stTextInput label{
    color:white !important;
}

.stTextInput input{
    background:#2a2a2a !important;
    color:white !important;
    border-radius:12px;
}

.lock{
    text-align:center;
    font-size:60px;
    margin-bottom:20px;
}

img{
    border-radius:18px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# TARJETA
# =====================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("""
<div class="lock">
    🔒
</div>
""", unsafe_allow_html=True)

if Path("integral.png").exists():
    st.image("integral.png", use_container_width=True)

st.markdown(
    "<h2 style='text-align:center;'>Acceso protegido</h2>",
    unsafe_allow_html=True
)

st.write("Para desbloquear tu regalo, tendrá que resolver la integral del día... Solo se aceptan dígitos, comas y el signo negativo (-). La contraseña tiene 6 dígitos (sin contar con la coma decimal y el signo negativo, si es que hay), así que deberá redondear correctamente el resultado.")

password = st.text_input(
    "Contraseña",
    type="password"
)

if st.button("Desbloquear", use_container_width=True):

    if password == PASSWORD:

        st.success("✅ Acceso concedido, ¡felicidades!")

        if Path("archivo.zip").exists():

            with open("archivo.zip", "rb") as f:

                st.download_button(
                    label="📦 Descargar archivo sin virus :)",
                    data=f,
                    file_name="archivo.zip",
                    mime="application/zip",
                    use_container_width=True
                )

        else:
            st.error("No se encontró su regalo... Contacte con el creador.")

    else:
        st.error("❌ Contraseña incorrecta")

st.markdown("</div>", unsafe_allow_html=True)
