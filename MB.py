from sqlite3 import connect

with connect("kitoblar.db") as db:
    kursor = db.cursor()
    kursor.execute(
        """
        create table Kitob(
            nom varchar,
            narx varchar
        )
        """
    )

    kursor.execute(
        """
        Insert into Kitob
        values
        ("Ufq", "4.63"),
        ("Ikki eshik orasi", "3.05"),
        ("Alvido, bolalik", "3.94"),
        ("Usmonov", "3.49"),
        ("Qo'rqma", "4.12"),
        ("Halqa", "5.23")
        """
    )