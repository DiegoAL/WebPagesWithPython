//IMPORTANTE: Os erros de javascript são logados no console do browser e não na IDE
//Utilizar o console do browser pode ser uma boa ideia para testar o retorno de cada função
//	ou entender o que pode estar ocorrendo com seu codigo, podendo até mesmo ser possivel 
//	sobrescrever o valor de variaveis


 /*com o addEventListener é possivel atrelar uma função a um evento de um objeto no caso um botão
	dentro do metodo é declado o tipo de evento (onclick) e o objeto(button) que recebera essa 'esculta'
	alem do metodo que será chamado quando esse evento ocorrer no caso 'contador'*/
document.addEventListener('DOMContentLoaded', function() {
	document.querySelector('button').onclick = contador;	
});


let cont = 0;

function contador(){
	cont++
	document.querySelector('#numero').innerHTML = cont;
	
	if(cont % 10 === 0){
		alert(`Contador é igual a ${cont}`);
	}
};


//As 3 formas de declarar variaveis em JS

//const declara uma variavel que nunca tera seu valor alterado
const constante = 1;

//let é uma vavivel que existe apenas dentro de um bloco, fora do bloco ela n existe
let local = 10;

//var é uma variavel que vai existir em toda a função, sendo mais "global"
var global = 5;


//Quando o formulario #form for submetido sera exibido um pop up com o nome digitado no input
document.addEventListener('DOMContentLoaded', function(){
	document.querySelector('#form').onsubmit = function(){
		const nome = document.querySelector('#nome').value;
		alert(`Ola ${nome}`)
	};
});


//com a função 'style' é possivel acessar qualquer propriedade CSS
document.addEventListener('DOMContentLoaded', function(){
	
	document.querySelector('#btVermelho').onclick = function(){
		document.querySelector('#mudarCor').style.color = 'red';
	};

	document.querySelector('#btVerde').onclick = function(){
		document.querySelector('#mudarCor').style.color = 'green';
	};
	
	document.querySelector('#btAzul').onmouseover = function(){
		document.querySelector('#mudarCor').style.color = 'blue';
	}
});