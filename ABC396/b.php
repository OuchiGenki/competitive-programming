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
$q = $sc->nextInt();
$stack = new SplStack();
for ($i = 0; $i < 100; $i++) $stack->push(0);
for ($i = 0; $i < $q; $i++){
    $query = $sc->nextInt();
    if ($query === 1) {
        $x = $sc->nextInt();
        $stack->push($x);
    } else {
        out::println($stack->pop());
    }
}