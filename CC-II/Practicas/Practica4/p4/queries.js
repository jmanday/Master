	Objetivo Nº 1
1. db.pedidos.find().pretty();
2. db.pedidos.findOne(); / db.pedidos.find().limit(1).pretty();
3. db.pedidos.find({id_cliente: 2222}).pretty();
4. db.pedidos.find({"Pedidos.Productos.Precio_unidad": {$gte: 94}}, {"Nombre":1, "_id":0});
5. db.pedidos.find({"Localidad": {$in:["Salamanca", "Jaen"]}}, {"Pedidos":0, "_id":0}).pretty();
6. db.pedidos.find({Pedidos: {$exists: false}}, {"_id":0}).pretty();
7. db.pedidos.find({$and: [{"Fnacimiento": {$gte: ISODate("1963-01-01T00:00:00Z")}}, {"Fnacimiento": {$lte: ISODate("1963-12-31T00:00:00Z")}}]}, {"Pedidos":0, "_id":0}).pretty();
8. db.pedidos.find({$or: [{"Pedidos.Productos.Fabricante": "Canon"}, {"Pedidos.Productos.Precio_unidad": 15}]}).pretty();
9. db.pedidos.find({$or: [{"Nombre": /^C/}, {"Nombre": /^c/}]}, {"Pedidos":0, "_id":0, "Facturacion":0}).pretty();
10. db.pedidos.find({}, {"_id":0, "Facturacion":0, "Pedidos":0}).limit(4).pretty();
11. db.pedidos.find({}, {"_id":0, "Facturacion":0, "Pedidos":0}).limit(4).sort({"Localidad":1}).pretty();
	db.pedidos.find({}, {"_id":0, "Facturacion":0, "Pedidos":0}).limit(4).sort({"id_cliente":-1}).pretty();
	
	
	Objetivo Nº 2
1. db.pedidos.count();	
2. db.pedidos.find({"Localidad": "Jaen"}).count();
3. db.pedidos.aggregate([{$group: {_id: "$Localidad", TOTAL: {$sum: "$Facturacion"}}}]);
4. db.pedidos.aggregate({$group: {_id: "$Localidad", MEDIA: {$avg: "$Facturacion"}}}, {$match: {$and: [{MEDIA: {$gt: 5000}}, {_id: {$ne: "Jaen"}}]}}, {$sort: {_id:-1}}, {$project: {"_id":0, "MEDIA":1, Localidad: {$toUpper: "$_id"}}});
5. db.pedidos.aggregate({$unwind: "$Pedidos"}, {$unwind: "$Pedidos.Productos"}, {$project: {"id_cliente":1, "Nombre":1, Subtotal: {$multiply: ["$Pedidos.Productos.Precio_unidad", "$Pedidos.Productos.Cantidad"]}}}, {$group: {_id: {IDENTIFICADOR: "$id_cliente", NOMBRE: "$Nombre"}, TOTAL: {$sum: "$Subtotal"}}}, {$project: {"_id":0, IDENTIFICADOR: "$_id.IDENTIFICADOR", NOMBRE: "$_id.NOMBRE", TOTAL: "$TOTAL"}}).pretty();


	Objetivo Nº 3
1. 

var mapFunction1 = function(){
	emit(
        this.CountryID,
        { 
            "data":
            [
                {
                    "city": this.City,
				   	"latitude": this.Latitude,
				   	"longitude": this.Longitude
                }
            ]
        }
    );
}


var reduceFunction1 = function(key, values){
	var reduceVal = { 
        "datas": [] 
    };
	for (var i in values) {
		var aux = values[i];
		for (var j in aux.data) {
			reduceVal.datas.push(aux.data[j]);
		}
	}
	return reduceVal;
}


var finalizeFunction1 = function(key, reduceVal){
	var dist_min = 999999999999999999999999;
	var nearestCity = {
						"firstCity": "",
					   	"secondCity": "",
					   	"distance": 0
					  };
					  
	if(reduceVal.datas.length == 1){
		return { 
            "message" : "Este país contiene solo una ciudad" 
    	};		
    }			
      
	for(var i = 0; i < reduceVal.datas.length; i++){
		var c1 = reduceVal.datas[i];
		for(var j = 0; j < reduceVal.datas.length; j++){
			if(i >= j){
				var c2 = reduceVal.datas[j];
				var dist = (c1.latitude - c2.latitude) * (c1.latitude - c2.latitude) +
							(c1.longitude - c2.longitude) * (c1.longitude - c2.longitude);
                
                if(dist < dist_min && dist > 0){
                	nearestCity.firstCity = c1.city;
                	nearestCity.secondCity = c2.city;
                	nearestCity.distance = Math.sqrt(dist);
                	dist_min = dist;
                }
			}
		}
	}
	
	return nearestCity;
}


db.runCommand({
    mapReduce: "cities",
    map: mapFunction1,
    reduce: reduceFunction1,
    finalize: finalizeFunction1,
    query: { CountryID: { $ne: 254 } },
    out: { merge: "near_cities" }
});

db.near_cities.find().pretty();


2.

var mapFunction2 = function(){
	emit(
        this.CountryID,
        { 
            "data":
            [
                {
                    "city": this.City,
				   	"latitude": this.Latitude,
				   	"longitude": this.Longitude
                }
            ]
        }
    );
}


var reduceFunction2 = function(key, values){
	var reduceVal = { 
        "datas": [] 
    };
	for (var i in values) {
		var aux = values[i];
		for (var j in aux.data) {
			reduceVal.datas.push(aux.data[j]);
		}
	}
	return reduceVal;
}


var finalizeFunction2 = function(key, reduceVal){
	var dist_max = 0;
	var farestCity = {
						"firstCity": "",
					   	"secondCity": "",
					   	"distance": 0
					  };
					  
	if(reduceVal.datas.length == 1){
		return { 
            "message" : "Este país contiene solo una ciudad" 
    	};		
    }			
      
	for(var i = 0; i < reduceVal.datas.length; i++){
		var c1 = reduceVal.datas[i];
		for(var j = 0; j < reduceVal.datas.length; j++){
			if(i >= j){
				var c2 = reduceVal.datas[j];
				var dist = (c1.latitude - c2.latitude) * (c1.latitude - c2.latitude) +
							(c1.longitude - c2.longitude) * (c1.longitude - c2.longitude);
                
                if(dist > dist_max && dist > 0){
                	farestCity.firstCity = c1.city;
                	farestCity.secondCity = c2.city;
                	farestCity.distance = Math.sqrt(dist);
                	dist_max = dist;
                }
			}
		}
	}
	
	return farestCity;
}


db.runCommand({
    mapReduce: "cities",
    map: mapFunction2,
    reduce: reduceFunction2,
    finalize: finalizeFunction2,
    query: { CountryID: { $ne: 254 } },
    out: { merge: "far_cities" }
});

db.far_cities.find().pretty();

3.

var mapFunction3 = function(){
	emit(
        this.CountryID,
        { 
            "data":
            [
                {
                    "city": this.City,
				   	"latitude": this.Latitude,
				   	"longitude": this.Longitude
                }
            ]
        }
    );
}


var reduceFunction3 = function(key, values){
	var reduceVal = { 
        "datas": [] 
    };
	for (var i in values) {
		var aux = values[i];
		for (var j in aux.data) {
			reduceVal.datas.push(aux.data[j]);
		}
	}
	return reduceVal;
}


var finalizeFunction3 = function(key, reduceVal){
	var dist_min = 999999999999999999999999;
	var nearestCity = {
						"cities": [],
					   	"distance": 0
					  };
					  
	if(reduceVal.datas.length == 1){
		return { 
            "message" : "Este país contiene solo una ciudad" 
    	};		
    }			
      
	for(var i = 0; i < reduceVal.datas.length; i++){
		var c1 = reduceVal.datas[i];
		for(var j = 0; j < reduceVal.datas.length; j++){
			if(i >= j){
				var c2 = reduceVal.datas[j];
				var dist = (c1.latitude - c2.latitude) * (c1.latitude - c2.latitude) +
							(c1.longitude - c2.longitude) * (c1.longitude - c2.longitude);
                
                if(dist <= dist_min && dist > 0){
                	nearestCity.cities.push(c1.city);
                	nearestCity.cities.push(c2.city);
                	nearestCity.distance = Math.sqrt(dist);
                	dist_min = dist;
                }
			}
		}
	}
	
	return nearestCity;
}


db.runCommand({
    mapReduce: "cities",
    map: mapFunction3,
    reduce: reduceFunction3,
    finalize: finalizeFunction3,
    query: { CountryID: { $ne: 254 } },
    out: { merge: "near_cities2" }
});

db.near_cities2.find().pretty();



4.

var mapFunction4 = function(){
	emit(
        this.CountryID,
        { 
            "data":
            [
                {
                    "city": this.City,
				   	"latitude": this.Latitude,
				   	"longitude": this.Longitude
                }
            ]
        }
    );
}


var reduceFunction4 = function(key, values){
	var reduceVal = { 
        "datas": [] 
    };
	for (var i in values) {
		var aux = values[i];
		for (var j in aux.data) {
			reduceVal.datas.push(aux.data[j]);
		}
	}
	return reduceVal;
}


var finalizeFunction4 = function(key, reduceVal){
	var dist_min = 999999999999999999999999;
	var nearestCity = {
						"firstCity": "",
					   	"secondCity": "",
					   	"numparejas"; 0,
					   	"distance": 0
					  };
					  
	if(reduceVal.datas.length == 1){
		return { 
            "message" : "Este país contiene solo una ciudad" 
    	};		
    }			
      
	for(var i = 0; i < reduceVal.datas.length; i++){
		var c1 = reduceVal.datas[i];
		for(var j = 0; j < reduceVal.datas.length; j++){
			if(i >= j){
				nearestCity.numparejas += 1;
				var c2 = reduceVal.datas[j];
				var dist = (c1.latitude - c2.latitude) * (c1.latitude - c2.latitude) +
							(c1.longitude - c2.longitude) * (c1.longitude - c2.longitude);
                
                if(dist < dist_min && dist > 0){
                	nearestCity.firstCity = c1.city;
                	nearestCity.secondCity = c2.city;
                	nearestCity.distance = Math.sqrt(dist);
                	dist_min = dist;
                }
			}
		}
	}
	
	return nearestCity;
}


db.runCommand({
    mapReduce: "cities",
    map: mapFunction4,
    reduce: reduceFunction4,
    finalize: finalizeFunction4,
    query: { CountryID: { $ne: 254 } },
    out: { merge: "near_cities3" }
});

db.near_cities3.find().pretty();



5.

var mapFunction5 = function(){
	emit(
        this.CountryID,
        { 
            "data":
            [
                {
                    "city": this.City,
				   	"latitude": this.Latitude,
				   	"longitude": this.Longitude
                }
            ]
        }
    );
}


var reduceFunction5 = function(key, values){
	var reduceVal = { 
        "datas": [] 
    };
	for (var i in values) {
		var aux = values[i];
		for (var j in aux.data) {
			reduceVal.datas.push(aux.data[j]);
		}
	}
	return reduceVal;
}


var finalizeFunction5 = function(key, reduceVal){
	var nearestCity = {
					   	"Averagedistance": 0
					  };
    var aux = 0;
					  
	if(reduceVal.datas.length > 1){
		for(var i = 0; i < reduceVal.datas.length; i++){
			var c1 = reduceVal.datas[i];
			for(var j = 0; j < reduceVal.datas.length; j++){
				if(i >= j){
					nearestCity.numparejas += 1;
					var c2 = reduceVal.datas[j];
					var dist = (c1.latitude - c2.latitude) * (c1.latitude - c2.latitude) +
								(c1.longitude - c2.longitude) * (c1.longitude - c2.longitude);
                
                	aux += dist;
				}
			}
		}
		nearestCity.Averagedistance = (aux / reduceVal.datas.length);
	}
	
	return nearestCity;
}


db.runCommand({
    mapReduce: "cities",
    map: mapFunction5,
    reduce: reduceFunction5,
    finalize: finalizeFunction5,
    query: { CountryID: { $ne: 254 } },
    out: { merge: "average_distance" }
});

db.average_distance.find().pretty();



6.

db.cities.ensureIndex({CountryID: 1});

var mapFunction6 = function(){
	emit(
        this.CountryID,
        { 
            "data":
            [
                {
                    "city": this.City,
				   	"latitude": this.Latitude,
				   	"longitude": this.Longitude
                }
            ]
        }
    );
}


var reduceFunction6 = function(key, values){
	var reduceVal = { 
        "datas": [] 
    };
	for (var i in values) {
		var aux = values[i];
		for (var j in aux.data) {
			reduceVal.datas.push(aux.data[j]);
		}
	}
	return reduceVal;
}


var finalizeFunction6 = function(key, reduceVal){
	var dist_min = 999999999999999999999999;
	var nearestCity = {
						"firstCity": "",
					   	"secondCity": "",
					   	"distance": 0
					  };
					  
	if(reduceVal.datas.length == 1){
		return { 
            "message" : "Este país contiene solo una ciudad" 
    	};		
    }			
      
	for(var i = 0; i < reduceVal.datas.length; i++){
		var c1 = reduceVal.datas[i];
		for(var j = 0; j < reduceVal.datas.length; j++){
			if(i >= j){
				var c2 = reduceVal.datas[j];
				var dist = (c1.latitude - c2.latitude) * (c1.latitude - c2.latitude) +
							(c1.longitude - c2.longitude) * (c1.longitude - c2.longitude);
                
                if(dist < dist_min && dist > 0){
                	nearestCity.firstCity = c1.city;
                	nearestCity.secondCity = c2.city;
                	nearestCity.distance = Math.sqrt(dist);
                	dist_min = dist;
                }
			}
		}
	}
	
	return nearestCity;
}


db.runCommand({
    mapReduce: "cities",
    map: mapFunction6,
    reduce: reduceFunction6,
    finalize: finalizeFunction6,
    query: { CountryID: { $ne: 254 } },
    out: { merge: "near_cities4" }
});