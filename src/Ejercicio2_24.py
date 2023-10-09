def euroCentimos (precio):
    euros = int(precio)
    centimos = int((precio - euros) * 100)
    return euros, centimos


if __name__ == "__main__":
    precio = float(input("Introduce el precio del producto  en euros(con dos decimales): "))

    euros, centimos = euroCentimos(precio)

    print(f"Los Euros del producto son: {euros}")
    print(f"Los céntimos del producto son: {centimos}")