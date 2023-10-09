def modificarCorreo(correo):
    nombreUsuario, dominio = correo.split('@')
    correoNuevo = nombreUsuario + '@ceu.es'
    return correoNuevo

if __name__ == "__main__":

    correo = input("introduce tu correo: ")

    correoNuevo = modificarCorreo(correo)

    print(f"El nuevo correo electronico es: {correoNuevo}")