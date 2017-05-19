<html xmlns="http://www.w3.org/1999/xhtml">
  <!--
    Modified from the Debian original for Ubuntu
    Last updated: 2014-03-19
    See: https://launchpad.net/bugs/1288690
  -->
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Ubuntu Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  }

  body, html {
    padding: 3px 3px 3px 3px;

    background-color: #D8DBE2;

    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  }

  div.main_page {
    position: relative;
    display: table;

    width: 800px;

    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;

    border-width: 2px;
    border-color: #212738;
    border-style: solid;

    background-color: #FFFFFF;

    text-align: center;
  }

  div.page_header {
    height: 99px;
    width: 100%;
    text-align: center;                                                                                                                                                                            background-color: #F5F6F7;

  }
  
  div.page_header span {
    margin: 15px 0px 0px 50px;
    text-align: center;                                                                                                                                                                            font-size: 180%;          
                                                                                                                                                                                                           
    font-weight: bold;                                                                                                                                                                                     
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.page_header img {                                                                                                                                                                                    
    margin: 3px 0px 0px 40px;                                                                                                                                                                              
                                                                                                                                                                                                           
    border: 0px 0px 0px;                                                                                                                                                                                   
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.table_of_contents {                                                                                                                                                                                  
    clear: left;                                                                                                                                                                                           
                                                                                                                                                                                                           
    min-width: 200px;                                                                                                                                                                                      
                                                                                                                                                                                                           
    margin: 3px 3px 3px 3px;                                                                                                                                                                               
                                                                                                                                                                                                           
    background-color: #FFFFFF;                                                                                                                                                                             
                                                                                                                                                                                                           
    text-align: left;                                                                                                                                                                                      
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.table_of_contents_item {                                                                                                                                                                             
    clear: left;                                                                                                                                                                                           
                                                                                                                                                                                                           
    width: 100%;                                                                                                                                                                                           
                                                                                                                                                                                                           
    margin: 4px 0px 0px 0px;                                                                                                                                                                               
                                                                                                                                                                                                           
    background-color: #FFFFFF;                                                                                                                                                                             
                                                                                                                                                                                                           
    color: #000000;                                                                                                                                                                                        
    text-align: left;                                                                                                                                                                                      
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.table_of_contents_item a {                                                                                                                                                                           
    margin: 6px 0px 0px 6px;                                                                                                                                                                               
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.content_section {                                                                                                                                                                                    
    margin: 3px 3px 3px 3px;                                                                                                                                                                               
                                                                                                                                                                                                           
    background-color: #FFFFFF;                                                                                                                                                                             
                                                                                                                                                                                                           
    text-align: left;                                                                                                                                                                                      
  }

  div.content_section_text {                                                                                                                                                                               
    padding: 4px 8px 4px 8px;                                                                                                                                                                              

    color: #000000;                                                                                                                                                                                        
    font-size: 100%;                                                                                                                                                                                       
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.content_section_text pre {                                                                                                                                                                           
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;                                                                                                                                                                              
                                                                                                                                                                                                           
    border-width: 1px;                                                                                                                                                                                     
    border-style: dotted;                                                                                                                                                                                  
    border-color: #000000;                                                                                                                                                                                 
                                                                                                                                                                                                           
    background-color: #F5F6F7;                                                                                                                                                                             
                                                                                                                                                                                                           
    font-style: italic;                                                                                                                                                                                    
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.content_section_text p {                                                                                                                                                                             
    margin-bottom: 6px;                                                                                                                                                                                    
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.content_section_text ul, div.content_section_text li {                                                                                                                                               
    padding: 4px 8px 4px 16px;                                                                                                                                                                             
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.section_header {                                                                                                                                                                                     
    padding: 3px 6px 3px 6px;                                                                                                                                                                              
                                                                                                                                                                                                           
    background-color: #8E9CB2;                                                                                                                                                                             
                                                                                                                                                                                                           
    color: #FFFFFF;                                                                                                                                                                                        
    font-weight: bold;                                                                                                                                                                                     
    font-size: 112%;                                                                                                                                                                                       
    text-align: center;                                                                                                                                                                                    
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.section_header_red {                                                                                                                                                                                 
    background-color: #CD214F;                                                                                                                                                                             
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.section_header_grey {                                                                                                                                                                                
    background-color: #9F9386;                                                                                                                                                                             
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  .floating_element {                                                                                                                                                                                      
    position: relative;                                                                                                                                                                                    
    float: left;                                                                                                                                                                                           
    text-align: center;                                                                                                                                                                                    
    margin-top: 10px;                                                                                                                                                                                      
  }

  div.table_of_contents_item a,                                                                                                                                                                            
  div.content_section_text a {                                                                                                                                                                             
    text-decoration: none;                                                                                                                                                                                 
    font-weight: bold;                                                                                                                                                                                     
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.table_of_contents_item a:link,                                                                                                                                                                       
  div.table_of_contents_item a:visited,                                                                                                                                                                    
  div.table_of_contents_item a:active {                                                                                                                                                                    
    color: #000000;                                                                                                                                                                                        
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.table_of_contents_item a:hover {                                                                                                                                                                     
    background-color: #000000;                                                                                                                                                                                              

    color: #FFFFFF;                                                                                                                                                                                        
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.content_section_text a:link,                                                                                                                                                                         
  div.content_section_text a:visited,                                                                                                                                                                      
   div.content_section_text a:active {                                                                                                                                                                     
    background-color: #DCDFE6;                                                                                                                                                                             
                                                                                                                                                                                                           
    color: #000000;                                                                                                                                                                                        
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.content_section_text a:hover {                                                                                                                                                                       
    background-color: #000000;                                                                                                                                                                             
                                                                                                                                                                                                           
    color: #DCDFE6;                                                                                                                                                                                        
  }                                                                                                                                                                                                        
                                                                                                                                                                                                           
  div.validator {                                                                                                                                                                                          
  }                                                                                                                                                                                                        
    </style>                                                                                                                                                                                               
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <span class="floating_element" text-align="center">
             Gestion de Usuarios
        </span>
      </div>
      <br><br><br><br>
      <div align="center">

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

                $sql = "SELECT ID, nombre, apellidos from Usuarios";
                $result = $conn->query($sql);

                if ($result->num_rows > 0) {
                        // output data of each row
                        echo "<br><h2><em>Lista de Usuarios</em></h2><br>";
                        echo "<table border='1' align='center'>";
                           echo "<tr>";
                              echo "<td><b>id</b></td>";
                              echo "<td><b>Nombre</b></td>";
                              echo "<td><b>Apellidos</b></td>";
                           echo "</tr>";
                        while($row = $result->fetch_assoc()) {
                                echo "<tr>";
                                   echo "<td>" . $row["ID"]. "</td>";
                                   echo "<td>" . $row["nombre"]. "</td>";
                                   echo "<td>" . $row["apellidos"]. "</td>";
                                   echo "<td><form action=\"delete_user.php\" method=\"POST\">";
                                        echo "<input class=\"form-btn\" name=\"borrar\" type=\"submit\" value=\"Borrar\" />";
                                        echo "<input type='hidden' name='id' value='" . $row["ID"]. "' />";
                                   echo "</form></td>";
                                echo "</tr>";
                        }
                        echo "</table>";
                } else {
                        echo "0 results";
                }

                $conn->close();
     ?>
        <br><br><br>
        <form action="insert_user.php" method="POST">                                                                                                                                                                
        <h2><em>Nuevo Usuario</em></h2><br>                                                                                                                                                                          
                <label for="nombre">Nombre <span><em>(requerido)</em></span></label>                                                                                                                                 
                 <input type="text" name="nombre" class="form-input" required/><br>                                                                                                                                  
                                                                                                                                                                                                                     
                 <label for="apellido">Apellido</label>                                                                                                                                                              
                 <input type="text" name="apellido" /><br>                                                                                                                                                           
                                                                                                                                                                                                                     
                <label for="edad">Edad </label>                                                                                                                                                                      
                <input type="numeric" name="edad" /><br><br><br>                                                                                                                                                     
                                                                                                                                                                                                                     
                <input class="form-btn" name="insertar" type="submit" value="Insertar" />                                                                                                                            
        </form><br><br>                                                                                                                                                                                              
      </div>                                                                                                                                                                                                         
    </div>                                                                                                                                                                                                           
  </body>                                                                                                                                                                                                            
</html>
