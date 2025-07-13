<?php
class Scanner {
    private $arr = [];
    private $count = 0;
    private $pointer = 0;
    public function next() {
        if(!$this->hasNext()) {
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
$S = $sc->next();
$n = strlen($S);
$ans = 0;
for ($i = 0; $i < $n; $i++){
    for ($j = $i+1; $j < $n; $j++){
        for ($k = $j+1; $k < $n; $k++){
            if (($k - $j === $j - $i) and ($S[$i] === 'A' and $S[$j] === 'B') and ($S[$k] === 'C')) {
                $ans++;
            }
        }
    }
}
out::println($ans);