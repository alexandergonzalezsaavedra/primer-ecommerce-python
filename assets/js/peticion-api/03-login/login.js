const formularioIngreso = document.querySelector('#formularioIngreso')
const user = document.querySelector('#user')
const pass = document.querySelector('#pass')
const limpiarFormulario = () => {
    user.value = ''
    pass.value = ''
}
let token
formularioIngreso.addEventListener('submit', async (e) => {
    e.preventDefault()
    let dataUser = user.value
    let dataPass = pass.value
    console.log(dataUser)
    console.log(dataPass)
    let cabeceras = new Headers();
    cabeceras.append("Cookie", "csrftoken=1AEnNNzrponbnN9s0gYBkzERXYEmCMpl; sessionid=r0kw715hiaq52cyaovx072k7qpz2xa3j");
    let formdata = new FormData();
    formdata.append("username", dataUser);
    formdata.append("password", dataPass);
    let opcionesPeticion = {
        method: 'POST',
        headers: cabeceras,
        body: formdata,
        redirect: 'follow'
    };
    let urlBase = 'http://127.0.0.1:3000/dj_rest_auth/login/'
    let data = await fetch(`${urlBase}`, opcionesPeticion)
    let resData = await data.json()
    if (data.status === 400) {
        console.log('Error, usuario y contraseña no validos')
        return limpiarFormulario()
    }
    else if (resData.key !== '') {
        console.log('Ingreso correctamente')
        token = resData.key
        window.location.replace(`file:///D:/Curso-full-stack/01-ejercicios-clase/14-primer-actividad-python/ecommerce/usuario.html?id=${token}`);
        return
    }
})