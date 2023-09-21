<?php
include('sqlcon.php');
    
 if(isset($_POST['submit']))
 {
    $name=$_POST['name'];
    $suggestions=$_POST['textarea'];
    $query="INSERT INTO firstwebsite(name,suggestions) VALUES ('$name','$suggestions')";
    $query_run=mysqli_query($conn,$query);
 
 if($query_run)
   {   echo"Thankyou, Please go back to the main page !";
    header('index.html');}
    else
    header index.html
   }
    $conn->close();
?>

