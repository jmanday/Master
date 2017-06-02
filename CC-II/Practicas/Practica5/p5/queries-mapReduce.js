
########################################################################
########################################################################

var mapFunction1 = function(){

    var key = this.CountryID;
    var value = {
        "city": this.City,
        "latitude": this.Latitude,
        "longitude": this.Longitude  
    };

    emit(key, value);
}

var reduceFunction1 = function(key, values){
    if(values.length == 1){
        return { 
            "message" : "Este país contiene solo una ciudad" 
        }; 
    }

    var reduceVal = { 
        "firstCity": "",
        "secondCity": "",
        "distance": 0
    };

    var dist_min = 99999999999999999999999;
    
    for (var i = 0; i < values.length; i++) {
        var c1 = values[i];
        for (var j = i + 1; j < values.length; j++) {
            var c2 = values[j];

            var dist = (c1.latitude - c2.latitude) * (c1.latitude - c2.latitude) + (c1.longitude - c2.longitude) * (c1.longitude - c2.longitude);

            if(dist < dist_min && dist > 0){
                reduceVal.firstCity = c1.city;
                reduceVal.secondCity = c2.city;
                reduceVal.distance = Math.sqrt(dist);
                dist_min = dist;
            }
        }
    }

    return {reduceVal};
    
}

db.runCommand({
    mapReduce: "cities",
    map: mapFunction1,
    reduce: reduceFunction1,
    query: { CountryID: { $ne: 254 } },
    out: { merge: "cidudades_cercanas" }
});

db.cidudades_cercanas.find().pretty();

########################################################################
########################################################################

var mapFunction2 = function(){

    var key = this.CountryID;
    var value = {
        "city": this.City,
        "latitude": this.Latitude,
        "longitude": this.Longitude  
    };

    emit(key, value);
}

var reduceFunction2 = function(key, values){
    if(values.length == 1){
        return { 
            "message" : "Este país contiene solo una ciudad" 
        }; 
    }

    var reduceVal = { 
        "firstCity": "",
        "secondCity": "",
        "distance": 0
    };

    var dist_max = 0;
    
    for (var i = 0; i < values.length; i++) {
        var c1 = values[i];
        for (var j = i + 1; j < values.length; j++) {
            var c2 = values[j];

            var dist = (c1.latitude - c2.latitude) * (c1.latitude - c2.latitude) + (c1.longitude - c2.longitude) * (c1.longitude - c2.longitude);

            if(dist > dist_max){
                reduceVal.firstCity = c1.city;
                reduceVal.secondCity = c2.city;
                reduceVal.distance = Math.sqrt(dist);
                dist_max = dist;
            }
        }
    }

    return {reduceVal};
    
}

db.runCommand({
    mapReduce: "cities",
    map: mapFunction2,
    reduce: reduceFunction2,
    query: { CountryID: { $ne: 254 } },
    out: { merge: "cidudades_lejanas" }
});

db.cidudades_lejanas.find().pretty();

########################################################################
########################################################################

var mapFunction3 = function(){

    var key = this.CountryID;
    var value = {
        "city": this.City,
        "latitude": this.Latitude,
        "longitude": this.Longitude  
    };

    emit(key, value);
}

var reduceFunction3 = function(key, values){
    if(values.length == 1){
        return { 
            "message" : "Este país contiene solo una ciudad" 
        }; 
    }

    var reduceVal = { 
        "firstCity": "",
        "secondCity": "",
        "distance": 0
    };

    var listCities = [];

    var dist_min = 99999999999999999999999;
    
    for (var i = 0; i < values.length; i++) {
        var c1 = values[i];
        for (var j = i + 1; j < values.length; j++) {
            var c2 = values[j];

            var dist = (c1.latitude - c2.latitude) * (c1.latitude - c2.latitude) + (c1.longitude - c2.longitude) * (c1.longitude - c2.longitude);

            if(dist <= dist_min && dist > 0){
                reduceVal.firstCity = c1.city;
                reduceVal.secondCity = c2.city;
                reduceVal.distance = Math.sqrt(dist);
                dist_min = dist;
                listCities.push(reduceVal);
            }
        }
    }

    return {listCities};
    
}

db.runCommand({
    mapReduce: "cities",
    map: mapFunction3,
    reduce: reduceFunction3,
    query: { CountryID: { $ne: 254 } },
    out: { merge: "cidudades_cercanas2" }
});

db.cidudades_cercanas2.find().pretty();

########################################################################
########################################################################

var mapFunction4 = function(){

    var key = this.CountryID;
    var value = {
        "city": this.City,
        "latitude": this.Latitude,
        "longitude": this.Longitude  
    };

    emit(key, value);
}

var reduceFunction4 = function(key, values){
    if(values.length == 1){
        return { 
            "message" : "Este país contiene solo una ciudad" 
        }; 
    }

    var reduceVal = { 
        "CountryID": key,
        "num_parejas": 
    };

    var num = 0;
    for(var i = values.length - 1; i > 0; i--)
        num += i;

    reduceVal.num_parejas = num;
    return {reduceVal};
    
}

db.runCommand({
    mapReduce: "cities",
    map: mapFunction4,
    reduce: reduceFunction4,
    query: { CountryID: { $ne: 254 } },
    out: { merge: "parejas_cidudades" }
});

db.parejas_cidudades.find().pretty();

########################################################################
########################################################################

var mapFunction5 = function(){

    var key = this.CountryID;
    var value = {
        "city": this.City,
        "latitude": this.Latitude,
        "longitude": this.Longitude  
    };

    emit(key, value);
}

var reduceFunction5 = function(key, values){
    if(values.length == 1){
        return { 
            "message" : "Este país contiene solo una ciudad" 
        }; 
    }

    var distancia_media = 0;

    for (var i = 0; i < values.length; i++) {
        var c1 = values[i];
        for (var j = i + 1; j < values.length; j++) {
            var c2 = values[j];

            var dist = (c1.latitude - c2.latitude) * (c1.latitude - c2.latitude) + (c1.longitude - c2.longitude) * (c1.longitude - c2.longitude);

            distancia_media += dist;
        }
    }

    distancia_media = distancia_media / values.length;
    return {distancia_media};
    
}

db.runCommand({
    mapReduce: "cities",
    map: mapFunction5,
    reduce: reduceFunction5,
    query: { CountryID: { $ne: 254 } },
    out: { merge: "distancia_media" }
});

db.distancia_media.find().pretty();

########################################################################
########################################################################

db.cities.ensureIndex({CountryID: 1});

var mapFunction6 = function(){

    var key = this.CountryID;
    var value = {
        "city": this.City,
        "latitude": this.Latitude,
        "longitude": this.Longitude  
    };

    emit(key, value);
}

var reduceFunction6 = function(key, values){
    if(values.length == 1){
        return { 
            "message" : "Este país contiene solo una ciudad" 
        }; 
    }

    var reduceVal = { 
        "firstCity": "",
        "secondCity": "",
        "distance": 0
    };

    var dist_min = 99999999999999999999999;
    
    for (var i = 0; i < values.length; i++) {
        var c1 = values[i];
        for (var j = i + 1; j < values.length; j++) {
            var c2 = values[j];

            var dist = (c1.latitude - c2.latitude) * (c1.latitude - c2.latitude) + (c1.longitude - c2.longitude) * (c1.longitude - c2.longitude);

            if(dist < dist_min && dist > 0){
                reduceVal.firstCity = c1.city;
                reduceVal.secondCity = c2.city;
                reduceVal.distance = Math.sqrt(dist);
                dist_min = dist;
            }
        }
    }

    return {reduceVal};
    
}

db.runCommand({
    mapReduce: "cities",
    map: mapFunction6,
    reduce: reduceFunction6,
    query: { CountryID: { $ne: 254 } },
    out: { merge: "cidudades_cercanas_index" }
});

db.cidudades_cercanas_index.find().pretty();
