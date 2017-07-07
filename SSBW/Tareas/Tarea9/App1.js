import React, { Component } from "react";
import "./App.css";

class WeatherDisplay extends Component {
  constructor() {
    super();
    this.state = {
      restaurantes: null,
      index: 0
    };
  }
  componentDidMount() {
    this.setState({ index: this.props.indice });

    const URL_API = "http://localhost:8000/api/restaurantes/";

    fetch(URL_API, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Token 98e774a4d7cb66770d69c4c8f0b50c6ecf643b2d',
      }
    }).then(res => res.json()).then(json => {
      this.setState({ restaurantes: json });
    });
  }
  render() {
    const restaurantes = this.state.restaurantes;
    const index = this.state.index;

    if (!restaurantes) return <div>Loading</div>;

    const rest = restaurantes[index];
    const imgURL = "https://maps.googleapis.com/maps/api/streetview?size=600x300&location=" + rest.address.coord.lat + "," + rest.address.coord.lon;
    return (
      <div>
        <h1>
          {rest.name}
        </h1>
        <p><img src={imgURL} alt=" " /></p>
        <p>Address: {rest.address.street}</p>
        <p>City: {rest.address.city}</p>
        <p>Zipcode: {rest.address.zipcode}</p>
        <p>Lat: {rest.address.coord.lat}</p>
        <p>Lon: {rest.address.coord.lon}</p>
      </div>
    );
  }
}

class App extends Component {
  constructor() {
    super();
    this.state = {
      restaurantes: null,
      activeRestaurante: 0
    };
  }

  componentDidMount() {
    const URL_API = "http://localhost:8000/api/restaurantes/";
    fetch(URL_API, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Token 98e774a4d7cb66770d69c4c8f0b50c6ecf643b2d',
      }
    }).then(res => res.json()).then(json => {
      this.setState({ restaurantes: json });
    });
  }

  render() {
    const restaurantes = this.state.restaurantes;
    const activeRestaurante = this.state.activeRestaurante;

    if (!restaurantes) return <div>Loading</div>;

    return (
      <div className="App">

        {restaurantes.map((rest, index) => (
          <button
            key={index}
            onClick={() => {
              this.setState({ activeRestaurante: index });
            }}
          >
            {rest.name}
          </button>
        ))}

        <WeatherDisplay key={activeRestaurante} indice={activeRestaurante} />

      </div>
    );
  }
}

export default App;
