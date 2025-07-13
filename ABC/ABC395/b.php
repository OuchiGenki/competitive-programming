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
$S = [];
for ($i = 0; $i < $n; $i++){
    $S[] = array_fill(0, $n, '.');
}

for ($i = 0; $i < $n; $i++){
    $j = $n - $i - 1;
    if ($i % 2) $chr = '.';
    else $chr = '#';
    if ($i > $j) continue;
    for ($r = $i; $r <= $j; $r++) {
        for ($c = $i; $c <= $j; $c++){
            $S[$r][$c] = $chr;
        }
    }
}

for ($i = 0; $i < $n; $i++) out::println(implode('',$S[$i]));