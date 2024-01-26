<?php
# 배열 선언
// $member = ["egoing","k8805", "sex"];
// echo $member[0];
// echo $member[1];
// echo $member[2];

# 같은 타입 요소가 아니어도 괜찮다.
$member = ["egoing","k8805", "sugar"];
array_push($member, 4);
array_push($member, "a");
array_unshift($member, "ee");
array_shift($member);
array_pop($member);
var_dump($member);

sort($member);
var_dump($member);
rsort($member);
var_dump($member);

# 연관 배열
$grades = array("egoing" =>10, "k8805" => 5 , "sorialgi"=> 12);
var_dump($grades);

$grade['egoing'] = 10;
$grade['k8805'] = 30;
$grade['sorialgi'] = 80;
var_dump($grade);

$grades = array("egoing" =>10, "k8805" => 5 , "sorialgi"=> 12);
var_dump($grades);

$grade['egoing'] = 10;
$grade['k8805'] = 30;
$grade['sorialgi'] = 80;
var_dump($grade);

# foreach 문 사용법과 문자열 치환 방법
foreach($grades as $key => $value){
    echo "key: {$key} value :${value}\n";
}

foreach($member as $key => $value){
    echo "key: {$key} value :${value}\n";
}

$member = ["egoing","k8805", "sugar"];
foreach($member as $value){
    echo "value :{$value}\n";
}
?>