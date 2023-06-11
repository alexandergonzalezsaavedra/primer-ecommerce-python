const resCategorias = document.querySelector('#resCategorias')
const templeteCategorias = document.querySelector('#templeteCategorias')
const fragment = document.createDocumentFragment()

let opcionesPeticion = {
    method: 'GET',
};
let urlBase = 'http://127.0.0.1:3000/orders'
const api = async () => {
    try {
        let data = await fetch(`${urlBase}/getsubcategories`, opcionesPeticion)
        let resData = await data.json()
        console.log(resData)
        resData.map((item) => {
            let clon = templeteCategorias.content.cloneNode(true)
            clon.querySelector(".tarjeta-categoria .info h3").textContent = item.nombreSubCategoria
            clon.querySelector(".tarjeta-categoria .imagen-tarjeta img").src = item.imagenSubcategoria
            clon.querySelector(".tarjeta-categoria .imagen-tarjeta img").alt = item.nombreSubCategoria
            clon.querySelector(".tarjeta-categoria p").textContent = item.descripcionSubcategoria
            fragment.appendChild(clon)
        })
        resCategorias.appendChild(fragment)
    } catch (error) {
    }
}
api()