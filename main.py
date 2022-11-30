# Importar Juegos y la funcion del juego
from Carrera_de_Tortuga import carreradetortuga
from ta_te_ti import tateti

# Funcion Menu
def menu():
    opcion = 0
    print('¿Que juego quieres jugar?');
    print('1. Carrera de Tortugas');
    print('2. Ta Te Ti');
    print('3. Salir');
    
    if opcion == 0:
        opcion = input('Elige una opcion: ');
    if opcion == '1':
        carreradetortuga();
        menu()
    elif opcion == '2':
        tateti();
        menu()
    elif opcion == '3':
        print('Hasta luego!');

# Ejecuto funcion        
menu()