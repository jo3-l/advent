source $(realpath $0 | xargs dirname)/config.txt

padded_day=$(printf %02s $DAY)
project_dir=$(realpath $0 | xargs dirname | xargs dirname)
file=$project_dir/$YEAR/$padded_day/input.txt

if [ ! -e "$file" ]; then
	curl -A "jo3-l <https://github.com/jo3-l>" -s https://adventofcode.com/$YEAR/day/$DAY/input --cookie "session=$AOC_SESSION" > $file
	echo "Successfully downloaded"
else
	echo "Input already downloaded; skipping"
fi
