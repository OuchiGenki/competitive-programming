<?php
class Scanner {
    private $arr = [];
    private $count = 0;
    private $pointer = 0;
    public function next() {
        if($this->pointer >= $this->count) {
            $str = trim(fgets(STDIN));
            $this->arr = explode(' ', $str);
            $this->count = count($this->arr);
            $this->pointer = 0;
        }
        $result = $this->arr[$this->pointer];
        $this->pointer++;
        return $result;
    }
	public function hasNext() {
		return $this->pointer < $this->count;
	}
    public function nextInt() {
        return (int)$this->next();
    }
    public function nextDouble() {
        return (double)$this->next();
    }
}
class out {
    public static function println($str = "") {
        echo $str . PHP_EOL;
    }
}
$sc = new Scanner();


#solution
$A = [];
for ($i = 0; $i < 3; $i++) $A[] = $sc->nextInt();
$ans = 'No';
if (($A[0] * $A[1] === $A[2]) or ($A[1] * $A[2] === $A[0]) or ($A[2] * $A[0] === $A[1])){
    $ans = 'Yes';
}
out::println($ans);