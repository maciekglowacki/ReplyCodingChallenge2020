run=""
if [ $# -eq 2 ]; then
  run="python3"
else
  run="python"
fi
$run randomizer.py < inputs/$1.txt > outputs/$1.txt
awk 1 inputs/$1.txt outputs/$1.txt | $run scoring.py
