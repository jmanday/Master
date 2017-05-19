<?php

        if(isset($_POST['id'])){
              $var=$_POST['id'];

              $servername = "172.17.2.190";
              $username = "root";
              $password = "root";
              $dbname = "Docker";

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
