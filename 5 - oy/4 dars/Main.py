import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="postgras",      
    user="Able_me",     
    password="a369963A"  
)

cursor = connection.cursor()
try:
    cursor.execute("DROP TABLE IF EXISTS avtomabillar CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS clientlar CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS buyurtmalar CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS xodimlar CASCADE;")
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS avtomabillar(
            id SERIAL PRIMARY KEY,
            nomi TEXT NOT NULL,
            madel TEXT NOT NULL,
            yil INT,
            narx NUMERIC(12,2),
            mavjudlig BOOLEAN DEFAULT TRUE
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientlar(
            id SERIAL PRIMARY KEY,
            ism VARCHAR(50) NOT NULL,
            familya VARCHAR(50),
            telefon CHAR(13),
            manzil TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS buyurtmalar(
            id SERIAL PRIMARY KEY,
            avtomabil_id INTEGER REFERENCES avtomabillar(id),
            client_id INTEGER REFERENCES clientlar(id),
            sana DATE,
            umumiy_narx NUMERIC(12,2)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS xodimlar(
            id SERIAL PRIMARY KEY,
            ism VARCHAR(50),
            lavozim VARCHAR(50),
            maosh NUMERIC(10, 2)
        );
    ''')

    connection.commit()

    cursor.execute('''
        INSERT INTO avtomabillar(nomi, madel, yil, narx, mavjudlig) VALUES
        ('BMW', 'M5 F40', 2010, 15000, TRUE),
        ('Lambargini', 'URUS', 2020, 150000, TRUE);
    ''')

    cursor.execute('''
        INSERT INTO clientlar(ism, familya, telefon, manzil) VALUES
        ('Ali', 'Alijonov', '+998 .. ... .. ..', 'Fargona'),
        ('Vali', 'Valijonov', '+998 .. ... .. ..', 'Toshkent');
    ''')

    cursor.execute('''
        INSERT INTO buyurtmalar (avtomabil_id, client_id, sana, umumiy_narx) VALUES
        (1, 1, '2024-11-01', 20000),
        (2, 2, '2024-11-02', 25000);
    ''')

    cursor.execute('''
        INSERT INTO xodimlar(ism, lavozim, maosh) VALUES
        ('Aziz', 'Sotuvchi', 200),
        ('Laziz', 'Boshqaruvchi', 500);
    ''')

    connection.commit()

    cursor.execute('''
        ALTER TABLE clientlar ADD COLUMN email VARCHAR(100);
    ''')

    cursor.execute('''
        ALTER TABLE clientlar RENAME COLUMN ism TO fio;
    ''')

    cursor.execute('''
        ALTER TABLE clientlar RENAME TO mijozlar;
    ''')

    connection.commit()

    cursor.execute('''
        INSERT INTO mijozlar (fio, telefon, email) VALUES
        ('Ali Valiyev', '+998901234567', 'ali@example.com'),
        ('Zarina Karimova', '+998901234568', 'zarina@example.com');
    ''')

    cursor.execute('''
        INSERT INTO avtomabillar (nomi, madel, yil, narx, mavjudlig) VALUES
        ('Toyota', 'Corolla', 2022, 22000, TRUE),
        ('Chevrolet', 'Malibu', 2023, 23000, TRUE);
    ''')

    cursor.execute('''
        INSERT INTO xodimlar (ism, lavozim, maosh) VALUES
        ('Olim', 'Hisobchi', 300),
        ('Mahmud', 'Sotuvchi', 250);
    ''')

    cursor.execute('''
        INSERT INTO buyurtmalar (avtomabil_id, client_id, sana, umumiy_narx) VALUES
        (1, 1, '2024-11-01', 22000),
        (2, 2, '2024-11-02', 27000);
    ''')

    connection.commit()

    cursor.execute('''
        UPDATE xodimlar SET ism = 'Azamat' WHERE ism = 'Olim';
    ''')

    cursor.execute('''
        UPDATE xodimlar SET ism = 'Bahrom' WHERE ism = 'Mahmud';
    ''')

    connection.commit()

    cursor.execute('''
        DELETE FROM xodimlar WHERE ism = 'Aziz';
    ''')

    connection.commit()

    cursor.execute('SELECT * FROM mijozlar;')
    mijozlar = cursor.fetchall()
    print("Mijozlar:", mijozlar)

    cursor.execute('SELECT * FROM avtomabillar;')
    avtomabillar = cursor.fetchall()
    print("Avtomabillar:", avtomabillar)

    cursor.execute('SELECT * FROM xodimlar;')
    xodimlar = cursor.fetchall()
    print("Xodimlar:", xodimlar)

    cursor.execute('SELECT * FROM buyurtmalar;')
    buyurtmalar = cursor.fetchall()
    print("Buyurtmalar:", buyurtmalar)

except Exception as e:
    print("Xato yuz berdi:", e)
    connection.rollback()
finally:
    cursor.close()
    connection.close()






