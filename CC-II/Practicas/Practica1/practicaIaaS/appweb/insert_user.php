<?php
        $servername = "192.168.10.77";

        $username = "root";

        $password = "root";

        $dbname = "OpenNebula";



        // Create connection                                                                                                                                                                                                 
  
        $conn = new mysqli($servername, $username, $password, $dbname);



        // Check connection                                                                                                                                                                                                  
  
        if ($conn->connect_error) {

                 die("Connection failed: " . $conn->connect_error);

        }

        $subs_name = utf8_decode($_POST['nombre']);
        $subs_apellidos = utf8_decode($_POST['apellido']);
        $subs_edad = utf8_decode($_POST['edad']);

        $sql = "INSERT INTO Usuarios(nombre, apellidos, edad) values(\"$subs_name\", \"$subs_apellidos\", $subs_edad)";

        if ($conn->query($sql) === TRUE) {
                header('Location: index.php');
        } else {
                echo "Error: " . $sql . "<br>" . $conn->error;
        }

        $conn->close();

?>
