/* funcion del DOMContentLoaded es esperar que el documento html cargue completo y despues ejecutar una funcion o metodo */
document.addEventListener("DOMContentLoaded",console.log("tu mai"))

const title = document.getElementById("titulo")
const btn1 = document.getElementById("botonone")
const btn2 = document.getElementById("botontwo")
const bod = document.getElementById("cuerpo")

function tituloColorred() {
    title.style.color="brown"
    bod.style.background = "white"

}

function tituloColorblue(){
    title.style.color="rgb(42, 50, 165)";
    bod.style.background = "black"
}

btn1.addEventListener("click",tituloColorred)
btn2.addEventListener("click",tituloColorblue)