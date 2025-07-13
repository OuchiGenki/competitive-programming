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
$m = $sc->nextInt();
$freq = array_fill(0, $n+1, 0);
for ($i = 0; $i < $m; $i++) $freq[$sc->nextInt()]++;
$ans = [];
for ($i = 1; $i <= $n; $i++) {
    if ($freq[$i] == 0) $ans[] = $i;
}
out::println(count($ans));
out::println(implode(' ', $ans));