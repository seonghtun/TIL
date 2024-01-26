<?php
    function numbering() {
        $i = 0;
        while ($i < 10){
            echo $i;
            $i += 1;
        }
    }
    numbering()

    function get_member1(){
        return "egoing";
    }
    
    function get_member2(){
        return 'k8805';
    }
    
    echo get_member1();
    echo " , ";
    echo get_member2();

    function get_argment($arg){
        return $arg;
    }
    
    function get_argments($arg1, $arg2){
        return $arg1+$arg2;
    }

    function get_argment2($arg = 100){
        return $arg;
    }
    
    print get_argment(1);
    print get_argment(2);
    print get_argments(10, 20);
    print get_argments(30, 40);
    print get_argment2();
    print get_argment2(30);

    $test = 1;
    function get_argument3(){
            // echo $test; 정의안된된 변수라고 에러뜸뜸
            global $test;
            $test = 2;
    }
    get_argument3();
    echo $test;
?>