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
$out = new out();


#solution
$n = $sc->nextInt();
$ans = str_repeat('-', $n);
if ($n % 2) $ans[floor($n/2)] = '=';
else {
    $ans[floor($n/2)-1] = '=';
    $ans[floor($n/2)] = '=';
}
out::println($ans);