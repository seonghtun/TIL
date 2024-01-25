<?php
    // var_dump("333");
    // var_dump(12);
    // 똑같다
    // echo var_dump("333");
    // echo var_dump(12);
    # echo에는 줄바꿈이 포함되지 않는다.

    // 문자와 문자 결합 dot
    // echo "hello"." "."world"

    // escape 문자
    // echo "그는 \"안녕하세요\" 라고 말했다."

    # 변수 사용 $
    // $a=1;
    // echo $a+1;
    // echo "<br>\n";
    // $a=2;
    // print $a+1;

    # 상수 사용
    // define("TITLE", "PHP Tutorial");
    // echo TITLE;
    // 재할당시 error 발생
    // define("TITLE", "JAVA Tutorial");

    # 변수 데이터타입
    // $a = 100;
    // echo gettype($a);
    // echo "\n";
    // echo settype($a, 'double');
    // # 가변변수
    // $title = 'subject';
    // $$title = "PHP tutorial"; # $$title = $subject
    // echo "\n".$subject;

    # 비교 연산자 boolean
    // echo "1==2 : ";
    // var_dump(1==2); # 1==2 : bool(false)

    # 입력 서버 query string을 보내주면 서버가 php 입력으로 넣어준다.
    // echo $_GET['id']; # GET 방식 데이터 받은것
    // echo $_POST['id']; # POST 방식 데이터 받은것

    # 조건문 if (조건) 조건은 비교 연산으로 대체 가능하다
    // if (false) {
    //     echo 'result : true';
    // }

    // if (true) {
    //     echo 'result : true';
    // } 
    # else
    // if (true) {
    //     echo 'result : true';
    // } else {
    //    echo 2;
    // }

    # else if
    // if (false) {
    //     echo 'result : true';
    // }else if (true) {
    //     echo 2;
    // } else {
    //     echo 'result : false';
    // }
    # === ,  == 둘다 비교연산 가능
    # 논리 연산자 : and == && , or == || , ! 부정
    # 1 == true , 0 == false
    // if (true and false){
    //     echo "true and false";
    // } else if (true or false) {
    //     echo "true or false"
    // }

    # php type comparison table 검색 
?>
