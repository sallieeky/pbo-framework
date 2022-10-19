
# PBO GUI Framework

Framework GUI berbasis PyQt5 yang telah terintegrasi dengan database mysql menggunakan pymysql untuk mata kuliah PBO



## Installation

Install framework ini dengan melakukan clone repository ini. 

Disarankan untuk mengganti nama folder sesuai dengan project yang akan dibangun.

Setelah itu masuk ke folder yang telah di clone atau buka dengan menggunakan text editor (Disarankan menggunakan VSCode)

Lalu, buka terminal dan ketikkan
```bash
  pip install -r requirements.txt
  py app.py
```


    
## Konsep

Konsep yang digunakan pada framework ini yaitu OOP dengan memisahkan antara Pages dan Model untuk memudahkan dalam mengelola antara data dan tampilan

- `Model` berhubungan dengan database agar dapat mengelola, memperbarui, dan menginput data
- `Migration` memungkinkan kita untuk mengelola database dengan lebih mudah seperti skema dan tipedata
- `Seeder` merupakan fitur untuk mengisi data pada table secara default 
## Koneksi Database

Untuk database yang disupport yaitu terbatas hanya mysql. Jika ingin menggunakan database, maka perlu untuk mengatur beberapa hal.

- buat database pada pypmyadmin
- lalu buka `config/connection.py` ubah data di bawah ini sesuai dengan data kalian.
```
host = "localhost"
user = "root"
passwd = ""
database = "tespbo"

```
- tes koneksi ke database dengan melakukan migrasi dengan perintah `py pbo migrate`
## Command

Framework ini memiliki cli helper untuk membantu dalam pengembangan dengan menggunakan perintah
`py pbo [command]`

- `py pbo migrate` digunakan untuk melakukan migrasi skema database yang telah di buat
- `py pbo migrate:fresh` digunakan untuk melakukan drop seluruh table dan migrasi ulang skema database yang dibuat
- `py pbo migrate:fresh --seed` (REKOMENDED) digunakan untuk melakukan drop seluruh table dan migrasi ulang skema database dan mengisi data pada table secara sekaligus
- `py pbo drop` digunakan untuk melakukan drop seluruh table yang ada di database
- `py pbo seed` digunakan untuk memasukkan data kedalam database
- `py pbo make:msm [namafile]` (REKOMENDED) digunakan untuk membuat model, migration, dan seeder secara sekaligus
```
py pbo make:msm Mahasiswa

akan secara otomatis membuat file
- models/Mahasiswa.py
- migrations/create_mahasiswa_table.py
- seeders/MahasiswaSeeder.py

```
- `py pbo make:page [namafile]` (REKOMENDED) digunakan untuk membuat page
```
py pbo make:page Beranda

akan secara otomatis membuat file
- pages/BerandaPage.py

```
- `py pbo refresh:seeder [namafile]` digunakan untuk menyinkronkan seeder dengan column pada table yang ada di database secara otomatis
```
py pbo refresh:seeder Mahasiswa

akan secara otomatis akan mengubah isi pada file seeders/MahasiswaSeeder.py

apabila schema pada migrations/create_mahasiswa_table.py
def schema(self):
    self.query += Schema.id()
    self.query += Schema.varchar("nama")
    self.query += Schema.varchar("nim")
    self.query += Schema.varchar("prodi")
    self.query += Schema.timestamps()
    return self.query

maka seed pada seeders/MahasiswaSeeder.py
def seed(self):
    self.model.create({
        'nama': '',
        'nim': '',
        'prodi': '',
    })

```
## Helper

Framework ini juga memiliki 3 helper untuk membantu memudahkan dalam pengembangan

### Auth
Helper ini dapat digunakan untuk membuat fitur login. Auth ini berhubungan dengan model `User` yang ada pada `models/User.py`.

Helper ini secara default akan memvalidasi `username` dan `password` pada table user, namun anda dapat merubah validasi pada model `models/User.py` dengan mengubah nilai pada `self.auth`
```
self.auth = "username"
``` 

Cara penggunaan
```
from helper.auth import Auth


auth = Auth()
result = auth.login("username", "password")
```
Output
- `True` apabila username dan password benar
- `False` apabila username atau password salah

### Hash
Helper ini dapat digunakan untuk membantu mengenkripsi data
```
from helper.hash import encrypt
from helper.hash import decrypt

encrypt('admin123')

output:
$2b$12$qO6qf0znC6pXQvLLF.Y0XenLOGKhkdyVznavlYf8aF3UaU2n2zATG

decrypt('admin123', '$2b$12$qO6qf0znC6pXQvLLF.Y0XenLOGKhkdyVznavlYf8aF3UaU2n2zATG')

output:
True
False
```

### DB
Helper ini dapat digunakan untuk melakukan query CRUD database dengan menginputkan query sql secara manual.

- `DB.select(query)`
```
from helper.db import DB

DB.select("SELECT * FROM user")

output:
[{'id': 1, 'username': 'admin', 'password': '$2b$12$pYHxgWPLgIqS9xPG8vfTIO2CsAIES4T2dgqSpVtfUW.5tI/yP.zk6', 'created_at': datetime.datetime(2022, 10, 19, 8, 55, 21), 'updated_at': datetime.datetime(2022, 10, 19, 8, 55, 21)}, {'id': 2, 'username': 'admin2', 'password': '$2b$12$zeW.YJtO09T3u1Ts1Ycpw.NPmtvE9IwoC89k7SHgrbR1HPg5xzzea', 'created_at': datetime.datetime(2022, 10, 19, 8, 55, 21), 'updated_at': datetime.datetime(2022, 10, 19, 8, 55, 21)}]
```
- `DB.create(query)`
```
from helper.db import DB

DB.create("INSERT INTO user(username,password) VALUES ('aa', 'adad');")

output:
True
```
- `DB.update(query)`
```
from helper.db import DB

DB.update("UPDATE user SET username='adminupdate' WHERE id=1;")

output:
True
```
- `DB.delete(query)`
```
from helper.db import DB

DB.delete("DELETE FROM user WHERE id=1;")

output:
True
```

## Skema Migration

Skema yang dapat digunakan pada migration dapat di lihat pada `migrations/schema.py`
- `varchar`
- `integer`
- `char`
- `text`
- `boolean`
- `float`
- `datetime`
- `date`

contoh penggunaan pada migration
```
Yang perlu di sesuaikan hanya pada method schema(). Untuk id dan timestamps WAJIB ADA
tambahkan atribute lain dibawah id dan di atas timestamps

def schema(self):
    self.query += Schema.id()
    self.query += Schema.varchar("nama")
    self.query += Schema.char("nim",8)
    self.query += Schema.float("ipk")
    self.query += Schema.integer("umur")
    self.query += Schema.timestamps()
    return self.query
```
## Seeder

Seeder berfungsi untuk menambahkan data pada table yang ada di database. Seeder otomatis terhubung dengan modelnya seperti.

- `UserSeeder` terhubung dengan model `User`
- `MahasiswaSeeder` terhubung dengan model `Mahasiswa`

contoh penggunaan seeder
```
Yang perlu di sesuaikan hanya pada method seed(). 
sesuaikan atribute yang ada pada skema tablenya.

contoh skema pada migration
def schema(self):
    self.query += Schema.id()
    self.query += Schema.varchar("username", unique=True)
    self.query += Schema.varchar("password")
    self.query += Schema.timestamps()
    return self.query

maka seed nya
def seed(self):
    self.model.create({
        'username': 'admin',
        'password': encrypt('admin123'),
    })
    
untuk id dan timestamps tidak perlu ditulis karena akan terisi otomatis
```
## Model

Model ini menghubungkan antara Framework dengan database sehingga mempermudah dalam melakukan query.

Beberapa query yang bisa di handle oleh model dapat di lihat pada `models/model.py`
- `all()`
```
from models.User import User

model = User()
model.all()

output
[{'id': 1, 'username': 'admin', 'password': '$2b$12$drvLlOsH1LGUtj6vrwu9te84RLcdxcSsigEDQPcbAhN7tX8FXbZY2', 'created_at': datetime.datetime(2022, 10, 18, 9, 49, 2), 'updated_at': datetime.datetime(2022, 10, 18, 9, 49, 2)}, {'id': 2, 'username': 'admin2', 'password': '$2b$12$VvokdXRZaQ.Ax3hRjj3c8e3sW1XKRKWlco1yjJ4eq.u3YXVuN56Ye', 'created_at': datetime.datetime(2022, 10, 18, 9, 49, 2), 'updated_at': datetime.datetime(2022, 10, 18, 9, 49, 2)}]
```
- `find(id)`
```
from models.User import User

model = User()
model.find(1)

output
{'id': 1, 'username': 'admin', 'password': '$2b$12$qO6qf0znC6pXQvLLF.Y0XenLOGKhkdyVznavlYf8aF3UaU2n2zATG', 'created_at': datetime.datetime(2022, 10, 18, 7, 53, 15), 'updated_at': datetime.datetime(2022, 10, 18, 7, 53, 15)}
```
- `first()`
```
from models.User import User

model = User()
model.first()

output
{'id': 1, 'username': 'admin', 'password': '$2b$12$qO6qf0znC6pXQvLLF.Y0XenLOGKhkdyVznavlYf8aF3UaU2n2zATG', 'created_at': datetime.datetime(2022, 10, 18, 7, 53, 15), 'updated_at': datetime.datetime(2022, 10, 18, 7, 53, 15)}
```
- `last()`
```
from models.User import User

model = User()
model.last()

output
{'id': 2, 'username': 'admin2', 'password': '$2b$12$VvokdXRZaQ.Ax3hRjj3c8e3sW1XKRKWlco1yjJ4eq.u3YXVuN56Ye', 'created_at': datetime.datetime(2022, 10, 18, 9, 49, 2), 'updated_at': datetime.datetime(2022, 10, 18, 9, 49, 2)}
```
- `whereMany(column, operator, value)`
```
from models.User import User

model = User()
model.whereMany('username', '=', 'admin')

output
[{'id': 1, 'username': 'admin', 'password': '$2b$12$drvLlOsH1LGUtj6vrwu9te84RLcdxcSsigEDQPcbAhN7tX8FXbZY2', 'created_at': datetime.datetime(2022, 10, 18, 9, 49, 2), 'updated_at': datetime.datetime(2022, 10, 18, 9, 49, 2)}]
```

- `whereOnly(column, operator, value)`
```
from models.User import User

model = User()
model.whereOnly('username', '=', 'admin')

output
{'id': 1, 'username': 'admin', 'password': '$2b$12$drvLlOsH1LGUtj6vrwu9te84RLcdxcSsigEDQPcbAhN7tX8FXbZY2', 'created_at': datetime.datetime(2022, 10, 18, 9, 49, 2), 'updated_at': datetime.datetime(2022, 10, 18, 9, 49, 2)}
```
- `create(data)`
```
from models.User import User

model = User()
model.create({
    'username': 'admin',
    'password': encrypt('admin123'),
})
```
- `update(id, data)`
```
from models.User import User

model = User()
model.update(1, {
    'username': 'adminupdate',
})
```
- `delete(id)`
```
from models.User import User

model = User()
model.delete(2)
```
- `truncate(id)`
```
from models.User import User

model = User()
model.truncate(2)
```