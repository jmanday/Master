<?php

        if(isset($_POST['id'])){
              $var=$_POST['id'];

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

              $sql = "DELETE FROM  Usuarios WHERE ID = $var";

              if ($conn->query($sql) === TRUE) {
                  header('Location: index.php');
              } else {
                  echo "Error: " . $sql . "<br>" . $conn->error;
              }

              $conn->close();
        }

?>
