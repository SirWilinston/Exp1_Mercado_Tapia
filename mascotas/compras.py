class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, producto):
        if producto.id not in self.carrito.keys():
            self.carrito[producto.id]={
                "producto_id":producto.id, 
                "precio": str (producto.precio),
                "cantidad": 1,
                "total": producto.precio,

            }
        else:
            for key, value in self.carrito.items():
                if key==producto.id:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = producto.precio
                    value["total"]= value["total"] + producto.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True


    def eliminar(self, prod):
        id = prod.id
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,prod):
        for key, value in self.carrito.items():
            if key == prod.id:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- prod.precio
                if value["cantidad"] < 1:   
                    self.eliminar(prod)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 