from flask import Flask, render_template

app = Flask(__name__)

peliculas = [
    {
        "titulo": "Troya",
        "genero": "Drama",
        "imagen": "imagenes/troya poster.webp",
        "año": 2004,
        "sinopsis": "El príncipe Paris de Troya se lleva a Helena, esposa del rey de Esparta, provocando una guerra entre ambos pueblos.",
        "trailer": "https://www.youtube.com/watch?v=znTLzRJimeY"
    },
    {
        "titulo": "F1",
        "genero": "Deportes",
        "imagen": "imagenes/f1 poster.jpg",
        "año": 2025,
        "sinopsis": "Un veterano piloto de Fórmula 1 regresa a las pistas para ayudar a un joven compañero y salvar a su equipo.",
        "trailer": "https://www.youtube.com/watch?v=aw8YyC4B1EA&t=1s"
    },
    {
        "titulo": "Barbarian",
        "genero": "Terror",
        "imagen": "imagenes/barbarian poster.jpg",
        "año": 2022,
        "sinopsis": "Una joven llega a una casa que alquiló y descubre que hay mucho más escondido en ella de lo que imaginaba.",
        "trailer": "https://www.youtube.com/watch?v=Dr89pmKrqkI"
    },
    {
        "titulo": "El sexto sentido",
        "genero": "Terror",
        "imagen": "imagenes/sexto sentido poster.jpg",
        "año": 1999,
        "sinopsis": "Un psicólogo infantil intenta ayudar a un niño que asegura poder ver y hablar con personas muertas.",
        "trailer": "https://www.youtube.com/watch?v=zfOdk9JDzSw"
    },
    {
        "titulo": "Match Point",
        "genero": "Drama",
        "imagen": "imagenes/match point poster.jpg",
        "año": 2005,
        "sinopsis": "Un extenista se introduce en una familia adinerada y queda atrapado entre la ambición, el deseo y el peligro.",
        "trailer": "https://www.youtube.com/watch?v=XgMe91ia5C0"
    },
    {
        "titulo": "Gonjiam: Haunted Asylum",
        "genero": "Terror",
        "imagen": "imagenes/gonjiam poster.jpg",
        "año": 2018,
        "sinopsis": "Un grupo de jóvenes entra en un antiguo hospital psiquiátrico abandonado para transmitir su exploración en directo.",
        "trailer": "https://www.youtube.com/watch?v=QtUiEQYXDAU"
    },
    {
        "titulo": "El conjuro 2",
        "genero": "Terror",
        "imagen": "imagenes/el conjuro 2 poster.jpg",
        "año": 2016,
        "sinopsis": "Ed y Lorraine Warren viajan a Inglaterra para ayudar a una familia aterrorizada por una presencia sobrenatural.",
        "trailer": "https://www.youtube.com/watch?v=cuDBjj_Gs0M"
    },
    {
        "titulo": "Wer",
        "genero": "Terror",
        "imagen": "imagenes/wer poster.jpg",
        "año": 2013,
        "sinopsis": "Una abogada intenta demostrar que un hombre acusado de un brutal asesinato podría no ser lo que parece.",
        "trailer": "https://www.youtube.com/watch?v=DEBt92Ij81s"
    },
    {
        "titulo": "Get Out",
        "genero": "Terror",
        "imagen": "imagenes/get out poster.jpg",
        "año": 2017,
        "sinopsis": "Un joven visita por primera vez a la familia de su novia y descubre que algo muy extraño ocurre en la casa.",
        "trailer": "https://www.youtube.com/watch?v=dHj6a5g4ROY"
    },
    {
        "titulo": "No respires",
        "genero": "Terror",
        "imagen": "imagenes/no respires poster.jpg",
        "año": 2016,
        "sinopsis": "Tres jóvenes entran a robar en la casa de un hombre ciego, pero descubren que ellos son quienes están en peligro.",
        "trailer": "https://www.youtube.com/watch?v=mvEetUDCKxE"
    },
    {
        "titulo": "Terrifier",
        "genero": "Terror",
        "imagen": "imagenes/terrifier poster.webp",
        "año": 2016,
        "sinopsis": "Un payaso siniestro comienza a perseguir a dos jóvenes durante la noche de Halloween.",
        "trailer": "https://www.youtube.com/watch?v=53WqptOMQCM"
    }
]


@app.route("/")
def inicio():
    return render_template("index.html", peliculas=peliculas)


@app.route("/pelicula/<titulo>")
def detalle_pelicula(titulo):

    for pelicula in peliculas:

        if pelicula["titulo"] == titulo:
            return render_template("pelicula.html", pelicula=pelicula)

    return "Película no encontrada", 404


if __name__ == "__main__":
    app.run(debug=True)