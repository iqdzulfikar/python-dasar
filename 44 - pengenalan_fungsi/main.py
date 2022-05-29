# 44 - Pengenalan Fungsi

# def nama_function():

def hello_world():
    ''' Function utk menampilkan hellow world '''
    print("Hello world")
    print("Hello Ucup")
    print("Hello Otong\n")


hello_world()
hello_world()
hello_world()

# ini_fungsi()  # ERROR <- karena disimpan sebelum fungsinya didefinisikan

def ini_fungsi():
    '''Pemanggilan fungsi di python harus setelah fungsi dibuat,
    bukan di bawah dari fungsinya'''
    print('Ini adalah fungsi')
    
ini_fungsi()