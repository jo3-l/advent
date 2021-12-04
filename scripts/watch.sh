source $(realpath $0 | xargs dirname)/config.txt

padded_day=$(printf %02s $DAY)
project_dir=$(realpath $0 | xargs dirname | xargs dirname)
nodemon --config "$project_dir/nodemon.json" "$project_dir/$YEAR/$padded_day/solution.py"
