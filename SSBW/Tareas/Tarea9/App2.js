import React, { Component } from "react";
import "./App.css";

import "bootstrap/dist/css/bootstrap.css";
import { Navbar, NavItem, Nav, Grid, Row, Col } from "react-bootstrap";

class RestaurantesDisplay extends Component {
  constructor() {
    super();
    this.state = {
      restaurante: null,
      index: 0
    };
  }
  componentDidMount() {
    this.setState({ index: this.props.indice });
    this.setState({ restaurante: this.props.restaurante });
  }

  render() {
    //const restaurantes = this.state.restaurantes;
    //const index = this.state.index;
    const restaurante = this.state.restaurante;

    if (!restaurante) return <div>Loading</div>;

    const imgURL = "https://maps.googleapis.com/maps/api/streetview?size=600x300&location=" + restaurante.address.coord.lat + "," + restaurante.address.coord.lon;
    return (

      <div>
        <h1>
          {restaurante.name}
        </h1>
        <p><img src={imgURL} alt=" " /></p>
        <p>Address: {restaurante.address.street}</p>
        <p>City: {restaurante.address.city}</p>
        <p>Zipcode: {restaurante.address.zipcode}</p>
        <p>Lat: {restaurante.address.coord.lat}</p>
        <p>Lon: {restaurante.address.coord.lon}</p>
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
      <div>
        <Navbar>
          <Navbar.Header>
            <Navbar.Brand>
              React Simple Restaurantes App
            </Navbar.Brand>
          </Navbar.Header>
        </Navbar>
        <Grid>
          <Row>
            <Col md={4} sm={4}>
              <h3>Selecciona un restaurante</h3>
              <Nav
                bsStyle="pills"
                stacked
                activeKey={activeRestaurante}
                onSelect={index => {
                  this.setState({ activeRestaurante: index });
                }}
              >
                {restaurantes.map((rest, index) => (
                  <NavItem key={index} eventKey={index}>{rest.name}</NavItem>
                ))}
              </Nav>
            </Col>
            <Col md={8} sm={8}>
              <RestaurantesDisplay key={activeRestaurante} indice={activeRestaurante} restaurante={restaurantes[activeRestaurante]}/>
            </Col>
          </Row>
        </Grid>
      </div>
    );
  }
}

export default App;
