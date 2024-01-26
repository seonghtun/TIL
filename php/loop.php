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

    # 반복문 자체를 완전히 중단시킴
    for ($i = 0; $i < 10; $i++){
        if($i === 5){
            break;
        }
        echo "conding everybody";
    }

    # i = 5 일때 건너뛰기
    for ($i = 0; $i < 10; $i++){
        if($i === 5){
            continue;
        }
        echo "conding everybody";
    }
?>