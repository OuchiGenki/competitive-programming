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
for ($i = 0; $i < 7; $i++) $A[] = $sc->nextInt();
$mp = [];
for ($i = 0; $i < 7; $i++) {
    if (array_key_exists($A[$i], $mp)) $mp[$A[$i]]++;
    else $mp[$A[$i]] = 1;
}
arsort($mp);
if ($mp[0] >= 3 and $mp[1] >= 2) out::println('Yes');
else out::println('No');