<?php
    # while 무한루프
    // while(true) {
    //     echo "conding everybody"
    // }

    // $i = 0;
    // while($i < 10){
    //     echo "conding everybody";
    //     $i += 1;
    // }

    # for loop
    # for(초기화; 반복 지속 여부; 반복 실행) {
    for ($i = 0; $i < 10; $i++){
        echo "conding everybody";
    }

    for ($i = 0; $i < 10; $i++){
        if($i === 5){
            break;
        }
        echo "conding everybody";
    }
?>