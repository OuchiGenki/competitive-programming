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
$n = $sc->nextInt();
$A = [];
for ($i = 0; $i < $n; $i++) $A[] = $sc->nextInt();
$flag = true;
for ($i = 0; $i < $n-1; $i++){
    if ($A[$i] >= $A[$i+1]) $flag = false;
}
if ($flag) out::println('Yes');
else out::println('No');