source ./config.txt

padded_day=$(printf %2s $DAY | tr ' ' "0")
full_path=$(realpath $0)
script_dir=$(dirname $full_path)
project_dir=$(dirname $script_dir)
file=$project_dir/$YEAR/$padded_day/input.txt

if [ ! -e "$file" ]; then
	curl -s https://adventofcode.com/$YEAR/day/$DAY/input --cookie "session=$AOC_SESSION" > $file
	echo "Successfully downloaded"
else
	echo "Input already downloaded; skipping"
fi
