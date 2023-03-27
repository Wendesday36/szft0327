<?php
// Az űrlap adatainak feldolgozása és valamilyen válasz küldése
// Ebben az esetben csak egy üzenetet küldünk vissza a "success" kulcs alatt
$response = array('success' => 'Az űrlap sikeresen elküldve!');
echo json_encode($response);
?>