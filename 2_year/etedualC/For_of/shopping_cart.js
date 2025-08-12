var items=[
	{"Pilha":20},
	{"Tomate":40},
	{"Cartilha":60},
	{"Geladeira":80}
]
for(i of items){
	console.log(Object.keys(i)[0]+" a "+i[Object.keys(i)[0]]+" dinheiros imaginarios");
}
