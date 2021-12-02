source ./config.txt

padded_day=$(printf %2s $DAY | tr ' ' "0")
full_path=$(realpath $0)
script_dir=$(dirname $full_path)
project_dir=$(dirname $script_dir)
day_dir=$project_dir/$YEAR/$padded_day

if [[ $1 == "-s" ]]; then
	py ${day_dir}/solution.py ${day_dir}/sample.txt
else
	py ${day_dir}/solution.py ${day_dir}/input.txt
fi