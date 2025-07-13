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

function is_same($i, $j){
    global $S, $T, $n, $m;
    for ($r = 0; $r < $m; $r++) {
        for ($c = 0; $c < $m; $c++) {
            if (($i + $r >= $n) or ($i + $c >= $n)) return false; 
            if ($S[$i + $r][$j + $c] !== $T[$r][$c]) return false;
        }
    }
    return true;
}

$n = $sc->nextInt();
$m = $sc->nextInt();
$S = [];
$T = [];
for ($i = 0; $i < $n; $i++) $S[] = $sc->next();
for ($i = 0; $i < $m; $i++) $T[] = $sc->next();
for ($i = 0; $i < $n; $i++) {
    for ($j = 0; $j < $n; $j++){
        if (is_same($i, $j)) out::println(implode(' ', [$i+1, $j+1]));
    }
}